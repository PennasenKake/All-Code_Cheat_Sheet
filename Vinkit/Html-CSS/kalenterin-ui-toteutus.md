<!-- tags: vinkit, html-css -->

# Kalenterin UI-toteutus HTML/CSS/JS:llä

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yksinkertainen, siisti ja responsiivinen kalenteri-käyttöliittymä toteutettuna puhtaalla HTML:llä, CSS:llä ja JavaScriptillä.

## HTML

```html
<div class="calendar">
  <div class="calendar-header">
    <button class="prev">&#10094;</button>
    <h2 class="month-year">May 2025</h2>
    <button class="next">&#10095;</button>
  </div>
  <div class="weekdays">
    <span>Sun</span><span>Mon</span><span>Tue</span>
    <span>Wed</span><span>Thu</span><span>Fri</span>
    <span>Sat</span>
  </div>
  <div class="days"></div>
</div>
```

## CSS

```css
.calendar {
  width: 350px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,.1);
  font-family: 'Poppins', sans-serif;
  overflow: hidden;
}
```

## JavaScript

```javascript
const daysEl = document.querySelector('.days');
const monthYearEl = document.querySelector('.month-year');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

let date = new Date();

function renderCalendar() {
  const year = date.getFullYear();
  const month = date.getMonth();
  const firstDay = new Date(year, month, 1).getDay();
  const lastDate = new Date(year, month + 1, 0).getDate();
  const months = ["January","February","March","April","May",
    "June","July","August","September","October","November","December"];

  monthYearEl.textContent = `${months[month]} ${year}`;
  daysEl.innerHTML = '';

  // empty cells before the 1st of the month
  for (let i = 0; i < firstDay; i++) {
    daysEl.innerHTML += '<div class="empty"></div>';
  }

  // days of the month
  for (let i = 1; i <= lastDate; i++) {
    const today = new Date();
    const isToday = i === today.getDate() &&
      month === today.getMonth() && year === today.getFullYear();
    daysEl.innerHTML += `<div class="day ${isToday ? 'today' : ''}">${i}</div>`;
  }
}

prevBtn.addEventListener('click', () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});
nextBtn.addEventListener('click', () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();
```

## Miten se toimii

- `renderCalendar()` laskee kuukauden ensimmäisen päivän viikonpäivän (`firstDay`) ja kuukauden viimeisen päivän (`lastDate`), ja täyttää `.days`-elementin vastaavalla määrällä tyhjiä soluja ja päiväsoluja.
- Nykyinen päivä (`isToday`) merkitään omalla `today`-luokalla, jolloin se voidaan korostaa CSS:llä (esimerkkikuvassa sininen ympyrä).
- `prev`- ja `next`-painikkeet vaihtavat kuukautta `date.setMonth()`-metodilla ja piirtävät kalenterin uudelleen.
- Sunnuntait ja lauantait korostetaan yleensä eri värillä (esim. punainen/sininen) selkeyden vuoksi.

## Ominaisuudet

- Moderni ja siisti ulkoasu
- Responsiivinen design
- Kuukausien välillä navigointi
- Nykyisen päivän korostus
