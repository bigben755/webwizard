from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def update_demo() -> None:
    path = Path("demo-editor.html")
    text = path.read_text(encoding="utf-8")

    text = replace_once(
        text,
        ".asset-preview{margin-top:9px;display:flex;align-items:center;gap:10px;padding:10px;border:1px solid var(--line);border-radius:11px;background:#fbfbfe}.asset-thumb{width:48px;height:48px;border-radius:10px;border:1px solid var(--line);display:grid;place-items:center;background:#fff;overflow:hidden;color:#9b9baa;font-size:.62rem;font-weight:800}.asset-thumb.favicon{width:34px;height:34px;border-radius:8px}.asset-thumb img{width:100%;height:100%;object-fit:contain}.asset-copy strong{display:block;font-size:.72rem}.asset-copy span{font-size:.64rem;color:var(--muted)}",
        ".asset-preview{margin-top:9px;display:flex;align-items:center;gap:10px;padding:10px;border:1px solid var(--line);border-radius:11px;background:#fbfbfe}.asset-thumb{width:48px;height:48px;border-radius:10px;border:1px solid var(--line);display:grid;place-items:center;background:#fff;overflow:hidden;color:#9b9baa;font-size:.62rem;font-weight:800;flex:0 0 auto}.asset-thumb.favicon{width:34px;height:34px;border-radius:8px}.asset-thumb img{width:100%;height:100%;object-fit:contain}.asset-copy{min-width:0;flex:1}.asset-copy strong{display:block;font-size:.72rem}.asset-copy span{font-size:.64rem;color:var(--muted)}.asset-remove{margin-left:auto;border:1px solid #efcaca;border-radius:9px;background:#fff6f6;color:#9b2f2f;padding:7px 9px;font-size:.66rem;font-weight:900;white-space:nowrap}.asset-remove:hover{background:#ffeded}.asset-remove[hidden]{display:none}",
        "asset remove styles",
    )

    text = replace_once(
        text,
        "transition:max-width .25s ease}.browser.mobile{max-width:420px}",
        "transition:max-width .25s ease}.browser.tablet{max-width:820px}.browser.mobile{max-width:420px}",
        "tablet preview width",
    )

    mobile_rules = """/* Device preview rules: these are tied to the simulated viewport, not the outer browser width. */
.browser.mobile .site-nav{padding:10px 16px;align-items:flex-start}.browser.mobile .site-brand{font-size:.94rem}.browser.mobile .site-brand-logo{width:38px;height:38px}.browser.mobile .site-links{display:none}.browser.mobile .demo-hero{grid-template-columns:1fr;min-height:0}.browser.mobile .hero-copy{padding:38px 22px}.browser.mobile .hero-copy h2,.browser.mobile .inner-hero h2{font-size:2.35rem}.browser.mobile .hero-copy p{font-size:.9rem}.browser.mobile .hero-image{min-height:265px}.browser.mobile .inner-hero{padding:48px 22px}.browser.mobile .site-section{padding:40px 22px}.browser.mobile .services-grid,.browser.mobile .content-grid,.browser.mobile .gallery-grid{grid-template-columns:1fr}.browser.mobile .contact-strip{grid-template-columns:1fr;padding:30px 22px}.browser.mobile .contact-details{text-align:left}.browser.mobile .site-footer{padding:20px 22px;flex-direction:column}.browser.mobile .faq-item{padding:16px}.browser.tablet .hero-copy h2,.browser.tablet .inner-hero h2{font-size:clamp(2.25rem,6vw,3.8rem)}
"""
    text = replace_once(text, "@media(max-width:920px){", mobile_rules + "@media(max-width:920px){", "device preview responsive rules")

    text = replace_once(
        text,
        '<div class="preview-toolbar"><span class="preview-label">Live preview <span id="previewPageName"></span></span><div class="device-switch"><button class="active" data-device="desktop">Desktop</button><button data-device="mobile">Mobile</button></div></div>',
        '<div class="preview-toolbar"><span class="preview-label">Live preview <span id="previewPageName"></span></span><div class="device-switch"><button class="active" data-device="desktop">Desktop</button><button data-device="tablet">Tablet</button><button data-device="mobile">Mobile</button></div></div>',
        "device switch toolbar",
    )

    text = replace_once(
        text,
        '<div class="asset-preview"><div class="asset-thumb" id="logoThumb">Logo</div><div class="asset-copy"><strong>Header logo</strong><span>PNG, JPG, WebP or SVG recommended.</span></div></div>',
        '<div class="asset-preview"><div class="asset-thumb" id="logoThumb">Logo</div><div class="asset-copy"><strong>Header logo</strong><span>PNG, JPG, WebP or SVG recommended.</span></div><button class="asset-remove" id="logoRemove" type="button" hidden>Remove</button></div>',
        "logo remove control",
    )

    text = replace_once(
        text,
        '<div class="asset-preview"><div class="asset-thumb favicon" id="faviconThumb">Icon</div><div class="asset-copy"><strong>Browser icon</strong><span>Square image recommended. This appears beside the website address.</span></div></div>',
        '<div class="asset-preview"><div class="asset-thumb favicon" id="faviconThumb">Icon</div><div class="asset-copy"><strong>Browser icon</strong><span>Square image recommended. This appears beside the website address.</span></div><button class="asset-remove" id="faviconRemove" type="button" hidden>Remove</button></div>',
        "favicon remove control",
    )

    text = replace_once(
        text,
        '<div class="upload"><label>Hero image</label><div class="upload-box">Choose an image<input id="heroUpload" type="file" accept="image/*"></div></div>',
        '<div class="upload"><label>Hero image</label><div class="upload-box">Choose or replace image<input id="heroUpload" type="file" accept="image/*"></div><div class="asset-preview"><div class="asset-thumb" id="heroThumb">Image</div><div class="asset-copy"><strong>Homepage hero image</strong><span>Use a wide, high-quality image for best results.</span></div><button class="asset-remove" id="heroRemove" type="button" ${state.heroImage?\'\':\'hidden\'}>Remove</button></div></div>',
        "hero remove control",
    )

    text = replace_once(
        text,
        " heroUpload?.addEventListener('change',e=>handleAsset(e,'heroImage'));\n deletePage?.addEventListener('click',deleteActivePage);duplicatePage?.addEventListener('click',duplicateActivePage);",
        " heroUpload?.addEventListener('change',e=>handleAsset(e,'heroImage'));\n heroRemove?.addEventListener('click',()=>removeAsset('heroImage'));\n deletePage?.addEventListener('click',deleteActivePage);duplicatePage?.addEventListener('click',duplicateActivePage);",
        "hero remove handler",
    )

    text = replace_once(
        text,
        " logoThumb.innerHTML=state.logo?`<img src=\"${state.logo}\" alt=\"\">`:'Logo';\n faviconThumb.innerHTML=state.favicon?`<img src=\"${state.favicon}\" alt=\"\">`:'Icon';\n browserFavicon.src=state.favicon||'webwizard.png';demoFavicon.href=state.favicon||'webwizard.png';",
        " logoThumb.innerHTML=state.logo?`<img src=\"${state.logo}\" alt=\"\">`:'Logo';\n faviconThumb.innerHTML=state.favicon?`<img src=\"${state.favicon}\" alt=\"\">`:'Icon';\n const heroThumb=document.getElementById('heroThumb');if(heroThumb)heroThumb.innerHTML=state.heroImage?`<img src=\"${state.heroImage}\" alt=\"\">`:'Image';\n const logoRemove=document.getElementById('logoRemove'),faviconRemove=document.getElementById('faviconRemove'),heroRemove=document.getElementById('heroRemove');if(logoRemove)logoRemove.hidden=!state.logo;if(faviconRemove)faviconRemove.hidden=!state.favicon;if(heroRemove)heroRemove.hidden=!state.heroImage;\n browserFavicon.src=state.favicon||'webwizard.png';demoFavicon.href=state.favicon||'webwizard.png';",
        "asset state rendering",
    )

    text = replace_once(
        text,
        "function handleAsset(e,key){const f=e.target.files&&e.target.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{state[key]=r.result;setDirty();renderPreview();showNotice(key==='logo'?'Logo updated':key==='favicon'?'Favicon updated':'Image updated','This demo asset stays in your browser session.')};r.readAsDataURL(f)}",
        "function removeAsset(key){state[key]=null;setDirty();renderAssetThumbs();renderPreview();showNotice(key==='logo'?'Logo removed':key==='favicon'?'Favicon removed':'Image removed','The demo has returned to the default placeholder.')}\nfunction handleAsset(e,key){const f=e.target.files&&e.target.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{state[key]=r.result;setDirty();renderPreview();showNotice(key==='logo'?'Logo updated':key==='favicon'?'Favicon updated':'Image updated','This demo asset stays in your browser session.')};r.readAsDataURL(f)}",
        "remove asset function",
    )

    text = replace_once(
        text,
        "logoUpload.addEventListener('change',e=>handleAsset(e,'logo'));faviconUpload.addEventListener('change',e=>handleAsset(e,'favicon'));",
        "logoUpload.addEventListener('change',e=>handleAsset(e,'logo'));faviconUpload.addEventListener('change',e=>handleAsset(e,'favicon'));document.getElementById('logoRemove').addEventListener('click',()=>removeAsset('logo'));document.getElementById('faviconRemove').addEventListener('click',()=>removeAsset('favicon'));",
        "logo favicon remove handlers",
    )

    text = replace_once(
        text,
        "document.querySelectorAll('[data-device]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-device]').forEach(x=>x.classList.remove('active'));b.classList.add('active');browser.classList.toggle('mobile',b.dataset.device==='mobile')});",
        "document.querySelectorAll('[data-device]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-device]').forEach(x=>x.classList.remove('active'));b.classList.add('active');browser.classList.remove('mobile','tablet');if(b.dataset.device==='mobile')browser.classList.add('mobile');if(b.dataset.device==='tablet')browser.classList.add('tablet')});",
        "device switch behaviour",
    )

    path.write_text(text, encoding="utf-8")


