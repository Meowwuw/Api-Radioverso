from flask import Flask
from app.config import Config
from app.routes import register_routes
from app.repositories.audio_repository import AudioRepository
from app.services.audio_service import AudioService

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    audio_repository = AudioRepository(app.config['AUDIO_FOLDER'])
    audio_service = AudioService(audio_repository)

    from app.controllers import audio_controller
    audio_controller.audio_service = audio_service

    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
