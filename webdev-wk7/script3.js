// Smooth scroll
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

// Stats counter
const counters = document.querySelectorAll('.counter');
let started = false;
function startCounters() {
    if (!started && window.scrollY + window.innerHeight > document.querySelector('#problem').offsetTop) {
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            let count = 0;
            const speed = target / 50;
            const updateCount = () => {
                if (count < target) {
                    count += speed;
                    counter.innerText = Math.ceil(count);
                    requestAnimationFrame(updateCount);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        });
        started = true;
    }
}
window.addEventListener('scroll', startCounters);

// Fade in on scroll
window.addEventListener('scroll', () => {
    document.querySelectorAll('.fade-section').forEach(section => {
        const position = section.getBoundingClientRect().top;
        if (position < window.innerHeight - 100) {
            section.classList.add('visible');
        }
    });
});

// Form submission
document.getElementById('waitlistForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert("Thank you for joining the BloodLink AI waitlist! We’ll contact you soon.");
    this.reset();
});
