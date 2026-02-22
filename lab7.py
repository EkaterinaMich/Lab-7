import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_URL = 'https://newsapi.org/v2/everything'
API = os.getenv('news_api')  



class NewsModel:
    def __init__(self, api=API, url=NEWS_URL):
        self.api = api
        self.url = url

    def get_news(self, topic):

        params = {
            "q": topic,
            "apiKey": self.api,
            "pageSize": 1,
            "language": "ru",
            "sortBy": "publishedAt"
        }

        try:
            res = requests.get(self.url, params=params)
            res.raise_for_status()

            data = res.json()

            articles = data.get('articles', [])
            if not articles:
                return "Статья не найдена"

            article = articles[0]

            source = article['source']['name']
            author = article.get('author', 'Неизвестно')
            title = article['title']
            description = article.get('description', 'Нет описания')
            url = article['url']

            return f"""Источник: {source}
Автор: {author}
Заголовок: {title}
Описание: {description}
Ссылка: {url}"""

        except Exception as e:
            return f"Произошла ошибка при получении новостей: {e}"


if __name__ == '__main__':
    news = NewsModel()
    topic = "котики"
    result = news.get_news(topic)
    print(result)