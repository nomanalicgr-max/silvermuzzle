#!/usr/bin/env python3
"""Build SilverMuzzle static site. Run: python3 build.py — regenerates all .html pages."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))
AFF = "YOUR-AFFILIATE-TAG-20"
DISCLAIMER = "This content is for general information only and is not veterinary advice. Always consult your vet about your dog's health."
def amz(query):
    from urllib.parse import quote_plus
    return f"https://www.amazon.com/s?k={quote_plus(query)}&tag={AFF}"
def header(prefix, title, desc):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | SilverMuzzle</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title} | SilverMuzzle"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">
<link rel="stylesheet" href="{prefix}styles.css"></head>
<body><header class="site-header"><div class="header-inner">
<a class="logo" href="{prefix}index.html">Silver<span>Muzzle</span><span class="tagline">Comfort for older dogs, calmly chosen</span></a>
<button class="nav-toggle" aria-label="Menu">☰ Menu</button>
<nav class="main-nav"><a href="{prefix}index.html">Home</a><a href="{prefix}categories/orthopedic-beds.html">Beds</a><a href="{prefix}categories/ramps-stairs-mobility.html">Ramps</a><a href="{prefix}categories/harnesses-leashes-walking.html">Harnesses</a><a href="{prefix}categories/feeding.html">Feeding</a><a href="{prefix}categories/grooming-hygiene.html">Grooming</a><a href="{prefix}categories/home-safety.html">Home Safety</a><a href="{prefix}about.html">About</a></nav>
</div></header><main class="wrap">
"""
FOOTER = """</main><footer class="site-footer"><div class="footer-grid">
<div><h4>SilverMuzzle</h4><p>Warm, practical guides and product roundups for owners of older dogs (7+ years). No pushy selling, no medical claims — just comfort, safety and everyday quality of life.</p></div>
<div><h4>Shop by need</h4><p><a href="CATEGORIES_PLACEHOLDER">Orthopedic beds</a><br><a href="RAMPS_PLACEHOLDER">Ramps &amp; mobility</a><br><a href="HARNESS_PLACEHOLDER">Harnesses</a><br><a href="FEEDING_PLACEHOLDER">Feeding</a><br><a href="GROOMING_PLACEHOLDER">Grooming</a><br><a href="SAFETY_PLACEHOLDER">Home safety</a></p></div>
<div><h4>Good to know</h4><p><a href="ABOUT_PLACEHOLDER">About &amp; how we research</a><br><a href="DISCLOSURE_PLACEHOLDER">Affiliate disclosure</a><br><a href="PRIVACY_PLACEHOLDER">Privacy policy</a><br><a href="CONTENT_PLACEHOLDER">Content roadmap</a></p><p class="meta">As an Amazon Associate, we earn from qualifying purchases.</p></div>
</div><div class="footer-bottom">© 2026 SilverMuzzle · This content is for general information only and is not veterinary advice. Always consult your vet about your dog's health.</div></footer>
<script src="SCRIPT_PLACEHOLDER"></script></body></html>
"""
def footer(prefix):
    f = FOOTER
    f = f.replace("CATEGORIES_PLACEHOLDER", prefix+"categories/orthopedic-beds.html")
    f = f.replace("RAMPS_PLACEHOLDER", prefix+"categories/ramps-stairs-mobility.html")
    f = f.replace("HARNESS_PLACEHOLDER", prefix+"categories/harnesses-leashes-walking.html")
    f = f.replace("FEEDING_PLACEHOLDER", prefix+"categories/feeding.html")
    f = f.replace("GROOMING_PLACEHOLDER", prefix+"categories/grooming-hygiene.html")
    f = f.replace("SAFETY_PLACEHOLDER", prefix+"categories/home-safety.html")
    f = f.replace("ABOUT_PLACEHOLDER", prefix+"about.html")
    f = f.replace("DISCLOSURE_PLACEHOLDER", prefix+"affiliate-disclosure.html")
    f = f.replace("PRIVACY_PLACEHOLDER", prefix+"privacy.html")
    f = f.replace("CONTENT_PLACEHOLDER", prefix+"content-plan.html")
    f = f.replace("SCRIPT_PLACEHOLDER", prefix+"script.js")
    return f
def page(path, prefix, title, desc, body, disclaimer=True):
    d = f'<div class="disclaimer"><strong>Please note:</strong> {DISCLAIMER}</div>' if disclaimer else ''
    html = header(prefix, title, desc) + body + d + footer(prefix)
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as fh: fh.write(html)
    print("wrote", path)
def aff_note():
    return '<div class="affiliate-note">As an Amazon Associate, we earn from qualifying purchases. Prices change, so please check the listing before you buy. Links below go to Amazon search results for that type of product — choose the size and style that fits your dog.</div>'
