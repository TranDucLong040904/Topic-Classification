// ============================================
// TOPIC CLASSIFICATION - MAIN SCRIPT
// Dùng cho frontend của ứng dụng phân loại chủ đề văn bản
// ============================================

// DOM Elements
const textInput = document.getElementById('textInput');
const charCounter = document. getElementById('charCounter');
const classifyBtn = document.getElementById('classifyBtn');
const clearBtn = document.getElementById('clearBtn');

// States
const emptyState = document.getElementById('emptyState');
const loadingState = document. getElementById('loadingState');
const errorState = document. getElementById('errorState');
const resultSection = document.getElementById('resultSection');

// Result Elements
const mainTopicCard = document.getElementById('mainTopicCard');
const mainTopicIcon = document.getElementById('mainTopicIcon');
const mainTopicText = document.getElementById('mainTopicText');
const donutChart = document.getElementById('donutChart');
const topicsList = document.getElementById('topicsList');
const errorMessage = document. getElementById('errorMessage');

// ============================================
// CHARACTER COUNTER
// Dùng để đếm ký tự và bật/tắt nút phân loại
// ============================================

textInput.addEventListener('input', () => {
    const length = textInput.value.length;
    charCounter.textContent = `${length}/5000 ký tự`;
    
    // Enable/disable classify button
    classifyBtn.disabled = length < 10;
});

// ============================================
// CLEAR BUTTON
// ============================================

clearBtn.addEventListener('click', () => {
    textInput.value = '';
    charCounter.textContent = '0/5000 ký tự';
    classifyBtn.disabled = true;
    showEmptyState();
});

// ============================================
// STATE MANAGEMENT
// ============================================

function showEmptyState() {
    emptyState.classList.remove('hidden');
    emptyState.classList.add('flex');
    loadingState.classList.add('hidden');
    errorState.classList. add('hidden');
    resultSection.classList.add('hidden');
}

function showLoadingState() {
    emptyState.classList.add('hidden');
    loadingState.classList.remove('hidden');
    loadingState.classList.add('flex');
    errorState.classList.add('hidden');
    resultSection.classList.add('hidden');
}

function showErrorState(message) {
    emptyState.classList.add('hidden');
    loadingState.classList.add('hidden');
    errorState.classList.remove('hidden');
    errorState.classList. add('flex');
    resultSection.classList.add('hidden');
    errorMessage.textContent = message;
}

function showResultState() {
    emptyState.classList.add('hidden');
    loadingState.classList.add('hidden');
    errorState.classList.add('hidden');
    resultSection.classList.remove('hidden');
    resultSection.classList.add('flex');
}

// ============================================
// API CALL
// Dùng để gọi API phân loại chủ đề
// ============================================

