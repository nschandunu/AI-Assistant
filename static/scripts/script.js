// Typing animation for welcome message
document.addEventListener('DOMContentLoaded', () => {
    const welcomeMessage = "Hello! I'm your AI assistant. How can I help you today?";
    const messageElement = document.querySelector('.welcome-message .message-content');
    
    function typeWriter(element, text, speed = 40) {
        let i = 0;
        element.innerHTML = ''; // Clear existing text
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        // Start typing
        type();
    }

    // Initialize typing animation if welcome message exists
    if (messageElement) {
        typeWriter(messageElement, welcomeMessage);
    }
});

// Add this to your existing script
document.querySelector('.mobile-menu-btn').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('show');
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-content')) {
        document.querySelector('.nav-links').classList.remove('show');
    }
});
