from flask_cors import CORS

from app import create_app

if __name__ == '__main__':
    app = create_app(config_name='development')
    CORS(app)

    host = '0.0.0.0'
    port = 5000

    app.run(host=host, port=port, debug=True)
