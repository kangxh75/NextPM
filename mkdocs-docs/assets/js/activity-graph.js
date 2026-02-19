/**
 * Activity Graph Visualization with D3.js
 * Gitflow-style timeline showing specs, commits, and PRs
 */

(function() {
    'use strict';

    // Graph configuration
    const config = {
        margin: { top: 50, right: 50, bottom: 50, left: 100 },
        masterBranchY: 100,
        branchSpacing: 80,
        nodeRadius: 8,
        prNodeWidth: 120,
        prNodeHeight: 40,
        colors: {
            spec: '#667eea',        // Indigo for specs
            commit: '#6b7280',      // Gray for commits
            pr: '#764ba2',          // Purple for PRs
            branch: '#9ca3af',      // Light gray for branches
            master: '#374151'       // Dark gray for master
        }
    };

    let timelineData = null;
    let svg = null;
    let width = 0;
    let height = 0;
    let xScale = null;
    let zoom = null;

    /**
     * Initialize the activity graph
     */
    async function init() {
        // Check if D3.js is loaded
        if (typeof d3 === 'undefined') {
            console.warn('D3.js not loaded, skipping activity graph');
            return;
        }

        const container = document.getElementById('activity-graph-container');
        if (!container) {
            console.warn('Activity graph container not found');
            return;
        }

        try {
            // Load timeline data
            const response = await fetch('../../assets/js/activity-timeline.json');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            timelineData = data.events || [];

            if (timelineData.length === 0) {
                showEmptyState(container);
                return;
            }

            // Initialize D3 visualization
            initializeGraph(container);
            renderGraph();

        } catch (error) {
            console.error('Failed to load activity timeline:', error);
            showErrorState(container);
        }
    }

    /**
     * Initialize D3 SVG canvas and scales
     */
    function initializeGraph(container) {
        // Set dimensions
        const containerWidth = container.clientWidth || 1200;
        width = containerWidth - config.margin.left - config.margin.right;
        height = 600 - config.margin.top - config.margin.bottom;

        // Create SVG
        svg = d3.select(container)
            .append('svg')
            .attr('width', containerWidth)
            .attr('height', 600)
            .attr('class', 'activity-graph');

        // Create main group for zoom/pan
        const g = svg.append('g')
            .attr('class', 'graph-content')
            .attr('transform', `translate(${config.margin.left},${config.margin.top})`);

        // Setup zoom behavior
        zoom = d3.zoom()
            .scaleExtent([0.5, 3])
            .on('zoom', (event) => {
                g.attr('transform', `translate(${config.margin.left},${config.margin.top}) ${event.transform}`);
            });

        svg.call(zoom);

        // Parse dates and create time scale
        const dates = timelineData
            .map(d => new Date(d.date))
            .filter(d => !isNaN(d));

        if (dates.length === 0) {
            console.error('No valid dates found in timeline data');
            return;
        }

        const minDate = d3.min(dates);
        const maxDate = d3.max(dates);

        // Add some padding to the date range
        const dateRange = maxDate - minDate;
        const paddedMin = new Date(minDate.getTime() - dateRange * 0.1);
        const paddedMax = new Date(maxDate.getTime() + dateRange * 0.1);

        xScale = d3.scaleTime()
            .domain([paddedMin, paddedMax])
            .range([0, width]);
    }

    /**
     * Render the complete graph
     */
    function renderGraph() {
        const g = svg.select('.graph-content');

        // Draw master branch line
        drawMasterBranch(g);

        // Draw time axis
        drawTimeAxis(g);

        // Group events by spec
        const specGroups = groupEventsBySpec();

        // Draw each spec's development flow
        let branchIndex = 0;
        for (const [specId, events] of Object.entries(specGroups)) {
            drawSpecFlow(g, specId, events, branchIndex);
            branchIndex++;
        }

        // Add legend
        drawLegend(g);
    }

    /**
     * Draw the master branch horizontal line
     */
    function drawMasterBranch(g) {
        g.append('line')
            .attr('class', 'master-branch')
            .attr('x1', 0)
            .attr('y1', config.masterBranchY)
            .attr('x2', width)
            .attr('y2', config.masterBranchY)
            .attr('stroke', config.colors.master)
            .attr('stroke-width', 3);

        // Add master branch label
        g.append('text')
            .attr('class', 'branch-label')
            .attr('x', -10)
            .attr('y', config.masterBranchY + 5)
            .attr('text-anchor', 'end')
            .attr('fill', config.colors.master)
            .attr('font-size', '12px')
            .attr('font-weight', 'bold')
            .text('master');
    }

    /**
     * Draw time axis
     */
    function drawTimeAxis(g) {
        const axis = d3.axisBottom(xScale)
            .ticks(8)
            .tickFormat(d3.timeFormat('%b %d'));

        g.append('g')
            .attr('class', 'time-axis')
            .attr('transform', `translate(0,${height - 50})`)
            .call(axis);
    }

    /**
     * Group events by spec ID
     */
    function groupEventsBySpec() {
        const groups = {};

        timelineData.forEach(event => {
            const specId = event.spec_id;
            if (!groups[specId]) {
                groups[specId] = [];
            }
            groups[specId].push(event);
        });

        return groups;
    }

    /**
     * Draw development flow for a single spec
     */
    function drawSpecFlow(g, specId, events, branchIndex) {
        const branchY = config.masterBranchY + (branchIndex + 1) * config.branchSpacing;

        // Find spec creation event
        const specEvent = events.find(e => e.type === 'spec_created');
        if (!specEvent) return;

        const startX = xScale(new Date(specEvent.date));

        // Draw feature branch line
        const branchEndX = width; // Extend to end for now

        g.append('line')
            .attr('class', 'feature-branch')
            .attr('x1', startX)
            .attr('y1', config.masterBranchY)
            .attr('x2', startX)
            .attr('y2', branchY)
            .attr('stroke', config.colors.branch)
            .attr('stroke-width', 2)
            .attr('stroke-dasharray', '5,5');

        g.append('line')
            .attr('class', 'feature-branch')
            .attr('x1', startX)
            .attr('y1', branchY)
            .attr('x2', branchEndX)
            .attr('y2', branchY)
            .attr('stroke', config.colors.branch)
            .attr('stroke-width', 2);

        // Draw spec node
        drawSpecNode(g, specEvent, startX, branchY);

        // Draw commits
        events.filter(e => e.type === 'commit').forEach((commit, idx) => {
            const x = xScale(new Date(commit.date));
            drawCommitNode(g, commit, x, branchY);
        });

        // Draw PRs
        events.filter(e => e.type === 'pr_merged').forEach((pr, idx) => {
            const x = xScale(new Date(pr.date));
            drawPRNode(g, pr, x, branchY);

            // Draw merge arrow back to master
            drawMergeArrow(g, x, branchY, x, config.masterBranchY);
        });
    }

    /**
     * Draw spec creation node (diamond shape)
     */
    function drawSpecNode(g, spec, x, y) {
        const diamond = g.append('g')
            .attr('class', 'spec-node')
            .attr('transform', `translate(${x},${y})`)
            .style('cursor', 'pointer')
            .on('click', () => {
                window.location.href = `engineering/specs/${spec.spec_id}.md`;
            });

        // Diamond shape
        diamond.append('path')
            .attr('d', 'M 0,-12 L 12,0 L 0,12 L -12,0 Z')
            .attr('fill', config.colors.spec)
            .attr('stroke', '#fff')
            .attr('stroke-width', 2);

        // Tooltip
        addTooltip(diamond, `
            <strong>📋 Spec Created</strong><br>
            ${spec.title}<br>
            <small>${spec.spec_id}</small><br>
            <small>Status: ${spec.status}</small>
        `);
    }

    /**
     * Draw commit node (circle)
     */
    function drawCommitNode(g, commit, x, y) {
        const node = g.append('g')
            .attr('class', 'commit-node')
            .attr('transform', `translate(${x},${y})`)
            .style('cursor', 'pointer');

        node.append('circle')
            .attr('r', config.nodeRadius)
            .attr('fill', config.colors.commit)
            .attr('stroke', '#fff')
            .attr('stroke-width', 2);

        // Tooltip
        addTooltip(node, `
            <strong>📝 Commit ${commit.hash}</strong><br>
            ${commit.message}<br>
            <small>👤 ${commit.author}</small><br>
            <small>📁 ${commit.files_changed} files</small>
        `);
    }

    /**
     * Draw PR node (rounded rectangle)
     */
    function drawPRNode(g, pr, x, y) {
        const node = g.append('g')
            .attr('class', 'pr-node')
            .attr('transform', `translate(${x},${y})`)
            .style('cursor', 'pointer')
            .on('click', () => {
                if (pr.github_url) {
                    window.open(pr.github_url, '_blank');
                }
            });

        node.append('rect')
            .attr('x', -config.prNodeWidth / 2)
            .attr('y', -config.prNodeHeight / 2)
            .attr('width', config.prNodeWidth)
            .attr('height', config.prNodeHeight)
            .attr('rx', 8)
            .attr('fill', config.colors.pr)
            .attr('stroke', '#fff')
            .attr('stroke-width', 2);

        node.append('text')
            .attr('text-anchor', 'middle')
            .attr('dy', '0.35em')
            .attr('fill', '#fff')
            .attr('font-size', '12px')
            .attr('font-weight', 'bold')
            .text(`PR #${pr.pr_number}`);

        // Tooltip
        addTooltip(node, `
            <strong>🔀 Pull Request #${pr.pr_number}</strong><br>
            ${pr.title}<br>
            <small>👤 ${pr.author}</small><br>
            <small>🌿 ${pr.branch}</small>
        `);
    }

    /**
     * Draw merge arrow
     */
    function drawMergeArrow(g, x1, y1, x2, y2) {
        const curve = d3.linkVertical()
            .x(d => d.x)
            .y(d => d.y);

        const link = curve({
            source: { x: x1, y: y1 },
            target: { x: x2, y: y2 }
        });

        g.append('path')
            .attr('class', 'merge-arrow')
            .attr('d', link)
            .attr('fill', 'none')
            .attr('stroke', config.colors.pr)
            .attr('stroke-width', 2)
            .attr('opacity', 0.6)
            .attr('marker-end', 'url(#arrowhead)');

        // Add arrowhead marker (if not already defined)
        if (svg.select('#arrowhead').empty()) {
            svg.append('defs')
                .append('marker')
                .attr('id', 'arrowhead')
                .attr('viewBox', '0 0 10 10')
                .attr('refX', 5)
                .attr('refY', 5)
                .attr('markerWidth', 6)
                .attr('markerHeight', 6)
                .attr('orient', 'auto')
                .append('path')
                .attr('d', 'M 0 0 L 10 5 L 0 10 z')
                .attr('fill', config.colors.pr);
        }
    }

    /**
     * Add tooltip to node
     */
    function addTooltip(node, content) {
        node.on('mouseenter', function(event) {
            const tooltip = d3.select('body').append('div')
                .attr('class', 'activity-graph-tooltip')
                .style('position', 'absolute')
                .style('background', 'rgba(0, 0, 0, 0.9)')
                .style('color', '#fff')
                .style('padding', '8px 12px')
                .style('border-radius', '4px')
                .style('font-size', '12px')
                .style('pointer-events', 'none')
                .style('z-index', '10000')
                .html(content);

            const [x, y] = d3.pointer(event, document.body);
            tooltip
                .style('left', `${x + 10}px`)
                .style('top', `${y + 10}px`);
        })
        .on('mouseleave', function() {
            d3.selectAll('.activity-graph-tooltip').remove();
        });
    }

    /**
     * Draw legend
     */
    function drawLegend(g) {
        const legend = g.append('g')
            .attr('class', 'legend')
            .attr('transform', `translate(${width - 200}, 20)`);

        const items = [
            { label: 'Spec', color: config.colors.spec, shape: 'diamond' },
            { label: 'Commit', color: config.colors.commit, shape: 'circle' },
            { label: 'Pull Request', color: config.colors.pr, shape: 'rect' }
        ];

        items.forEach((item, i) => {
            const g = legend.append('g')
                .attr('transform', `translate(0, ${i * 25})`);

            if (item.shape === 'diamond') {
                g.append('path')
                    .attr('d', 'M 0,-8 L 8,0 L 0,8 L -8,0 Z')
                    .attr('fill', item.color);
            } else if (item.shape === 'circle') {
                g.append('circle')
                    .attr('r', 6)
                    .attr('fill', item.color);
            } else if (item.shape === 'rect') {
                g.append('rect')
                    .attr('x', -8)
                    .attr('y', -6)
                    .attr('width', 16)
                    .attr('height', 12)
                    .attr('rx', 2)
                    .attr('fill', item.color);
            }

            g.append('text')
                .attr('x', 15)
                .attr('y', 5)
                .attr('font-size', '12px')
                .text(item.label);
        });
    }

    /**
     * Show empty state
     */
    function showEmptyState(container) {
        container.innerHTML = '<div class="activity-graph-empty" style="text-align:center;padding:3rem;color:#9ca3af;"><p>No activity data available yet. Start creating specs and making commits!</p></div>';
    }

    /**
     * Show error state
     */
    function showErrorState(container) {
        container.innerHTML = '<div class="activity-graph-error" style="text-align:center;padding:3rem;color:#ef4444;"><p>Failed to load activity timeline. Please try refreshing the page.</p></div>';
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
