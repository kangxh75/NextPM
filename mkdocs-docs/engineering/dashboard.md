# 📊 NextPM Spec Dashboard

<div class="dashboard-container">

## 📈 Statistics

<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-number">4</div>
        <div class="stat-label">Total Specs</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">0</div>
        <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">1</div>
        <div class="stat-label">In Progress</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Draft</div>
    </div>
</div>

## 🎯 Status Breakdown

<div class="status-breakdown">
    <div class="status-item">
        <span class="spec-state-badge spec-state-draft">Draft</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: 75.0%"></div>
        </div>
        <span class="count">3</span>
    </div>
    <div class="status-item">
        <span class="spec-state-badge spec-state-in-progress">In Progress</span>
        <div class="progress-bar">
            <div class="progress-fill" style="width: 25.0%"></div>
        </div>
        <span class="count">1</span>
    </div>
</div>

## 🔄 Recent Activity

<div class="recent-activity">
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/2026-02-13-01-nextpm-spec-driven-development-showcase.md">2026-02-13-01 NextPM Spec-Driven Development Showcase</a></strong>
            <span class="spec-state-badge spec-state-in-progress" data-status="in-progress" data-priority="high">
    🔥 In Progress
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-13 |
            Priority: High
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/2026-02-10-01-authentication.md">2026-02-10-01 Site Authentication</a></strong>
            <span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-13 |
            Priority: Medium
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/2026-02-09-01-engineering-history-tracking.md">2026-02-09-01 Engineering History Tracking System</a></strong>
            <span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-13 |
            Priority: Medium
        </div>
    </div>
    <div class="activity-item">
        <div class="activity-header">
            <strong><a href="../specs/0.00-project-start.md">0.00 Project Start - NextPM AI-Native Knowledge Hub</a></strong>
            <span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>
        </div>
        <div class="activity-meta">
            Updated: 2026-02-13 |
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
