<!-- tags: vinkit, javascript-react -->

# Valuuttamuunnin HTML/CSS/JS-projektina

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Pieni projektiesimerkki: valuuttamuunnin, joka hakee reaaliaikaiset kurssit API:sta. Ominaisuuksia: reaaliaikaiset kurssit, 100+ valuuttaa, valuuttojen vaihto (swap), responsiivinen design.

## HTML

```html
<div class="converter">
  <h2>Currency Converter</h2>
  <div class="amount-group">
    <input type="number" id="amount" value="1" min="0">
  </div>
  <div class="select-group">
    <div class="from-group">
      <label>From</label>
      <select id="from"></select>
    </div>
    <div class="swap">&#8646;</div>
    <div class="to-group">
      <label>To</label>
      <select id="to"></select>
    </div>
  </div>
  <button id="convert">Convert</button>
  <div class="result">
    <h3 id="result">0.00</h3>
  </div>
  <div class="note">Rates are updated in real-time</div>
</div>
```

## CSS

```css
body { font-family: 'Poppins', sans-serif; background: #f5f7ff; }
.converter { background: #fff; max-width: 420px; margin: 40px auto; padding: 25px; border-radius: 16px; box-shadow: 0 8px 25px rgba(0,0,0,.1); }
h2 { text-align: center; margin-bottom: 20px; color: #2a2a72; }
.amount-group input { width: 100%; padding: 12px; font-size: 18px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 20px; }
.select-group { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }
select { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 10px; font-size: 16px; background: #fafafa; }
.swap { background: #eef2ff; color: #4f46e5; font-size: 20px; cursor: pointer; transition: .3s; border-radius: 10px; padding: 10px 14px; }
.swap:hover { background: #4f46e5; color: #fff; }
button { width: 100%; background: linear-gradient(135deg, #6366f1, #8b5cf6); color: #fff; padding: 14px; font-size: 18px; border-radius: 10px; border: none; cursor: pointer; font-weight: 600; transition: .3s; }
button:hover { transform: translateY(-2px); }
.result { margin-top: 20px; text-align: center; padding: 20px; background: #f0f9ff; border-radius: 10px; }
.result h3 { margin: 0; font-size: 28px; color: #0f172a; border: 1px solid #d0e0ff; }
.note { text-align: center; margin-top: 12px; font-size: 14px; color: #64748b; }
```

## JavaScript

```javascript
const apiKey = "YOUR_API_KEY"; // Get free key from exchangerate.host
const amountInput = document.getElementById("amount");
const fromSelect = document.getElementById("from");
const toSelect = document.getElementById("to");
const resultEl = document.getElementById("result");
const convertBtn = document.getElementById("convert");

// Load currencies
fetch("https://api.exchangerate.host/symbols?access_key=" + apiKey)
  .then(res => res.json())
  .then(data => {
    for (let code in data.symbols) {
      let option1 = new Option(code, code);
      let option2 = new Option(code, code);
      fromSelect.add(option1);
      toSelect.add(option2);
    }
    fromSelect.value = "USD";
    toSelect.value = "INR";
    convert();
  });

// Convert function
function convert() {
  let amount = amountInput.value;
  let from = fromSelect.value;
  let to = toSelect.value;
  fetch(`https://api.exchangerate.host/convert?access_key=${apiKey}&from=${from}&to=${to}&amount=${amount}`)
    .then(res => res.json())
    .then(data => {
      resultEl.innerText = `${amount} ${from} = ${data.result.toFixed(2)} ${to}`;
    });
}

convertBtn.addEventListener("click", convert);
document.querySelector(".swap").addEventListener("click", () => {
  [fromSelect.value, toSelect.value] = [toSelect.value, fromSelect.value];
  convert();
});
```

## Huomioita

- Kurssidata haetaan `exchangerate.host`-API:sta (vaatii ilmaisen API-avaimen).
- Swap-painike vaihtaa "From"- ja "To"-valuutan keskenään ja päivittää tuloksen.
- Esimerkkitulos: 100 USD = 8 316,28 INR (1 USD = 83,16 INR).
