from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)

# ---------------- Demo editor ----------------
demo_path = Path("demo-editor.html")
demo = demo_path.read_text(encoding="utf-8")

old_browser_css = ".browser{width:100%;max-width:1280px;margin:0 auto;background:#fff;border:1px solid rgba(21,21,37,.13);border-radius:18px;box-shadow:var(--shadow);overflow:hidden;transition:max-width .25s ease}.browser.tablet{max-width:820px}.browser.mobile{max-width:420px}.browser-bar{height:42px;background:#f1f1f6;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:12px;padding:0 13px}.dots{display:flex;gap:6px}.dots i{width:8px;height:8px;border-radius:50%;background:#c9c9d2}.address{flex:1;max-width:560px;height:25px;border-radius:7px;background:#fff;border:1px solid #dedee7;display:flex;align-items:center;gap:7px;padding:0 10px;color:#8a8a99;font-size:.64rem}.browser-favicon{width:14px;height:14px;border-radius:3px;object-fit:contain;background:#ececf2}.site{--site-accent:#7657ff;color:#20202d;background:#fff;min-height:700px}"
new_browser_css = ".browser{width:100%;max-width:none;margin:0 auto;background:#fff;border:0;border-radius:10px;box-shadow:none;overflow:hidden;container-type:inline-size}.browser-bar{height:42px;background:#f1f1f6;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:12px;padding:0 13px}.dots{display:flex;gap:6px}.dots i{width:8px;height:8px;border-radius:50%;background:#c9c9d2}.address{flex:1;max-width:560px;height:25px;border-radius:7px;background:#fff;border:1px solid #dedee7;display:flex;align-items:center;gap:7px;padding:0 10px;color:#8a8a99;font-size:.64rem;min-width:0}.address span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.browser-favicon{width:14px;height:14px;border-radius:3px;object-fit:contain;background:#ececf2;flex:0 0 auto}.site{--site-accent:#7657ff;color:#20202d;background:#fff;min-height:700px;min-width:0;overflow:hidden}"
demo = replace_once(demo, old_browser_css, new_browser_css, "browser css")

frame_css = r'''
.device-stage{display:flex;justify-content:center;align-items:flex-start;min-width:0;padding:10px 8px 58px;overflow:auto}
.device-frame{position:relative;width:100%;transition:width .28s ease,max-width .28s ease,padding .28s ease,border-radius .28s ease;background:#23232d;box-shadow:0 24px 70px rgba(18,16,44,.23)}
.device-frame.device-laptop{max-width:1280px;padding:14px 14px 24px;border-radius:20px 20px 9px 9px}
.device-frame.device-tablet{max-width:820px;padding:16px;border-radius:32px}
.device-frame.device-mobile{max-width:420px;padding:12px;border-radius:36px}
.device-frame::before{content:'';position:absolute;z-index:3;left:50%;transform:translateX(-50%);background:#0f0f15}
.device-frame.device-laptop::before{top:5px;width:6px;height:6px;border-radius:50%;box-shadow:0 0 0 2px #343442}
.device-frame.device-tablet::before{top:5px;width:7px;height:7px;border-radius:50%;box-shadow:0 0 0 2px #343442}
.device-frame.device-mobile::before{top:5px;width:72px;height:18px;border-radius:999px}
.device-frame.device-laptop::after{content:'';position:absolute;left:-4%;right:-4%;bottom:-16px;height:18px;border-radius:0 0 60px 60px;background:linear-gradient(#c8cad2,#9396a0);box-shadow:0 8px 12px rgba(18,16,44,.18)}
.device-frame.device-tablet::after{content:'';position:absolute;left:50%;bottom:5px;width:48px;height:4px;transform:translateX(-50%);border-radius:999px;background:#555663}
.device-frame.device-mobile::after{content:'';position:absolute;left:50%;bottom:4px;width:92px;height:4px;transform:translateX(-50%);border-radius:999px;background:#6e6f78}
.device-frame.device-tablet .browser,.device-frame.device-mobile .browser{border-radius:18px}
.device-frame.device-mobile .browser-bar{height:36px;padding:0 9px;gap:8px}.device-frame.device-mobile .dots{display:none}.device-frame.device-mobile .address{height:22px;font-size:.58rem;padding:0 7px}
.device-label{position:absolute;left:50%;bottom:-42px;transform:translateX(-50%);font-size:.66rem;font-weight:900;color:#747486;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}
'''
demo = replace_once(demo, ".site-nav{min-height:68px", frame_css + "\n.site-nav{min-height:68px", "device frame css insertion")

