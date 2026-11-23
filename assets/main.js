// Sharp Brains Schools — shared behavior

document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
  }

  // FAQ accordion
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    var question = item.querySelector('.faq-q');
    if (!question) return;
    question.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      faqItems.forEach(function (i) { i.classList.remove('open'); });
      if (!isOpen) {
        item.classList.add('open');
      }
      faqItems.forEach(function (i) {
        var symbol = i.querySelector('.faq-symbol');
        if (symbol) symbol.textContent = i.classList.contains('open') ? '−' : '+';
      });
    });
  });

  // Inquiry form (contact page) — placeholder submit handler.
  // Replace this with a real endpoint (GoHighLevel form action, Formspree, etc.) before going live.
  var form = document.querySelector('#inquiry-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = document.querySelector('#form-note');
      if (note) {
        note.textContent = 'Thanks! This form isn’t wired to a backend yet — connect it to your CRM or form handler to start receiving real inquiries.';
        note.style.display = 'block';
      }
    });
  }
});
