from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re



# links to pages - de parcurs si salvat retetele pentru toate paginile (sus e doar pentru prima pagina)
for i in range(1, 3):
    print("!!!!!!!!!!!!!PAGINA", i)
    url = "https://www.vegansociety.com/lifestyle/recipes?page="
    url += str(i)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    data = soup.findAll('div', attrs={'class': 'view-content'})
    set_links = set()
    for div in data:
        links = div.findAll('a')
        for a in links:
            set_links.add(a['href'])
    print(set_links)

    url = "https://www.vegansociety.com"
    for page in set_links:
        if "recipes" in page:
            link = url + page
            print(link)
            # request catre fiecare pagina cu reteta
            req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            # title
            title = soup.find('h1').text.strip()
            print("Recipe title = ", title)

            # ingredients
            data = soup.find('div', attrs={'class': 'field-item even'}).find('ul')
            ingr_list = []
            for li in data.findAll('li'):
                ingr_list.append(li.text.strip())
            print("Ingredients list = ", ingr_list)

            # method
            data = soup.find('div', attrs={'class': 'field-item even'}).find('ol')
            steps_list = []
            if data is None:
                p = soup.find('div', attrs={'class': 'field-item even'}).find('p')
                steps_list.append(p.text.strip())
                print("Method steps list = ", steps_list)
            else:
                for li in data.findAll('li'):
                    steps_list.append(li.text.strip())
                print("Method steps list = ", steps_list)
            # datele afisate ar trebui adaugate intr-o baza de date


