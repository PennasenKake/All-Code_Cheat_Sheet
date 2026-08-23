<!-- tags: vinkit, html-css -->

# HTML5:n semanttinen rakenne

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Nykyaikaisen verkkosivun layout-arkkitehtuuri semanttisilla HTML5-elementeillä.

## Sivun perusrakenne

```
<header>   - sivun/sivuston intro tai brändäys, sisältää usein <nav>:n
<nav>      - navigaatiolinkit (Home, About, Services, Blog, Contact)
<main>     - sivun pääsisältö
  <section>  - sisällön looginen ryhmä, esim. <h2> + <p>
  <aside>    - sivupalkki / liittyvä sisältö
<footer>   - alatunniste, sisältää mm. some-linkit
```

## Semanttiset tagit

- **`<header>`** – edustaa johdantosisältöä tai navigaatiolinkkien joukkoa.
- **`<nav>`** – määrittää navigaatiolinkkien osion.
- **`<main>`** – edustaa dokumentin pääsisältöä. Pitäisi olla uniikki sivulla.
- **`<section>`** – määrittää osion dokumentissa, ryhmittää liittyvää sisältöä.
- **`<aside>`** – sisältää pääsisältöön liittyvää sisältöä, usein sivupalkkeja varten.
- **`<footer>`** – edustaa dokumentin tai osion alatunnistetta, sisältää alatunnistetiedot.

## Esimerkki HTML-rakenteesta

```html
<!DOCTYPE html>
<html lang="en">
  <head>...</head>
  <body>
    <header>...</header>
    <nav>...</nav>
    <main>
      <section>...</section>
      <aside>...</aside>
    </main>
    <footer>...</footer>
  </body>
</html>
```

## Miksi käyttää semanttista HTML:ää?

- Parantaa saavutettavuutta
- Parempi hakukoneoptimointi (SEO)
- Puhtaampaa ja helpommin ylläpidettävää koodia
- Parempi kehittäjäkokemus
- Tulevaisuuden kestävää (future proof)
