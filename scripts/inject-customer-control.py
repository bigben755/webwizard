from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

MARKER = "<!-- WEB-WIZARD-CUSTOMER-CONTROL -->"
if MARKER in html:
    raise SystemExit(0)

css = r'''

    /* Customer control / demo editor section */
    .customer-control {
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at 88% 12%, rgba(54,215,218,.12), transparent 27%),
        radial-gradient(circle at 8% 86%, rgba(109,74,255,.12), transparent 30%),
        linear-gradient(180deg, #ffffff 0%, #f7f6ff 100%);
    }
    .customer-control-grid {
      display: grid;
      grid-template-columns: .92fr 1.08fr;
      gap: clamp(42px, 7vw, 88px);
      align-items: center;
    }
    .customer-control-copy .section-title { max-width: 690px; }
    .customer-control-copy .section-lead { max-width: 640px; }
    .control-points {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
      margin: 30px 0 34px;
    }
    .control-point {
      padding: 19px;
      border: 1px solid var(--line);
      border-radius: 16px;
      background: rgba(255,255,255,.82);
      box-shadow: var(--shadow-soft);
    }
    .control-point-icon {
      width: 38px;
      height: 38px;
      display: grid;
      place-items: center;
      margin-bottom: 13px;
      border-radius: 12px;
      color: var(--purple-dark);
      background: var(--surface-soft);
    }
    .control-point-icon svg { width: 19px; height: 19px; }
    .control-point strong {
      display: block;
      margin-bottom: 5px;
      color: var(--night);
      font-size: .96rem;
      line-height: 1.25;
    }
    .control-point span {
      display: block;
      color: var(--muted);
      font-size: .84rem;
      line-height: 1.55;
    }
    .control-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }
    .control-actions .button-secondary {
      color: var(--night);
      border-color: var(--line);
      background: #fff;
      box-shadow: var(--shadow-soft);
    }
    .editor-demo-card {
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(109,74,255,.18);
      border-radius: 26px;
      background: #fff;
      box-shadow: 0 30px 80px rgba(43,34,102,.16);
    }
    .editor-demo-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 17px 19px;
      color: #fff;
      background: linear-gradient(135deg, #11102a, #24205b);
    }
    .editor-demo-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: .82rem;
      font-weight: 900;
    }
    .editor-demo-mark {
      width: 31px;
      height: 31px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      color: #fff;
      background: linear-gradient(135deg, var(--purple), #8d78ff);
      font-size: .75rem;
    }
    .editor-demo-status {
      padding: 6px 9px;
      border: 1px solid rgba(255,255,255,.14);
      border-radius: 999px;
      color: rgba(255,255,255,.76);
      background: rgba(255,255,255,.07);
      font-size: .68rem;
      font-weight: 800;
    }
    .editor-demo-body {
      display: grid;
      grid-template-columns: 165px 1fr;
      min-height: 390px;
    }
    .editor-demo-sidebar {
      padding: 18px 13px;
      border-right: 1px solid var(--line);
      background: #fafafe;
    }
    .editor-demo-sidebar small {
      display: block;
      padding: 0 8px 8px;
      color: var(--muted);
      font-size: .63rem;
      font-weight: 900;
      letter-spacing: .09em;
      text-transform: uppercase;
    }
    .editor-page-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
      padding: 9px 9px;
      border-radius: 9px;
      color: #555568;
      font-size: .72rem;
      font-weight: 800;
    }
    .editor-page-row.active {
      color: var(--purple-dark);
      background: #eeebff;
    }
    .editor-page-dot {
      width: 21px;
      height: 21px;
      display: grid;
      place-items: center;
      flex: 0 0 auto;
      border: 1px solid var(--line);
      border-radius: 7px;
      background: #fff;
      font-size: .55rem;
    }
    .editor-add-row {
      margin-top: 10px;
      padding: 9px;
      border: 1px dashed rgba(109,74,255,.35);
      border-radius: 9px;
      color: var(--purple-dark);
      text-align: center;
      font-size: .69rem;
      font-weight: 900;
    }
    .editor-demo-preview {
      padding: 20px;
      background: #f1f1f7;
    }
    .mini-browser {
      overflow: hidden;
      height: 100%;
      min-height: 345px;
      border: 1px solid var(--line);
      border-radius: 15px;
      background: #fff;
      box-shadow: 0 14px 32px rgba(25,18,66,.09);
    }
    .mini-browser-bar {
      display: flex;
      align-items: center;
      gap: 6px;
      height: 31px;
      padding: 0 10px;
      border-bottom: 1px solid var(--line);
      background: #f8f8fb;
    }
    .mini-browser-bar i {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #c5c5cf;
    }
    .mini-browser-address {
      width: 58%;
      height: 15px;
      margin-left: 6px;
      border: 1px solid #e5e5ec;
      border-radius: 999px;
      background: #fff;
    }
    .mini-site-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 12px 15px;
      border-bottom: 1px solid var(--line);
      font-size: .61rem;
      font-weight: 900;
    }
    .mini-site-links { display: flex; gap: 10px; color: #777789; font-weight: 750; }
    .mini-site-hero {
      padding: 35px 24px 32px;
      background: linear-gradient(135deg, #f7f5ff, #fff);
    }
    .mini-kicker {
      width: 72px;
      height: 6px;
      margin-bottom: 13px;
      border-radius: 999px;
      background: var(--purple);
      opacity: .65;
    }
    .mini-heading {
      width: 78%;
      height: 17px;
      margin-bottom: 8px;
      border-radius: 999px;
      background: #222039;
      box-shadow: 0 25px 0 #222039;
    }
    .mini-copy {
      width: 67%;
      height: 6px;
      margin-top: 47px;
      border-radius: 999px;
      background: #c8c7d2;
      box-shadow: 0 12px 0 #d9d8e0;
    }
    .mini-button {
      width: 82px;
      height: 25px;
      margin-top: 28px;
      border-radius: 999px;
      background: var(--purple);
    }
    .mini-site-cards {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      padding: 18px;
    }
    .mini-site-card {
      height: 72px;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: #fff;
    }
    @media (max-width: 980px) {
      .customer-control-grid { grid-template-columns: 1fr; }
      .editor-demo-card { max-width: 720px; margin-inline: auto; width: 100%; }
    }
    @media (max-width: 620px) {
      .control-points { grid-template-columns: 1fr; }
      .control-actions { display: grid; }
      .control-actions .button { width: 100%; }
      .editor-demo-body { grid-template-columns: 1fr; }
      .editor-demo-sidebar { display: none; }
      .mini-site-links { display: none; }
    }
'''

