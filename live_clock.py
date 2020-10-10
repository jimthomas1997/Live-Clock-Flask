from flask import Flask,render_template
app=Flask(__name__)

import requests
from bs4 import BeautifulSoup

page=requests.get('https://weather.com/en-IN/weather/today/l/9b6182fe7982a37d6eb65491b0218d1c7e7ee13e0b60e40bfaa9669973e7e933')
# print(page)
soup=BeautifulSoup(page.content,'html.parser')
item1=soup.find('div',class_="_1A9zV")
new=item1.find('span',class_="_3KcTQ").get_text()


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', data=new)
 

if __name__=='__main__':
    app.run( debug = True)