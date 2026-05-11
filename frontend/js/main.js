// Sayt yuklanganda ishga tushadigan funksiyalar
document.addEventListener('DOMContentLoaded', function() {
    console.log("URTT Sayti muvaffaqiyatli yuklandi!");

    // Formani tekshirish (Validation)
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = document.querySelector('input[name="name"]').value;
            if (name.length < 3) {
                alert("Ismingiz juda qisqa!");
                e.preventDefault();
            }
        });
    }

    // Scroll effektlari (Navbar uchun)
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('bg-white', 'shadow-sm');
        } else {
            navbar.classList.remove('shadow-sm');
        }
    });
});
