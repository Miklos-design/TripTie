function refreshPage() {
    var countdown = 4; // Set the initial countdown value
    var countdownElement = document.getElementById('countdown'); // Get the countdown element

    // Function to update the countdown display
    function updateCountdown() {
        countdown--; // Decrease countdown by 1
        countdownElement.textContent = countdown; // Update the countdown element
        if (countdown <= 0) {
            location.reload(); // Reload the page when countdown reaches 0
        } else {
            setTimeout(updateCountdown, 1000); // Update countdown every second
        }
    }

    updateCountdown(); // Start the countdown

    // Function to refresh the page after 3 seconds
    function startRefresh() {
        setTimeout(refreshPage, 4000);
    }

    startRefresh(); // Start the refresh cycle
}

refreshPage(); // Initial call to start the process