async function classifyText() {
    const text = textInput.value.trim();
    
    // Validate
    if (text.length < 10) {
        showErrorState('Văn bản quá ngắn!  Vui lòng nhập ít nhất 10 ký tự.');
        return;
    }
    
    // Show loading
    showLoadingState();
    
    try {
        const response = await fetch(`${API_CONFIG.BASE_URL}${API_CONFIG.ENDPOINTS. PREDICT}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON. stringify({ text: text })
        });
        
        const data = await response.json();
        
        if (response.ok && data.status === 'success') {
            // Success - render results
            renderResults(data);
        } else {
            // API error
            showErrorState(data. message || 'Đã xảy ra lỗi khi phân tích văn bản.');
        }
        
    } catch (error) {
        console.error('API Error:', error);
        showErrorState('Không thể kết nối đến server. Vui lòng kiểm tra xem API đã chạy chưa.');
    }
}

classifyBtn.addEventListener('click', classifyText);

// Enter key to classify
textInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.ctrlKey && ! classifyBtn.disabled) {
        classifyText();
    }
});

// ============================================
// RENDER RESULTS
// Dùng để hiển thị kết quả phân loại
// ============================================

function renderResults(data) {
    const { top_topic, predictions } = data;
    
    // Render main topic
    const topPrediction = predictions[0];
    const iconName = TOPIC_ICONS[topPrediction.topic] || 'help';
    
    mainTopicIcon.textContent = iconName;
    mainTopicText.textContent = `${topPrediction.topic} (${topPrediction.probability}%)`;
    
    // Render donut chart
    renderDonutChart(predictions);
    
    // Render topics list
    renderTopicsList(predictions);
    
    // Save to history
    saveToHistory(textInput.value, predictions);
    
    // Show results
    showResultState();
}

// ============================================
// RENDER DONUT CHART
// ============================================

let chartInstance = null;

function renderDonutChart(predictions) {
    const ctx = document.getElementById('donutChart').getContext('2d');
    
    if (chartInstance) {
        chartInstance.destroy();
    }
    
    const labels = predictions.map(p => p.topic);
    const data = predictions.map(p => p.probability);
    const colors = CHART_COLORS.slice(0, predictions.length);
    
    chartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: colors,
                borderWidth: 0,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio:  true,
            cutout: '35%',
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    padding: 12,
                    bodyFont:  { size: 14 },
                    callbacks: {
                        label: (context) => `${context.label}: ${context.parsed}%`
                    }
                }
            },
            animation: {
                animateRotate: true,
                animateScale: true,
                duration: 1000
            }
        }
    });
}

// ============================================
// RENDER TOPICS LIST
// Dùng để hiển thị danh sách chủ đề với thanh tiến trình
// ============================================

function renderTopicsList(predictions) {
    topicsList.innerHTML = '';
    
    predictions.forEach((pred, index) => {
        const iconName = TOPIC_ICONS[pred.topic] || 'help';
        const color = CHART_COLORS[index % CHART_COLORS.length];
        
        // Create container
        const itemDiv = document. createElement('div');
        itemDiv.className = 'flex flex-col gap-2 animate-fade-in';
        itemDiv. style.animationDelay = `${index * 0.1}s`;
        
        // Create header
        const headerDiv = document.createElement('div');
        headerDiv.className = 'flex justify-between items-center text-sm font-medium';
        headerDiv.innerHTML = `
            <div class="flex items-center gap-2 text-gray-800 dark:text-gray-200">
                <span class="material-symbols-outlined text-base" style="color: ${color}">${iconName}</span>
                <span>${pred.topic}</span>
            </div>
            <span class="text-gray-600 dark:text-text-muted-dark font-bold">${pred.probability}%</span>
        `;
        
        // Create progress bar container
        const progressContainer = document.createElement('div');
        progressContainer.className = 'w-full bg-gray-300 dark:bg-gray-700 rounded-full h-3 overflow-hidden';
        
        // Create progress bar
        const progressBar = document.createElement('div');
        progressBar.className = 'h-3 rounded-full transition-all duration-1000 ease-out';
        progressBar.style.width = '0%';
        progressBar.style.backgroundColor = color;
        
        // Append elements
        progressContainer.appendChild(progressBar);
        itemDiv.appendChild(headerDiv);
        itemDiv.appendChild(progressContainer);
        topicsList.appendChild(itemDiv);
        
        // Animate progress bar
        setTimeout(() => {
            progressBar.style.width = `${pred.probability}%`;
        }, 100 + index * 100);
    });
}

// ============================================
// SAVE TO HISTORY
// ============================================

function saveToHistory(text, predictions) {
    const historyItem = {
        id:  Date.now().toString(),
        text: text,
        topic: predictions[0].topic,
        confidence: predictions[0].probability,
        topResults: predictions.slice(0, 3),
        timestamp: new Date().toISOString()
    };
    
    // Get existing history
    let history = [];
    const stored = localStorage.getItem('classificationHistory');
    if (stored) {
        try {
            history = JSON.parse(stored);
        } catch (e) {
            history = [];
        }
    }
    
    // Add new item to beginning
    history.unshift(historyItem);
    
    // Keep only last 100 items
    if (history.length > 100) {
        history = history.slice(0, 100);
    }
    
    // Save back
    localStorage.setItem('classificationHistory', JSON.stringify(history));
    
    console.log('✅ Saved to history');
}

// ============================================
// LOAD FROM HISTORY (from history page)
// ============================================

function loadFromHistory() {
    const classifyData = sessionStorage.getItem('classifyData');
    
    if (classifyData) {
        try {
            const data = JSON. parse(classifyData);
            
            // Fill textarea
            textInput.value = data. text;
            charCounter.textContent = `${data.text.length}/5000 ký tự`;
            classifyBtn.disabled = false;
            
            // Show previous result
            renderResults({
                top_topic: data. topic,
                predictions: data. topResults
            });
            
            // Clear sessionStorage
            sessionStorage.removeItem('classifyData');
            
            console.log('✅ Loaded from history');
        } catch (e) {
            console. error('Error loading classify data:', e);
            showEmptyState();
        }
    } else {
        // Initial state
        showEmptyState();
    }
}

// ============================================
// INITIALIZATION
// Dùng để khởi tạo ứng dụng
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    // Check if coming from history page
    loadFromHistory();
    
    // Disable classify button initially
    classifyBtn. disabled = true;
    
    console.log('✅ Topic Classification App initialized');
    console.log(`📡 API URL: ${API_CONFIG.BASE_URL}`);
});