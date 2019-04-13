from flask import Flask, jsonify


app = Flask(__name__)
app.config.from_object('config')




@app.route('/hello/')
def hello():
    return "hello"

# app.add_url_rule('/hello/', view_func=hello)

app.run(host='0.0.0.0', debug=app.config['DEBUG'])