old_rules_start = "/* Device preview rules: these are tied to the simulated viewport, not the outer browser width. */"
old_rules_end = ".browser.tablet .hero-copy h2,.browser.tablet .inner-hero h2{font-size:clamp(2.25rem,6vw,3.8rem)}"
start = demo.find(old_rules_start)
end = demo.find(old_rules_end)
if start == -1 or end == -1:
    raise RuntimeError("device rule block not found")
end += len(old_rules_end)
container_rules = r'''/* Responsive preview rules use the simulated preview width itself. */
@container (max-width:900px){
 .site .demo-hero{grid-template-columns:1fr;min-height:0}.site .hero-image{min-height:300px}.site .hero-copy{padding:46px 34px}.site .hero-copy h2,.site .inner-hero h2{font-size:clamp(2.4rem,7cqw,3.8rem)}.site .inner-hero{padding:56px 34px}.site .site-section{padding:48px 34px}.site .services-grid,.site .content-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.site .gallery-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.site .contact-strip{padding:32px 34px}
}
@container (max-width:560px){
 .site .site-nav{padding:10px 16px;align-items:center}.site .site-brand{font-size:.92rem;min-width:0}.site .site-brand-logo{width:36px;height:36px}.site .site-links{display:none}.site .site-nav::after{content:'☰';display:grid;place-items:center;width:34px;height:34px;border:1px solid rgba(24,24,40,.1);border-radius:10px;background:#f7f7fb;color:#45455a;font-size:1rem;font-weight:900;flex:0 0 auto}.site .hero-copy{padding:34px 20px}.site .hero-copy h2,.site .inner-hero h2{font-size:clamp(2rem,10cqw,2.55rem);overflow-wrap:anywhere}.site .hero-copy p{font-size:.9rem}.site .hero-button{width:100%;justify-content:center}.site .hero-image{min-height:230px}.site .inner-hero{padding:42px 20px}.site .site-section{padding:36px 20px}.site .services-grid,.site .content-grid,.site .gallery-grid{grid-template-columns:1fr}.site .contact-strip{grid-template-columns:1fr;padding:28px 20px}.site .contact-details{text-align:left}.site .site-footer{padding:19px 20px;flex-direction:column}.site .faq-item{padding:15px}.site .about-copy{font-size:.8rem}.site .service,.site .content-card{min-width:0}.site h2,.site h3,.site h4,.site p{max-width:100%;overflow-wrap:anywhere}
}'''
demo = demo[:start] + container_rules + demo[end:]

old_preview = '''<main class="preview-zone">
  <div class="preview-toolbar"><span class="preview-label">Live preview <span id="previewPageName"></span></span><div class="device-switch"><button class="active" data-device="desktop">Desktop</button><button data-device="tablet">Tablet</button><button data-device="mobile">Mobile</button></div></div>
  <div class="browser" id="browser">
    <div class="browser-bar"><div class="dots"><i></i><i></i><i></i></div><div class="address"><img class="browser-favicon" id="browserFavicon" src="webwizard.png" alt=""><span id="addressBar"></span></div></div>
    <article class="site" id="sitePreview">
      <nav class="site-nav">
        <button class="site-brand" id="pvBusinessName"><img class="site-brand-logo" id="pvLogo" alt="" hidden><span id="pvBusinessText"></span></button>
        <div class="site-links" id="pvNav"></div>
      </nav>
      <div id="pagePreview"></div>
      <footer class="site-footer"><span id="pvFooter"></span><span>Privacy &nbsp; · &nbsp; Terms</span></footer>
    </article>
  </div>
</main>'''
new_preview = '''<main class="preview-zone">
  <div class="preview-toolbar"><span class="preview-label">Live preview <span id="previewPageName"></span></span><div class="device-switch"><button class="active" data-device="desktop">Laptop</button><button data-device="tablet">Tablet</button><button data-device="mobile">Mobile</button></div></div>
  <div class="device-stage">
    <div class="device-frame device-laptop" id="deviceFrame">
      <div class="browser" id="browser">
        <div class="browser-bar"><div class="dots"><i></i><i></i><i></i></div><div class="address"><img class="browser-favicon" id="browserFavicon" src="webwizard.png" alt=""><span id="addressBar"></span></div></div>
        <article class="site" id="sitePreview">
          <nav class="site-nav">
            <button class="site-brand" id="pvBusinessName"><img class="site-brand-logo" id="pvLogo" alt="" hidden><span id="pvBusinessText"></span></button>
            <div class="site-links" id="pvNav"></div>
          </nav>
          <div id="pagePreview"></div>
          <footer class="site-footer"><span id="pvFooter"></span><span>Privacy &nbsp; · &nbsp; Terms</span></footer>
        </article>
      </div>
      <span class="device-label" id="deviceLabel">Laptop preview</span>
    </div>
  </div>
</main>'''
demo = replace_once(demo, old_preview, new_preview, "preview frame markup")

