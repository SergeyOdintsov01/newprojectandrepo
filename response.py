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
        for headline in news_headlines:
            print(headline.text.strip())

    else:
        print(f"Ошибка при получении страницы. Код статуса: {response.status_code}")

#if __name__ == "__main__":
#    get_bybit_news()
