// Theme switcher functionality
document.addEventListener('DOMContentLoaded', function() {
  // Get stored theme or default to 'light'
  const currentTheme = localStorage.getItem('theme') || 'light';
  
  // Apply the current theme
  document.body.setAttribute('data-theme', currentTheme);
  
  // Update the toggle button state
  updateToggleButton(currentTheme);
  
  // Add click event to the theme toggle button
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      // Get current theme
      const currentTheme = document.body.getAttribute('data-theme');
      // Switch to the opposite theme
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      
      // Update body attribute
      document.body.setAttribute('data-theme', newTheme);
      
      // Save to localStorage
      localStorage.setItem('theme', newTheme);
      
      // Update button appearance
      updateToggleButton(newTheme);
    });
  }
});

// Update button icon and text based on current theme
function updateToggleButton(theme) {
  const toggleButton = document.getElementById('theme-toggle');
  if (!toggleButton) return;
  
  if (theme === 'dark') {
    toggleButton.innerHTML = '<i class="fas fa-sun"></i>';
    toggleButton.setAttribute('title', 'Switch to Light Mode');
  } else {
    toggleButton.innerHTML = '<i class="fas fa-moon"></i>';
    toggleButton.setAttribute('title', 'Switch to Dark Mode');
  }
}