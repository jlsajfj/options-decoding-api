import flask


app = flask.Flask(__name__)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'alive', 200

@app.route('/', methods=['GET'])
def get_home():
    return 'this page is under construction, instructions will go here', 503

@app.route('/', methods=['POST'])
def crawler_server():
    f_body = flask.request.json
    
    if 'option' not in f_body:
        return 'encoded option missing in request', 400
    
    return f_body, 200

if __name__ == '__main__':
    app.run()