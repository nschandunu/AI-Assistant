// Typing animation for welcome message
document.addEventListener('DOMContentLoaded', () => {
    const welcomeMessage = "Hello! I'm your AI assistant. How can I help you today?";
    const messageElement = document.querySelector('.welcome-message .message-content');
    
    function typeWriter(element, text, speed = 50) {
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
