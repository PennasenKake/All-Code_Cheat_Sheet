// Asynkroninen funktio ja odotus
function odota(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function aja() {
  console.log("Aloitetaan...");
  await odota(1000); // odotetaan 1 sekunti
  console.log("1 sekunti kulunut");
}

aja();
