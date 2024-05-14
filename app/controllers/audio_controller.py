from flask import Blueprint, jsonify, send_from_directory
from app.services.audio_service import AudioService
import os

audio_bp = Blueprint('audio', __name__)
audio_service = AudioService(audio_repository=None)  

@audio_bp.route('/api/audios', methods=['GET'])
def get_audios():
    audios = audio_service.get_all_audios()
    return jsonify([audio.__dict__ for audio in audios])

@audio_bp.route('/api/audio/<filename>', methods=['GET'])
def get_audio(filename):
    audio = audio_service.get_audio(filename)
    if audio:
        audio_folder = os.path.join(os.getcwd(), 'static', 'audio')
        return send_from_directory(audio_folder, filename)
    return jsonify({"error": "Audio not found"}), 404
