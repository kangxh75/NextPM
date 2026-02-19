# 📊 NextPM Spec Dashboard

## 📋 Spec Table

<div class="specs-table-container">
    <table class="specs-table" id="specs-table">
        <thead>
            <tr>
                <th data-sort="id" class="sortable">Spec ID</th>
                <th data-sort="status" class="sortable">Status</th>
                <th data-sort="commits" class="sortable">Commits</th>
                <th data-sort="prs" class="sortable">PRs</th>
                <th data-sort="updated" class="sortable">Last Updated</th>
            </tr>
        </thead>
        <tbody id="specs-table-body">
            <!-- Table rows will be populated by JavaScript from search-index.json -->
        </tbody>
    </table>
</div>

## 📈 Development History

<div id="activity-graph-container" style="width: 100%; min-height: 600px; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); padding: 1rem; margin: 2rem 0;">
    <div style="text-align: center; padding: 3rem; color: #9ca3af;">
        <p>Loading activity graph...</p>
    </div>
</div>

<!-- Dashboard Styles and JavaScript -->
<link rel="stylesheet" href="../../assets/css/dashboard.css?v=10">
<script src="../../assets/js/dashboard.js?v=6"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="../../assets/js/activity-graph.js?v=3"></script>
