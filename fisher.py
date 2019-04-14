from app import create_app

# app.add_url_rule('/hello/', view_func=hello)
app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

