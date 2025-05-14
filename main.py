import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv(dotenv_path="envs/.env")

api_key = os.environ.get('NEWS_API_KEY')
debug_mode = os.environ.get('DEBUG')
url = f"https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={api_key}&language=en"


r = requests.get(url)
data = r.json()

news_mail = ["Subject: Health News Today "]

for article in data['articles'][:5]:
   # Parse the published date
  published_date = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
  # Format date as DD Mon YY
  formatted_date = published_date.strftime("%d %b %y")
  
  formatted_post = formatted_date + '\n' \
    + f'{article["title"]}' + '\n' \
    + article["url"] + '\n' \
    + f'{article["description"]}' + 2 * '\n'
  
  news_mail.append(formatted_post)
  
news_mail = ''.join(news_mail)
news_mail = news_mail.encode('utf-8')

send_email(news_mail)
