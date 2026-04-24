/**
 * Smart Review Analyzer - Frontend JavaScript
 * Handles all UI interactions and API communication
 */

// ==================== Configuration ====================

const API_BASE_URL = 'http://localhost:5000';
let analysisResults = null;
let sentimentChart = null;

// ==================== DOM Elements ====================

const reviewInput = document.getElementById('reviewInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const clearBtn = document.getElementById('clearBtn');
const loadingSpinner = document.getElementById('loadingSpinner');
const resultsSection = document.getElementById('resultsSection');
const emptyState = document.getElementById('emptyState');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');
const filterButtons = document.querySelectorAll('.filter-btn');

// ==================== Event Listeners ====================

document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    showEmptyState();
});

function setupEventListeners() {
    analyzeBtn.addEventListener('click', analyzeReviews);
    clearBtn.addEventListener('click', clearInput);
    
    filterButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            filterReviews(this.dataset.filter);
        });
    });
}

// ==================== Main Analysis Function ====================

async function analyzeReviews() {
    const reviewsText = reviewInput.value.trim();
    
    // Validation
    if (!reviewsText) {
        showError('Please enter at least one review');
        return;
    }
    
    // Split reviews by newline and filter empty lines
    const reviews = reviewsText
        .split('\n')
        .map(r => r.trim())
        .filter(r => r.length > 0);
    
    if (reviews.length === 0) {
        showError('Please enter valid reviews');
        return;
    }
    
    // Show loading
    showLoading();
    
    try {
        // Make API request
        const response = await fetch(`${API_BASE_URL}/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                texts: reviews,
                summary_sentences: 2
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Analysis failed');
        }
        
        const data = await response.json();
        
        if (!data.success) {
            throw new Error(data.error || 'Analysis failed');
        }
        
        // Store results and display
        analysisResults = data.analysis;
        displayResults();
        hideLoading();
        
    } catch (error) {
        hideLoading();
        showError(`Error: ${error.message}`);
        console.error('Analysis error:', error);
    }
}

// ==================== Display Functions ====================

function displayResults() {
    // Hide empty state
    emptyState.classList.add('hidden');
    resultsSection.classList.remove('hidden');
    
    // Display sentiment statistics
    displaySentimentStats();
    
    // Display keywords
    displayKeywords();
    
    // Display summary
    displaySummary();
    
    // Display reviews
    displayReviews();
    
    // Create pie chart
    createSentimentChart();
    
    // Reset filters
    resetFilters();
}

function displaySentimentStats() {
    const stats = analysisResults.statistics;
    
    document.getElementById('positiveCount').textContent = stats.positive;
    document.getElementById('negativeCount').textContent = stats.negative;
    document.getElementById('neutralCount').textContent = stats.neutral;
    
    document.getElementById('positivePercent').textContent = stats.positive_percent + '%';
    document.getElementById('negativePercent').textContent = stats.negative_percent + '%';
    document.getElementById('neutralPercent').textContent = stats.neutral_percent + '%';
}

function displayKeywords() {
    const keywordsList = document.getElementById('keywordsList');
    keywordsList.innerHTML = '';
    
    if (!analysisResults.keywords || analysisResults.keywords.length === 0) {
        keywordsList.innerHTML = '<p style="color: #999;">No keywords found</p>';
        return;
    }
    
    analysisResults.keywords.forEach(kw => {
        const keywordTag = document.createElement('div');
        keywordTag.className = 'keyword-tag';
        keywordTag.innerHTML = `
            ${kw.word}
            <span class="keyword-score">${(kw.score * 100).toFixed(1)}%</span>
        `;
        keywordsList.appendChild(keywordTag);
    });
}

function displaySummary() {
    const summaryText = document.getElementById('summaryText');
    summaryText.textContent = analysisResults.summary || 'No summary available';
}

function displayReviews() {
    const reviewsList = document.getElementById('reviewsList');
    reviewsList.innerHTML = '';
    
    analysisResults.sentiments.forEach((item, index) => {
        const reviewCard = createReviewCard(item, index);
        reviewsList.appendChild(reviewCard);
    });
}

function createReviewCard(sentimentItem, index) {
    const card = document.createElement('div');
    const sentimentClass = sentimentItem.sentiment.toLowerCase();
    
    card.className = `review-card ${sentimentClass}`;
    card.dataset.sentiment = sentimentItem.sentiment;
    card.dataset.index = index;
    
    // Determine sentiment icon and emoji
    let sentimentEmoji = '➖';
    if (sentimentClass === 'positive') sentimentEmoji = '✅';
    else if (sentimentClass === 'negative') sentimentEmoji = '❌';
    
    card.innerHTML = `
        <div class="review-header">
            <span class="review-sentiment ${sentimentClass}">
                ${sentimentEmoji} ${sentimentItem.sentiment}
            </span>
        </div>
        <p class="review-text">${escapeHtml(sentimentItem.text)}</p>
        <p class="review-polarity">Polarity Score: ${sentimentItem.polarity}</p>
    `;
    
    return card;
}

function filterReviews(sentiment) {
    const reviewCards = document.querySelectorAll('.review-card');
    
    reviewCards.forEach(card => {
        if (sentiment === 'all') {
            card.classList.remove('hidden');
        } else {
            const cardSentiment = card.dataset.sentiment;
            if (cardSentiment === sentiment) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        }
    });
}

function createSentimentChart() {
    const ctx = document.getElementById('sentimentChart').getContext('2d');
    const stats = analysisResults.statistics;
    
    // Destroy previous chart if exists
    if (sentimentChart) {
        sentimentChart.destroy();
    }
    
    sentimentChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Negative', 'Neutral'],
            datasets: [{
                data: [
                    stats.positive,
                    stats.negative,
                    stats.neutral
                ],
                backgroundColor: [
                    '#27ae60',  // Green for positive
                    '#e74c3c',  // Red for negative
                    '#95a5a6'   // Gray for neutral
                ],
                borderColor: '#fff',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 15,
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

function resetFilters() {
    filterButtons.forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.filter === 'all') {
            btn.classList.add('active');
        }
    });
}

// ==================== UI State Functions ====================

function showLoading() {
    loadingSpinner.classList.remove('hidden');
    analyzeBtn.disabled = true;
}

function hideLoading() {
    loadingSpinner.classList.add('hidden');
    analyzeBtn.disabled = false;
}

function showEmptyState() {
    emptyState.classList.remove('hidden');
    resultsSection.classList.add('hidden');
}

function showError(message) {
    errorText.textContent = message;
    errorMessage.classList.remove('hidden');
    
    // Auto-hide after 5 seconds
    setTimeout(closeError, 5000);
}

function closeError() {
    errorMessage.classList.add('hidden');
}

// ==================== Utility Functions ====================

function clearInput() {
    reviewInput.value = '';
    showEmptyState();
    resetFilters();
    reviewInput.focus();
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ==================== Real-time Analysis (Optional Feature) ====================

// Uncomment to enable real-time analysis as user types
/*
let analysisTimeout;
reviewInput.addEventListener('input', function() {
    clearTimeout(analysisTimeout);
    analysisTimeout = setTimeout(function() {
        if (reviewInput.value.trim().length > 10) {
            analyzeReviews();
        }
    }, 1000);
});
*/

// ==================== Keyboard Shortcuts ====================

document.addEventListener('keydown', function(event) {
    // Ctrl+Enter or Cmd+Enter to analyze
    if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
        analyzeReviews();
    }
});
