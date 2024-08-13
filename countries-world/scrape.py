import requests
from bs4 import BeautifulSoup
import json

def fetch_countries():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    countries = []
    country_elements = soup.find_all('div', class_='col-md-4 country')

    for country in country_elements:
        name = country.find('h3', class_='country-name').text.strip()
        capital = country.find('span', class_='country-capital').text
        population = country.find('span', class_='country-population').text
        area = country.find('span', class_='country-area').text
        
        countries.append({
            'Name': name,
            'Capital': capital,
            'Population': population,
            'Area (km2)': area
        })

    return countries


def main():
    countries = fetch_countries()

    # Save data to json file
    with open('countries.json', 'w') as f:
        json.dump(countries, f, indent=2)

    # Save data to csv file
    with open('countries.csv', 'w') as f:
        # Write all dict keys in file with commas separated
        f.write(','.join(countries[0].keys()))
        f.write('\n')

        for row in countries:
            # Write the values in a row
            f.write(','.join(str(x) for x in row.values()))
            f.write('\n')

    print('Data is saved to countries.json and countries.csv')


if __name__ == "__main__":
    main()