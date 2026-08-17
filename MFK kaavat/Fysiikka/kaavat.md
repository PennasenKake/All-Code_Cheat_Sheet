Fysiikka

Johdanto
Fysiikan lait ohjaavat insinöörityön periaatteita, 
oli kyse sitten rakenteiden kestävyydestä, sähköjärjestelmien suunnittelusta 
tai prosessien optimoinnista. Tämä osio kattaa mekaniikan, sähkötekniikan, 
lämpöfysiikan, aalto-opin, optiikan, fluidimekaniikan ja modernin fysiikan kaavoja, 
jotka ovat välttämättömiä monilla insinöörialoilla.



Mekaniikka 

✸ Newtonin II laki
  ➤ F = m * a
  ➤ F = voima (N), m = massa (kg), a = kiihtyvyys (m/s²)  
✸ Kineettinen energia
  ➤ E_k = (1/2)mv²
  ➤ E_k = kineettinen energia (J), m = massa (kg), v = nopeus (m/s)  
✸ Potentiaalinen energia
  ➤ E_p = mgh
  ➤ E_p = potentiaalinen energia (J), m = massa (kg), g = painovoiman kiihtyvyys (9.81 m/s²), h = korkeus (m)  
✸ Momentti
  ➤ M = F * d
  ➤ M = momentti (Nm), F = voima (N), d = etäisyys (m)  
✸ Hooken laki
  ➤ F = -k * x
  ➤ F = voima (N), k = jousivakio (N/m), x = venymä (m)  
✸ Liikemäärä
  ➤ p = m * v
  ➤ p = liikemäärä (kg·m/s), m = massa (kg), v = nopeus (m/s)  
✸ Työ
  ➤ W = F * d * cos(θ)
  ➤ W = työ (J), F = voima (N), d = matka (m), θ = voiman ja liikkeen välinen kulma  
✸ Impulssi
  ➤ I = F * Δt
  ➤ I = impulssi (Ns), F = voima (N), Δt = aika (s)  
✸ Lisäys: Keskipakovoima
  ➤ F_c = m * v²/r
  ➤ F_c = keskipakovoima (N), m = massa (kg), v = nopeus (m/s), r = säde (m)
  ➤ Perustelu: Keskipakovoima on tärkeä esimerkiksi pyörivien koneiden (kuten moottoreiden tai turbiinien) suunnittelussa.
✸ Lisäys: Kitkavoima
  ➤ F_k = μ * N
  ➤ F_k = kitkavoima (N), μ = kitkakerroin, N = normaalivoima (N)
  ➤ Perustelu: Kitka on olennainen insinöörisovelluksissa, kuten jarrujärjestelmissä tai mekaanisissa liitoksissa.


Sähkötekniikka 
▬ Ohmin laki
  ⇢ U = R * I
  ⇢ U = jännite (V), R = vastus (Ω), I = virta (A)  
▬ Teho
  ⇢ P = U * I
  ⇢ P = teho (W), U = jännite (V), I = virta (A)  
▬ Kapasitanssi
  ⇢ Q = C * U
  ⇢ Q = varaus (C), C = kapasitanssi (F), U = jännite (V)  
▬ Sarjakytkentä (vastukset)
  ⇢ R_total = R_1 + R_2 + ... + R_n  
▬ Rinnankytkentä (vastukset)
  ⇢ 1/R_total = 1/R_1 + 1/R_2 + ... + 1/R_n  
▬ Sähköinen energia
  ⇢ E = P * t
  ⇢ E = energia (J), P = teho (W), t = aika (s)  
▬ Coulombin laki
  ⇢ F = k * (q_1 * q_2)/r²
  ⇢ F = voima (N), k = Coulombin vakio (8.99 × 10^9 Nm²/C²), q_1, q_2 = varaukset (C), r = etäisyys (m)  
▬ Lisäys: Induktanssi (käämin energia)
  ⇢ E_L = (1/2) * L * I²
  ⇢ E_L = käämin energia (J), L = induktanssi (H), I = virta (A)
  ⇢ Perustelu: Induktanssi on olennainen elektroniikassa, esimerkiksi muuntajissa ja moottoreissa.
▬ Lisäys: Vaihtovirran tehollinen arvo (RMS)
  ⇢ I_rms = I_peak / √2
  ⇢ I_rms = tehollinen virta (A), I_peak = huippuvirta (A)
  ⇢ Perustelu: Vaihtovirran teholliset arvot ovat tärkeitä sähköverkkojen ja laitteiden suunnittelussa.


