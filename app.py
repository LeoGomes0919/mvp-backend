from flask_cors import CORS

from app import create_app

if __name__ == '__main__':
    app = create_app(config_name='development')
    CORS(app)

    app.run(debug=True)
