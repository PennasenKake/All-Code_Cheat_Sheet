<!-- tags: vinkit, backend-api -->

# Spring Boot -sovelluksen rakennekaavio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tyypillinen kerrosarkkitehtuuri (layered architecture) Spring Boot -sovellukselle, pakettitasolla jaoteltuna.

## Controller — sisääntulopiste (Entry point)

- Käsittelee HTTP-pyynnöt
- Validoi DTO:t
- Kutsuu palveluita (service-kerrosta)
- Sääntö: ei liiketoimintalogiikkaa controllerissa

## Service — liiketoimintalogiikka (Business logic)

- Domain-säännöt
- Työnkulkujen orkestrointi
- Politiikat (policies)
- Transaktiot
- Sääntö: ei suoraa persistenssilogiikkaa servicessä

## Repository — pysyvyys (Persistence)

- JPA / Hibernate
- JDBC
- Ulkoiset API:t

## Model / Entity — toimialueen esitys (Domain representation)

- Pidä johdonmukaisena
- Pidä yksinkertaisena
- Määrittele selkeät invariantit

## DTO — API-sopimus (API contract)

- Vältä entiteettien paljastamista suoraan ulos
- Suojaa sisäisiä muutoksia
- Ylläpidä API:n vakautta

## Config — konfiguraatio (Configuration)

- Tietoturva (security)
- Beanit
- Infrastruktuuri
- Integraatiot

## Exception Handling — globaali virheenkäsittely

- Globaalit virheet käsitellään keskitetysti (esim. `@ControllerAdvice`)

## Yhteenveto

Kerrosarkkitehtuurin idea on erottaa vastuut selkeästi: Controller vastaanottaa pyynnöt, Service toteuttaa liiketoimintalogiikan, Repository hoitaa tietokantayhteydet, ja Model/Entity sekä DTO pitävät toimialueen mallin ja ulkoisen rajapinnan erillään toisistaan. Näin sovellus pysyy testattavana ja ylläpidettävänä sen kasvaessa.
