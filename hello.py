from flask import Flask, render_template, request #追加

app = Flask(__name__)

@app.route('/') # root
def default():
    request.args.to_dict()
    return 'add path /hello or /home in the address\n add path /hello2?name=eritsi' 

@app.route('/hello2')
def hello2():
    name = request.args.get('name')
    return render_template('home.html', title='flask test', name=name) 

@app.route('/hello', methods=['POST', 'GET']) #Methodを明示する必要あり
def hello():
    
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return render_template('hello.html', title='flask test', name=name) 

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == 'POST':# リクエストがPOSTの場合
        name2 = request.form.get('name2')# nameを取得
        return render_template('home.html', name=name2)# name2をhome.htmlに送る
    return render_template('signup.html')



## おまじない
if __name__ == "__main__":
    app.run(debug=True)
# https://qiita.com/zaburo/items/5091041a5afb2a7dffc8
# https://www.nblog09.com/w/2021/11/26/flask_post/