import requests
from bs4 import BeautifulSoup

def get_bybit_news():
    url = 'https://blog.bybit.com/'

    # Отправляем GET-запрос к сайту
    response = requests.get(url)

    if response.status_code == 200:
        # Используем BeautifulSoup для анализа HTML-страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлекаем заголовки новостей
        news_headlines = soup.find_all('h2', class_='post-title')  # Обновите класс или тег, если требуется

        # Выводим заголовки новостей
        for index, headline in enumerate(news_headlines, start=1):
            print(f"{index}. {headline.text.strip()}")

    else:
        print(f"Ошибка при получении страницы. Код статуса: {response.status_code}")

get_bybit_news()