old_switch = "document.querySelectorAll('[data-device]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-device]').forEach(x=>x.classList.remove('active'));b.classList.add('active');browser.classList.remove('mobile','tablet');if(b.dataset.device==='mobile')browser.classList.add('mobile');if(b.dataset.device==='tablet')browser.classList.add('tablet')});"
new_switch = "document.querySelectorAll('[data-device]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-device]').forEach(x=>x.classList.remove('active'));b.classList.add('active');const d=b.dataset.device;deviceFrame.className='device-frame '+(d==='mobile'?'device-mobile':d==='tablet'?'device-tablet':'device-laptop');deviceLabel.textContent=(d==='mobile'?'Mobile':d==='tablet'?'Tablet':'Laptop')+' preview'});"
demo = replace_once(demo, old_switch, new_switch, "device switch js")

demo_path.write_text(demo, encoding="utf-8")

# ---------------- Main site pricing ----------------
index_path = Path("index.html")
index = index_path.read_text(encoding="utf-8")

nav_old = '''        <a href="#services">Services</a>
        <a href="#work">Our work</a>
        <a href="#process">Process</a>'''
nav_new = '''        <a href="#services">Services</a>
        <a href="#work">Our work</a>
        <a href="#pricing">Pricing</a>
        <a href="#process">Process</a>'''
index = replace_once(index, nav_old, nav_new, "pricing nav link")

pricing_css = r'''
    /* Pricing */
    .pricing-section{position:relative;background:linear-gradient(180deg,#fff 0%,#f7f6ff 100%)}
    .pricing-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:34px;align-items:stretch}
    .price-card{position:relative;display:flex;flex-direction:column;padding:28px;border:1px solid var(--line);border-radius:22px;background:#fff;box-shadow:var(--shadow-soft)}
    .price-card.featured{border-color:rgba(109,74,255,.42);box-shadow:0 24px 60px rgba(83,57,190,.14);transform:translateY(-6px)}
    .price-badge{position:absolute;top:16px;right:16px;padding:6px 9px;border-radius:999px;background:var(--surface-soft);color:var(--purple-dark);font-size:.66rem;font-weight:900;text-transform:uppercase;letter-spacing:.06em}
    .price-card h3{margin:0;color:var(--night);font-size:1.22rem}
    .price-for{margin-top:5px;color:var(--muted);font-size:.82rem;line-height:1.5}
    .price{display:flex;align-items:flex-end;gap:7px;margin:23px 0 18px;color:var(--night)}
    .price strong{font-size:2.7rem;line-height:.9;letter-spacing:-.06em}.price span{padding-bottom:4px;color:var(--muted);font-size:.8rem;font-weight:800}
    .price-list{display:grid;gap:10px;margin:0 0 26px;padding:0;list-style:none;color:#555568;font-size:.86rem}
    .price-list li{position:relative;padding-left:24px;line-height:1.45}.price-list li::before{content:'✓';position:absolute;left:0;top:0;color:var(--purple);font-weight:950}
    .price-card .button{margin-top:auto;width:100%;justify-content:center}
    .care-strip{display:grid;grid-template-columns:1fr auto;gap:26px;align-items:center;margin-top:22px;padding:25px 28px;border:1px solid rgba(109,74,255,.16);border-radius:20px;background:linear-gradient(135deg,#17142f,#29205d);color:#fff;box-shadow:var(--shadow-soft)}
    .care-strip h3{margin:0 0 7px;font-size:1.15rem}.care-strip p{margin:0;color:rgba(255,255,255,.7);font-size:.86rem;line-height:1.6;max-width:760px}
    .care-price{text-align:right;white-space:nowrap}.care-price strong{display:block;font-size:1.8rem;letter-spacing:-.04em}.care-price span{font-size:.72rem;color:rgba(255,255,255,.62)}
    .pricing-note{margin:20px auto 0;max-width:880px;text-align:center;color:var(--muted);font-size:.78rem;line-height:1.6}
    @media(max-width:900px){.pricing-grid{grid-template-columns:1fr}.price-card.featured{transform:none}.care-strip{grid-template-columns:1fr}.care-price{text-align:left}}
'''
index = replace_once(index, "    /* Customer control / demo editor section */", pricing_css + "\n    /* Customer control / demo editor section */", "pricing css insertion")

