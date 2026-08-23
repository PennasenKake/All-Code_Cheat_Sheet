<!-- tags: vinkit, javascript-react -->

# Reactin oleelliset kirjastot (Router, Axios, Zustand ym.)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tehokkaita kirjastoja parempien, nopeampien ja tehokkaampien React-sovellusten rakentamiseen.

## 1. React Router DOM – reititys React-sovelluksiin

```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
  </Routes>
</BrowserRouter>
```
**Käyttö:** sivureititys, sisäkkäiset reitit, reittien suojaus, navigointi. Virallinen ja aktiivisesti ylläpidetty.

## 2. Axios – Promise-pohjainen HTTP-client

```javascript
import axios from 'axios';

const res = await axios.get('/api/data');

axios.post('/api/user', {
  name: 'Parvez',
  role: 'Developer'
});
```
**Käyttö:** API-pyynnöt, interceptorit, virheenkäsittely, pyyntöjen peruutus. Toimii selaimessa ja Node.js:ssä.

## 3. React Query (TanStack Query) – datan haku ja tilanhallinta

```jsx
import { useQuery } from '@tanstack/react-query';

function Users() {
  const { data, isLoading } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(res => res.json())
  });
  if (isLoading) return <p>Loading...</p>;
  return <ul>{data.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```
**Käyttö:** datan haku, välimuistitus, taustapäivitykset, optimistinen UI. Tehokas välimuistitus ja synkronointi.

## 4. Zustand – pieni, nopea ja skaalautuva tilanhallinta

```jsx
import { create } from 'zustand';

const useStore = create((set) => ({
  count: 0,
  inc: () => set((state) => ({ count: state.count + 1 }))
}));

function Counter() {
  const { count, inc } = useStore();
  return <button onClick={inc}>{count}</button>;
}
```
**Käyttö:** globaali tila, minimaalinen boilerplate, korkea suorituskyky, middleware-tuki. Pieni koko, suuri suorituskyky.

## 5. React Hook Form – suorituskykyiset lomakkeet

```jsx
import { useForm } from 'react-hook-form';

function Form() {
  const { register, handleSubmit } = useForm();
  const onSubmit = data => console.log(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('name')} placeholder="Name" />
      <input type="submit" />
    </form>
  );
}
```
**Käyttö:** lomakkeiden validointi, minimaaliset uudelleenrenderöinnit, helppo integrointi, parempi UX. Rakennettu suorituskykyä ajatellen.

## 6. Framer Motion – animaatiokirjasto Reactille

```jsx
import { motion } from 'framer-motion';

function Box() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="box"
    >
      Animate Me
    </motion.div>
  );
}
```
**Käyttö:** sivusiirtymät, mikrointeraktiot, eleanimaatiot, layout-animaatio. Tuotantovalmiit animaatiot.

## 7. React Icons – suositut ikonit Reactiin

```jsx
import { FaReact, FaGithub, FaCode } from 'react-icons/fa';

function Icons() {
  return (
    <div className="icons">
      <FaReact color="#61DAFB" size={28} />
      <FaGithub color="#333" size={28} />
      <FaCode color="#4CAF50" size={28} />
    </div>
  );
}
```
**Käyttö:** kauniit ikonit, helppokäyttöisyys, muokattavuus. Yli 7000 ikonia.

## 8. React Toastify – kauniit toast-ilmoitukset

```jsx
import { toast, ToastContainer } from 'react-toastify';

function Notify() {
  const notify = () => toast.success('Saved!');
  return (
    <>
      <button onClick={notify}>Show Toast</button>
      <ToastContainer position="top-right" />
    </>
  );
}
```
**Käyttö:** onnistumisviestit, virheilmoitukset, infoilmoitukset, muokattavuus. Yksinkertainen, muokattava ja kevyt.

## Bonustyökalut

- **date-fns** – päivämäärätyökalut
- **lodash** – apufunktiot
- **clsx** – ehdolliset class-nimet
- **swr** – datan haku -hook
- **uuid** – uniikit ID:t

## Vinkit

- Valitse oikea työkalu tehtävään
- Älä käytä liikaa kirjastoja
- Pidä bundlen koko mielessä
- Lue dokumentaatio ja tutustu esimerkkeihin
