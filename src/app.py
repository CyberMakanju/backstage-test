
from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/vi/details')

def hello_world():
    return jsonify({
       'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
       'hostname': socket.gethostname()
    })

@app.route('/api/vi/healthz')

def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    
    app.run(host="0.0.0.0")



#'/api/vi/details'
#'/api/vi/healthz'