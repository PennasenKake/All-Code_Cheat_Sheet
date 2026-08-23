<!-- tags: vinkit, ai-ml -->

# Tilastotieteen kaavat

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Kymmenen keskeistä tilastotieteen kaavaa ja käsitettä.

## 1. Keskiluvut (Measures of Central Tendency)

- **Keskiarvo (Mean):** x̄ = (Σx) / n, missä Σx = kaikkien havaintojen summa, n = havaintojen lukumäärä.
- **Mediaani (Median):** keskimmäinen arvo järjestetystä datasta.
- **Moodi (Mode):** yleisin arvo.

## 2. Hajontaluvut (Measures of Dispersion)

- **Vaihteluväli (Range):** Range = Max − Min
- **Varianssi, populaatio:** σ² = Σ(x − μ)² / N
- **Varianssi, otos:** s² = Σ(x − x̄)² / (n − 1)
- **Keskihajonta (Standard Deviation):** σ = √(σ²) tai s = √(s²)

## 3. Todennäköisyyden perusteet

- **Todennäköisyyskaava:** P(A) = Suotuisat tapaukset / Kaikki tapaukset
- **Komplementtisääntö:** P(A') = 1 − P(A)

## 4. Ehdollinen todennäköisyys

P(A|B) = P(A ∩ B) / P(B)

- P(A|B) = todennäköisyys A:lle, kun B on jo tapahtunut
- P(A ∩ B) = todennäköisyys sekä A:lle että B:lle
- P(B) = todennäköisyys B:lle

## 5. Yhteenlaskusääntö (Addition Rule)

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

- P(A ∪ B) = todennäköisyys A:lle tai B:lle
- P(A ∩ B) = todennäköisyys sekä A:lle että B:lle

## 6. Kertolaskusääntö (Multiplication Rule)

Riippumattomille tapahtumille: P(A ∩ B) = P(A) · P(B) — todennäköisyys, että A ja B tapahtuvat molemmat.

## 7. Binomijakauma

P(X = k) = C(n, k) · p^k · (1 − p)^(n−k)

- n = kokeiden lukumäärä
- k = onnistumisten lukumäärä
- p = onnistumisen todennäköisyys
- 1 − p = epäonnistumisen todennäköisyys

## 8. Z-arvo (standardoitu arvo)

Z = (x − μ) / σ

- x = raakapistemäärä
- μ = keskiarvo
- σ = keskihajonta

## 9. Korrelaatiokerroin

r = Σ(x − x̄)(y − ȳ) / √( Σ(x − x̄)² · Σ(y − ȳ)² )

- r = korrelaatiokerroin, −1 ≤ r ≤ 1

## 10. Ydinoivallus

Tilastotieteen kaavat auttavat:

- Datan keräämisessä ja järjestämisessä.
- Datan analysoinnissa ja tulkinnassa.
- Ennusteissa ja tulevaisuuden arvioinnissa.
- Päätöksenteossa epävarmuuden vallitessa.

*"Statistics is the art of making sense of data."*
