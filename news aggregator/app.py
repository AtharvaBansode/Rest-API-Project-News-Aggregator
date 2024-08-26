from flask import Flask, render_template
import requests

app = Flask(__name__)

# News API key (replace with your own)
NEWS_API_KEY = '760b122982fd495bb50e1b4d4f25c8b0'

# Endpoint to fetch top headlines
NEWS_API_ENDPOINT = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'

@app.route('/')
def index():
    try:
        # Fetching data from News API
        response = requests.get(NEWS_API_ENDPOINT)
        data = response.json()
        
        # Extracting articles from response
        articles = data['articles']
        
        # Rendering index.html with articles
        return render_template('index.html', articles=articles)
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

