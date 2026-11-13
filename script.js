// SilverMuzzle — quiz routing + dog-size filter + mobile nav. No data leaves the browser.
(function(){
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) toggle.addEventListener('click', function(){ nav.classList.toggle('open'); });

  // Dog-size filter (category + roundup pages)
  var filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(function(btn){
    btn.addEventListener('click', function(){
      filterBtns.forEach(function(b){ b.classList.remove('active'); });
      btn.classList.add('active');
      var size = btn.getAttribute('data-size');
      document.querySelectorAll('.product').forEach(function(card){
        var sizes = (card.getAttribute('data-sizes') || 'small medium large giant').split(' ');
        var show = (size === 'all' || sizes.indexOf(size) !== -1);
        card.setAttribute('data-hidden', show ? 'false' : 'true');
      });
      var count = document.querySelectorAll('.product[data-hidden="false"]').length;
      var note = document.getElementById('filter-count');
      if (note) note.textContent = size === 'all' ? '' : count + ' option(s) shown for ' + size + ' dogs.';
    });
  });

  // "Find the right product" quiz — 3 questions, routes to a category or roundup
  var answers = {};
  var steps = document.querySelectorAll('.quiz-step');
  function showStep(n){
    steps.forEach(function(s, i){ s.classList.toggle('active', i === n); });
    var prog = document.getElementById('quiz-progress');
    if (prog) prog.textContent = n < steps.length ? 'Question ' + (n + 1) + ' of 3' : '';
  }
  document.querySelectorAll('[data-quiz]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var q = btn.getAttribute('data-quiz');
      answers[q] = btn.getAttribute('data-value');
      var current = parseInt(btn.closest('.quiz-step').getAttribute('data-step'), 10);
      if (current < 2) { showStep(current + 1); }
      else { showResult(); }
    });
  });
  var restart = document.getElementById('quiz-restart');
  if (restart) restart.addEventListener('click', function(){
    answers = {};
    document.getElementById('quiz-result').style.display = 'none';
    showStep(0);
  });
  function showResult(){
    steps.forEach(function(s){ s.classList.remove('active'); });
    var prog = document.getElementById('quiz-progress');
    if (prog) prog.textContent = 'Your match';
    // Route by main problem first, then size/budget refine the copy
    var map = {
      'comfort': {url: 'roundups/best-orthopedic-dog-beds-senior-dogs.html', title: 'Orthopedic beds', blurb: 'Start with the orthopedic beds roundup — comfort and pressure relief come first for most older dogs.'},
      'car': {url: 'roundups/best-dog-ramps-older-dogs.html', title: 'Dog ramps', blurb: 'A ramp is usually the kindest way to help an older dog in and out of the car. See the ramps roundup.'},
      'stairs': {url: 'comparisons/dog-ramp-vs-dog-stairs-senior-dogs.html', title: 'Ramp vs stairs', blurb: 'Ramps and stairs suit different homes and dogs. This comparison will help you choose.'},
      'slipping': {url: 'categories/home-safety.html', title: 'Home safety', blurb: 'Traction, rugs and night lights make the biggest day-to-day difference. Start with home safety.'},
      'walking': {url: 'roundups/best-harnesses-senior-dogs-weak-back-legs.html', title: 'Support harnesses', blurb: 'A well-fitting support harness can make walks steadier and less tiring. See the harnesses roundup.'},
      'feeding': {url: 'categories/feeding.html', title: 'Feeding', blurb: 'Raised bowls and slow feeders are small changes that can make mealtimes more comfortable.'},
      'grooming': {url: 'categories/grooming-hygiene.html', title: 'Grooming and hygiene', blurb: 'Gentle grooming tools and hygiene helpers keep an older dog comfortable at home.'}
    };
    var pick = map[answers.problem] || map['comfort'];
    var sizeLabel = answers.size ? ' for a ' + answers.size + ' dog' : '';
    var budgetLabel = answers.budget ? ' · Budget: ' + answers.budget : '';
    var result = document.getElementById('quiz-result');
    var link = document.getElementById('quiz-link');
    var text = document.getElementById('quiz-text');
    if (result && link && text) {
      // Fix relative path when quiz is on a sub-page (it lives on the home page, so root-relative is fine)
      link.href = pick.url;
      link.textContent = 'See ' + pick.title + ' →';
      text.textContent = pick.blurb + sizeLabel + budgetLabel + ' You can change your answers any time.';
      result.style.display = 'block';
      result.scrollIntoView({behavior: 'smooth', block: 'nearest'});
    }
  }
  if (steps.length) showStep(0);
})();
