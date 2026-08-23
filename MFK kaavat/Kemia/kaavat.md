<!-- tags: mfk-kaavat, kemia -->

# Kemia

Kemia on olennainen osa insinöörityötä, erityisesti prosessitekniikassa, materiaalitieteissä ja energiantuotannossa. Tämä osio sisältää kaavoja, jotka auttavat ymmärtämään kemiallisia reaktioita, materiaalien ominaisuuksia ja energiamuutoksia, joita tarvitaan esimerkiksi kemiallisten prosessien suunnittelussa ja korroosionestossa.

## Perusyhtälöt

**Moolimassa** — `M = m/n`
M = moolimassa (g/mol), m = massa (g), n = ainemäärä (mol)

**Ainemäärä** — `n = N/N_A`
n = ainemäärä (mol), N = hiukkasten lukumäärä, N_A = Avogadron vakio (6.022 × 10^23 mol^(-1))

**Konsentraatio** — `c = n/V`
c = konsentraatio (mol/L), n = ainemäärä (mol), V = tilavuus (L)

**Tiheys** — `ρ = m/V`
ρ = tiheys (kg/m³), m = massa (kg), V = tilavuus (m³)
*Tiheys on tärkeä materiaaliominaisuus, jota tarvitaan esimerkiksi kemiallisten prosessien suunnittelussa.*

## Reaktiot

**Reaktion tasapainovakio (K)** — `K = [tuotteet]^v / [reagenssit]^u`
[ ] = konsentraatiot (mol/L), v, u = stoikiometriset kertoimet

**Happo-emäs-titraus** — `c_1 * V_1 = c_2 * V_2`
c_1, c_2 = konsentraatiot (mol/L), V_1, V_2 = tilavuudet (L)

**pH-arvo** — `pH = -log[H⁺]`
[H⁺] = vetyionien konsentraatio (mol/L)

**Stoikiometria (reagenssin rajaus)** — `n_reagenssi = m/M`
n_reagenssi = ainemäärä (mol), m = massa (g), M = moolimassa (g/mol)
*Stoikiometria on tärkeää kemiallisten reaktioiden optimoinnissa, esimerkiksi teollisissa prosesseissa.*

**Reaktionopeus** — `v = k * [A]^m * [B]^n`
v = reaktionopeus (mol/(L·s)), k = nopeusvakio, [A], [B] = konsentraatiot (mol/L), m, n = reaktiokertoimet
*Reaktionopeus on olennainen kemiallisten prosessien suunnittelussa, kuten katalyyttien kehityksessä.*

## Termokemia

**Reaktiolämpö (entalpia)** — `ΔH = H_tuotteet - H_reagenssit`
ΔH = entalpian muutos (kJ/mol)

**Gibbsin vapaa energia** — `ΔG = ΔH - TΔS`
ΔG = vapaa energia (kJ/mol), ΔH = entalpia (kJ/mol), T = lämpötila (K), ΔS = entropia (J/(mol·K))

**Hessin laki** — `ΔH_reaktio = ΣΔH_f(tuotteet) - ΣΔH_f(reagenssit)`
ΔH_f = muodostumisentalpia (kJ/mol)
*Hessin laki on hyödyllinen reaktioiden energiamuutosten laskennassa, esimerkiksi polttoaineiden kehityksessä.*

## Elektrokemia

**Nernstin yhtälö** — `E = E^0 - (RT/nF) * ln(Q)`
E = kennon potentiaali (V), E^0 = standardipotentiaali (V), R = kaasuvakio (8.314 J/(mol·K)), T = lämpötila (K), n = elektronien määrä, F = Faradayn vakio (96485 C/mol), Q = reaktiovakio
*Elektrokemia on tärkeää esimerkiksi akkujen ja galvanointiprosessien suunnittelussa.*

**Faradayn laki (elektrolyysi)** — `m = (Q * M)/(n * F)`
m = saostunut massa (g), Q = varaus (C), M = moolimassa (g/mol), n = elektronien määrä, F = Faradayn vakio (96485 C/mol)
*Tämä on hyödyllinen pinnoitusprosesseissa ja korroosionestossa.*

## Materiaaliominaisuudet

**Kovuus (Brinell)** — `HB = (2F)/(pi * D * (D - √(D² - d²)))`
HB = Brinell-kovuus, F = voima (N), D = kuulan halkaisija (mm), d = painauman halkaisija (mm)
*Materiaalien mekaaniset ominaisuudet, kuten kovuus, ovat tärkeitä insinöörimateriaaleissa.*

**Lämpökapasiteetti** — `C = Q/ΔT`
C = lämpökapasiteetti (J/K), Q = lämpöenergia (J), ΔT = lämpötilan muutos (K)
*Lämpökapasiteetti on tärkeä materiaalien valinnassa esimerkiksi jäähdytysjärjestelmissä.*
