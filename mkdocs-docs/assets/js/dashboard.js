/**
 * Dashboard Table Controller
 * Loads spec data from search-index.json and renders interactive sortable table
 */

(function() {
    'use strict';

    let specsData = [];
    let currentSort = { column: 'updated', ascending: false }; // Default: newest first

    /**
     * Initialize dashboard when DOM is ready
     */
    function init() {
        // Hide right sidebar and maximize content width
        const rightSidebar = document.querySelector('.md-sidebar--secondary');
        if (rightSidebar) {
            rightSidebar.style.display = 'none';
        }

        const mdContent = document.querySelector('.md-content');
        if (mdContent) {
            mdContent.style.maxWidth = 'none';
        }

        const mdContentInner = document.querySelector('.md-content__inner');
        if (mdContentInner) {
            mdContentInner.style.maxWidth = '100%';
            mdContentInner.style.marginLeft = '0';
            mdContentInner.style.marginRight = '0';
        }

        loadSpecsData();
    }

    /**
     * Load specs from search-index.json
     */
    async function loadSpecsData() {
        try {
            const response = await fetch('../../assets/js/search-index.json');
            const data = await response.json();
            specsData = data.index || [];

            renderTable();
            attachEventListeners();
        } catch (error) {
            console.error('Failed to load specs data:', error);
            document.getElementById('specs-table-body').innerHTML =
                '<tr><td colspan="5" style="text-align:center;padding:2rem;">Failed to load specifications data</td></tr>';
        }
    }

    /**
     * Render table rows from specs data
     */
    function renderTable() {
        const tbody = document.getElementById('specs-table-body');
        if (!tbody) {
            console.error('Table body not found!');
            return;
        }

        // Sort data based on current sort settings
        const sortedData = sortData([...specsData]);

        // Clear existing rows
        tbody.innerHTML = '';

        // Generate and append table rows
        sortedData.forEach(spec => {
            const row = createTableRow(spec);
            tbody.appendChild(row);
        });
    }

    /**
     * Create HTML for a single table row
     */
    function createTableRow(spec) {
        const statusBadge = getStatusBadge(spec.status);
        const specUrl = spec.url || `engineering/specs/${spec.filename}`;
        const lastUpdated = formatDate(spec.last_updated);

        // Create row element
        const row = document.createElement('tr');
        row.className = 'spec-row';
        row.setAttribute('data-spec-id', spec.id);

        // Create cells (removed title column since it's duplicate of ID)
        const cells = [
            { class: 'spec-id', html: `<a href="${specUrl}">${spec.id}</a>` },
            { class: 'spec-status', html: statusBadge },
            { class: 'spec-commits', html: spec.git_commits || 0 },
            { class: 'spec-prs', html: spec.pull_requests || 0 },
            { class: 'spec-updated', html: lastUpdated }
        ];

        cells.forEach((cellData, index) => {
            const td = document.createElement('td');
            td.className = cellData.class;
            td.innerHTML = cellData.html;
            row.appendChild(td);

            // Debug: log first row's cells
            if (spec.id === specsData[0].id && index === 0) {
                console.log('First spec first cell:', {
                    class: cellData.class,
                    html: cellData.html,
                    cellCount: cells.length
                });
            }
        });

        return row;  // Return DOM element directly instead of outerHTML
    }

    /**
     * Get status badge HTML
     */
    function getStatusBadge(status) {
        const badges = {
            'draft': '<span class="spec-state-badge spec-state-draft">📋 Draft</span>',
            'in-progress': '<span class="spec-state-badge spec-state-in-progress">🚧 In Progress</span>',
            'completed': '<span class="spec-state-badge spec-state-completed">✅ Completed</span>',
            'archived': '<span class="spec-state-badge spec-state-archived">📦 Archived</span>'
        };
        return badges[status] || badges['draft'];
    }

    /**
     * Get priority badge HTML
     */
    function getPriorityBadge(priority) {
        const badges = {
            'low': '<span class="priority-badge priority-low">▽ Low</span>',
            'medium': '<span class="priority-badge priority-medium">◇ Medium</span>',
            'high': '<span class="priority-badge priority-high">△ High</span>',
            'critical': '<span class="priority-badge priority-critical">⚠️ Critical</span>'
        };
        return badges[priority] || badges['medium'];
    }

    /**
     * Format date string
     */
    function formatDate(dateString) {
        if (!dateString) return '-';
        const date = new Date(dateString);
        if (isNaN(date)) return dateString;

        const now = new Date();
        const diffMs = now - date;
        const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

        if (diffDays === 0) return 'Today';
        if (diffDays === 1) return 'Yesterday';
        if (diffDays < 7) return `${diffDays} days ago`;

        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    }

    /**
     * Sort specs data by column
     */
    function sortData(data) {
        const column = currentSort.column;
        const ascending = currentSort.ascending;

        return data.sort((a, b) => {
            let valA, valB;

            switch(column) {
                case 'id':
                    valA = a.id || '';
                    valB = b.id || '';
                    break;
                case 'title':
                    valA = a.title || '';
                    valB = b.title || '';
                    break;
                case 'status':
                    valA = a.status || '';
                    valB = b.status || '';
                    break;
                case 'priority':
                    const priorityOrder = { 'low': 1, 'medium': 2, 'high': 3, 'critical': 4 };
                    valA = priorityOrder[a.priority] || 0;
                    valB = priorityOrder[b.priority] || 0;
                    break;
                case 'estimated_hours':
                    valA = a.estimated_hours || 0;
                    valB = b.estimated_hours || 0;
                    break;
                case 'actual_hours':
                    valA = a.actual_hours || 0;
                    valB = b.actual_hours || 0;
                    break;
                case 'commits':
                    valA = a.git_commits || 0;
                    valB = b.git_commits || 0;
                    break;
                case 'prs':
                    valA = a.pull_requests || 0;
                    valB = b.pull_requests || 0;
                    break;
                case 'updated':
                    valA = new Date(a.last_updated || 0);
                    valB = new Date(b.last_updated || 0);
                    break;
                case 'assignee':
                    valA = a.assignee || '';
                    valB = b.assignee || '';
                    break;
                default:
                    return 0;
            }

            // Compare values
            if (valA < valB) return ascending ? -1 : 1;
            if (valA > valB) return ascending ? 1 : -1;
            return 0;
        });
    }

    /**
     * Attach event listeners
     */
    function attachEventListeners() {
        // Sort by column headers
        const headers = document.querySelectorAll('.specs-table th.sortable');
        headers.forEach(header => {
            header.addEventListener('click', function() {
                const column = this.getAttribute('data-sort');
                handleSort(column);
            });
        });

        // Make rows clickable (navigate to spec)
        document.addEventListener('click', function(e) {
            const row = e.target.closest('.spec-row');
            if (row && !e.target.closest('a')) {
                const link = row.querySelector('.spec-id a');
                if (link) {
                    window.location.href = link.href;
                }
            }
        });
    }

    /**
     * Handle sort by column
     */
    function handleSort(column) {
        // Toggle direction if clicking same column
        if (currentSort.column === column) {
            currentSort.ascending = !currentSort.ascending;
        } else {
            currentSort.column = column;
            currentSort.ascending = true;
        }

        // Update sort indicators
        updateSortIndicators();

        // Re-render table
        renderTable();
    }

    /**
     * Update visual sort indicators in table headers
     */
    function updateSortIndicators() {
        const headers = document.querySelectorAll('.specs-table th.sortable');
        headers.forEach(header => {
            const column = header.getAttribute('data-sort');
            header.classList.remove('sort-asc', 'sort-desc');

            if (column === currentSort.column) {
                header.classList.add(currentSort.ascending ? 'sort-asc' : 'sort-desc');
            }
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
