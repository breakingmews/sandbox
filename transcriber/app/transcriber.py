import logging
import os
from datetime import datetime

import utils
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

    def transcribe_files(
        self, input_dir: str = settings.audio, output_dir: str = settings.transcription
    ) -> None:
        _log.info(f"Input dir: {input_dir}")
        _log.info(f"Output dir: {output_dir}")

        os.makedirs(output_dir, exist_ok=True)

        filepaths = utils.get_filepaths(input_dir)
        _log.info(f"Transcribing {len(filepaths)} files: \n{"\n".join(filepaths)}")

        for filepath in filepaths:
            try:
                transcription = self.transcribe(filepath)
                destination = utils.get_destnation(input_dir, output_dir, filepath)
                utils.write(destination, transcription)
            except Exception as e:
                _log.error("Error transcribing %s: %s" % (filepath, e), stack_info=True)