def filter_ui():
    return '''<h2>Filter by dog size</h2><div class="filters" role="group" aria-label="Filter by dog size">
<button class="filter-btn active" data-size="all">All sizes</button>
<button class="filter-btn" data-size="small">Small</button>
<button class="filter-btn" data-size="medium">Medium</button>
<button class="filter-btn" data-size="large">Large</button>
<button class="filter-btn" data-size="giant">Giant</button></div><p class="meta" id="filter-count"></p>'''
def product_card(name, sizes, price, blurb, query, badge=""):
    b = f'<span class="pill">{badge}</span> ' if badge else ''
    return f'''<article class="card product" data-sizes="{sizes}">{b}<h3>{name}</h3>
<p class="meta">Fits: {sizes.replace(" ", " · ")} · <span class="price">{price}</span></p><p>{blurb}</p>
<p><a class="btn btn-teal" href="{amz(query)}" rel="nofollow sponsored" target="_blank">Check price on Amazon →</a></p></article>'''
# Part 2 — home, about, disclosure, content-plan page (appended into build.py by running cat)
HOME_BODY = """
<section class="hero"><p class="eyebrow">For dogs aged 7 and over</p>
<h1>Comfort for older dogs,<br>calmly chosen.</h1>
<p class="lead">SilverMuzzle helps you find beds, ramps, harnesses and small home changes that make everyday life easier for a senior dog — without the hard sell, and without guessing.</p>
<div class="cta-row"><a class="btn" href="#quiz">Find the right product →</a><a class="btn btn-ghost" href="roundups/best-orthopedic-dog-beds-senior-dogs.html">Best orthopedic beds</a></div></section>

<section class="quiz" id="quiz"><h2>Find the right product</h2>
<p>Three quick questions. We will point you to the category or roundup that fits best.</p>
<p class="quiz-progress" id="quiz-progress">Question 1 of 3</p>
<div class="quiz-step active" data-step="0"><h3>1. How big is your dog?</h3><div class="quiz-options">
<button data-quiz="size" data-value="small">Small — up to about 10 kg / 22 lb</button>
<button data-quiz="size" data-value="medium">Medium — about 10–25 kg / 22–55 lb</button>
<button data-quiz="size" data-value="large">Large — about 25–40 kg / 55–90 lb</button>
<button data-quiz="size" data-value="giant">Giant — over 40 kg / 90 lb</button></div></div>
<div class="quiz-step" data-step="1"><h3>2. What is the main problem right now?</h3><div class="quiz-options">
<button data-quiz="problem" data-value="comfort">Stiff or restless sleep — needs a more comfortable bed</button>
<button data-quiz="problem" data-value="car">Struggling to get into the car</button>
<button data-quiz="problem" data-value="stairs">Struggling with stairs or getting on furniture</button>
<button data-quiz="problem" data-value="slipping">Slipping on hard floors at home</button>
<button data-quiz="problem" data-value="walking">Weak back legs or unsteady on walks</button>
<button data-quiz="problem" data-value="feeding">Mealtimes are awkward or messy</button>
<button data-quiz="problem" data-value="grooming">Grooming and hygiene are getting harder</button></div></div>
<div class="quiz-step" data-step="2"><h3>3. What is your budget range?</h3><div class="quiz-options">
<button data-quiz="budget" data-value="Under $50">Under $50</button>
<button data-quiz="budget" data-value="$50–$100">$50–$100</button>
<button data-quiz="budget" data-value="$100–$200">$100–$200</button>
<button data-quiz="budget" data-value="$200+">$200+</button></div></div>
<div class="quiz-result" id="quiz-result"><h3>Your match</h3><p id="quiz-text"></p><p><a class="btn btn-teal" id="quiz-link" href="#">See recommendation →</a> <button class="btn btn-ghost" id="quiz-restart" type="button">Start again</button></p></div>
</section>

<h2>Shop by need</h2>
<div class="grid">
<div class="card"><h3><a href="categories/orthopedic-beds.html">Orthopedic Beds and Comfort</a></h3><p>Supportive beds, bolsters and blankets designed to support comfort for stiff joints and restless sleep.</p></div>
<div class="card"><h3><a href="categories/ramps-stairs-mobility.html">Ramps, Stairs and Mobility Aids</a></h3><p>Ramps, steps and slings that help an older dog reach the car, sofa or bed with less jumping.</p></div>
<div class="card"><h3><a href="categories/harnesses-leashes-walking.html">Harnesses, Leashes and Walking Gear</a></h3><p>Support harnesses, gentle leads and walking helpers for weak back legs and shorter, steadier walks.</p></div>
<div class="card"><h3><a href="categories/feeding.html">Feeding</a></h3><p>Raised bowls, slow feeders and food storage that make mealtimes calmer and tidier.</p></div>
<div class="card"><h3><a href="categories/grooming-hygiene.html">Grooming and Hygiene</a></h3><p>Gentle brushes, wipes, paw care and bathing helpers for dogs who tire easily.</p></div>
<div class="card"><h3><a href="categories/home-safety.html">Home Safety</a></h3><p>Rugs, traction, gates and night lights that make the house safer to move around in.</p></div>
</div>

<h2>Most-read roundups</h2>
<div class="grid">
<div class="card"><span class="pill">Roundup</span><h3><a href="roundups/best-orthopedic-dog-beds-senior-dogs.html">Best Orthopedic Dog Beds for Senior Dogs</a></h3><p>Five beds compared by thickness, cover, washability and size — so you can match the bed to your dog, not the other way round.</p></div>
<div class="card"><span class="pill">Roundup</span><h3><a href="roundups/best-dog-ramps-older-dogs.html">Best Dog Ramps for Older Dogs</a></h3><p>Car ramps, folding ramps and indoor ramps, with weight limits and grip checked.</p></div>
<div class="card"><span class="pill">Roundup</span><h3><a href="roundups/best-harnesses-senior-dogs-weak-back-legs.html">Best Harnesses for Senior Dogs with Weak Back Legs</a></h3><p>Rear-support and full-body harnesses that spread pressure and give you a steady handle.</p></div>
</div>

<h2>Guides worth reading first</h2>
<div class="grid">
<div class="card"><h3><a href="articles/10-signs-dog-entering-senior-years.html">10 Signs Your Dog Is Entering Their Senior Years</a></h3><p>Small changes to watch for — and when to mention them to your vet.</p></div>
<div class="card"><h3><a href="articles/senior-dog-slipping-hardwood-floors.html">Senior Dog Slipping on Hardwood Floors? Practical Fixes</a></h3><p>Rugs, socks, paw grips and layout changes that work in a real home.</p></div>
<div class="card"><h3><a href="articles/how-often-should-senior-dog-walk.html">How Often Should a Senior Dog Walk?</a></h3><p>Shorter, more frequent walks, rest days, and what tiredness looks like.</p></div>
</div>

<div class="trust-box"><h2>How we choose products</h2><p>We read owner reviews, check materials and safety details, and compare specifications side by side — size, weight limit, washability, grip and warranty. We do not claim hands-on testing unless we have actually done it. If a product has a real drawback, we say so. Read the full method on our <a href="about.html">About page</a>.</p></div>
"""

