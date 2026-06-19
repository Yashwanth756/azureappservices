from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

# Simple HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Azure Flask App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        .header { color: #0078d4; }
        .info { background-color: #f3f3f3; padding: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="header">Welcome to Azure Flask App</h1>
        <div class="info">
            <p><strong>Server Time:</strong> {{ current_time }}</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
            <p><strong>Hostname:</strong> {{ hostname }}</p>
        </div>
        <h2>API Endpoints:</h2>
        <ul>
            <li><a href="/">/</a> - Home page</li>
            <li><a href="/api/hello">/api/hello</a> - JSON response</li>
            <li><a href="/api/status">/api/status</a> - Status endpoint</li>
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment=os.getenv('FLASK_ENV', 'production'),
        hostname=os.getenv('COMPUTERNAME', 'local')
    )

@app.route('/api/hello')
def hello():
    return jsonify({
        'message': 'Hello from Azure Flask App!',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'service': 'Flask App on Azure App Services',
        'python_version': '3.9+',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/config')
def config():
    return jsonify({
        'app_name': app.name,
        'debug': app.debug,
        'environment': os.getenv('FLASK_ENV', 'production')
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error', 'message': str(error)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
