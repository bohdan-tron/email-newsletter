import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="envs/.env")

api_key = os.environ.get('NEWS_API_KEY')
debug_mode = os.environ.get('DEBUG')
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"


r = requests.get(url)
data = r.json()

for article in data['articles']:
  post = (article['title'], article['url'], article['publishedAt'])
  print(post)