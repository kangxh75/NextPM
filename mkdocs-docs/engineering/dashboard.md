# 📊 NextPM Spec Dashboard

<div class="dashboard-container">

## 🔍 Search & Filter

<div class="search-section">
    <div class="search-bar">
        <input type="text" id="spec-search" placeholder="Search specifications..." class="search-input" />
        <button id="clear-search" class="clear-button">Clear</button>
    </div>
    <div class="filter-row">
        <select id="status-filter" class="filter-dropdown">
            <option value="all">All Statuses</option>
        </select>
        <select id="priority-filter" class="filter-dropdown">
            <option value="all">All Priorities</option>
        </select>
        <select id="category-filter" class="filter-dropdown">
            <option value="all">All Categories</option>
        </select>
    </div>
    <div class="search-stats">
        <span id="search-stats">Showing 6 specifications</span>
    </div>
</div>

<div id="search-results" class="search-results-container">
    <!-- Search results will be populated here by JavaScript -->
</div>

## 📈 Statistics

<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-number">6</div>
        <div class="stat-label">Total Specs</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">0</div>
        <div class="stat-label">In Progress</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Draft</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">0</div>
        <div class="stat-label">Commits</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Pull Requests</div>
    </div>
</div>

## 🎯 Status Breakdown

<div class="status-breakdown">
    <div class="status-item">
        <span class="spec-state-badge spec-state-draft">Draft</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: 50.0%"></div>
        </div>
        <span class="count">3</span>
    </div>
    <div class="status-item">
        <span class="spec-state-badge spec-state-completed">Completed</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: 50.0%"></div>
        </div>
        <span class="count">3</span>
    </div>
</div>

## 🔄 Recent Activity

<div class="recent-activity">
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/20260219-pr-workflow.md">20260219-pr-workflow</a></strong>
            <span class="spec-state-badge spec-state-completed" data-status="completed" data-priority="high">
    🔥 Completed
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-19 |
            Priority: High
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/20260219-pr-tracking.md">20260219-pr-tracking</a></strong>
            <span class="spec-state-badge spec-state-completed" data-status="completed" data-priority="high">
    🔥 Completed
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-19 |
            Priority: High
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/20260219-dashboard.md">20260219-dashboard</a></strong>
            <span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-19 |
            Priority: Medium
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/20260213-spec-showcase.md">20260213-spec-showcase</a></strong>
            <span class="spec-state-badge spec-state-completed" data-status="completed" data-priority="high">
    🔥 Completed
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-19 |
            Priority: High
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/20260213-build-flow.md">20260213-build-flow</a></strong>
            <span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-19 |
            Priority: Medium
        </div>
    </div>
</div>

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
<script src="../../mkdocs-static/js/nextpm-search.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Initialize dashboard animations
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Animate progress bars
    const progressFills = document.querySelectorAll('.progress-fill');
    progressFills.forEach(fill => {
        setTimeout(() => {
            fill.style.transform = 'scaleX(1)';
        }, 500);
    });
});
</script>
