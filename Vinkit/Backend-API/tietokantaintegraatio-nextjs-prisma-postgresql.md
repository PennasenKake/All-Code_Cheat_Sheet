<!-- tags: vinkit, backend-api -->

# Tietokantaintegraatio Next.js:ssä (Prisma, PostgreSQL)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Miten se toimii

```
Client (Browser / Mobile)
  → Next.js App (Pages / App Router)
    → API Layer (Route Handlers / Server Actions)
      → Database Client (ORM / Query Builder / Driver)
        → Database (oma data)
```

## Suosittuja tietokantoja

PostgreSQL, MySQL, MongoDB, PlanetScale, SQLite, Supabase, Neon

## Suosittuja ORM- ja query-työkaluja

Prisma, Drizzle ORM, TypeORM, Mongoose, NextAuth.js (Auth + DB)

## Miksi tehdä tietokantakutsut palvelinpuolella?

- Tunnistetiedot ja kyselyt pysyvät turvassa
- Parempi suorituskyky
- Pääsy backend-resursseihin
- SEO- ja välimuistihyödyt

## Esimerkki: Next.js + Prisma + PostgreSQL

**1. Asenna riippuvuudet**
```bash
npm install prisma @prisma/client
npm install -D prisma
```

**2. prisma/schema.prisma**
```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
generator client {
  provider = "prisma-client-js"
}
model User {
  id        Int      @id @default(autoincrement())
  name      String
  email     String   @unique
  createdAt DateTime @default(now())
}
```

**3. lib/prisma.ts**
```typescript
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as
  unknown as { prisma: PrismaClient }

export const prisma = globalForPrisma.prisma ||
  new PrismaClient()

if (process.env.NODE_ENV !== 'production')
  globalForPrisma.prisma = prisma
```

**4. app/api/users/route.ts**
```typescript
import { NextResponse } from 'next/server'
import { prisma } from '@/lib/prisma'

export async function GET() {
  const users = await prisma.user.findMany()
  return NextResponse.json(users)
}

export async function POST(req: Request) {
  const body = await req.json()
  const user = await prisma.user.create({
    data: body,
  })
  return NextResponse.json(user, { status: 201 })
}
```

Näin API on käytettävissä osoitteessa `/api/users`, ja sillä voi tehdä täydet CRUD-operaatiot tietokantaan.

## Hyvät käytännöt

- Käytä ympäristömuuttujia tietokannan URL:eille
- Käytä connection poolingia (esim. PgBouncer, Prisma Data Proxy)
- Käsittele virheet ja reunatapaukset kunnolla
- Käytä indeksejä ja optimoi kyselyt
- Pidä arkaluontoinen logiikka palvelimella
- Käytä Server Actions -toiminnallisuutta (Next.js 14+) mutaatioihin

## Vinkki

Serverless-käyttöönotoissa kannattaa harkita Neonia, PlanetScalea tai Supabasea paremman skaalautuvuuden ja yhteydenhallinnan vuoksi.

## Käyttötapauksia

- Käyttäjäautentikaatio ja -profiilit
- Blogi / CMS / verkkokauppa
- Analytiikka ja raportointi
- SaaS-sovellukset
- Reaaliaikaiset sovellukset tilauksilla (subscriptions)
