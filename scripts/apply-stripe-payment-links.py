from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        ".price-card .button{margin-top:auto;width:100%;justify-content:center}\n",
        ".price-card .button{width:100%;justify-content:center}\n.payment-actions{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-top:auto}.payment-actions .button{font-size:.78rem;padding:11px 12px}.care-strip .button{white-space:nowrap}\n@media(max-width:520px){.payment-actions{grid-template-columns:1fr}}\n"
    ),
    (
        '<a class="button button-secondary" href="#contact">Choose One Page Launch</a>',
        '<div class="payment-actions"><a class="button button-secondary" href="https://buy.stripe.com/bJe6oJ8YH3vxfVV3Px77O06" target="_blank" rel="noopener noreferrer">Pay £132 in full</a><a class="button button-primary" href="https://buy.stripe.com/fZu28t4Ir5DFaBB0Dl77O05" target="_blank" rel="noopener noreferrer">Pay £11/month</a></div>'
    ),
    (
        '<a class="button button-primary" href="#contact">Choose Small Business</a>',
        '<div class="payment-actions"><a class="button button-secondary" href="https://buy.stripe.com/9B65kF6Qz8PR9xx3Px77O04" target="_blank" rel="noopener noreferrer">Pay £180 in full</a><a class="button button-primary" href="https://buy.stripe.com/28E14pej1d6725599R77O03" target="_blank" rel="noopener noreferrer">Pay £15/month</a></div>'
    ),
    (
        '<a class="button button-secondary" href="#contact">Choose Business Plus</a>',
        '<div class="payment-actions"><a class="button button-secondary" href="https://buy.stripe.com/14AeVf2AjaXZbFF5XF77O02" target="_blank" rel="noopener noreferrer">Pay £300 in full</a><a class="button button-primary" href="https://buy.stripe.com/14AeVf5Mv9TVeRR5XF77O01" target="_blank" rel="noopener noreferrer">Pay £25/month</a></div>'
    ),
    (
        '<div class="care-price"><strong>£6.99</strong><span>per month · optional</span></div>',
        '<div class="care-price"><strong>£6.99</strong><span>per month · optional</span><a class="button button-primary" href="https://buy.stripe.com/cNi6oJej15DFgZZ2Lt77O00" target="_blank" rel="noopener noreferrer" style="margin-top:12px">Add Website Care</a></div>'
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one occurrence, found {count}: {old[:100]!r}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Stripe payment links applied successfully.')