def update_index() -> None:
    path = Path("index.html")
    text = path.read_text(encoding="utf-8")

    text = replace_once(
        text,
        '<meta name="description" content="The Web Wizard creates clear, modern websites and digital platforms for businesses, organisations and community projects.">',
        '<meta name="description" content="The Web Wizard designs and launches professional websites for businesses and organisations, with simple editing, domain setup and ongoing support when you need it.">',
        "meta description",
    )
    text = replace_once(text, '<title>The Web Wizard | Websites Made Simple</title>', '<title>The Web Wizard | Professional Websites, Made Simple</title>', "page title")
    text = replace_once(
        text,
        '<h1><span class="gradient-text">Smart websites.</span><br>Made simple.</h1>\n          <p class="hero-copy">The Web Wizard turns good ideas into clear, modern websites that are easy to use, easy to manage and built around what your visitors need to do next.</p>',
        '<h1><span class="gradient-text">Professionally built.</span><br>Easy for you to update.</h1>\n          <p class="hero-copy">We design, build and launch your website for you — then give you a straightforward way to keep everyday content up to date. Your website, your domain and your content stay under your control.</p>',
        "hero proposition",
    )
    text = replace_once(
        text,
        '<p class="section-kicker">Your website, your control</p>\n          <h2 class="section-title">We build it. You stay in control.</h2>\n          <p class="section-lead">Your website should be easy to look after. We get everything set up and give you a simple editor for the everyday changes you want to make yourself.</p>',
        '<p class="section-kicker">Professionally built. Easy to manage.</p>\n          <h2 class="section-title">A proper business website — without being locked out of it.</h2>\n          <p class="section-lead">We handle the design, build and launch. Once your website is live, you get a straightforward editor for routine changes, while we remain available for the technical work, larger updates and ongoing support.</p>',
        "customer control proposition",
    )
    text = replace_once(
        text,
        '<strong>Need a domain?</strong>\n              <span>No problem. We can arrange and set up a suitable web address as part of your website.</span>',
        '<strong>Need a web address?</strong>\n              <span>Choose your own domain, or start with an included Web Wizard address such as yourbusiness.thewebdesignwizard.co.uk. We handle the setup either way.</span>',
        "domain options",
    )
    text = replace_once(
        text,
        '<div class="step-number">04</div>\n            <div><h3>Review and launch</h3><p>You review the finished site, final changes are completed and the project is prepared for a confident public launch.</p></div>',
        '<div class="step-number">04</div>\n            <div><h3>Review, launch and handover</h3><p>You review the finished site, final changes are completed, the domain is connected and you receive clear access to your website editor and the information you need after launch.</p></div>',
        "launch handover",
    )
    mobile_faq = '''          <details>\n            <summary>Will it work properly on mobile phones?</summary>\n            <p>Yes. Responsive behaviour is built in from the start so the content and navigation remain clear across common screen sizes.</p>\n          </details>'''
    faq_additions = mobile_faq + '''\n          <details>\n            <summary>Do I need to buy a domain before we start?</summary>\n            <p>No. If you already have a domain, we can connect it. If you need one, we can help arrange it. You can also start with an included Web Wizard address such as yourbusiness.thewebdesignwizard.co.uk and move to your own domain later.</p>\n          </details>\n          <details>\n            <summary>Who owns my domain, content and branding?</summary>\n            <p>You do. The service is designed so your business is not dependent on us for ownership of its identity or content. We can manage the technical setup for you while keeping the arrangement clear.</p>\n          </details>\n          <details>\n            <summary>Can you look after the website after launch?</summary>\n            <p>Yes. Ongoing website care can cover technical support, routine checks, larger content changes and help when you would rather hand an update back to us.</p>\n          </details>'''
    text = replace_once(text, mobile_faq, faq_additions, "professional FAQ additions")
    text = replace_once(
        text,
        '<div class="contact-point"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg><span>Clear, practical project discussion</span></div>',
        '<div class="contact-point"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg><span>Domain, launch and technical setup handled</span></div>',
        "contact assurance",
    )
    text = replace_once(
        text,
        '                  <option>Existing website improvement</option>\n                  <option>Not sure yet</option>',
        '                  <option>Existing website improvement</option>\n                  <option>Website care &amp; support</option>\n                  <option>Not sure yet</option>',
        "website care option",
    )

    path.write_text(text, encoding="utf-8")


update_demo()
update_index()
print("Web Wizard demo and professional positioning updates applied successfully.")
