// Haetaan HTML-elementit ID:n perusteella
const timerEl = document.getElementById('timer');
const startElBtn = document.getElementById('start');
const stopElBtn = document.getElementById('stop');
const resetElBtn = document.getElementById('reset');

// Muuttujat ajastimen tilaa varten
let startTime = 0; // Aloitusaika millisekunteina
let elapsedTime = 0; // Kulunut aika millisekunteina
let timerInterval; // Muuttuja setInterval-funktion ID:lle

// Varmistetaan, että elementit löytyvät ennen tapahtumakuuntelijoiden lisäämistä
if (timerEl && startElBtn && stopElBtn && resetElBtn) {
    // Lisätään tapahtumankuuntelijat painikkeille
    startElBtn.addEventListener('click', startTimer);
    stopElBtn.addEventListener('click', stopTimer);
    resetElBtn.addEventListener('click', resetTimer);
} else {
    console.error('Yksi tai useampi DOM-elementti ei löydy!');
}

// Funktio ajastimen käynnistämiseen
function startTimer() {
    startTime = Date.now() - elapsedTime; // Lasketaan aloitusaika
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime; // Lasketaan kulunut aika
        timerEl.textContent = formatTime(elapsedTime); // Päivitetään ajastimen näyttö
    }, 100); // Päivitetään 100 ms välein (riittävä sadasosasekunteihin)

    // Poistetaan aloituspainike käytöstä ja otetaan pysäytyspainike käyttöön
    startElBtn.disabled = true;
    stopElBtn.disabled = false;
}

// Funktio ajastimen pysäyttämiseen
function stopTimer() {
    clearInterval(timerInterval); // Pysäytetään ajastimen päivitys
    // Otetaan aloituspainike käyttöön ja poistetaan pysäytyspainike käytöstä
    startElBtn.disabled = false;
    stopElBtn.disabled = true;
}

// Funktio ajastimen nollaamiseen
function resetTimer() {
    elapsedTime = 0; // Nollataan kulunut aika
    timerEl.textContent = '00:00:00.00'; // Asetetaan näyttö oletusarvoon
    clearInterval(timerInterval); // Pysäytetään ajastin
    // Otetaan aloituspainike käyttöön ja poistetaan pysäytyspainike käytöstä
    startElBtn.disabled = false;
    stopElBtn.disabled = true;
}

// Funktio ajan muotoiluun HH:MM:SS.ms -muotoon
function formatTime(elapsedTime) {
    const milliseconds = Math.floor((elapsedTime % 1000) / 10); // Lasketaan sadasosasekunnit
    const seconds = Math.floor((elapsedTime / 1000) % 60); // Lasketaan sekunnit
    const minutes = Math.floor((elapsedTime / (1000 * 60)) % 60); // Lasketaan minuutit
    const hours = Math.floor(elapsedTime / (1000 * 60 * 60)); // Lasketaan tunnit

    // Muotoillaan aika merkkijonoksi, varmistetaan aina kaksinumeroiset arvot
    return (
        (hours < 10 ? '0' + hours : hours) + ':' +
        (minutes < 10 ? '0' + minutes : minutes) + ':' +
        (seconds < 10 ? '0' + seconds : seconds) + '.' +
        (milliseconds < 10 ? '0' + milliseconds : milliseconds)
    );
}

// Alustetaan pysäytyspainike disabled-tilaan sivun latautuessa
(function() {
    if (stopElBtn) {
        stopElBtn.disabled = true;
    }
})();