// ============================================
// HISTORY PAGE - COMPLETE REWRITE
// Dùng để quản lý và hiển thị lịch sử phân loại văn bản
// ============================================

(function() {
    'use strict';
    
    // ============================================
    // CONSTANTS & STATE
    // ============================================
    
    const ITEMS_PER_PAGE = 10;
    const STORAGE_KEY = 'classificationHistory';
    
    const TOPIC_META = {
        'Thể thao': { icon: '🏃', class: 'topic-sports' },
        'Kinh tế': { icon: '💰', class: 'topic-economy' },
        'Giải trí': { icon: '🎬', class: 'topic-entertainment' },
        'Công nghệ': { icon: '💻', class: 'topic-technology' },
        'Giáo dục': { icon:  '📚', class: 'topic-education' },
        'Sức khỏe':  { icon: '❤️', class: 'topic-health' },
        'Pháp luật': { icon: '⚖️', class: 'topic-law' },
        'Thời sự': { icon: '📰', class: 'topic-news' },
        'Khoa học': { icon: '🔬', class: 'topic-science' },
        'Văn hóa': { icon: '🎭', class: 'topic-culture' },
    };
    
    let history = [];
    let filteredHistory = [];
    let currentPage = 1;
    let selectedIds = new Set();
    
    // DOM Elements
    let historyList, pagination, selectAllBtn, deleteBtn, topicFilter;
    let prevBtn, nextBtn, pageInfo;
    
    // ============================================
    // INITIALIZATION
    // Dùng để khởi tạo trang lịch sử
    // ============================================
    
    function init() {
        // Get DOM elements
        historyList = document.getElementById('historyList');
        pagination = document.getElementById('pagination');
        selectAllBtn = document.getElementById('selectAllBtn');
        deleteBtn = document.getElementById('deleteBtn');
        topicFilter = document.getElementById('topicFilter');
        prevBtn = document.getElementById('prevBtn');
        nextBtn = document.getElementById('nextBtn');
        pageInfo = document.getElementById('pageInfo');
        
        // Load history
        loadHistory();
        
        // Render
        renderHistory();
        
        // Attach events
        attachEventListeners();
        
        console.log('✅ History page initialized');
    }
    
    // ============================================
    // LOCALSTORAGE
    // ============================================
    
    function loadHistory() {
        const stored = localStorage.getItem(STORAGE_KEY);
        
        if (stored) {
            try {
                history = JSON.parse(stored);
                history. sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
            } catch (e) {
                console.error('Error parsing history:', e);
                history = [];
            }
        }
        
        filteredHistory = [... history];
    }
    
    function saveHistory() {
        localStorage.setItem(STORAGE_KEY, JSON. stringify(history));
    }
    
    // ============================================
    // RENDER
    // ============================================
    
    function renderHistory() {
        historyList.innerHTML = '';
        
        if (filteredHistory.length === 0) {
            renderEmptyState();
            pagination.style.display = 'none';
            return;
        }
        
        pagination.style.display = 'flex';
        
        // Pagination
        const totalPages = Math.ceil(filteredHistory.length / ITEMS_PER_PAGE);
        const start = (currentPage - 1) * ITEMS_PER_PAGE;
        const end = start + ITEMS_PER_PAGE;
        const pageItems = filteredHistory.slice(start, end);
        
        // Render items
        pageItems. forEach(item => {
            const itemEl = createHistoryItem(item);
            historyList.appendChild(itemEl);
        });
        
        // Update pagination
        updatePagination(totalPages);
        
        // Update buttons
        updateButtonStates();
    }
    
    function renderEmptyState() {
        historyList.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">📭</div>
                <h2 class="empty-title">Chưa có lịch sử</h2>
                <p class="empty-desc">Các văn bản bạn phân loại sẽ hiển thị ở đây</p>
                <a href="classify.html" class="empty-cta">Bắt đầu phân loại →</a>
            </div>
        `;
    }
    
    function createHistoryItem(item) {
        const div = document.createElement('div');
        div.className = 'history-item';
        div.dataset.id = item.id;
        
        const meta = TOPIC_META[item. topic] || { icon: '📄', class: 'topic-news' };
        
        // Checkbox
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'history-checkbox';
        checkbox.checked = selectedIds.has(item.id);
        checkbox.addEventListener('change', (e) => {
            e.stopPropagation();
            toggleSelection(item.id);
        });
        
        // Content
        const content = document.createElement('div');
        content.className = 'history-content';
        content.innerHTML = `
            <div class="history-text">${escapeHtml(item.text)}</div>
            <div class="history-meta">
                <span class="history-topic ${meta.class}">
                    ${meta.icon} ${item.topic}
                </span>
                <span class="history-confidence">${item.confidence. toFixed(1)}%</span>
                <span class="history-time">${formatTimestamp(item.timestamp)}</span>
            </div>
        `;
        
        // Delete button
        const deleteIconBtn = document.createElement('button');
        deleteIconBtn.className = 'history-delete';
        deleteIconBtn.innerHTML = '🗑️';
        deleteIconBtn.title = 'Xóa mục này';
        deleteIconBtn.addEventListener('click', (e) => {
            e. stopPropagation();
            deleteSingleItem(item.id);
        });
        
        // Click to navigate
        div.addEventListener('click', (e) => {
            // Ignore if clicking checkbox or delete button
            if (e. target === checkbox || e.target === deleteIconBtn) return;
            navigateToClassify(item);
        });
        
        div.appendChild(checkbox);
        div.appendChild(content);
        div.appendChild(deleteIconBtn);
        
        return div;
    }
    
    function updatePagination(totalPages) {
        pageInfo.textContent = `Trang ${currentPage} / ${totalPages}`;
        prevBtn.disabled = currentPage === 1;
        nextBtn.disabled = currentPage === totalPages || totalPages === 0;
    }
    
    function updateButtonStates() {
        const hasSelection = selectedIds.size > 0;
        const allSelected = selectedIds.size === filteredHistory. length && filteredHistory.length > 0;
        
        // Update delete button
        deleteBtn.disabled = !hasSelection;
        deleteBtn.textContent = hasSelection ? `🗑️ Xóa (${selectedIds.size})` : '🗑️ Xóa';
        
        // Update select all button
        selectAllBtn.textContent = allSelected ? 'Bỏ chọn tất cả' : 'Chọn tất cả';
    }
    
    // ============================================
    // EVENT LISTENERS
    // ============================================
    
    function attachEventListeners() {
        selectAllBtn.addEventListener('click', toggleSelectAll);
        deleteBtn. addEventListener('click', deleteSelected);
        topicFilter.addEventListener('change', filterByTopic);
        prevBtn.addEventListener('click', () => changePage(-1));
        nextBtn.addEventListener('click', () => changePage(1));
    }
    
    // ============================================
    // SELECTION
    // ============================================
    
    function toggleSelection(id) {
        if (selectedIds.has(id)) {
            selectedIds.delete(id);
        } else {
            selectedIds.add(id);
        }
        updateButtonStates();
    }
    
    function toggleSelectAll() {
        const allSelected = selectedIds.size === filteredHistory. length && filteredHistory.length > 0;
        
        if (allSelected) {
            // Deselect all
            selectedIds. clear();
        } else {
            // Select all visible items
            selectedIds.clear();
            filteredHistory.forEach(item => selectedIds.add(item.id));
        }
        
        // Update checkboxes
        const checkboxes = document.querySelectorAll('.history-checkbox');
        checkboxes. forEach(cb => {
            const itemId = cb.closest('.history-item').dataset.id;
            cb.checked = selectedIds.has(itemId);
        });
        
        updateButtonStates();
    }
    
    // ============================================
    // DELETE
    // ============================================
    
    function deleteSingleItem(id) {
        if (!confirm('Bạn có chắc muốn xóa mục này?')) return;
        
        const index = history.findIndex(item => item. id === id);
        if (index !== -1) {
            history. splice(index, 1);
            saveHistory();
            selectedIds.delete(id);
            
            // Reload
            loadHistory();
            applyCurrentFilter();
            renderHistory();
        }
    }
    
    function deleteSelected() {
        if (selectedIds.size === 0) return;
        
        const count = selectedIds.size;
        const message = count === 1 
            ? 'Bạn có chắc muốn xóa 1 mục đã chọn?' 
            : `Bạn có chắc muốn xóa ${count} mục đã chọn?`;
        
        if (!confirm(message)) return;
        
        // Remove selected items
        history = history.filter(item => ! selectedIds.has(item.id));
        saveHistory();
        selectedIds.clear();
        
        // Reload
        loadHistory();
        applyCurrentFilter();
        
        // Reset to page 1 if current page is now empty
        const totalPages = Math.ceil(filteredHistory.length / ITEMS_PER_PAGE);
        if (currentPage > totalPages && totalPages > 0) {
            currentPage = totalPages;
        } else if (filteredHistory.length === 0) {
            currentPage = 1;
        }
        
        renderHistory();
    }
    
    // ============================================
    // FILTER
    // ============================================
    
    function filterByTopic() {
        const selectedTopic = topicFilter.value;
        
        if (selectedTopic === 'all') {
            filteredHistory = [... history];
        } else {
            filteredHistory = history.filter(item => item.topic === selectedTopic);
        }
        
        // Reset to page 1
        currentPage = 1;
        
        // Clear selections
        selectedIds.clear();
        
        renderHistory();
    }
    
    function applyCurrentFilter() {
        const selectedTopic = topicFilter.value;
        
        if (selectedTopic === 'all') {
            filteredHistory = [...history];
        } else {
            filteredHistory = history. filter(item => item.topic === selectedTopic);
        }
    }
    
    // ============================================
    // PAGINATION
    // ============================================
    
    function changePage(delta) {
        const totalPages = Math.ceil(filteredHistory.length / ITEMS_PER_PAGE);
        const newPage = currentPage + delta;
        
        if (newPage >= 1 && newPage <= totalPages) {
            currentPage = newPage;
            renderHistory();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }
    
    // ============================================
    // NAVIGATION
    // ============================================
    
    function navigateToClassify(item) {
        // Save to sessionStorage
        sessionStorage.setItem('classifyData', JSON.stringify({
            text: item.text,
            topic: item.topic,
            confidence: item.confidence,
            topResults: item.topResults || [
                { topic: item.topic, probability: item.confidence }
            ]
        }));
        
        // Navigate
        window.location.href = 'classify.html';
    }
    
    // ============================================
    // HELPERS
    // ============================================
    
    function formatTimestamp(timestamp) {
        const date = new Date(timestamp);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        
        return `${day}/${month}/${year} ${hours}:${minutes}`;
    }
    
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // ============================================
    // START
    // ============================================
    
    document.addEventListener('DOMContentLoaded', init);
    
})();