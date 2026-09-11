from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        ".monthly-option{display:flex;align-items:baseline;flex-wrap:wrap;gap:6px 8px;margin:-6px 0 21px;padding:11px 13px;border:1px solid rgba(109,74,255,.14);border-radius:12px;background:#faf9ff;color:var(--muted);font-size:.76rem;line-height:1.45}.monthly-option strong{color:var(--purple-dark);font-size:1rem}.monthly-option small{flex-basis:100%;font-size:.68rem;color:var(--muted)}\n",
        ".billing-choice{display:flex;align-items:center;justify-content:center;gap:14px;margin:28px 0 6px;color:var(--muted);font-size:.82rem;font-weight:800}.billing-toggle{display:inline-flex;padding:4px;border:1px solid rgba(109,74,255,.18);border-radius:999px;background:#fff;box-shadow:var(--shadow-soft)}.billing-toggle button{appearance:none;border:0;border-radius:999px;padding:9px 16px;background:transparent;color:var(--muted);font:inherit;font-size:.78rem;font-weight:900;cursor:pointer;transition:.2s ease}.billing-toggle button.active{background:var(--purple);color:#fff;box-shadow:0 8px 20px rgba(109,74,255,.22)}.billing-detail{margin:-6px 0 21px;padding:11px 13px;border:1px solid rgba(109,74,255,.14);border-radius:12px;background:#faf9ff;color:var(--muted);font-size:.76rem;line-height:1.45}\n"
    ),
    (
        ".payment-actions{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:auto}.payment-actions .button{font-size:.78rem;padding:11px 12px}.care-strip .button{white-space:nowrap}\n@media(max-width:520px){.payment-actions{grid-template-columns:1fr}}\n",
        ".billing-pay-link{margin-top:auto}.care-strip .button{white-space:nowrap}\n@media(max-width:520px){.billing-choice{flex-direction:column;gap:9px}}\n"
    ),
    (
        '          <p class="section-lead">You get a professionally built website rather than another DIY subscription to figure out yourself. Choose a simple starting point and only add complexity when your business actually needs it.</p>\n        </div>\n\n        <div class="pricing-grid">',
        '          <p class="section-lead">You get a professionally built website rather than another DIY subscription to figure out yourself. Choose a simple starting point and only add complexity when your business actually needs it.</p>\n        </div>\n\n        <div class="billing-choice">\n          <span>Choose how you want to pay</span>\n          <div class="billing-toggle" id="billingToggle" role="group" aria-label="Payment frequency">\n            <button type="button" class="active" data-billing="monthly" aria-pressed="true">Monthly</button>\n            <button type="button" data-billing="annual" aria-pressed="false">Annual</button>\n          </div>\n        </div>\n\n        <div class="pricing-grid">'
    ),
    (
        '<article class="price-card reveal">\n            <h3>One Page Launch</h3>',
        '<article class="price-card reveal" data-monthly-price="£11" data-annual-price="£132" data-monthly-url="https://buy.stripe.com/fZu28t4Ir5DFaBB0Dl77O05" data-annual-url="https://buy.stripe.com/bJe6oJ8YH3vxfVV3Px77O06">\n            <h3>One Page Launch</h3>'
    ),
    (
        '            <div class="price"><strong>£132</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£11/month</strong><small>12 monthly payments · total £132</small></div>',
        '            <div class="price"><strong>£11</strong><span>per month</span></div>\n            <div class="billing-detail">12 monthly payments · total £132</div>'
    ),
    (
        '            <div class="payment-actions"><a class="button button-secondary" href="https://buy.stripe.com/bJe6oJ8YH3vxfVV3Px77O06" target="_blank" rel="noopener noreferrer">Pay £132 in full</a><a class="button button-primary" href="https://buy.stripe.com/fZu28t4Ir5DFaBB0Dl77O05" target="_blank" rel="noopener noreferrer">Pay £11/month</a></div>',
        '            <a class="button button-primary billing-pay-link" href="https://buy.stripe.com/fZu28t4Ir5DFaBB0Dl77O05" target="_blank" rel="noopener noreferrer">Choose monthly — £11/month</a>'
    ),
    (
        '<article class="price-card featured reveal">\n            <span class="price-badge">Most popular</span>\n            <h3>Small Business</h3>',
        '<article class="price-card featured reveal" data-monthly-price="£15" data-annual-price="£180" data-monthly-url="https://buy.stripe.com/28E14pej1d6725599R77O03" data-annual-url="https://buy.stripe.com/9B65kF6Qz8PR9xx3Px77O04">\n            <span class="price-badge">Most popular</span>\n            <h3>Small Business</h3>'
    ),
    (
        '            <div class="price"><strong>£180</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£15/month</strong><small>12 monthly payments · total £180</small></div>',
        '            <div class="price"><strong>£15</strong><span>per month</span></div>\n            <div class="billing-detail">12 monthly payments · total £180</div>'
    ),
    (
        '            <div class="payment-actions"><a class="button button-secondary" href="https://buy.stripe.com/9B65kF6Qz8PR9xx3Px77O04" target="_blank" rel="noopener noreferrer">Pay £180 in full</a><a class="button button-primary" href="https://buy.stripe.com/28E14pej1d6725599R77O03" target="_blank" rel="noopener noreferrer">Pay £15/month</a></div>',
        '            <a class="button button-primary billing-pay-link" href="https://buy.stripe.com/28E14pej1d6725599R77O03" target="_blank" rel="noopener noreferrer">Choose monthly — £15/month</a>'
    ),
    (
        '<article class="price-card reveal">\n            <h3>Business Plus</h3>',
        '<article class="price-card reveal" data-monthly-price="£25" data-annual-price="£300" data-monthly-url="https://buy.stripe.com/14AeVf5Mv9TVeRR5XF77O01" data-annual-url="https://buy.stripe.com/14AeVf2AjaXZbFF5XF77O02">\n            <h3>Business Plus</h3>'
    ),
    (
        '            <div class="price"><strong>£300</strong><span>one-off</span></div>\n            <div class="monthly-option"><span>or</span><strong>£25/month</strong><small>12 monthly payments · total £300</small></div>',
        '            <div class="price"><strong>£25</strong><span>per month</span></div>\n            <div class="billing-detail">12 monthly payments · total £300</div>'
    ),
    (
        '            <div class="payment-actions"><a class="button button-secondary" href="https://buy.stripe.com/14AeVf2AjaXZbFF5XF77O02" target="_blank" rel="noopener noreferrer">Pay £300 in full</a><a class="button button-primary" href="https://buy.stripe.com/14AeVf5Mv9TVeRR5XF77O01" target="_blank" rel="noopener noreferrer">Pay £25/month</a></div>',
        '            <a class="button button-primary billing-pay-link" href="https://buy.stripe.com/14AeVf5Mv9TVeRR5XF77O01" target="_blank" rel="noopener noreferrer">Choose monthly — £25/month</a>'
    ),
    (
        '<p class="pricing-note">Choose to pay the website price once or split exactly the same total across 12 monthly payments. Existing domain connection is included where technically possible.',
        '<p class="pricing-note">Choose monthly or annual billing above. Website Care is optional and billed separately at £6.99 per month. Existing domain connection is included where technically possible.'
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one occurrence, found {count}: {old[:120]!r}')
    text = text.replace(old, new, 1)

script = '''\n  <script>\n    (() => {\n      const toggle = document.getElementById('billingToggle');\n      if (!toggle) return;\n      const buttons = [...toggle.querySelectorAll('[data-billing]')];\n      const cards = [...document.querySelectorAll('.price-card[data-monthly-price][data-annual-price]')];\n\n      function setBilling(mode) {\n        buttons.forEach((button) => {\n          const active = button.dataset.billing === mode;\n          button.classList.toggle('active', active);\n          button.setAttribute('aria-pressed', String(active));\n        });\n\n        cards.forEach((card) => {\n          const monthly = card.dataset.monthlyPrice;\n          const annual = card.dataset.annualPrice;\n          const price = card.querySelector('.price strong');\n          const period = card.querySelector('.price span');\n          const detail = card.querySelector('.billing-detail');\n          const link = card.querySelector('.billing-pay-link');\n\n          if (mode === 'annual') {\n            price.textContent = annual;\n            period.textContent = 'per year';\n            detail.textContent = `Annual payment · ${annual} per year`;\n            link.href = card.dataset.annualUrl;\n            link.textContent = `Choose annual — ${annual}/year`;\n          } else {\n            price.textContent = monthly;\n            period.textContent = 'per month';\n            detail.textContent = `12 monthly payments · total ${annual}`;\n            link.href = card.dataset.monthlyUrl;\n            link.textContent = `Choose monthly — ${monthly}/month`;\n          }\n        });\n      }\n\n      buttons.forEach((button) => button.addEventListener('click', () => setBilling(button.dataset.billing)));\n      setBilling('monthly');\n    })();\n  </script>\n'''

if text.count('</body>') != 1:
    raise SystemExit('Expected one closing body tag')
text = text.replace('</body>', script + '</body>', 1)

path.write_text(text, encoding='utf-8')
print('Billing toggle update applied successfully.')
