from file_manager_app import create_app
from config import Config


flask_app = create_app(Config)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=8000, debug=True)
