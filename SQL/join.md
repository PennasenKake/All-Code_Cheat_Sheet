
-- INNER JOIN

/* Käyttötarkoitus: Kun tarvitset tietueet, 
joilla on vastaavat arvot molemmissa tauluissa. */

/* Esim: Asiakkaiden löytäminen, jotka ovat tehneet tilauksia. */

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date
FROM
    customers c
INNER JOIN
    orders o ON c.customer_id = o.customer_id;


-- LEFT JOIN

/* Käyttötarkoitus: Kun tarvitset kaikki vasemman taulun tietueet 
ja vastaavat tietueet oikeasta taulusta. Oikeasta taulusta löytymättömät tietueet ovat NULL. */

/* Esim: Kaikkien asiakkaiden löytäminen, myös niiden, jotka eivät ole tehneet tilausta. */

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date
FROM
    customers c
LEFT JOIN
    orders o ON c.customer_id = o.customer_id;


-- RIGHT JOIN

/* Käyttötarkoitus: Kun tarvitset kaikki oikean taulun tietueet 
ja vastaavat tietueet vasemmasta taulusta. Vasemman taulun löytymättömät tietueet ovat NULL. */

/* Esim: Kaikkien tilausten listaaminen ja niiden asiakkaiden, jotka ovat ne tehneet (jos on asiakas). */

SELECT
    o.order_id,
    o.order_date,
    c.customer_id,
    c.customer_name
FROM
    customers c
RIGHT JOIN
    orders o ON c.customer_id = o.customer_id;


-- FULL JOIN

/* Käyttötarkoitus: Kun tarvitset kaikki tietueet, joilla on vastaavuuksia joko 
vasemmassa tai oikeassa taulussa. Puuttuvat tietueet ovat NULL. */

/* Esim: Kaikkien asiakkaiden ja tilausten löytäminen, myös ilman vastaavuutta olevien. */

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date
FROM
    customers c
FULL JOIN
    orders o ON c.customer_id = o.customer_id;


-- CROSS JOIN

/* Käyttötarkoitus: Kun tarvitset taulukoiden karteesisen tulon 
(kaikki mahdolliset riviyhdistelmät). 
Ole varovainen, sillä tämä voi tuottaa paljon rivejä! */

/* Esim: Jokaisen asiakkaan yhdistäminen kaikkiin tuotteisiin. */

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date
FROM
    customers c
CROSS JOIN
    orders o;


-- SELF JOIN

/* Käyttötarkoitus: Kun haluat yhdistää taulun itseensä 
vertaillaksesi rivejä saman taulun sisällä. */

/* Esim: Samalla esimiehellä olevien työntekijäparien löytäminen. */

SELECT
    e1.employee_name AS työntekijä_1,
    e2.employee_name AS työntekijä_2,
    e1.manager_id
FROM
    employees e1
JOIN
    employees e2 ON e1.manager_id = e2.employee_id
WHERE
    e1.employee_id <> e2.employee_id;

-- https://www.instagram.com/p/DGyFJ8fSsxB/?utm_source=ig_web_copy_link