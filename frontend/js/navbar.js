// ============================================
// NAVBAR - ACTIVE PAGE DETECTION
// ============================================

(function() {
    'use strict';
    
    // Detect current page and set active class
    function setActivePage() {
        const currentPath = window.location.pathname;
        const currentPage = currentPath.split('/').pop() || 'home.html';
        
        // Map filenames to navigation items
        const pageMap = {
            'home.html': 'home',
            'index.html': 'home',
            'classify.html': 'classify',
            'history.html': 'history'
        };
        
        const activePage = pageMap[currentPage] || 'home';
        
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