section = r'''

    <!-- WEB-WIZARD-CUSTOMER-CONTROL -->
    <section class="customer-control" id="control">
      <div class="container customer-control-grid">
        <div class="customer-control-copy reveal">
          <p class="section-kicker">Your website, your control</p>
          <h2 class="section-title">We build it. You stay in control.</h2>
          <p class="section-lead">Your website should be easy to look after. We get everything set up and give you a simple editor for the everyday changes you want to make yourself.</p>

          <div class="control-points">
            <div class="control-point">
              <div class="control-point-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 010 18M12 3a15 15 0 000 18"/></svg></div>
              <strong>Already have a domain?</strong>
              <span>Keep it. We connect your new website to the web address your customers already know.</span>
            </div>
            <div class="control-point">
              <div class="control-point-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg></div>
              <strong>Need a domain?</strong>
              <span>No problem. We can arrange and set up a suitable web address as part of your website.</span>
            </div>
            <div class="control-point">
              <div class="control-point-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/></svg></div>
              <strong>Make your own changes</strong>
              <span>Edit text, images, services and pages through a straightforward website editor whenever you need to.</span>
            </div>
            <div class="control-point">
              <div class="control-point-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 7l-8 10-5-5"/><path d="M3 3h18v18H3z"/></svg></div>
              <strong>We handle the technical side</strong>
              <span>You concentrate on your business. We take care of getting the website online and keeping the technical setup straightforward.</span>
            </div>
          </div>

          <div class="control-actions">
            <a class="button button-primary" href="demo-editor.html" target="_blank" rel="noopener noreferrer">Try the demo editor
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M8 7h9v9"/></svg>
            </a>
            <a class="button button-secondary" href="#contact">Discuss your website</a>
          </div>
        </div>

        <div class="editor-demo-card reveal" aria-label="Example Web Wizard website editor">
          <div class="editor-demo-top">
            <div class="editor-demo-brand"><span class="editor-demo-mark">W</span><span>Your website editor</span></div>
            <span class="editor-demo-status">Website live</span>
          </div>
          <div class="editor-demo-body">
            <div class="editor-demo-sidebar">
              <small>Pages</small>
              <div class="editor-page-row active"><span class="editor-page-dot">⌂</span>Home</div>
              <div class="editor-page-row"><span class="editor-page-dot">A</span>About</div>
              <div class="editor-page-row"><span class="editor-page-dot">S</span>Services</div>
              <div class="editor-page-row"><span class="editor-page-dot">✉</span>Contact</div>
              <div class="editor-add-row">+ Add page</div>
            </div>
            <div class="editor-demo-preview">
              <div class="mini-browser">
                <div class="mini-browser-bar"><i></i><i></i><i></i><span class="mini-browser-address"></span></div>
                <div class="mini-site-nav"><span>Your Business</span><span class="mini-site-links"><span>About</span><span>Services</span><span>Contact</span></span></div>
                <div class="mini-site-hero"><div class="mini-kicker"></div><div class="mini-heading"></div><div class="mini-copy"></div><div class="mini-button"></div></div>
                <div class="mini-site-cards"><div class="mini-site-card"></div><div class="mini-site-card"></div><div class="mini-site-card"></div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

hero_old = '            <a class="button button-secondary" href="#work">View recent work</a>'
hero_new = '''            <a class="button button-secondary" href="#work">View recent work</a>\n            <a class="button button-secondary" href="demo-editor.html" target="_blank" rel="noopener noreferrer">Try the website editor</a>'''
if hero_old not in html:
    raise SystemExit("Could not find hero button insertion point")
html = html.replace(hero_old, hero_new, 1)

style_close = "\n  </style>"
if style_close not in html:
    raise SystemExit("Could not find style insertion point")
html = html.replace(style_close, css + style_close, 1)

process_marker = '    <section id="process">'
if process_marker not in html:
    raise SystemExit("Could not find process section insertion point")
html = html.replace(process_marker, section + "\n" + process_marker, 1)

path.write_text(html, encoding="utf-8")
