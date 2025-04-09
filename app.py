from flask import Flask
app = Flask(__name__)

@app.route('/new/<name>')
def home(name):
    return " Hello %s How are You" %name

# app.add_url_rule('/hi', 'home', home)
if __name__ == '__main__':
    app.run(debug=True)