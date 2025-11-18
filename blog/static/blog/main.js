document.addEventListener('DOMContentLoaded', function() {
  // Theme toggle initialization (ensures proper behavior)
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      if (document.body.classList.contains('dark-theme')) {
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
        themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
      } else {
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
      }
    });
  }

  // Add page refresh functionality to "Read Full Post" buttons
  const refreshButtons = document.querySelectorAll('.refresh-page');
  
  if (refreshButtons.length > 0) {
    refreshButtons.forEach(button => {
      button.addEventListener('click', function(e) {
        // Store the href to navigate to
        const href = this.getAttribute('href');
        
        // Open the link with a page refresh (default behavior)
        window.location.href = href;
        
        // Prevent default to ensure our code runs
        e.preventDefault();
      });
    });
  }
  
  // Add icon rotation for collapsible sections using Bootstrap's collapse events
  $('.collapse').on('show.bs.collapse', function() {
    $(this).prev('.post-header').find('.toggle-icon')
      .removeClass('fa-chevron-down')
      .addClass('fa-chevron-up');
  });
  
  $('.collapse').on('hide.bs.collapse', function() {
    $(this).prev('.post-header').find('.toggle-icon')
      .removeClass('fa-chevron-up')
      .addClass('fa-chevron-down');
  });
});