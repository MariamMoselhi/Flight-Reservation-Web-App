
document.addEventListener("DOMContentLoaded", () => {
  const radioButtons = document.querySelectorAll('input[name="flight-select"]');
  const purchaseButton = document.getElementById("purchase-btn");

  // Enable purchase button when a radio button is selected
  radioButtons.forEach((radioButton) => {
    radioButton.addEventListener("change", () => {
      purchaseButton.disabled = false; 
    });
  });

  // Handle purchase button click
  purchaseButton.addEventListener("click", () => {
    const selectedFlight = document.querySelector(
      'input[name="flight-select"]:checked'
    );
    if (selectedFlight) {
      alert(`You selected ${selectedFlight.value}. Functionality not implemented yet.`);
    }
  });

  // Toggle results section visibility
  const toggleButton = document.getElementById('toggle-results-btn');
  const resultsSection = document.getElementById('results-section');

  toggleButton.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent form submission
    if (resultsSection.style.display === 'none' || resultsSection.style.display === '') {
      resultsSection.style.display = 'block'; }// Show section
    //  toggleButton.textContent = 'Hide Results'; 
    //  else {
    //   resultsSection.style.display = 'none'; // Hide section
    // //  toggleButton.textContent = 'Show Results'; 
    // }
  });
});
