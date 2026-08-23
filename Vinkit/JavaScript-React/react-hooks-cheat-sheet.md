<!-- tags: vinkit, javascript-react -->

# React Hooks -cheat sheet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

React-hookien peruskonseptit, joita käytetään päivittäin.

## 1. useState

Lisää tilan (state) funktiokomponenttiin.

```jsx
const [state, setState] = useState(initialValue);
setState(newValue);
```

**Milloin käytetään:** kun komponentin täytyy tallentaa dataa.

## 2. useEffect

Suorittaa sivuvaikutuksia (side effects) funktiokomponenteissa.

```jsx
useEffect(() => {
  // side effect
  return () => {}; // cleanup
}, [dependencies]);
```

**Milloin käytetään:** datan haku (data fetching), tilaukset (subscriptions) tai DOM-päivitykset.

## 3. useContext

Pääsy contextiin ilman prop drillingiä.

```jsx
const value = useContext(MyContext);
```

**Milloin käytetään:** kun dataa tarvitaan monessa komponentissa eri tasoilla.

## 4. useRef

Pääsy DOM-elementteihin tai arvojen säilyttäminen ilman uudelleenrenderöintiä.

```jsx
const ref = useRef(initialValue);
ref.current
```

**Milloin käytetään:** DOM-pääsyyn tai muuttuvien arvojen säilyttämiseen ilman re-renderiä.

## 5. useMemo

Muistaa (memoize) raskaita laskutoimituksia.

```jsx
const memoized = useMemo(() => compute(), [dependencies]);
```

**Milloin käytetään:** kun laskutoimitus on raskas ja syötteet muuttuvat harvoin.

## 6. useCallback

Muistaa funktioita, jotta vältetään turhat uudelleenrenderöinnit.

```jsx
const memoizedFn = useCallback(() => {
  doSomething();
}, [dependencies]);
```

**Milloin käytetään:** kun funktioita välitetään lapsikomponenteille.

## 7. useReducer

Hallitsee monimutkaista tilalogiikkaa.

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
dispatch(action);
```

**Milloin käytetään:** kun tilalla on useita ala-arvoja tai monimutkaisia päivityksiä.

## 8. useLayoutEffect

Kuten useEffect, mutta laukeaa ennen selaimen piirtoa (paint).

```jsx
useLayoutEffect(() => {
  // measure or DOM mutations
}, [dependencies]);
```

**Milloin käytetään:** kun DOM täytyy mitata ennen kuin selain piirtää sen.

## 9. useImperativeHandle

Mukauttaa refin kautta paljastettavan instanssin arvon.

```jsx
useImperativeHandle(ref, () => ({
  method: () => {}
}), [dependencies]);
```

**Milloin käytetään:** kun paljastetaan mukautettuja metodeja vanhempikomponentille.

## 10. useId

Generoi uniikkeja ID:itä, jotka ovat SSR-turvallisia (SSR-safe).

```jsx
const id = useId();
<div id={id}></div>
```

**Milloin käytetään:** kun tarvitaan uniikkeja ID:itä saavutettavuuteen (labelit, inputit).

## Vinkki

Hallitse nämä hookit, niin olet valmis rakentamaan mitä tahansa Reactilla. Harjoittele pienillä projekteilla päivittäin: rakenna, julkaise, opi, toista (Build. Ship. Learn. Repeat.)
