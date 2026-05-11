document.addEventListener('DOMContentLoaded', () => {
    console.log("Urganch RTT sayti yuklandi!");
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseover', () => {
            card.style.borderColor = '#ffcc00';
        });
        card.addEventListener('mouseout', () => {
            card.style.borderColor = '#003366';
        });
    });
});
