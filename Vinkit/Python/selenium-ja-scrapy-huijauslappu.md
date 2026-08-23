<!-- tags: vinkit, python -->

# Selenium ja Scrapy -huijauslappu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com.

## Selenium

### Työnkulku

```python
from selenium import webdriver
web = "www.google.com"
path = 'introduce chromedriver path'
driver = webdriver.Chrome(path)
driver.get(web)
```

**Elementin haku**
```python
driver.find_element_by_id('name')
```

**Useamman elementin haku**
```python
driver.find_elements_by_class_name()
driver.find_elements_by_css_selector()
driver.find_elements_by_xpath()
driver.find_elements_by_tag_name()
driver.find_elements_by_name()
```

**Ajurin sulkeminen**
```python
driver.quit()
```

**Tekstin hakeminen**
```python
data = element.text
```

**Implisiittiset odotukset (Implicit Waits)**
```python
import time
time.sleep(2)
```

**Eksplisiittiset odotukset (Explicit Waits)**
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'id_name')))
# Odota 5 sekuntia kunnes elementti on klikattavissa
```

**Asetukset: headless-tila, ikkunan koon muutos**
```python
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(path, options=options)
```

## Scrapy

Scrapy on tehokkain web scraping -framework Pythonissa, mutta sen käyttöönotto on hieman monimutkaisempi.

### Projektin ja hämähäkin (spider) luonti

Luo uusi projekti terminaalissa:
```bash
scrapy startproject my_first_spider
```

Luo uusi spider (vaihda ensin hakemistoa):
```bash
cd my_first_spider
scrapy genspider example example.com
```

### Peruspohja (basic template)

Kun spider luodaan, saadaan seuraavansisältöinen pohja:

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
```

Luokka (`class`) sisältää edellisessä vaiheessa annetut tiedot. `parse`-metodi pitää rakentaa itse alla olevilla funktioilla.

### Elementtien etsiminen

Scrapyssä elementtejä etsitään `response`-argumentilla `parse`-metodin sisällä:

```python
response.xpath('//tag[@AttributeName="Value"]')
```

### Tekstin hakeminen

Tekstielementin saa `text()`-funktiolla ja joko `.get()`- tai `.getall()`-metodilla:

```python
response.xpath('//h1/text()').get()
response.xpath('//tag[@Attribute="Value"]/text()').getall()
```

### Poimitun datan palauttaminen

Poimitun datan näkemiseksi täytyy käyttää `yield`-avainsanaa:

```python
def parse(self, response):
    title = response.xpath('//h1/text()').get()

    # Palauta poimittu data
    yield {'titles': title}
```

### Spiderin ajaminen ja datan vienti CSV:ksi tai JSON:ksi

```bash
scrapy crawl example
scrapy crawl example -o name_of_file.csv
scrapy crawl example -o name_of_file.json
```
