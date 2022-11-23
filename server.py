import flask, os, re, decoder
from flask_cors import CORS
import block_list


app = flask.Flask(__name__)
CORS(app)

@app.before_request
def block_method():
    ip = flask.request.environ.get('REMOTE_ADDR')
    
    if ip in block_list.ips:
        flask.abort(403)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'alive', 200

@app.route('/usage', methods=['GET'])
def get_usage():
    return flask.render_template('index.html')

@app.route('/usage', methods=['POST'])
def post_usage():
    return flask.send_file('api.json')

@app.route('/', methods=['GET'])
def get_home():
    return flask.redirect('/usage', code=302)

@app.route('/decode-option', methods=['POST'])
def crawler_server():
    f_body = flask.request.json
    
    if 'option' not in f_body:
        return 'encoded option missing in request', 400
        
    if re.search('[A-Z]{1,6}\\d{6}[CP]\\d{8}', f_body['option']):
        return decoder.decode_option(f_body['option']), 200
    
    return 'invalid option format', 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)