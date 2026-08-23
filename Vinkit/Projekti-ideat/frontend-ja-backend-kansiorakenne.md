<!-- tags: vinkit, projekti-ideat -->

# Frontend- ja Backend-kehittäjän kansiorakenne

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Organisoitu, skaalautuva, ylläpidettävä ja ammattimainen projektirakenne frontend- ja backend-kehitykseen.

## Frontend-kehittäjä (React / Angular / Vue)

```
frontend-project/
├── public/
│   ├── images/
│   ├── icons/
│   └── favicon.ico
├── src/
│   ├── assets/
│   │   ├── images/
│   │   ├── fonts/
│   │   └── styles/
│   ├── components/
│   │   ├── Header/
│   │   ├── Footer/
│   │   ├── Button/
│   │   └── Card/
│   ├── context/
│   │   └── AuthContext.js
│   ├── pages/
│   │   ├── Home/
│   │   ├── About/
│   │   ├── Contact/
│   │   └── Dashboard/
│   ├── routes/
│   │   └── AppRoutes.js
│   ├── services/
│   │   ├── api.js
│   │   └── auth.js
│   ├── utils/
│   │   ├── helpers.js
│   │   └── constants.js
│   ├── hooks/
│   │   ├── useAuth.js
│   │   └── useFetch.js
│   ├── store/
│   │   └── redux/
│   ├── App.jsx
│   └── main.jsx
├── package.json
└── README.md
```

### Frontend-vastuualueet

- UI-kehitys
- Responsiivinen suunnittelu
- API-integraatio
- Tilanhallinta (State Management)
- Lomakkeiden validointi
- Reititys (Routing)
- Autentikoinnin käyttöliittymä

## Backend-kehittäjä (Node.js / Express)

```
backend-project/
├── src/
│   ├── config/
│   │   ├── db.js
│   │   └── env.js
│   ├── controllers/
│   │   ├── userController.js
│   │   └── authController.js
│   ├── models/
│   │   ├── User.js
│   │   └── Product.js
│   ├── routes/
│   │   ├── userRoutes.js
│   │   └── authRoutes.js
│   ├── middleware/
│   │   ├── authMiddleware.js
│   │   └── errorMiddleware.js
│   ├── services/
│   │   └── userService.js
│   ├── utils/
│   │   ├── jwt.js
│   │   └── logger.js
│   ├── validations/
│   │   └── userValidation.js
│   ├── database/
│   │   ├── migrations/
│   │   └── seeders/
│   └── app.js
├── uploads/
├── tests/
├── .env
├── package.json
└── server.js
```

### Backend-vastuualueet

- REST API -kehitys
- Tietokannan hallinta
- Autentikointi ja valtuutus (Authentication & Authorization)
- Liiketoimintalogiikka (Business Logic)
- Tietoturva
- Tiedostojen lataus (File Upload)
- Sähköpostipalvelut
- Maksuporttien integraatio (Payment Gateway)

## Full Stack -projektirakenne

```
fullstack-project/
├── client/     (Frontend)
├── server/     (Backend)
├── docs/
├── docker/
├── .gitignore
└── README.md
```

### Projektin hyödyt

- Parempi organisointi
- Helppo yhteistyö
- Skaalautuva arkkitehtuuri
- Siisti ja luettava koodi
- Helppo ylläpito

## Sovelluksen datavirta (Application Flow)

**Frontend (React / Angular)** → **REST API / GraphQL** → **Backend (Node.js / Java / Spring / .NET)** → **Database (MySQL / PostgreSQL / MongoDB)**

## Haastattelukysymys

**K: Miksi erotamme Controllerit, Servicet ja Modelit?**

**V:**
- **Controller** – käsittelee pyynnöt ja vastaukset.
- **Service** – sisältää liiketoimintalogiikan.
- **Model** – on vuorovaikutuksessa tietokannan kanssa.

Tämä erottelu tekee sovelluksesta skaalautuvamman, ylläpidettävämmän ja helpommin testattavan.

## Esimerkkiteknologiapino

**Frontend:** React, Angular, Vue

**Backend:** Node.js, Express, MongoDB
