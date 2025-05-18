# HTML-multimediatagit

## Ääni

* `<audio>`: Upottaa äänisisältöä.
    * Esimerkki:

        ```html
        <audio controls>
          <source src="audio.mp3" type="audio/mpeg">
          Selaimesi ei tue audio-elementtiä.
        </audio>
        ```

## Video

* `<video>`: Upottaa videosisältöä.
    * Esimerkki:

        ```html
        <video controls width="250">
          <source src="video.mp4" type="video/mp4">
          Selaimesi ei tue video-tagia.
        </video>
        ```

## Mediaresurssit

* `<source>`: Määrittää useita mediaresursseja `<audio>`- tai `<video>`-elementille.
    * Esimerkki:

        ```html
        <audio controls>
          <source src="audio.ogg" type="audio/ogg">
          <source src="audio.mp3" type="audio/mpeg">
          Selaimesi ei tue audio-elementtiä.
        </audio>
        ```

## Tekstitykset

* `<track>`: Määrittää tekstiraitoja `<video>`- ja `<audio>`-elementeille (esim. tekstitykset).
    * Esimerkki:

        ```html
        <video controls>
          <source src="video.mp4" type="video/mp4">
          <track src="tekstitys.vtt" kind="subtitles" srclang="fi" label="Suomi">
        </video>
        ```

## Upotukset

* `<embed>`: Upottaa ulkoista sisältöä, tyypillisesti multimediaa kuten Flash-tiedostoja.
    * Esimerkki:

        ```html
        <embed src="tiedosto.swf">
        ```

* `<object>`: Upottaa multimediatiedostoja, kuten kuvia, PDF-tiedostoja, Flash-sisältöä jne.
    * Esimerkki:

        ```html
        <object data="tiedosto.pdf" type="application/pdf" width="300" height="200">
          Selaimesi ei tue PDF-tiedostojen upottamista.
        </object>
        ```

* `<param>`: Määrittää parametreja `<object>`-elementin lisäosille (plugins).
    * Esimerkki (käytetään `<object>`-elementin sisällä):

        ```html
        <object data="peli.swf">
          <param name="quality" value="high">
        </object>
        ```

## Grafiikka

* `<canvas>`: Käytetään grafiikan piirtämiseen lennossa JavaScriptin avulla.
    * Esimerkki:

        ```html
        <canvas id="piirtoalusta" width="200" height="100"></canvas>
        <script>
          const canvas = document.getElementById('piirtoalusta');
          const ctx = canvas.getContext('2d');
          ctx.fillStyle = 'green';
          ctx.fillRect(10, 10, 50, 50);
        </script>
        ```

## Responsiiviset kuvat

* `<picture>`: Toimii säiliönä yhdelle tai useammalle `<source>`-elementille ja yhdelle `<img>`-elementille tarjotakseen eri versioita kuvasta eri näyttölaitteille.
    * Esimerkki:

        ```html
        <picture>
          <source srcset="kuva_pieni.webp" media="(max-width: 600px)" type="image/webp">
          <source srcset="kuva_suuri.webp" type="image/webp">
          <img src="kuva.jpg" alt="Kuvan kuvaus">
        </picture>
        ```

## Kuvat

* `<img>`: Upottaa kuvan.
    * Esimerkki:

        ```html
        <img src="kuva.jpg" alt="Kuvan kuvaus">
        ```