Lämpöfysiikka 
◈ Lämpölaajeneminen
  ➔ ΔL = L_0 * α * ΔT
  ➔ ΔL = pituuden muutos (m), L_0 = alkupituus (m), α = lämpölaajenemiskerroin, ΔT = lämpötilan muutos (K)  
◈ Ideaalikaasun tilanyhtälö
  ➔ PV = nRT
  ➔ P = paine (Pa), V = tilavuus (m³), n = ainemäärä (mol), R = kaasuvakio (8.314 J/(mol·K)), T = lämpötila (K)  
◈ Lämpöenergia
  ➔ Q = m * c * ΔT
  ➔ Q = lämpöenergia (J), m = massa (kg), c = ominaislämpökapasiteetti (J/(kg·K)), ΔT = lämpötilan muutos (K)  
◈ Lisäys: Lämmönsiirto (konduktio)
  ➔ Q = k * A * ΔT * t / d
  ➔ Q = siirtynyt lämpö (J), k = lämmönjohtavuus (W/(m·K)), A = pinta-ala (m²), ΔT = lämpötilaero (K), t = aika (s), d = paksuus (m)
  ➔ Perustelu: Lämmönsiirto on keskeistä insinöörisovelluksissa, kuten lämmöneristyksen suunnittelussa.
◈ Lisäys: Entropian muutos
  ➔ ΔS = Q/T
  ➔ ΔS = entropian muutos (J/K), Q = lämpöenergia (J), T = lämpötila (K)
  ➔ Perustelu: Entropia on tärkeä termodynamiikassa, erityisesti prosessien tehokkuuden analysoinnissa.


Aalto-oppi 
✷ Aallon nopeus
  ⬟ v = f * λ
  ⬟ v = aallon nopeus (m/s), f = taajuus (Hz), λ = aallonpituus (m)
  ⬟ Perustelu: Aalto-oppi on tärkeää esimerkiksi akustiikassa ja värähtelyjen analyysissä.
✷ Doppler-ilmiö
  ⬟ f' = f * (v + v_o)/(v - v_s)
  ⬟ f' = havaittu taajuus (Hz), f = alkuperäinen taajuus (Hz), v = aallon nopeus (m/s), v_o = havaitsijan nopeus (m/s), v_s = lähteen nopeus (m/s)
  ⬟ Perustelu: Doppler-ilmiö on hyödyllinen esimerkiksi tutkasovelluksissa ja ääniaalloissa.


Optiikka 
❂ Linssikaava
  ➼ 1/f = 1/d_o + 1/d_i
  ➼ f = polttoväli (m), d_o = kohteen etäisyys (m), d_i = kuvan etäisyys (m)
  ➼ Perustelu: Optiikka on tärkeää esimerkiksi instrumenttien (kuten mikroskooppien) suunnittelussa.
❂ Valon taittuminen (Snellin laki)
  ➼ n_1 * sin(θ_1) = n_2 * sin(θ_2)
  ➼ n_1, n_2 = taitekertoimet, θ_1, θ_2 = tulokulma ja taittumiskulma
  ➼ Perustelu: Valon taittuminen on olennainen optisissa järjestelmissä, kuten linsseissä ja kuituoptiikassa.
Fluidimekaniikka (lisäys)
✠ Bernoullin yhtälö
   P + (1/2)ρv² + ρgh = vakio
   P = paine (Pa), ρ = tiheys (kg/m³), v = nopeus (m/s), g = painovoiman kiihtyvyys (m/s²), h = korkeus (m)
   Perustelu: Bernoullin yhtälö on tärkeä nesteiden virtausten analyysissä, esimerkiksi putkistoissa ja siipiprofiileissa.
✠ Jatkuvuusyhtälö
   A_1 * v_1 = A_2 * v_2
   A_1, A_2 = poikkipinta-alat (m²), v_1, v_2 = nopeudet (m/s)
   Perustelu: Jatkuvuusyhtälö on keskeinen fluididynamiikassa, esimerkiksi pumppujen ja venttiilien suunnittelussa.

   
Moderni fysiikka 
 Einsteinin massa-energiaekvivalenssi
  ⤷ E = mc²
  ⤷ E = energia (J), m = massa (kg), c = valonnopeus (3.00 × 10^8 m/s)
  ⤷ Perustelu: Tämä on tärkeä ydinteknologiassa ja energiantuotannossa.
 Planckin kaava (säteilyenergia)
  ⤷ E = h * f
  ⤷ E = energia (J), h = Planckin vakio (6.626 × 10^(-34) Js), f = taajuus (Hz)
  ⤷ Perustelu: Planckin kaava on olennainen kvanttifysiikassa, esimerkiksi fotonien energian laskennassa.