pricing_html = r'''
    <section class="pricing-section" id="pricing">
      <div class="container">
        <div class="section-head reveal">
          <div>
            <p class="section-kicker">Straightforward pricing</p>
            <h2 class="section-title">Professional websites. Small-business prices.</h2>
          </div>
          <p class="section-lead">You get a professionally built website rather than another DIY subscription to figure out yourself. Choose a simple starting point and only add complexity when your business actually needs it.</p>
        </div>

        <div class="pricing-grid">
          <article class="price-card reveal">
            <h3>One Page Launch</h3>
            <p class="price-for">For a new venture, local service or simple professional presence.</p>
            <div class="price"><strong>£129</strong><span>one-off</span></div>
            <ul class="price-list">
              <li>Professionally designed one-page website</li>
              <li>Mobile, tablet and desktop responsive</li>
              <li>Contact form and social links</li>
              <li>Basic search-friendly setup</li>
              <li>One round of revisions</li>
              <li>Web Wizard address included</li>
            </ul>
            <a class="button button-secondary" href="#contact">Choose One Page Launch</a>
          </article>

          <article class="price-card featured reveal">
            <span class="price-badge">Most popular</span>
            <h3>Small Business</h3>
            <p class="price-for">A complete website for most sole traders, small businesses and organisations.</p>
            <div class="price"><strong>£179</strong><span>one-off</span></div>
            <ul class="price-list">
              <li>Up to five professionally built pages</li>
              <li>Customer editor for routine updates</li>
              <li>Contact form, maps and social links</li>
              <li>Basic on-page SEO across the site</li>
              <li>Content and wording tidy-up</li>
              <li>Two rounds of revisions</li>
              <li>Existing domain connection included</li>
            </ul>
            <a class="button button-primary" href="#contact">Choose Small Business</a>
          </article>

          <article class="price-card reveal">
            <h3>Business Plus</h3>
            <p class="price-for">For businesses needing more pages, content types and room to grow.</p>
            <div class="price"><strong>£299</strong><span>one-off</span></div>
            <ul class="price-list">
              <li>Up to ten professionally built pages</li>
              <li>News, blog, gallery or FAQ sections as required</li>
              <li>Analytics and Search Console setup</li>
              <li>Enhanced on-page SEO structure</li>
              <li>Customer editor for routine updates</li>
              <li>Three rounds of revisions</li>
              <li>Priority launch support</li>
            </ul>
            <a class="button button-secondary" href="#contact">Choose Business Plus</a>
          </article>
        </div>

        <div class="care-strip reveal">
          <div>
            <h3>Optional Website Care</h3>
            <p>Technical hosting, SSL, monitoring, version recovery and ongoing support for <strong>£6.99 a month</strong>. One small assisted content change each quarter is included. Prefer to manage routine content yourself? Your editor remains available without taking the care plan.</p>
          </div>
          <div class="care-price"><strong>£6.99</strong><span>per month · optional</span></div>
        </div>
        <p class="pricing-note">Existing domain connection is included where technically possible. If you need a new custom domain, registration is charged separately at the registrar cost. A Web Wizard address such as <strong>yourbusiness.thewebdesignwizard.co.uk</strong> can be used instead. Bespoke integrations, online shops and unusually complex functionality are quoted separately before work begins.</p>
      </div>
    </section>

'''
index = replace_once(index, "    <!-- WEB-WIZARD-CUSTOMER-CONTROL -->", pricing_html + "    <!-- WEB-WIZARD-CUSTOMER-CONTROL -->", "pricing html insertion")

index_path.write_text(index, encoding="utf-8")
print("Pricing and device preview update prepared successfully")
