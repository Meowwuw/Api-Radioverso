class AudioService:
    def __init__(self, audio_repository):
        self.audio_repository = audio_repository

    def get_all_audios(self):
        return self.audio_repository.get_all_audios()

    def get_audio(self, filename):
        return self.audio_repository.get_audio(filename)