ABOUT_BODY = """
<p class="breadcrumbs"><a href="index.html">Home</a> / About</p>
<h1>About SilverMuzzle</h1>
<p class="lead">SilverMuzzle is a small, independent guide for people caring for an older dog. We write about comfort, safety and everyday quality of life — the practical things that make a senior dog's days easier.</p>
<h2>About the author</h2>
<p><strong>[YOUR NAME]</strong> — [dog ownership experience: e.g. “I have shared my home with older dogs for [X] years, including caring for a senior [breed] through stiff joints, slower walks and night-time restlessness.” Replace this placeholder with your real experience before publishing.]</p>
<p>That experience is why this site exists: not to sell you everything, but to help you choose the one thing that will actually help your dog, and to skip the rest.</p>
<h2>How We Research Products</h2>
<p>We do not claim hands-on testing unless it is true. Here is what we do for every roundup and category:</p>
<ul><li><strong>Read owner reviews</strong> — especially long-term reviews from owners of senior dogs, and reviews that mention size, weight and durability.</li>
<li><strong>Check materials and safety</strong> — cover fabric, foam type and thickness, grip and non-slip bases, buckles, stitching and any small parts.</li>
<li><strong>Compare specifications</strong> — dimensions, weight limits, washability, warranty and what is actually included in the box.</li>
<li><strong>Look for the drawback</strong> — if a bed is hard to wash, a ramp is heavy to carry, or a harness runs small, we say so.</li>
<li><strong>Update when things change</strong> — prices, sizes and listings change. Check the listing before you buy.</li></ul>
<p>We never claim a product treats, cures or prevents any condition. Wording like “designed to support comfort” means exactly that — comfort and support, not medicine.</p>

<!-- Vet review box: hidden until a real vet reviewer is added. Do not unhide with placeholder text. -->
<section class="vet-review" hidden aria-hidden="true">
<h2>Reviewed by a veterinarian</h2>
<p><strong>[Vet name, qualifications]</strong> reviewed this page on [date].</p>
</section>
<p class="meta">The box above stays hidden until a real veterinarian reviews our content. We will not show a vet review badge without a named, qualified reviewer.</p>

<h2>How this site makes money</h2>
<p>SilverMuzzle earns a small commission when you buy through an Amazon link on this site, at no extra cost to you. That does not change what we recommend. See our <a href="affiliate-disclosure.html">affiliate disclosure</a>. Google AdSense may be added later.</p>
<h2>Contact</h2>
<p>Questions or a correction? Email [YOUR EMAIL] and we will look into it.</p>
"""

PRIVACY_BODY = """
<p class="breadcrumbs"><a href="index.html">Home</a> / Privacy Policy</p>
<h1>Privacy Policy</h1>
<p>SilverMuzzle is a small informational website. We do not run accounts, and we do not ask you to sign up for anything on this site.</p>
<h2>What we collect</h2><p>We do not collect names, email addresses or payment details through this site. If you email us, we use your email only to reply to you.</p>
<h2>Cookies and analytics</h2><p>We do not set our own tracking cookies. Google AdSense may be added later; if it is, Google may use cookies to show ads, and this page will be updated with details and an opt-out link before ads go live.</p>
<h2>Affiliate links</h2><p>Links to Amazon are affiliate links. When you click one, Amazon may set cookies to track the referral, under Amazon's own privacy policy. See our <a href="affiliate-disclosure.html">affiliate disclosure</a>.</p>
<h2>Contact</h2><p>Questions about this policy? Email [YOUR EMAIL].</p>
<p class="meta">Last updated: November 2026.</p>
"""

DISCLOSURE_BODY = """
<p class="breadcrumbs"><a href="index.html">Home</a> / Affiliate Disclosure</p>
<h1>Affiliate Disclosure</h1>
<p>SilverMuzzle is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com.</p>
<p>When you click an Amazon link on this site and make a qualifying purchase, we may earn a small commission at no extra cost to you. That commission does not affect the price you pay, and it does not affect what we recommend.</p>
<p>We recommend products based on our research method — reading owner reviews, checking materials and safety, and comparing specifications — not on commission rates. Prices and availability change, so please check the listing before you buy.</p>
<p>Google AdSense may be added later. If it is, this page will be updated.</p>
"""

