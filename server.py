import flask


app = flask.Flask(__name__)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'alive', 200

if __name__ == '__main__':
    app.run()