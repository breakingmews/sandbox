import logging
from datetime import datetime

from faster_whisper import WhisperModel
from setting import settings

_log = logging.getLogger(__name__)


class Transcriber:
    def __init__(self, model_size=settings.model_size):
        _log.info(f"Using model: {model_size}")
        self.model = WhisperModel(model_size)

    def transcribe(self, filepath):
        start = datetime.now()
        _log.info("Transcribing %s" % filepath)

        segments, info = self.model.transcribe(filepath, beam_size=5)

        text = ""
        for segment in segments:
            _log.debug(
                "[%.2fs - %.2fs] %s" % (segment.start, segment.end, segment.text)
            )
            text += segment.text + " "

        end = datetime.now()
        duration = end - start
        _log.info(f"Duration: {duration}")

        return text
