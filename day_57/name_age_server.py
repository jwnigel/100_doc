from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Enter a name in the URL'

@app.route('/<name>')
def name(name):
    g_response = requests.get(f'https://api.genderize.io?name={name.lower()}').json()
    gender = g_response['gender']
    age_response = requests.get(f'https://api.agify.io/?name={name.lower()}').json()
    print(age_response)
    age = age_response['age']
    return render_template('name_age_index.html', name=name, gender=gender, age=age)

if __name__ == '__main__':
    app.run(debug=True)
