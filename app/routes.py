from app.controllers.audio_controller import audio_bp

def register_routes(app):
    app.register_blueprint(audio_bp)