# --- Categories ---
CATS = [
 ("categories/orthopedic-beds.html", "Orthopedic Beds and Comfort", "Supportive beds for senior dogs: memory foam, bolsters, washable covers and sizing.",
  "<p class='lead'>A good bed is where comfort starts. Older dogs sleep more, and a bed that supports their weight evenly can make mornings less stiff and nights less restless.</p><h2>What to look for</h2><ul><li><strong>Foam thickness:</strong> 4 inches or more for medium and large dogs; thinner beds flatten quickly.</li><li><strong>Washable cover:</strong> accidents happen. A removable, machine-washable cover matters more than a fancy pattern.</li><li><strong>Non-slip base:</strong> so the bed stays put on hard floors.</li><li><strong>Size:</strong> your dog should be able to stretch out fully. Measure them lying down, then add a few inches.</li><li><strong>Bolsters or flat?</strong> Some dogs lean on a bolster; others prefer a flat mat they can step onto. Watch how yours sleeps.</li></ul><p>See the full comparison in our roundup: <a href='../roundups/best-orthopedic-dog-beds-senior-dogs.html'>Best Orthopedic Dog Beds for Senior Dogs</a>. Also useful: <a href='../comparisons/memory-foam-vs-egg-crate-dog-beds.html'>Memory Foam vs Orthopedic Egg-Crate Dog Beds</a>.</p>",
  [("Thick memory foam bed with bolster", "small medium large", "From about $60", "Even support across the body, with a raised edge to lean on. Look for a waterproof liner under the cover.", "orthopedic dog bed memory foam bolster"),
   ("Flat orthopedic mat, 4-inch foam", "medium large giant", "From about $80", "Easy to step onto, no edge to climb over. A good fit for dogs who struggle to lift their legs.", "flat orthopedic dog bed large senior"),
   ("Washable bolster bed, small breeds", "small medium", "From about $45", "Compact, soft cover, fully washable. Check the stated weight limit before choosing.", "small orthopedic dog bed washable cover"),
   ("Cooling gel-top orthopedic bed", "medium large", "From about $90", "A cooler sleeping surface for dogs who overheat. The gel layer is for comfort, not a medical treatment.", "cooling orthopedic dog bed senior"),
   ("Extra-large orthopedic bed, giant breeds", "large giant", "From about $130", "Sized for dogs over 40 kg. Measure your floor space as well as your dog.", "giant breed orthopedic dog bed extra large")]),
 ("categories/ramps-stairs-mobility.html", "Ramps, Stairs and Mobility Aids", "Dog ramps, pet stairs and support slings for senior dogs who struggle with cars, sofas and beds.",
  "<p class='lead'>Jumping gets harder with age. A ramp or a set of steps lets an older dog reach the car, sofa or bed without that jolt on landing.</p><h2>What to look for</h2><ul><li><strong>Weight limit:</strong> choose a ramp rated well above your dog's weight.</li><li><strong>Grip:</strong> a textured or carpeted surface helps paws hold on, especially in rain.</li><li><strong>Length and slope:</strong> longer ramps are gentler. Measure the height you need to reach.</li><li><strong>Weight of the ramp itself:</strong> if you will carry it daily, a lighter folding ramp is kinder on your back too.</li></ul><p>Compare the two options: <a href='../comparisons/dog-ramp-vs-dog-stairs-senior-dogs.html'>Dog Ramp vs Dog Stairs for Senior Dogs</a>. Roundup: <a href='../roundups/best-dog-ramps-older-dogs.html'>Best Dog Ramps for Older Dogs</a>.</p>",
  [("Folding car ramp, non-slip surface", "small medium large giant", "From about $70", "Folds for the boot, with a high-traction surface. Check folded length fits your car.", "folding dog ramp car senior large"),
   ("Lightweight telescoping ramp", "small medium large", "From about $90", "Adjusts to different heights. Lighter to carry, so good for daily use.", "telescoping dog ramp lightweight"),
   ("Indoor ramp for sofa and bed", "small medium", "From about $60", "Shorter, gentler slope for indoors. Pair with a rug at the base so it does not slide.", "indoor dog ramp sofa small dog"),
   ("Pet stairs with wide, deep steps", "small medium", "From about $55", "Wide steps are easier than narrow ones. Best for small and medium dogs who still lift their legs.", "pet stairs wide steps small dog"),
   ("Rear support sling", "medium large giant", "From about $25", "A handle under the hindquarters for a short lift up steps or into the car. Use gently, and let your dog set the pace.", "dog rear support sling harness senior")]),
 ("categories/harnesses-leashes-walking.html", "Harnesses, Leashes and Walking Gear", "Support harnesses and walking gear for senior dogs with weak back legs.",
  "<p class='lead'>A good harness spreads pressure across the chest and body instead of the neck, and gives you a handle for a steadying lift when your dog stumbles.</p><h2>What to look for</h2><ul><li><strong>Fit:</strong> measure chest and neck, and check the maker's size chart — sizes vary a lot between brands.</li><li><strong>Padding:</strong> soft lining matters on thin skin and bony areas.</li><li><strong>Handle:</strong> a top handle helps with steps, curbs and getting up.</li><li><strong>Easy on and off:</strong> step-in or clip designs are kinder than over-the-head styles for stiff dogs.</li></ul><p>Roundup: <a href='../roundups/best-harnesses-senior-dogs-weak-back-legs.html'>Best Harnesses for Senior Dogs with Weak Back Legs</a>.</p>",
  [("Rear-support harness with handle", "medium large giant", "From about $35", "Lifts the hindquarters gently. Padded straps spread pressure.", "rear support dog harness weak back legs"),
   ("Full-body support harness", "medium large", "From about $50", "Front and rear support in one harness. Good for dogs who need help standing as well as walking.", "full body support harness senior dog"),
   ("Padded step-in harness", "small medium large", "From about $25", "No pulling over the head. Soft padding, easy clips.", "padded step in dog harness senior"),
   ("Hands-free walking lead with bungee", "small medium large", "From about $20", "A little give in the lead softens sudden pulls. Keep walks short and steady.", "hands free dog leash bungee senior"),
   ("Reflective harness for evening walks", "small medium large giant", "From about $30", "Reflective strips help drivers see you both on darker evenings.", "reflective dog harness large senior")]),
 ("categories/feeding.html", "Feeding: Raised Bowls, Slow Feeders and Food Storage", "Raised bowls, slow feeders and storage for senior dogs — comfort at mealtimes, no diet claims.",
  "<p class='lead'>Mealtimes should be calm. A raised bowl can mean less bending for a stiff neck, a slow feeder can slow a gulper down, and a good container keeps food fresh.</p><p>We do not give nutrition or diet advice here. What and how much your dog eats is a question for your vet.</p><h2>What to look for</h2><ul><li><strong>Bowl height:</strong> the rim should sit near your dog's chest, not at floor level and not up at chin height. Adjustable stands help.</li><li><strong>Stability:</strong> a non-slip base stops the bowl sliding across the floor.</li><li><strong>Slow-feeder design:</strong> shallow ridges slow eating without frustrating your dog. Avoid very deep puzzles for older dogs.</li><li><strong>Easy to clean:</strong> stainless steel or ceramic bowls wash well and do not hold smells.</li></ul>",
  [("Adjustable raised feeder, two bowls", "small medium large", "From about $35", "Height adjusts as you find what suits your dog. Non-slip feet, removable steel bowls.", "adjustable raised dog feeder bowls"),
   ("Single raised bowl, large dogs", "large giant", "From about $30", "A simple raised stand for bigger dogs. Check the bowl size against your dog's usual portion.", "raised dog bowl large breed stand"),
   ("Slow feeder bowl, shallow ridges", "small medium large", "From about $15", "Gentle ridges to slow fast eaters. Choose a size your dog can reach comfortably.", "slow feeder dog bowl senior"),
   ("Non-slip mat under bowls", "small medium large giant", "From about $12", "Keeps bowls and water in one place and protects the floor.", "non slip mat dog bowls"),
   ("Airtight food storage container", "small medium large giant", "From about $20", "Keeps kibble fresh and dry, with a scoop included in many sets.", "airtight dog food storage container")]),
 ("categories/grooming-hygiene.html", "Grooming and Hygiene", "Gentle grooming tools, wipes and paw care for older dogs.",
  "<p class='lead'>Older dogs tire faster, and their skin can be thinner. Short, gentle grooming sessions beat long ones — and the right tools make them easier for both of you.</p><h2>What to look for</h2><ul><li><strong>Soft bristles:</strong> gentle on skin, no scratching.</li><li><strong>Lightweight tools:</strong> easier on your hands during a longer groom.</li><li><strong>Waterless options:</strong> wipes and dry shampoo help between baths, when a full bath is too much.</li><li><strong>Paw care:</strong> check paws regularly for cracks, and keep nails trimmed — long nails change how a dog walks.</li></ul>",
  [("Soft slicker brush, gentle pins", "small medium large giant", "From about $12", "Soft pins for regular brushing without scratching thin skin.", "soft slicker brush dog gentle senior"),
   ("Grooming wipes, unscented", "small medium large giant", "From about $10", "Quick clean-ups between baths. Choose unscented if your dog has sensitive skin.", "dog grooming wipes unscented senior"),
   ("Paw balm", "small medium large giant", "From about $10", "A simple balm for dry pads. Apply after walks, and check paws for cracks.", "dog paw balm dry pads"),
   ("Non-slip bath mat", "small medium large giant", "From about $15", "Grip underfoot in the bath or shower makes washing less stressful.", "non slip bath mat dog"),
   ("Nail clippers with guard", "small medium large", "From about $14", "A guard helps avoid cutting too short. If you are unsure, ask a groomer or vet to show you.", "dog nail clippers guard senior")]),
 ("categories/home-safety.html", "Home Safety: Rugs, Traction, Gates and Night Lights", "Home safety for senior dogs: traction, rugs, gates and night lights.",
  "<p class='lead'>Most slips happen at home, on the floors your dog crosses every day. A few well-placed rugs and a night light can change that.</p><h2>What to look for</h2><ul><li><strong>Rug grip:</strong> rugs need a non-slip backing or a separate grip pad underneath, or they become a hazard themselves.</li><li><strong>Clear paths:</strong> keep the route to water, the door and the bed clear of clutter and trailing cables.</li><li><strong>Gates:</strong> a gate at the top of stairs is worth more than any gadget if your dog is unsteady.</li><li><strong>Night lights:</strong> older eyes see less well in the dark. A low light on the hallway helps.</li></ul><p>Read the guide: <a href='../articles/senior-dog-slipping-hardwood-floors.html'>Senior Dog Slipping on Hardwood Floors? Practical Fixes</a> and <a href='../articles/make-home-safer-senior-dog.html'>How to Make Your Home Safer for a Senior Dog</a>.</p>",
  [("Non-slip rug runner, hallway", "small medium large giant", "From about $30", "A runner on the main walking route gives paws grip all the way through the house.", "non slip rug runner hallway dog"),
   ("Grip pads for under rugs", "small medium large giant", "From about $15", "Stop existing rugs sliding. Cut to size, washable in many cases.", "rug grip pad non slip under rug"),
   ("Paw grip socks", "small medium large", "From about $15", "Rubberised soles for indoor grip. Introduce them gradually — most dogs need a day or two.", "dog grip socks non slip paws"),
   ("Pressure-mounted safety gate", "small medium large giant", "From about $35", "No drilling. Fits doorways and the top of stairs. Check the width before ordering.", "pressure mounted baby gate dog stairs"),
   ("Motion-sensor night lights", "small medium large giant", "From about $18", "Light up when your dog moves at night. Place them along the hallway to the garden door.", "motion sensor night light hallway")]),
]

