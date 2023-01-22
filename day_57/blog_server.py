from flask import Flask, render_template
import requests

app = Flask(__name__)

url = 'https://api.npoint.io/83f24c15aaef9687da0e'

response = requests.get(url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)