from flask import Flask, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = 'https://www.meuip.com.br/'

@app.route("/meuip")
def scrapper():
    response = urlopen(URL)

    html = response.read()
    html = html.decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    ip = soup.findAll('h3')
    meu_ip = ip[0].text
    meu_ip = meu_ip.split('Meu ip é ')

    return jsonify({'ip': meu_ip[1]})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
