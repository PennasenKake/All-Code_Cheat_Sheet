<!-- tags: vinkit, backend-api -->

# Role-Based Access Control (RBAC) -vuokaavio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

RBAC on valtuutusmekanismi (authorization mechanism), jossa käyttäjille myönnetään oikeuksia heidän roolinsa perusteella.

## Ydinkäsite

**Users** (Ketä he ovat?) → **Roles** (Mikä rooli heillä on?) → **Permissions** (Mitä he voivat tehdä?)

Kulku: Users → Roles → Permissions → Access.

## 1. RBAC-vuon yleiskuva

1. **User Login** – käyttäjä kirjautuu sisään.
2. **Authentication** (JWT / Session) – tunnistautuminen.
3. **Fetch User Role** (Admin, Manager, User) – käyttäjän roolin haku.
4. **Check Permission** – oikeuksien tarkistus.
5. Lopputulos:
   - **Allowed** ✅ – pääsy resurssiin.
   - **Denied** ❌ – luvaton (unauthorized) sivu.

## 2. Esimerkkiroolit

### Admin
- Hallitse käyttäjiä (Manage Users)
- Luo / poista tuotteita (Create / Delete Products)
- Näytä raportit (View Reports)
- Hallitse rooleja (Manage Roles)

### Manager
- Näytä raportit (View Reports)
- Hallitse tilauksia (Manage Orders)
- Päivitä tuotteita (Update Products)

### User
- Näytä tuotteet (View Products)
- Tee tilauksia (Place Orders)
- Hallitse profiilia (Manage Profile)

## 3. Oikeusmatriisi (Permission Matrix)

| Ominaisuus | Admin | Manager | User |
|---|---|---|---|
| Dashboard | ✅ | ✅ | ✅ |
| Manage Users | ✅ | ❌ | ❌ |
| Manage Orders | ✅ | ✅ | ❌ |
| View Reports | ✅ | ✅ | ❌ |
| Place Orders | ✅ | ✅ | ✅ |
| Manage Roles | ✅ | ❌ | ❌ |

## 4. Frontend RBAC -vuo (React)

Kulku: Login → Receive JWT Token → Decode User Role → Store Role (Redux / Context API) → Protected Route → **Has Permission** (Render Page) tai **No Permission** (Redirect / 403 Page).

### Protected Route -esimerkki (React)

```jsx
const ProtectedRoute = ({
  children,
  allowedRoles
}) => {
  const { role } = useAuth();

  return allowedRoles.includes(role)
    ? children
    : <Navigate to="/403" replace />;
};
```

### Käyttöesimerkki

```jsx
<Route
  path="/admin"
  element={
    <ProtectedRoute allowedRoles={["Admin"]}>
      <AdminDashboard />
    </ProtectedRoute>
  }
/>
```

## 5. Backend RBAC -vuo (Node.js)

Kulku: Request → JWT Verification → Extract User Role → Authorization Middleware → **Allowed** (Controller) tai **Denied** (403 Forbidden).

### Authorization Middleware -esimerkki

```javascript
const authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        message: "Access Denied"
      });
    }
    next();
  };
};
```

### Käyttöesimerkki

```javascript
router.delete(
  "/users/:id",
  authenticate,
  authorize("Admin"),
  deleteUser
);
```

## 6. Koko full stack -vuo

User Login → Backend Authenticates User → JWT Generated → Token Sent to Frontend → Frontend Stores Token → User Opens Protected Page → API Request with JWT → Backend Verifies Role → **Success** (Data Returned) tai **Failure** (403 Forbidden).

## 7. Parhaat käytännöt

- Älä koskaan luota vain frontendin roolitarkistuksiin.
- Validoi roolit aina backendissä.
- Tallenna roolit JWT-payloadiin.
- Käytä middlewarea valtuutukseen (authorization).
- Noudata vähimpien oikeuksien periaatetta (Principle of Least Privilege).
- Piilota luvattomat käyttöliittymäelementit.

## Haastattelukysymys

**K: Mikä on RBAC?**

**V:** RBAC (Role-Based Access Control) on valtuutusmekanismi, jossa pääsy resursseihin myönnetään käyttäjän roolien perusteella. Sen sijaan, että oikeuksia annettaisiin suoraan käyttäjille, oikeudet liitetään rooleihin, ja käyttäjät perivät oikeudet heille määrättyjen roolien kautta.

## Keskeinen johtopäätös

- **Autentikointi** (Authentication) kertoo, kuka käyttäjä on.
- **Valtuutus** (Authorization) kertoo, mitä käyttäjä voi tehdä.
- RBAC varmistaa, että oikeilla ihmisillä on oikeat oikeudet.

## Yleisiä rooleja käytännössä

Admin, Manager, User, Guest.
