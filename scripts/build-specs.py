#!/usr/bin/env python3
"""
Enhanced NextPM spec automation with state management and visual timeline support.

This script:
1. Scans project/specs/ for all .md files (except README.md)
2. Parses YAML frontmatter for spec state management
3. Copies specs to mkdocs-docs/engineering/specs/ with enhanced processing
4. Injects visual timeline data and animations
5. Auto-generates navigation entries in mkdocs.yml with state indicators
6. Creates interactive dashboard with spec statistics
7. Preserves existing non-spec navigation structure
"""

import os
import shutil
import re
from pathlib import Path
import yaml
import codecs
import json
from datetime import datetime
from collections import defaultdict

def extract_title_from_spec(spec_path):
    """Extract the title from a spec file's first H1 heading."""
    try:
        with open(spec_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for first H1 heading
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Warning: Could not extract title from {spec_path}: {e}")

    # Fallback: generate title from filename
    filename = Path(spec_path).stem
    # Handle special case for 0.00-project-start
    if filename == '0.00-project-start':
        return '0.00 Project Start'

    # For YYYY-MM-DD-nn format, create readable title
    match = re.match(r'^(\d{4}-\d{2}-\d{2}-\d{2})-(.+)$', filename)
    if match:
        spec_id, name_part = match.groups()
        # Convert kebab-case to Title Case
        title_part = name_part.replace('-', ' ').title()
        return f"{spec_id} {title_part}"

    # Final fallback
    return filename.replace('-', ' ').title()

def get_spec_sort_key(filename):
    """Generate sort key for spec files."""
    stem = Path(filename).stem

    # Handle special case for 0.00-project-start (should be first)
    if stem == '0.00-project-start':
        return '0000-00-00-00'

    # For YYYY-MM-DD-nn format
    match = re.match(r'^(\d{4}-\d{2}-\d{2}-\d{2})', stem)
    if match:
        return match.group(1)

    # Fallback: use filename as-is
    return stem

def parse_spec_frontmatter(spec_path):
    """Parse YAML frontmatter from a spec file."""
    try:
        with open(spec_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if content starts with YAML frontmatter
        if content.startswith('---\n'):
            # Find the closing ---
            end_marker = content.find('\n---\n', 4)
            if end_marker != -1:
                yaml_content = content[4:end_marker]
                markdown_content = content[end_marker + 5:]
                try:
                    frontmatter = yaml.safe_load(yaml_content) or {}
                    return frontmatter, markdown_content
                except yaml.YAMLError as e:
                    print(f"Warning: YAML parsing error in {spec_path}: {e}")

        # No frontmatter found, return empty dict and full content
        return {}, content
    except Exception as e:
        print(f"Warning: Could not parse frontmatter from {spec_path}: {e}")
        with open(spec_path, 'r', encoding='utf-8') as f:
            return {}, f.read()

def process_spec_metadata(frontmatter, filename):
    """Process and enhance spec metadata."""
    metadata = frontmatter.copy()

    # Set defaults for missing fields
    defaults = {
        'status': 'draft',
        'priority': 'medium',
        'estimated_hours': 0,
        'actual_hours': 0,
        'assignee': 'Kang',
        'category': 'nextpm-feature',
        'demonstrates': [],
        'state_history': []
    }

    for key, default_value in defaults.items():
        if key not in metadata:
            metadata[key] = default_value

    # Extract spec ID from filename
    stem = Path(filename).stem
    if stem != '0.00-project-start':
        match = re.match(r'^(\d{4}-\d{2}-\d{2}-\d{2})', stem)
        if match:
            metadata['spec_id'] = match.group(1)
        else:
            metadata['spec_id'] = stem
    else:
        metadata['spec_id'] = '0.00'

    # Add computed fields
    metadata['filename'] = filename
    metadata['last_updated'] = datetime.now().isoformat()

    return metadata

def generate_state_badge_html(status, priority='medium'):
    """Generate HTML for animated state badge."""
    status_colors = {
        'draft': 'orange',
        'review': 'blue',
        'approved': 'green',
        'in-progress': 'purple',
        'completed': 'success'
    }

    priority_indicators = {
        'high': '🔥',
        'medium': '📋',
        'low': '📝'
    }

    color = status_colors.get(status, 'gray')
    icon = priority_indicators.get(priority, '📋')

    return f'''<span class="spec-state-badge spec-state-{status}" data-status="{status}" data-priority="{priority}">
    {icon} {status.replace('-', ' ').title()}
</span>'''

def inject_timeline_data(content, metadata):
    """Inject timeline visualization data and commit timeline into spec content."""
    # Create timeline data structure
    timeline_data = {
        'spec_id': metadata.get('spec_id', ''),
        'status': metadata.get('status', 'draft'),
        'state_history': metadata.get('state_history', []),
        'estimated_hours': metadata.get('estimated_hours', 0),
        'actual_hours': metadata.get('actual_hours', 0),
        'priority': metadata.get('priority', 'medium'),
        'category': metadata.get('category', 'nextpm-feature'),
        'demonstrates': metadata.get('demonstrates', [])
    }

    # Generate state badge
    state_badge = generate_state_badge_html(
        metadata.get('status', 'draft'),
        metadata.get('priority', 'medium')
    )

    # Generate commit timeline if available
    git_data = metadata.get('git_commits', {})
    commit_timeline = generate_commit_timeline_html(git_data)

    # Inject at the beginning of content after the first header
    lines = content.split('\n')
    header_found = False
    for i, line in enumerate(lines):
        if line.startswith('# ') and not header_found:
            header_found = True
            # Insert state badge, timeline container, and commit timeline after header
            lines.insert(i + 1, '')
            lines.insert(i + 2, state_badge)
            lines.insert(i + 3, '')
            lines.insert(i + 4, f'<div class="spec-timeline" data-timeline="{json.dumps(timeline_data).replace('"', "&quot;")}"></div>')
            lines.insert(i + 5, '')
            if git_data.get('commits'):
                lines.insert(i + 6, commit_timeline)
                lines.insert(i + 7, '')
            break

    return '\n'.join(lines)

def collect_git_data(spec_id):
    """Collect comprehensive git data for spec-commit linking."""
    try:
        import subprocess

        git_data = {
            'commits': [],
            'branches': [],
            'pull_requests': [],
            'file_changes': [],
            'contributors': []
        }

        # Get commits that reference this spec ID
        cmd = ['git', 'log', '--grep', f'#{spec_id}', '--pretty=format:%H|%ad|%s|%an', '--date=iso']
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')

        if result.returncode == 0 and result.stdout.strip():
            for line in result.stdout.strip().split('\n'):
                parts = line.split('|', 3)
                if len(parts) == 4:
                    commit_hash = parts[0]

                    # Get file changes for this commit
                    files_cmd = ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit_hash]
                    files_result = subprocess.run(files_cmd, capture_output=True, text=True, cwd='.')
                    changed_files = files_result.stdout.strip().split('\n') if files_result.returncode == 0 else []

                    git_data['commits'].append({
                        'hash': parts[0][:8],  # Short hash
                        'full_hash': parts[0],
                        'date': parts[1],
                        'message': parts[2],
                        'author': parts[3],
                        'files_changed': len(changed_files),
                        'changed_files': changed_files[:10]  # Limit to first 10 files
                    })

        # Get branches that might be related (containing the spec ID in name)
        branches_cmd = ['git', 'branch', '-a', '--list', f'*{spec_id}*']
        branches_result = subprocess.run(branches_cmd, capture_output=True, text=True, cwd='.')
        if branches_result.returncode == 0 and branches_result.stdout.strip():
            git_data['branches'] = [branch.strip(' *') for branch in branches_result.stdout.strip().split('\n')]

        # Get recent activity (commits in last 30 days that might be related)
        recent_cmd = ['git', 'log', '--since=30.days.ago', '--grep', spec_id, '--pretty=format:%H|%ad|%s', '--date=short']
        recent_result = subprocess.run(recent_cmd, capture_output=True, text=True, cwd='.')
        if recent_result.returncode == 0 and recent_result.stdout.strip():
            recent_activity = []
            for line in recent_result.stdout.strip().split('\n')[:5]:  # Last 5 recent commits
                parts = line.split('|', 2)
                if len(parts) == 3:
                    recent_activity.append({
                        'hash': parts[0][:8],
                        'date': parts[1],
                        'message': parts[2]
                    })
            git_data['recent_activity'] = recent_activity

        # Get contributors for this spec
        contributors = set()
        for commit in git_data['commits']:
            contributors.add(commit['author'])
        git_data['contributors'] = list(contributors)

        return git_data

    except Exception as e:
        print(f"Warning: Could not collect git data for {spec_id}: {e}")
        return {
            'commits': [],
            'branches': [],
            'pull_requests': [],
            'file_changes': [],
            'contributors': [],
            'recent_activity': [],
            'error': str(e)
        }

def generate_commit_timeline_html(git_data):
    """Generate HTML visualization for commit timeline."""
    if not git_data.get('commits'):
        return '<div class="commit-timeline-empty">No commits linked to this spec yet.</div>'

    html = '<div class="commit-timeline">\n'
    html += '    <h4>📝 Development Timeline</h4>\n'
    html += '    <div class="timeline-container">\n'

    for i, commit in enumerate(git_data['commits']):
        is_latest = i == 0
        timeline_class = 'timeline-item latest' if is_latest else 'timeline-item'

        html += f'''        <div class="{timeline_class}">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#{commit['hash']}</span>
                    <span class="commit-date">{commit['date'][:10]}</span>
                </div>
                <div class="commit-message">{commit['message']}</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 {commit['author']}</span>
                    <span class="files-changed">📁 {commit['files_changed']} files changed</span>
                </div>
            </div>
        </div>
'''

    html += '    </div>\n</div>\n'
    return html

def auto_generate_dev_workflow(spec_metadata):
    """Automatically generate dev workflow summaries for specs with commits."""
    dev_workflows_dir = Path('mkdocs-docs/engineering/dev-workflows')
    dev_workflows_dir.mkdir(parents=True, exist_ok=True)

    generated_workflows = []

    for metadata in spec_metadata:
        git_data = metadata.get('git_commits', {})
        if not isinstance(git_data, dict) or not git_data.get('commits'):
            continue

        spec_id = metadata.get('spec_id', '')
        if not spec_id:
            continue

        # Generate a dev workflow file for this spec
        workflow_filename = f"{spec_id.replace('-', '_')}_implementation_summary.md"
        workflow_path = dev_workflows_dir / workflow_filename

        # Check if this workflow already exists and is recent
        if workflow_path.exists():
            continue  # Skip existing workflows for now

        # Generate workflow content
        title = extract_title_from_spec(Path('project/specs') / metadata['filename'])

        workflow_content = f"""# {spec_id} Implementation Summary

**Spec**: [{title}](../specs/{metadata['filename']})
**Status**: {metadata.get('status', 'unknown').title()}
**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Development Activity

{generate_commit_timeline_html(git_data)}

## Implementation Statistics

- **Total Commits**: {len(git_data['commits'])}
- **Contributors**: {', '.join(git_data.get('contributors', []))}
- **Branches**: {len(git_data.get('branches', []))}
- **Files Changed**: {sum(commit.get('files_changed', 0) for commit in git_data['commits'])}

## Key Development Decisions

_This section will be enhanced with AI-powered commit analysis in a future update._

{''.join([f"- **{commit['date'][:10]}**: {commit['message']}" + chr(10) for commit in git_data['commits'][:5]])}

## Next Steps

- Continue monitoring development progress
- Update spec status as implementation progresses
- Generate more detailed analysis as commits accumulate

---

**Auto-generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Source**: Automated dev workflow generation from git commit data
"""

        with open(workflow_path, 'w', encoding='utf-8') as f:
            f.write(workflow_content)

        generated_workflows.append(workflow_filename)
        print(f"Generated dev workflow: {workflow_filename}")

    return generated_workflows

def process_spec_content(content, filename):
    """Process spec content to fix broken links for MkDocs compatibility."""
    # Define link replacements/fixes
    link_fixes = {
        # Root project files that don't exist in MkDocs
        r'\]\(\.\.\/\.\.\/AI-NATIVE\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/AI-NATIVE.md)',
        r'\]\(\.\.\/\.\.\/GETTING-STARTED\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/GETTING-STARTED.md)',
        r'\]\(\.\.\/\.\.\/mkdocs\.yml\)': '](https://github.com/kangxh75/NextPM/blob/master/mkdocs.yml)',

        # AI context files
        r'\]\(\.\.\/\.\.\/ai-context\/README\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/ai-context/README.md)',
        r'\]\(\.\.\/\.\.\/ai-context\/conventions\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/ai-context/conventions.md)',

        # Meta/ADR files
        r'\]\(\.\.\/\.\.\/meta\/adr\/[^)]+\)': lambda m: f'](https://github.com/kangxh75/NextPM/blob/master/{m.group(0)[2:-1]})',
        r'\]\(\.\.\/meta\/adr\/[^)]+\)': lambda m: f'](https://github.com/kangxh75/NextPM/blob/master/{m.group(0)[2:-1].replace("../", "")})',

        # Project internal links that should go to GitHub
        r'\]\(\.\.\/\.\.\/project\/[^)]+\)': lambda m: f'](https://github.com/kangxh75/NextPM/blob/master/{m.group(0)[2:-1]})',
    }

    processed_content = content

    for pattern, replacement in link_fixes.items():
        if callable(replacement):
            processed_content = re.sub(pattern, replacement, processed_content)
        else:
            processed_content = re.sub(pattern, replacement, processed_content)

    return processed_content
    """Extract the title from a spec file's first H1 heading."""
    try:
        with open(spec_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for first H1 heading
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Warning: Could not extract title from {spec_path}: {e}")

    # Fallback: generate title from filename
    filename = Path(spec_path).stem
    # Handle special case for 0.00-project-start
    if filename == '0.00-project-start':
        return '0.00 Project Start'

    # For YYYY-MM-DD-nn format, create readable title
    match = re.match(r'^(\d{4}-\d{2}-\d{2}-\d{2})-(.+)$', filename)
    if match:
        spec_id, name_part = match.groups()
        # Convert kebab-case to Title Case
        title_part = name_part.replace('-', ' ').title()
        return f"{spec_id} {title_part}"

    # Final fallback
    return filename.replace('-', ' ').title()

def get_spec_sort_key(filename):
    """Generate sort key for spec files."""
    stem = Path(filename).stem

    # Handle special case for 0.00-project-start (should be first)
    if stem == '0.00-project-start':
        return '0000-00-00-00'

    # For YYYY-MM-DD-nn format
    match = re.match(r'^(\d{4}-\d{2}-\d{2}-\d{2})', stem)
    if match:
        return match.group(1)

    # Fallback: use filename as-is
    return stem

def process_spec_content(content, filename):
    """Process spec content to fix broken links for MkDocs compatibility."""
    # Define link replacements/fixes
    link_fixes = {
        # Root project files that don't exist in MkDocs
        r'\]\(\.\.\/\.\.\/AI-NATIVE\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/AI-NATIVE.md)',
        r'\]\(\.\.\/\.\.\/GETTING-STARTED\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/GETTING-STARTED.md)',
        r'\]\(\.\.\/\.\.\/mkdocs\.yml\)': '](https://github.com/kangxh75/NextPM/blob/master/mkdocs.yml)',

        # AI context files
        r'\]\(\.\.\/\.\.\/ai-context\/README\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/ai-context/README.md)',
        r'\]\(\.\.\/\.\.\/ai-context\/conventions\.md\)': '](https://github.com/kangxh75/NextPM/blob/master/ai-context/conventions.md)',

        # Meta/ADR files
        r'\]\(\.\.\/\.\.\/meta\/adr\/[^)]+\)': lambda m: f'](https://github.com/kangxh75/NextPM/blob/master/{m.group(0)[2:-1]})',
        r'\]\(\.\.\/meta\/adr\/[^)]+\)': lambda m: f'](https://github.com/kangxh75/NextPM/blob/master/{m.group(0)[2:-1].replace("../", "")})',

        # Project internal links that should go to GitHub
        r'\]\(\.\.\/\.\.\/project\/[^)]+\)': lambda m: f'](https://github.com/kangxh75/NextPM/blob/master/{m.group(0)[2:-1]})',
    }

    processed_content = content

    for pattern, replacement in link_fixes.items():
        if callable(replacement):
            processed_content = re.sub(pattern, replacement, processed_content)
        else:
            processed_content = re.sub(pattern, replacement, processed_content)

    return processed_content

def copy_specs_to_docs():
    """Copy spec files from project/specs/ to mkdocs-docs/engineering/specs/ with enhanced processing."""
    source_dir = Path('project/specs')
    target_dir = Path('mkdocs-docs/engineering/specs')

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory {source_dir} does not exist")

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # Remove all existing files in target directory (clean rebuild)
    for file in target_dir.glob('*.md'):
        file.unlink()

    # Copy all .md files except README.md with enhanced processing
    spec_files = []
    spec_metadata_collection = []

    for spec_file in source_dir.glob('*.md'):
        if spec_file.name.lower() != 'readme.md':
            # Parse frontmatter and content
            frontmatter, content = parse_spec_frontmatter(spec_file)
            metadata = process_spec_metadata(frontmatter, spec_file.name)

            # Collect git data for this spec
            git_data = collect_git_data(metadata.get('spec_id', ''))
            metadata['git_commits'] = git_data

            # Process the content to fix links
            processed_content = process_spec_content(content, spec_file.name)

            # Inject timeline data and visualizations
            enhanced_content = inject_timeline_data(processed_content, metadata)

            # Write the processed content to target
            target_file = target_dir / spec_file.name
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)

            spec_files.append(spec_file.name)
            spec_metadata_collection.append(metadata)
            print(f"Copied and enhanced: {spec_file.name} (Status: {metadata.get('status', 'draft')})")

    return spec_files, spec_metadata_collection

def generate_spec_dashboard(spec_metadata_collection):
    """Generate interactive dashboard with spec statistics."""
    dashboard_path = Path('mkdocs-docs/engineering/dashboard.md')
    dashboard_path.parent.mkdir(parents=True, exist_ok=True)

    # Calculate statistics
    total_specs = len(spec_metadata_collection)
    status_counts = defaultdict(int)
    priority_counts = defaultdict(int)
    category_counts = defaultdict(int)

    for metadata in spec_metadata_collection:
        status_counts[metadata.get('status', 'draft')] += 1
        priority_counts[metadata.get('priority', 'medium')] += 1
        category_counts[metadata.get('category', 'nextpm-feature')] += 1

    # Get recent activity
    recent_specs = sorted(spec_metadata_collection,
                         key=lambda x: x.get('last_updated', ''),
                         reverse=True)[:5]

    # Generate dashboard content
    content = f"""# 📊 NextPM Spec Dashboard

<div class="dashboard-container">

## 📈 Statistics

<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-number">{total_specs}</div>
        <div class="stat-label">Total Specs</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{status_counts.get('completed', 0)}</div>
        <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{status_counts.get('in-progress', 0)}</div>
        <div class="stat-label">In Progress</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{status_counts.get('draft', 0)}</div>
        <div class="stat-label">Draft</div>
    </div>
</div>

## 🎯 Status Breakdown

<div class="status-breakdown">
"""

    for status, count in status_counts.items():
        percentage = (count / total_specs * 100) if total_specs > 0 else 0
        content += f"""    <div class="status-item">
        <span class="spec-state-badge spec-state-{status}">{status.replace('-', ' ').title()}</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {percentage}%"></div>
        </div>
        <span class="count">{count}</span>
    </div>
"""

    content += f"""</div>

## 🔄 Recent Activity

<div class="recent-activity">
"""

    for spec in recent_specs:
        state_badge = generate_state_badge_html(
            spec.get('status', 'draft'),
            spec.get('priority', 'medium')
        )
        title = extract_title_from_spec(Path('project/specs') / spec['filename'])

        content += f"""    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/{spec['filename']}">{title}</a></strong>
            {state_badge}
        </div>
        <div class="activity-meta">
            Updated: {spec.get('last_updated', 'Unknown')[:10]} |
            Priority: {spec.get('priority', 'medium').title()}
        </div>
    </div>
"""

    content += f"""</div>

## 🎨 Live Development

<div class="live-dev-feed">
    <div class="dev-item">
        <span class="dev-status">🚧 Currently implementing</span>
        <span class="dev-description">Enhanced spec state management and visual timeline system</span>
    </div>
    <div class="dev-item">
        <span class="dev-status">⏭️ Next up</span>
        <span class="dev-description">Git integration and automated commit tracking</span>
    </div>
</div>

</div>

<!-- Dashboard JavaScript -->
<script>
document.addEventListener('DOMContentLoaded', function() {{
    // Initialize dashboard animations
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {{
        setTimeout(() => {{
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }}, index * 100);
    }});

    // Animate progress bars
    const progressFills = document.querySelectorAll('.progress-fill');
    progressFills.forEach(fill => {{
        setTimeout(() => {{
            fill.style.transform = 'scaleX(1)';
        }}, 500);
    }});
}});
</script>
"""

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Generated interactive dashboard")
    return dashboard_path

def generate_spec_navigation(spec_files, spec_metadata_collection):
    """Generate navigation entries for specs with status indicators."""
    nav_entries = []

    # Create a mapping from filename to metadata
    metadata_map = {metadata['filename']: metadata for metadata in spec_metadata_collection}

    # Sort spec files chronologically
    sorted_files = sorted(spec_files, key=get_spec_sort_key)

    for filename in sorted_files:
        source_path = Path('project/specs') / filename
        title = extract_title_from_spec(source_path)

        # Add status indicator to navigation title
        metadata = metadata_map.get(filename, {})
        status = metadata.get('status', 'draft')

        # Status emojis
        status_icons = {
            'draft': '📝',
            'review': '👀',
            'approved': '✅',
            'in-progress': '🚧',
            'completed': '🎉'
        }

        icon = status_icons.get(status, '📝')
        nav_title = f"{icon} {title}"

        nav_entry = {nav_title: f'engineering/specs/{filename}'}
        nav_entries.append(nav_entry)

    return nav_entries

def update_mkdocs_nav(spec_nav_entries):
    """Update mkdocs.yml with new spec navigation using simple replacement."""
    mkdocs_file = Path('mkdocs.yml')

    if not mkdocs_file.exists():
        raise FileNotFoundError("mkdocs.yml not found")

    # Read the entire file
    with open(mkdocs_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build the specs navigation section
    specs_nav_lines = [
        "      - Specs:",
        "          - Overview: engineering/specs/index.md"
    ]

    for entry in spec_nav_entries:
        for title, path in entry.items():
            specs_nav_lines.append(f"          - {title}: {path}")

    specs_section = "\n".join(specs_nav_lines)

    # Replace just the Specs section content
    # Find the pattern: "      - Specs:" followed by its content until the next section
    specs_pattern = r'      - Specs:.*?(?=\n      - PM Workflows \(Legacy\):)'

    updated_content = re.sub(specs_pattern, specs_section, content, flags=re.DOTALL)

    # Write back to file
    with open(mkdocs_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("Updated mkdocs.yml navigation")

def create_specs_index():
    """Create an index page for the specs section."""
    index_path = Path('mkdocs-docs/engineering/specs/index.md')
    index_path.parent.mkdir(parents=True, exist_ok=True)

    content = """# Specifications

This section contains the complete PM specifications for NextPM features. These are the single source of truth for all feature planning and requirements.

## About These Specs

- **Source**: Files are automatically published from `project/specs/` directory
- **Format**: Each spec follows the NextPM specification template
- **Workflow**: PMs work directly on these files - no manual copying required
- **Navigation**: This page and navigation are auto-generated during build

## Spec Naming Convention

- **Format**: `YYYY-MM-DD-nn-descriptive-name.md`
- **Example**: `2026-02-09-01-engineering-history-tracking.md`
- **Exception**: `0.00-project-start.md` (grandfathered first spec)

## Legacy Migration

The [PM Workflows (Legacy)](../pm-workflows/index.md) section contains manually created summaries from before the automated publishing system. These will remain for reference during the transition period.

For development implementation summaries, see [Dev Workflows](../dev-workflows/index.md).
"""

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Created specs index page")

def update_mkdocs_nav(spec_nav_entries):
    """Update mkdocs.yml with new spec navigation using simple replacement."""
    mkdocs_file = Path('mkdocs.yml')

    if not mkdocs_file.exists():
        raise FileNotFoundError("mkdocs.yml not found")

    # Read the entire file
    with open(mkdocs_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build the specs navigation section
    specs_nav_lines = [
        "      - Specs:",
        "          - Overview: engineering/specs/index.md"
    ]

    for entry in spec_nav_entries:
        for title, path in entry.items():
            specs_nav_lines.append(f"          - {title}: {path}")

    specs_section = "\n".join(specs_nav_lines)

    # Replace just the Specs section content
    # Find the pattern: "      - Specs:" followed by its content until the next section
    specs_pattern = r'      - Specs:.*?(?=\n      - PM Workflows \(Legacy\):)'

    updated_content = re.sub(specs_pattern, specs_section, content, flags=re.DOTALL)

    # Write back to file
    with open(mkdocs_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("Updated mkdocs.yml navigation")

def create_specs_index():
    """Create an index page for the specs section."""
    index_path = Path('mkdocs-docs/engineering/specs/index.md')
    index_path.parent.mkdir(parents=True, exist_ok=True)

    content = """# Specifications

This section contains the complete PM specifications for NextPM features. These are the single source of truth for all feature planning and requirements.

## About These Specs

- **Source**: Files are automatically published from `project/specs/` directory
- **Format**: Each spec follows the NextPM specification template
- **Workflow**: PMs work directly on these files - no manual copying required
- **Navigation**: This page and navigation are auto-generated during build

## Spec Naming Convention

- **Format**: `YYYY-MM-DD-nn-descriptive-name.md`
- **Example**: `2026-02-09-01-engineering-history-tracking.md`
- **Exception**: `0.00-project-start.md` (grandfathered first spec)

## Legacy Migration

The [PM Workflows (Legacy)](../pm-workflows/index.md) section contains manually created summaries from before the automated publishing system. These will remain for reference during the transition period.

For development implementation summaries, see [Dev Workflows](../dev-workflows/index.md).
"""

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Created specs index page")

def main():
    """Enhanced build process with state management and dashboard generation."""
    print("NextPM Enhanced Spec Build Process")
    print("=" * 40)

    try:
        # Change to project root directory
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        os.chdir(project_root)

        print(f"Working directory: {os.getcwd()}")

        # Step 1: Copy specs to docs directory with enhanced processing
        print("\n1. Copying and processing spec files...")
        spec_files, spec_metadata = copy_specs_to_docs()
        print(f"Processed {len(spec_files)} spec files with state management")

        # Step 2: Generate dashboard
        print("\n2. Generating interactive dashboard...")
        generate_spec_dashboard(spec_metadata)

        # Step 3: Generate navigation with status indicators
        print("\n3. Generating enhanced navigation...")
        spec_nav = generate_spec_navigation(spec_files, spec_metadata)

        # Step 4: Update mkdocs.yml
        print("\n4. Updating mkdocs.yml...")
        update_mkdocs_nav(spec_nav)

        # Step 5: Create index page
        print("\n5. Creating specs index...")
        create_specs_index()

        # Step 6: Generate automated dev workflows
        print("\n6. Generating automated dev workflows...")
        generated_workflows = auto_generate_dev_workflow(spec_metadata)
        if generated_workflows:
            print(f"Generated {len(generated_workflows)} dev workflow summaries")
        else:
            print("No dev workflows generated (no commits found)")

        # Step 7: Prepare search infrastructure (for future implementation)
        print("\n7. Preparing search infrastructure...")
        print("Search index generation: Ready for Phase 3 implementation")

        print("\nEnhanced build completed successfully!")
        print(f"Published {len(spec_files)} specifications with visual timelines")

        # Print summary statistics
        status_counts = {}
        for metadata in spec_metadata:
            status = metadata.get('status', 'draft')
            status_counts[status] = status_counts.get(status, 0) + 1

        print("\nSpec Status Summary:")
        for status, count in status_counts.items():
            print(f"  {status.replace('-', ' ').title()}: {count}")

    except Exception as e:
        print(f"\nBuild failed: {e}")
        raise

if __name__ == '__main__':
    main()