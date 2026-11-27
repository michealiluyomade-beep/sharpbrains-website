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

  // Mobile testimonial tickers — pause the row the visitor is touching
  // so a passing card can be held still long enough to finish reading.
  var tickerRows = document.querySelectorAll('.testi-ticker-row');
  tickerRows.forEach(function (row) {
    var pause = function () { row.classList.add('is-paused'); };
    var resume = function () { row.classList.remove('is-paused'); };
    row.addEventListener('pointerdown', pause);
    row.addEventListener('pointerup', resume);
    row.addEventListener('pointercancel', resume);
    row.addEventListener('pointerleave', resume);
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
