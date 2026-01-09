// ============================================
// NAVBAR - ACTIVE PAGE DETECTION
// ============================================

(function() {
    'use strict';
    
    // Detect current page (supports clean URLs without .html) and set active class
    function setActivePage() {
        const currentPath = window.location.pathname;
        const rawPage = currentPath.split('/').pop() || 'index.html';
        const cleaned = rawPage.split('#')[0].split('?')[0];
        const pageKey = cleaned.replace(/\.html$/, '') || 'index';
        
        // Map filenames/clean URLs to nav keys
        const pageMap = {
            'home': 'home',
            'index': 'home',
            'classify': 'classify',
            'history': 'history'
        };
        
        const activePage = pageMap[pageKey] || 'home';
        
        // Set active class on all nav links (desktop + mobile)
        const allLinks = document.querySelectorAll('[data-page]');
        
        allLinks.forEach(link => {
            const linkPage = link.getAttribute('data-page');
            
            if (linkPage === activePage) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }
    
    // Initialize on page load
    document.addEventListener('DOMContentLoaded', () => {
        setActivePage();
        console.log('✅ Navbar active page detected');
    });
})();