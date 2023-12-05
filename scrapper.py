import requests
from bs4 import BeautifulSoup

import psycopg2
from psycopg2 import sql

def save_to_database(title, description, image_url, link):
    # Connect to the existing PostgreSQL database
    connection = psycopg2.connect(
        dbname="aexjcmyn",
        user="aexjcmyn",
        password="QlHahIT_R8Bi4CDHuiiRYMFj7t0MVkHF",
        host="batyr.db.elephantsql.com",
        port="5432"
    )
    cursor = connection.cursor()


    title_text = title.text.strip() if title else "Not found"
    description_text = description.text.strip() if description else "Not found"
    image_url_text = image_url['src'].strip() if image_url else "Not found"
    link_text = link['href'].strip() if link else "Not found"


    insert_query = sql.SQL('''
        INSERT INTO news (title, description, image_url, link)
        VALUES (%s, %s, %s, %s)
    ''')
    cursor.execute(insert_query, (title_text, description_text, image_url_text, link_text))


    connection.commit()
    connection.close()

def scrape_computer_weekly(news_limit=4):
    url = "https://www.computerweekly.com/es/recursos/Prevencion-de-amenazas"


    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')


        news_containers = soup.find_all(['li', 'div','ul'], class_=['topic-related-content-list', 'topic-related-item-info'])


        for index, news_container in enumerate(news_containers, start=1):

            title = news_container.find('h3')
            description = news_container.find('p')
            image_url = news_container.find('img')
            link = news_container.find('a', class_='read-more')


            
            save_to_database(title,
                             description,
                             image_url,
                             link)

            if index == news_limit:
                break
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

if __name__ == "__main__":
    scrape_computer_weekly(news_limit=20)
