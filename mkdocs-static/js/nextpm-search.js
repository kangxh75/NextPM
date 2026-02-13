/**
 * NextPM Search System
 * Client-side search and filtering for specifications
 */

class NextPMSearch {
    constructor() {
        this.searchIndex = null;
        this.currentResults = [];
        this.filters = {
            status: 'all',
            priority: 'all',
            category: 'all'
        };
        this.init();
    }

    async init() {
        try {
            await this.loadSearchIndex();
            this.setupEventListeners();
            this.initializeFilters();
            console.log('NextPM Search initialized successfully');
        } catch (error) {
            console.error('Failed to initialize NextPM Search:', error);
        }
    }

    async loadSearchIndex() {
        try {
            const response = await fetch('/mkdocs-static/js/search-index.json');
            if (!response.ok) throw new Error('Failed to load search index');
            this.searchIndex = await response.json();
            console.log(`Loaded search index with ${this.searchIndex.total_specs} specs`);
        } catch (error) {
            console.error('Error loading search index:', error);
            throw error;
        }
    }

    setupEventListeners() {
        const searchInput = document.getElementById('spec-search');
        const statusFilter = document.getElementById('status-filter');
        const priorityFilter = document.getElementById('priority-filter');
        const categoryFilter = document.getElementById('category-filter');
        const clearButton = document.getElementById('clear-search');

        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.performSearch(e.target.value);
            });
        }

        if (statusFilter) {
            statusFilter.addEventListener('change', (e) => {
                this.filters.status = e.target.value;
                this.applyFilters();
            });
        }

        if (priorityFilter) {
            priorityFilter.addEventListener('change', (e) => {
                this.filters.priority = e.target.value;
                this.applyFilters();
            });
        }

        if (categoryFilter) {
            categoryFilter.addEventListener('change', (e) => {
                this.filters.category = e.target.value;
                this.applyFilters();
            });
        }

        if (clearButton) {
            clearButton.addEventListener('click', () => {
                this.clearSearch();
            });
        }
    }

    initializeFilters() {
        if (!this.searchIndex) return;

        const statuses = [...new Set(this.searchIndex.index.map(spec => spec.status))];
        const priorities = [...new Set(this.searchIndex.index.map(spec => spec.priority))];
        const categories = [...new Set(this.searchIndex.index.map(spec => spec.category))];

        this.populateFilterDropdown('status-filter', statuses);
        this.populateFilterDropdown('priority-filter', priorities);
        this.populateFilterDropdown('category-filter', categories);
    }

    populateFilterDropdown(elementId, options) {
        const dropdown = document.getElementById(elementId);
        if (!dropdown) return;

        // Clear existing options except "All"
        while (dropdown.children.length > 1) {
            dropdown.removeChild(dropdown.lastChild);
        }

        options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option.charAt(0).toUpperCase() + option.slice(1).replace('-', ' ');
            dropdown.appendChild(optionElement);
        });
    }

    performSearch(query) {
        if (!this.searchIndex || !query || query.trim().length < 2) {
            this.currentResults = this.searchIndex ? this.searchIndex.index : [];
            this.displayResults(this.currentResults);
            return;
        }

        const searchTerm = query.toLowerCase().trim();
        const results = this.searchIndex.index.filter(spec => {
            return spec.title.toLowerCase().includes(searchTerm) ||
                   spec.content.includes(searchTerm) ||
                   spec.demonstrates.some(demo => demo.toLowerCase().includes(searchTerm)) ||
                   spec.category.toLowerCase().includes(searchTerm);
        });

        // Sort results by relevance
        results.sort((a, b) => {
            const aTitle = a.title.toLowerCase().includes(searchTerm) ? 10 : 0;
            const bTitle = b.title.toLowerCase().includes(searchTerm) ? 10 : 0;
            const aContent = a.content.includes(searchTerm) ? 5 : 0;
            const bContent = b.content.includes(searchTerm) ? 5 : 0;

            return (bTitle + bContent) - (aTitle + aContent);
        });

        this.currentResults = results;
        this.applyFilters();
    }

    applyFilters() {
        let filteredResults = this.currentResults;

        if (this.filters.status !== 'all') {
            filteredResults = filteredResults.filter(spec => spec.status === this.filters.status);
        }

        if (this.filters.priority !== 'all') {
            filteredResults = filteredResults.filter(spec => spec.priority === this.filters.priority);
        }

        if (this.filters.category !== 'all') {
            filteredResults = filteredResults.filter(spec => spec.category === this.filters.category);
        }

        this.displayResults(filteredResults);
        this.updateSearchStats(filteredResults.length);
    }

    displayResults(results) {
        const resultsContainer = document.getElementById('search-results');
        if (!resultsContainer) return;

        if (results.length === 0) {
            resultsContainer.innerHTML = `
                <div class="no-results">
                    <div class="no-results-icon">🔍</div>
                    <div class="no-results-text">No specifications found matching your criteria.</div>
                    <div class="no-results-suggestion">Try adjusting your search terms or filters.</div>
                </div>
            `;
            return;
        }

        resultsContainer.innerHTML = results.map((spec, index) => {
            const statusIcon = this.getStatusIcon(spec.status);
            const priorityColor = this.getPriorityColor(spec.priority);

            return `
                <div class="search-result-item" style="animation-delay: ${index * 0.1}s">
                    <div class="search-result-header">
                        <h3 class="search-result-title">
                            <a href="${spec.url}">${spec.title}</a>
                        </h3>
                        <div class="search-result-badges">
                            <span class="spec-state-badge spec-state-${spec.status}">
                                ${statusIcon} ${spec.status.replace('-', ' ').toUpperCase()}
                            </span>
                            <span class="priority-badge priority-${spec.priority}" style="border-left-color: ${priorityColor}">
                                ${spec.priority.toUpperCase()}
                            </span>
                        </div>
                    </div>
                    <div class="search-result-meta">
                        <span class="result-meta-item">📂 ${spec.category.replace('-', ' ')}</span>
                        <span class="result-meta-item">⏱️ ${spec.estimated_hours}h estimated</span>
                        <span class="result-meta-item">📝 ${spec.git_commits} commits</span>
                        <span class="result-meta-item">👤 ${spec.assignee}</span>
                    </div>
                    <div class="search-result-preview">
                        ${this.getPreviewText(spec.content)}
                    </div>
                    <div class="search-result-demonstrates">
                        ${spec.demonstrates.map(demo =>
                            `<span class="demo-tag">${demo.replace('-', ' ')}</span>`
                        ).join('')}
                    </div>
                </div>
            `;
        }).join('');

        // Animate results
        const resultItems = resultsContainer.querySelectorAll('.search-result-item');
        resultItems.forEach((item, index) => {
            setTimeout(() => {
                item.classList.add('animated');
            }, index * 50);
        });
    }

    getStatusIcon(status) {
        const icons = {
            'draft': '📝',
            'review': '👀',
            'approved': '✅',
            'in-progress': '🚧',
            'completed': '🎉'
        };
        return icons[status] || '📝';
    }

    getPriorityColor(priority) {
        const colors = {
            'high': '#ff3b30',
            'medium': '#ff9500',
            'low': '#30d158'
        };
        return colors[priority] || '#6c757d';
    }

    getPreviewText(content) {
        // Extract first meaningful sentence
        const sentences = content.split('.').filter(s => s.trim().length > 20);
        const preview = sentences[0] || content;
        return preview.length > 150 ? preview.substring(0, 150) + '...' : preview;
    }

    updateSearchStats(resultCount) {
        const statsElement = document.getElementById('search-stats');
        if (statsElement) {
            const totalSpecs = this.searchIndex ? this.searchIndex.total_specs : 0;
            statsElement.textContent = `Showing ${resultCount} of ${totalSpecs} specifications`;
        }
    }

    clearSearch() {
        const searchInput = document.getElementById('spec-search');
        const statusFilter = document.getElementById('status-filter');
        const priorityFilter = document.getElementById('priority-filter');
        const categoryFilter = document.getElementById('category-filter');

        if (searchInput) searchInput.value = '';
        if (statusFilter) statusFilter.value = 'all';
        if (priorityFilter) priorityFilter.value = 'all';
        if (categoryFilter) categoryFilter.value = 'all';

        this.filters = { status: 'all', priority: 'all', category: 'all' };
        this.currentResults = this.searchIndex ? this.searchIndex.index : [];
        this.displayResults(this.currentResults);
        this.updateSearchStats(this.currentResults.length);
    }
}

// Initialize search when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Only initialize search on pages that have search functionality
    if (document.getElementById('spec-search') || document.getElementById('search-results')) {
        window.nextPMSearch = new NextPMSearch();
    }

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