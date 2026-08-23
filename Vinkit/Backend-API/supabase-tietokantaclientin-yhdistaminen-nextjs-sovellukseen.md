<!-- tags: vinkit, backend-api -->

# Supabase-tietokantaclientin yhdistäminen Next.js-sovellukseen

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Ohje Supabase-clientin asennukseen ja käyttöönottoon Next.js-sovelluksessa.

## 1. Asenna paketti

```bash
npm install @supabase/supabase-js
```

## 2. Luo Supabase-client-tiedosto

```
lib/
└── supabase.js
```

## 3. Alusta client

```javascript
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseKey)
```

## 4. Lisää ympäristömuuttujat

```
NEXT_PUBLIC_SUPABASE_URL=your_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_key
```

## 5. Esimerkki datan hakemisesta

```javascript
const { data, error } = await supabase
  .from('users')
  .select('*')
```

## Datavirta (Data Flow)

Next.js App **käyttää** (Uses) → Supabase Client **yhdistää** (Connects) → Supabase Database (PostgreSQL).

## Teknologiapino (Tech Stack)

- **Next.js** – React-kehys tuotantokäyttöön.
- **Supabase** – avoimen lähdekoodin backend.
- **PostgreSQL** – tehokas relaatiotietokanta.
- **JavaScript** – moderni ohjelmointikieli.

## Vinkki

Supabase tarjoaa tehokkaan backendin, jossa on tuki reaaliaikaiselle (realtime) tietokannalle. Ominaisuudet: Secure, Scalable, Realtime – rakennettu moderneja sovelluksia varten.