# --- Roundups ---
ROUNDUPS = [
 ("roundups/best-orthopedic-dog-beds-senior-dogs.html", "Best Orthopedic Dog Beds for Senior Dogs", "Five orthopedic beds for senior dogs compared by foam thickness, washability, size and value.",
  "<p class='lead'>We compared five beds on foam thickness, cover washability, size range and price — and noted the drawback of each, so you can choose with your eyes open.</p><p>These beds are designed to support comfort. They are not a treatment for any condition.</p>",
  [("Best overall — 7-inch memory foam bed with bolster", "medium large", "About $90–$140", "Thick, even support with a bolster to lean on. Removable washable cover and waterproof liner. Heavy to move when wet — wash the cover, not the foam.", "orthopedic dog bed memory foam 7 inch bolster"),
   ("Best for large dogs — flat orthopedic mat, 4-inch foam", "large giant", "About $100–$160", "No edge to climb over, so dogs who struggle to lift their legs can step straight on. Non-slip base. Very firm at first; give it a few nights.", "large orthopedic dog bed flat mat senior"),
   ("Best budget — washable bolster bed", "small medium", "About $40–$70", "Good support for the price, fully washable cover. Foam is thinner than premium beds, so best for small and medium dogs.", "orthopedic dog bed washable budget senior"),
   ("Best for warm sleepers — cooling gel-top bed", "medium large", "About $90–$130", "A cooler top layer for dogs who move around looking for a cool spot. The cover washes well. Gel layer adds weight.", "cooling orthopedic dog bed gel top"),
   ("Best for giant breeds — extra-large orthopedic bed", "giant", "About $130–$200", "Sized for dogs over 40 kg, with foam that holds its shape under weight. Measure your floor space first — it is big.", "extra large orthopedic dog bed giant breed")]),
 ("roundups/best-dog-ramps-older-dogs.html", "Best Dog Ramps for Older Dogs", "Car ramps, folding ramps and indoor ramps for older dogs compared by weight limit, grip and portability.",
  "<p class='lead'>A ramp only helps if your dog will actually use it. We looked at weight limits, grip, slope and how heavy the ramp is to carry — then picked five that cover most cars and homes.</p>",
  [("Best overall — folding car ramp, high-traction surface", "medium large giant", "About $70–$110", "Folds for the boot, holds large dogs, textured surface for grip. Check folded length against your boot.", "folding dog ramp car large senior"),
   ("Best lightweight — telescoping ramp", "small medium large", "About $90–$130", "Adjusts to different car heights and is light enough to carry daily. Shorter when collapsed, so it fits smaller boots.", "telescoping dog ramp lightweight car"),
   ("Best for small dogs — indoor ramp for sofa and bed", "small medium", "About $55–$85", "Gentle slope, carpeted surface. Best indoors; too short for most cars.", "indoor dog ramp sofa small dog"),
   ("Best budget — simple folding ramp", "small medium", "About $45–$70", "Does the job for small and medium dogs at a lower price. Surface is smoother than premium ramps, so pair it with a rug at the base.", "folding dog ramp budget small medium"),
   ("Best for giant breeds — heavy-duty ramp, high weight limit", "giant", "About $120–$180", "Rated for very heavy dogs, with a wide walking surface. It is heavy to carry — best kept by the car.", "heavy duty dog ramp giant breed large")]),
 ("roundups/best-harnesses-senior-dogs-weak-back-legs.html", "Best Harnesses for Senior Dogs with Weak Back Legs", "Support harnesses for senior dogs with weak back legs: rear support, full-body and padded step-in options.",
  "<p class='lead'>Weak back legs need support that spreads pressure, not a collar that pulls on the neck. These five harnesses do that in different ways — rear lift, full-body help, or simple padded walking support.</p><p>Fit matters more than brand. Measure your dog's chest and check the maker's size chart before ordering.</p>",
  [("Best rear support — padded rear harness with handle", "medium large giant", "About $30–$50", "Lifts the hindquarters with a comfortable handle. Padded straps spread pressure. Best for dogs who can still walk but tire or stumble.", "rear support dog harness handle weak back legs"),
   ("Best full-body — front and rear support harness", "medium large", "About $45–$75", "Supports both ends, so it helps with standing up as well as walking. More straps to adjust — take time fitting it the first time.", "full body dog support harness senior"),
   ("Best everyday — padded step-in harness", "small medium large", "About $20–$35", "No pulling over the head, soft lining, easy clips. Good for daily walks when your dog needs gentle support, not a lift.", "padded step in dog harness senior large"),
   ("Best for small dogs — lightweight support harness", "small", "About $20–$30", "Light and soft, with a small handle. Sized for small breeds — check the chest measurement carefully.", "small dog support harness weak legs"),
   ("Best for night walks — reflective support harness", "medium large giant", "About $30–$45", "Rear support plus reflective strips for darker evenings. Padding is thinner than the top pick, so check for rubbing on longer walks.", "reflective dog harness support senior")]),
]
# --- Comparisons ---
COMPARISONS = [
 ("comparisons/dog-ramp-vs-dog-stairs-senior-dogs.html", "Dog Ramp vs Dog Stairs for Senior Dogs", "Ramp or stairs for a senior dog? Compare slope, space, weight limits and which dogs suit each.",
  """<p class="lead">Both help an older dog reach higher places without jumping. The right choice depends on your dog, your car and your home — not on which one looks better in a photo.</p>
<table><tr><th></th><th>Dog ramp</th><th>Dog stairs</th></tr>
<tr><td><strong>Best for</strong></td><td>Dogs who struggle to lift their legs, large and giant dogs, car access</td><td>Small and medium dogs who can still step up, indoor use</td></tr>
<tr><td><strong>Slope</strong></td><td>Gentle, continuous slope</td><td>Stepped — each step is a small lift</td></tr>
<tr><td><strong>Space needed</strong></td><td>More floor space (longer is gentler)</td><td>Less floor space, but needs room at the base</td></tr>
<tr><td><strong>Weight limit</strong></td><td>Often higher — good for large dogs</td><td>Check carefully; many sets suit small dogs only</td></tr>
<tr><td><strong>Learning curve</strong></td><td>Some dogs hesitate at first; treats and patience help</td><td>Usually familiar — most dogs have used steps before</td></tr>
<tr><td><strong>Portability</strong></td><td>Folding ramps travel well</td><td>Heavier sets stay in one place</td></tr></table>
<h2>Our take</h2><p>Choose a <strong>ramp</strong> if your dog struggles to lift their legs, if they are large, or if the main job is getting into the car. Choose <strong>stairs</strong> if your dog is small or medium, still steps up happily, and the main job is the sofa or bed indoors.</p><p>If you are unsure, a ramp is the safer first try for most senior dogs — the slope is gentler, and there is no step to misjudge. Whichever you choose, introduce it slowly, with treats, and never force your dog up it.</p>
<h2>What to check before you buy</h2><ul><li>Measure the height you need to reach, and the floor space you have.</li><li>Check the weight limit — choose one rated well above your dog.</li><li>Check the surface grip, especially for outdoor or car use.</li></ul>
<p>Related: <a href="../roundups/best-dog-ramps-older-dogs.html">Best Dog Ramps for Older Dogs</a> · <a href="../articles/how-to-help-older-dog-get-into-car.html">How to Help an Older Dog Get Into the Car</a></p>"""),
 ("comparisons/memory-foam-vs-egg-crate-dog-beds.html", "Memory Foam vs Orthopedic Egg-Crate Dog Beds", "Memory foam or egg-crate foam for a senior dog bed? Compare support, durability, price and washability.",
  """<p class="lead">Both are sold as “orthopedic” beds, but they feel and last quite differently. Here is the honest difference, without the marketing.</p>
<table><tr><th></th><th>Memory foam</th><th>Egg-crate foam</th></tr>
<tr><td><strong>How it feels</strong></td><td>Dense, even support; moulds slowly to the body</td><td>Lighter, softer, with peaks and valleys</td></tr>
<tr><td><strong>Support</strong></td><td>Generally better for heavier dogs; holds shape longer</td><td>Comfortable at first, but can flatten faster under weight</td></tr>
<tr><td><strong>Durability</strong></td><td>Lasts longer if thick enough (4 inches or more)</td><td>May need replacing sooner for large dogs</td></tr>
<tr><td><strong>Price</strong></td><td>Usually higher</td><td>Usually lower</td></tr>
<tr><td><strong>Weight</strong></td><td>Heavier to move</td><td>Lighter to move and store</td></tr>
<tr><td><strong>Best for</strong></td><td>Medium, large and giant dogs; dogs who sleep in one spot</td><td>Small dogs; lighter dogs; a spare or travel bed</td></tr></table>
<h2>Our take</h2><p>For most senior dogs, <strong>memory foam is the better long-term choice</strong> — especially if your dog is medium or large. Egg-crate foam is a fair budget option for small, light dogs, or as a second bed.</p><p>Whatever the foam type, check the thickness and whether the cover is removable and washable. A thin bed of either type will flatten quickly and stop supporting your dog.</p>
<p>Related: <a href="../roundups/best-orthopedic-dog-beds-senior-dogs.html">Best Orthopedic Dog Beds for Senior Dogs</a> · <a href="../categories/orthopedic-beds.html">Orthopedic Beds and Comfort</a></p>"""),
]

