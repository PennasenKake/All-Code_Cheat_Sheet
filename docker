Docker CLI - Peruskomennot
==========================
Konttien hallinta (Containers):
Kontin käynnistys: docker run IMAGE Esim. docker run nginx

Kontin käynnistys taustalla: docker run -d IMAGE Esim. docker run -d nginx

Näytä kaikki kontit (myös pysäytetyt): docker ps -a

Pysäytä kontti: docker stop CONTAINER Esim. docker stop mycontainer

Poista kontti: docker rm CONTAINER Esim. docker rm mycontainer

Käynnistä komentoa suoraan kontissa: docker exec -it CONTAINER COMMAND Esim. docker exec -it mycontainer bash

Kuvien hallinta (Images):
Lataa kuva: docker pull IMAGE[:TAG] Esim. docker pull nginx

Näytä ladatut kuvat: docker images

Poista kuva: docker rmi IMAGE Esim. docker rmi nginx

Rakenna uusi kuva Dockerfilestä: docker build -t IMAGE DIRECTORY Esim. docker build -t myapp .

Tallenna kuva tiedostoksi: docker save IMAGE > FILE Esim. docker save nginx > nginx.tar

Verkon ja liitännän hallinta:
Portin uudelleenohjaus: docker run -p HOSTPORT:CONTAINERPORT IMAGE Esim. docker run -p 8080:80 nginx

Liitä paikallinen hakemisto konttiin: docker run -v /HOSTDIR:/CONTAINERDIR IMAGE Esim. docker run -v /data:/app/data myapp

Tilastoja ja tietoja:
Näytä käynnissä olevan kontin resurssikäyttö: docker stats

Näytä kontin lokit: docker logs CONTAINER Esim. docker logs mycontainer

Tutki konttia tai kuvaa tarkemmin: docker inspect OBJECT Esim. docker inspect nginx

Siivous:
Poista pysäytetyt kontit: docker container prune

Poista käyttämättömät kuvat: docker image prune -a