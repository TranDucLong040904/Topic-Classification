// ============================================
// THEME MANAGEMENT - DARK MODE TOGGLE
// Dùng để quản lý chế độ giao diện sáng/tối
// ============================================

(function() {
    'use strict';
    
    // Load theme from localStorage
    function loadTheme() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        
        updateThemeIcon(savedTheme);
    }
    
    // Toggle theme
    function toggleTheme() {
        const isDark = document.documentElement.classList.toggle('dark');
        const newTheme = isDark ? 'dark' : 'light';
        
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    }
    
    // Update theme icon
    function updateThemeIcon(theme) {
        const icons = document.querySelectorAll('.theme-toggle-icon');
        
        icons.forEach(icon => {
            icon.textContent = theme === 'dark' ? '🌙' : '☀️';
        });
    }
    
    // Initialize on page load
    document.addEventListener('DOMContentLoaded', () => {
        // Load saved theme
        loadTheme();
        
        // Attach toggle listeners
        const toggleButtons = document.querySelectorAll('.theme-toggle');
        
        toggleButtons.forEach(button => {
            button.addEventListener('click', toggleTheme);
        });
        
        console.log('✅ Theme system initialized');
    });
})();