# --- Articles (5) ---
ARTICLES = [
 ("articles/10-signs-dog-entering-senior-years.html", "10 Signs Your Dog Is Entering Their Senior Years", "Ten gentle signs your dog is becoming a senior — and when to mention them to your vet.",
  """<p class="lead">Dogs do not become senior overnight. The changes are usually small, and they creep in over months. Noticing them early means you can make small adjustments — a better bed, shorter walks, a rug on a slippery floor — before they become problems.</p>
<p>These are common changes owners notice. They are not a diagnosis. If you are worried about any of them, mention it to your vet.</p>
<ol><li><strong>Slower on walks.</strong> Your dog still enjoys going out, but lags behind, or wants to turn for home sooner.</li>
<li><strong>Stiffer in the morning.</strong> Slow to get up after a sleep, then loosens up after a few minutes.</li>
<li><strong>Grey around the muzzle.</strong> The classic sign — and usually the least worrying one.</li>
<li><strong>Sleeping more.</strong> Longer naps, deeper sleep, less interest in staying up late with you.</li>
<li><strong>Less interest in jumping.</strong> Hesitating before the car, the sofa or the bed.</li>
<li><strong>Cloudy eyes or less keen hearing.</strong> Bumping into things in dim light, or not hearing you call from another room.</li>
<li><strong>Changes in weight.</strong> Gaining or losing weight without a change in food. Your vet can advise on this — we do not give diet advice.</li>
<li><strong>More accidents indoors.</strong> Needing to go out more often, or not quite making it to the door.</li>
<li><strong>Less patience with noise or fuss.</strong> Older dogs often prefer calm and routine.</li>
<li><strong>Thinner coat or drier skin.</strong> Grooming needs change with age; gentle brushing helps.</li></ol>
<h2>What to do next</h2><p>Start with the easy wins: a supportive bed, a non-slip route through the house, and shorter, more frequent walks. Keep a note of changes and take it to your vet — a short list is more useful than a vague worry.</p>
<p>Related: <a href="make-home-safer-senior-dog.html">How to Make Your Home Safer for a Senior Dog</a> · <a href="../categories/orthopedic-beds.html">Orthopedic Beds and Comfort</a></p>"""),
 ("articles/make-home-safer-senior-dog.html", "How to Make Your Home Safer for a Senior Dog", "Practical, low-cost ways to make your home safer for a senior dog: floors, stairs, lighting and layout.",
  """<p class="lead">You do not need to rebuild your house. Most of the risk for a senior dog is in three places: slippery floors, stairs, and dark hallways. Fix those, and the rest is detail.</p>
<h2>1. Give paws something to grip</h2><p>Put a rug runner on the route your dog uses most — bed to water bowl to door. Make sure rugs have a non-slip backing or a grip pad underneath, or they slide and become a hazard themselves. See <a href="../categories/home-safety.html">Home Safety</a> for options.</p>
<h2>2. Block the stairs if needed</h2><p>If your dog is unsteady, a gate at the top of the stairs is worth more than any gadget. Choose a pressure-mounted gate that fits your doorway, and check it stays firm.</p>
<h2>3. Light the night route</h2><p>Older eyes see less well in the dark. A motion-sensor night light in the hallway, and one near the garden door, helps your dog find their way at 3 a.m. without waking the house.</p>
<h2>4. Clear the paths</h2><p>Move trailing cables, shoes and clutter off the main walking routes. Keep water, food and bed in the same places — routine helps a dog who cannot see or hear as well as they used to.</p>
<h2>5. Make the bed and sofa reachable</h2><p>A ramp or low steps beside the sofa or bed means your dog does not have to jump. Read <a href="../comparisons/dog-ramp-vs-dog-stairs-senior-dogs.html">Ramp vs Stairs</a> to choose.</p>
<h2>6. Check the garden</h2><p>Fill holes, block gaps in fences, and make sure the step out of the back door is not a trip hazard. A ramp over one high step can help.</p>
<p>Related: <a href="senior-dog-slipping-hardwood-floors.html">Senior Dog Slipping on Hardwood Floors? Practical Fixes</a></p>"""),
 ("articles/how-to-help-older-dog-get-into-car.html", "How to Help an Older Dog Get Into the Car", "Gentle ways to help an older dog get into the car: ramps, lifting, and making the boot comfortable.",
  """<p class="lead">The car used to mean a jump and a wag. Now it can mean a pause, a look at you, and a small struggle. Here is how to make it easy again.</p>
<h2>Use a ramp</h2><p>A folding ramp is the kindest option for most dogs. Choose one rated well above your dog's weight, with a non-slip surface. Introduce it at home first — flat on the ground, with treats — before you try it at the car. See our <a href="../roundups/best-dog-ramps-older-dogs.html">Best Dog Ramps for Older Dogs</a>.</p>
<h2>If you need to lift</h2><p>Support the chest and hindquarters together, and lift in one smooth movement. A rear support sling can help for the back end. If lifting hurts your back, or your dog is heavy, a ramp is the better answer — do not risk an injury to either of you.</p>
<h2>Make the car comfortable</h2><p>A non-slip mat in the boot, a familiar blanket, and a little space to lie down help. Keep the car cool, and never leave a dog in a hot car.</p>
<h2>Keep practising gently</h2><p>Short, calm trips with a reward at the end keep the car a happy place. If your dog is very anxious about the car, talk to your vet — anxiety is a health question, not a training failure.</p>"""),
 ("articles/senior-dog-slipping-hardwood-floors.html", "Senior Dog Slipping on Hardwood Floors? Practical Fixes", "Why senior dogs slip on hardwood floors, and practical fixes: rugs, socks, paw grips and layout changes.",
  """<p class="lead">Hardwood looks lovely and is easy to clean. For an older dog with weaker legs, it can feel like an ice rink. The good news: you do not need to replace the floor.</p>
<h2>Why it happens</h2><p>Older dogs have less muscle strength, less grip from worn pads, and slower reactions. A smooth floor gives paws nothing to hold on to, so legs splay and confidence drops.</p>
<h2>Fix 1: Rugs on the main routes</h2><p>Start with a runner from bed to door, and a rug by the water bowl. Use a non-slip backing or grip pad — a sliding rug is worse than no rug. See <a href="../categories/home-safety.html">Home Safety</a>.</p>
<h2>Fix 2: Paw grip socks or toe grips</h2><p>Rubberised socks give grip indoors. Introduce them for short periods first — most dogs need a day or two to get used to them. Check the fit; socks that are too tight or too loose will come off.</p>
<h2>Fix 3: Keep nails trimmed</h2><p>Long nails change how a paw meets the floor and make slipping worse. If you are unsure how to trim them, ask a groomer or vet to show you.</p>
<h2>Fix 4: Keep paws clean and dry</h2><p>Wet paws slip more. A quick wipe after coming in from the garden helps, and a mat by the door catches most of it.</p>
<h2>Fix 5: Slow down the house</h2><p>Excited greetings on a slippery floor end badly. Greet your dog calmly, and keep the main route clear so they do not have to turn sharply.</p>
<p>If slipping is sudden, or your dog seems in pain, talk to your vet. This guide covers the home, not the cause.</p>"""),
 ("articles/how-often-should-senior-dog-walk.html", "How Often Should a Senior Dog Walk?", "How often and how far should a senior dog walk? Shorter, more frequent walks, rest days and signs of tiredness.",
  """<p class="lead">There is no single number that fits every senior dog. A small, stiff dog and a large, still-energetic dog need different things. What works for most older dogs is shorter walks, more often, with rest built in.</p>
<h2>A good starting point</h2><p>Two or three short walks a day — 15 to 20 minutes each — suits many senior dogs better than one long walk. Let your dog sniff, pause and set the pace. Sniffing is tiring in a good way.</p>
<h2>Signs your dog has had enough</h2><ul><li>Lagging behind or stopping often</li><li>Panting hard, or lying down mid-walk</li><li>Stiffness the next morning that lasts longer than usual</li><li>Reluctance to go out the next day</li></ul><p>If you see these, shorten the next walk. If they persist, mention them to your vet.</p>
<h2>Rest days matter</h2><p>One quieter day a week — garden time and gentle play instead of a walk — helps older joints recover. It is not laziness; it is recovery.</p>
<h2>Make walks easier</h2><p>A padded harness with a handle helps on curbs and steps — see <a href="../roundups/best-harnesses-senior-dogs-weak-back-legs.html">Best Harnesses for Senior Dogs with Weak Back Legs</a>. Walk on grass or soft paths where you can, avoid the hottest part of the day, and carry water in warm weather.</p>
<p>Your dog will tell you what they need. The walk that ends with a happy, tired dog — not an exhausted one — is the right length.</p>"""),
]

