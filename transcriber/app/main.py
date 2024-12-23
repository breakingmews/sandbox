import logging
import logging.config
import os

import utils
from argparser import parse_args
from setting import settings
from transcriber import transcriber_

args = parse_args()
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)

logging.config.dictConfig(settings.logging)  # type: ignore[arg-type]
_log = logging.getLogger(__name__)


def transcribe(
    input_dir: str = settings.audio, output_dir: str = settings.transcription
) -> None:
    _log.info(f"Input dir: {input_dir}")
    _log.info(f"Output dir: {output_dir}")

    os.makedirs(output_dir, exist_ok=True)

    filepaths = utils.get_filepaths(input_dir)
    _log.info(f"Transcribing {len(filepaths)} files: \n{"\n".join(filepaths)}")

    for filepath in filepaths:
        try:
            transcription = transcriber_.transcribe(filepath)
            destination = utils.get_destnation(input_dir, output_dir, filepath)
            utils.write(destination, transcription)
        except Exception as e:
            _log.error("Error transcribing %s: %s" % (filepath, e), stack_info=True)


transcribe(input_dir=args.input_dir, output_dir=args.output_dir)
