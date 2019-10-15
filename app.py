from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        tgl = request.form['tgl']
        bln = request.form['bln']
        thn = request.form['thn']

        r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ican&tanggal={}-{}-{}'.format(tgl,bln,thn))

        data =r.json()

        list_data = []
        list_data.append((data['data']['lahir'],data['data']['usia'],data['data']['ultah'],data['data']['zodiak']))

        return render_template('detail.html',list_data=list_data)

    tgl = []
    bln = []
    thn = []

    for x in range(1,32):
        tgl.append(x)

    for y in range(1,13):
        bln.append(y)

    for w in range(1900, 2020):
        thn.append(w)

    return render_template('index.html',tgl=tgl, bln=bln, thn=thn)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 