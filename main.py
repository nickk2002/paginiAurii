import json
import re
from math import ceil
from pprint import pprint

import requests
from bs4 import BeautifulSoup

# sa modifici query cu ce vrei sa cauti
# ana+maria de exemplu
# o sa iti salveze un fisier .json cu numele query-ului
query = "autogara"
url = "http://www.paginiaurii.ro/cauta/" + query
debug = False  # sa pui True daca vrei sa vezi ce face in timp real


def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')
    result = soup.find("ul", class_="result-items")
    rows = result.find_all(class_="result")
    list_of_dict = []

    for row in rows:
        heading = None
        address = None
        phone_number = None
        stars = 0
        try:
            heading = row.find("h2", class_="item-heading").get_text().strip()
            address = row.find(class_="address").get_text().strip()
            phone_number = row.find("li", itemprop="telephone").get_text().strip()
            rating_indicator = row.find("div", class_="rating-indicator")
            stars_full = rating_indicator.find_all(class_="star full")
            stars = len(stars_full)
            print(heading)
        except Exception:
            if phone_number is None:
                print("There is no phone number for " + heading)
            else:
                print("There is some kind of error for " + heading)
        finally:
            row_data = {
                "title": heading,
                "address": address,
                "phone_number": phone_number,
                "stars": stars
            }
            list_of_dict.append(row_data)
    if debug:
        pprint(list_of_dict)
    return list_of_dict


def scrape_all_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')
    pagination = soup.find("ul", class_="pagination").get_text()
    try:
        number_results_per_page = int(re.findall("(\d+)/", pagination)[0])
    except Exception:
        number_results_per_page = 20
    number_results = int(re.findall("/(\d+)", pagination)[0])
    print("Going to url", url)
    print("Found", number_results, "results")
    nr_pages = ceil(number_results / number_results_per_page)
    print("Scraping ", nr_pages, "pages")
    results = []
    for page_nr in range(nr_pages):
        print("Scraping page", page_nr + 1)
        print("============")
        page_url = f"{url}/{page_nr + 1}/"
        results.extend(scrape(page_url))
    file = "json/" + query + ".json"
    with open(file, 'w') as f:
        json.dump(results, f)


scrape_all_pages(url)
