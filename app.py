from app import create_app

if __name__ == "__main__":
    app = create_app()
    
    host = '0.0.0.0'
    port = 5000
    
    app.run(host=host, port=port, debug=True)