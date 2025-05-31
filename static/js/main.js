const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d');
canvas.height = window.innerHeight;
canvas.width = window.innerWidth;
const chars = '01';
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = [];
for (let x = 0; x < columns; x++) {
    drops[x] = 1;
}
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0';
    ctx.font = fontSize + 'px monospace';
    for (let i = 0; i < drops.length; i++) {
        const text = chars.charAt(Math.floor(Math.random() * chars.length));
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}
setInterval(draw, 33);

document.querySelectorAll('.faq-item h5').forEach(item => {
    item.addEventListener('click', () => {
        const faqItem = item.parentElement;
        faqItem.classList.toggle('active');
    });
});

function searchFAQs() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const faqs = document.querySelectorAll('.faq-item');
    faqs.forEach(faq => {
        const question = faq.querySelector('h5').textContent.toLowerCase();
        const answer = faq.querySelector('p').textContent.toLowerCase();
        if (question.includes(input) || answer.includes(input)) {
            faq.style.display = 'block';
        } else {
            faq.style.display = 'none';
        }
    });
}
