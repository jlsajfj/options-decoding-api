import flask, os, re, decoder


app = flask.Flask(__name__)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'alive', 200

@app.route('/', methods=['GET'])
def get_home():
    return 'this page is under construction, instructions will go here', 503

@app.route('/decode-option', methods=['POST'])
def crawler_server():
    f_body = flask.request.json
    
    if 'option' not in f_body:
        return 'encoded option missing in request', 400
        
    if not re.search('[A-Z]{1,6}\\d{6}[CP]\\d{8}', f_body['option']):
        return 'invalid option format', 400
    
    return decoder.decode_option(f_body['option']), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)