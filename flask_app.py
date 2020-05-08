import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        url = "https://seekingalpha.com/market-news"

        r1 = requests.get(url)
        coverpage = r1.content

        soup1 = BeautifulSoup(coverpage, 'lxml')

        all_news = soup1.find_all('h4')
        data = []
        links= []
        # front_news = soup1.find(id="latest-news-list")
        # all_news = front_news.find_all('li')

        for news in all_news:
            data.append(news.text)
            data.append("https://seekingalpha.com/" + news.a['href'])

        return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True)
