import os
from app.models.audio import Audio

class AudioRepository:
    def __init__(self, audio_folder):
        self.audio_folder = audio_folder

    def get_all_audios(self):
        return [
            Audio("song1.mp3", "Canción 1", "Autor 1", "Descripción de la Canción 1"),
            Audio("song2.mp3", "Canción 2", "Autor 2", "Descripción de la Canción 2")
        ]

    def get_audio(self, filename):
        audio_files = self.get_all_audios()
        for audio in audio_files:
            if audio.filename == filename:
                return audio
        return None