# --- Build all pages ---
if __name__ == "__main__":
    page("index.html", "", "SilverMuzzle — Comfort for Older Dogs", "Warm, practical guides and product roundups for owners of senior dogs (7+). Beds, ramps, harnesses, feeding, grooming and home safety.", HOME_BODY, disclaimer=False)
    page("about.html", "", "About SilverMuzzle", "About SilverMuzzle: who writes it, how we research products, and our vet-review policy.", ABOUT_BODY, disclaimer=False)
    page("affiliate-disclosure.html", "", "Affiliate Disclosure", "SilverMuzzle affiliate disclosure: Amazon Associates, commissions and how recommendations are made.", DISCLOSURE_BODY, disclaimer=False)
    page("privacy.html", "", "Privacy Policy", "SilverMuzzle privacy policy: what we collect, cookies, analytics and affiliate links.", PRIVACY_BODY, disclaimer=False)
    # Content roadmap HTML page, generated from content-plan.md so a rebuild never loses it
    import re as _re
    _md = open(os.path.join(BASE, "content-plan.md")).read()
    _html = []
    for _line in _md.splitlines():
        if _line.startswith("## "):
            _html.append(f"<h2>{_line[3:]}</h2>")
        elif _line.startswith("# "):
            continue
        elif _line.startswith("|") and "---" not in _line:
            _cells = [c.strip() for c in _line.strip().strip("|").split("|")]
            if _cells[0] == "#":
                _html.append("<table><tr><th>#</th><th>Article idea</th><th>Intent</th><th>Internal link</th></tr>")
            else:
                _html.append(f"<tr><td>{_cells[0]}</td><td>{_cells[1]}</td><td>{_cells[2]}</td><td><a href='{_cells[3][1:]}'>{_cells[3]}</a></td></tr>")
        elif _line.startswith("|"):
            continue
        elif _line.strip() == "":
            _html.append("</table>" if _html and _html[-1].startswith("<tr") else "")
        else:
            _html.append(f"<p>{_line}</p>")
    _body = "<p class='breadcrumbs'><a href='index.html'>Home</a> / Content roadmap</p><h1>Content Roadmap — 40 More Article Ideas</h1><p class='lead'>Grouped by category, with search intent and the internal link each article should point to. The full source file is <a href='content-plan.md'>content-plan.md</a>.</p>" + "\n".join(_html)
    page("content-plan.html", "", "Content Roadmap — 40 Article Ideas", "SilverMuzzle content roadmap: 40 long-tail article ideas grouped by category with intent and internal links.", _body, disclaimer=False)
    for path, title, desc, intro, products in CATS:
        body = f"<p class='breadcrumbs'><a href='../index.html'>Home</a> / {title}</p><h1>{title}</h1>{intro}{aff_note()}{filter_ui()}<div class='grid'>"
        for name, sizes, price, blurb, q in products:
            body += product_card(name, sizes, price, blurb, q)
        body += "</div><div class='faq'><h2>Common questions</h2><details><summary>Do I need the most expensive option?</summary><p>Usually not. Match the size and weight limit to your dog first, then choose the best you can afford in that size. A well-fitting mid-price option beats a premium one in the wrong size.</p></details><details><summary>What if my dog will not use it?</summary><p>Introduce it slowly, with treats, and let your dog investigate it at their own pace. Never force them. If they still refuse after a few days, it may be the wrong shape or size — check the return policy before you buy.</p></details></div>"
        page(path, "../", title, desc, body)
    for path, title, desc, intro, products in ROUNDUPS:
        body = f"<p class='breadcrumbs'><a href='../index.html'>Home</a> / Roundup</p><h1>{title}</h1>{intro}{aff_note()}{filter_ui()}<div class='grid'>"
        for name, sizes, price, blurb, q in products:
            badge = name.split(" — ")[0]
            body += product_card(name, sizes, price, blurb, q, badge=badge)
        body += "</div><h2>How we chose these</h2><p>We read owner reviews, checked materials and safety details, and compared specifications — size, weight limit, washability and warranty. We do not claim hands-on testing unless we have actually done it. Prices change, so check the listing before you buy.</p>"
        page(path, "../", title, desc, body)
    for path, title, desc, body in COMPARISONS:
        page(path, "../", title, desc, f"<p class='breadcrumbs'><a href='../index.html'>Home</a> / Comparison</p><h1>{title}</h1>{body}")
    for path, title, desc, body in ARTICLES:
        page(path, "../", title, desc, f"<p class='breadcrumbs'><a href='../index.html'>Home</a> / Guide</p><h1>{title}</h1><div class='article-body'>{body}</div>")
    print("done")
