from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000)

# https://qiita.com/bauer/items/70abcb68d3b00d0d1794