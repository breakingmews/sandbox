import logging
import logging.config
import os

from argparser import parse_args
from setting import settings
from transcriber import transcriber_

args = parse_args()
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)

logging.config.dictConfig(settings.logging)  # type: ignore[arg-type]
_log = logging.getLogger(__name__)


def write(filepath: str, text: str) -> None:
    _log.info("Writing transcription to %s" % filepath)
    with open(filepath, "w") as f:
        f.write(text)


def get_destnation(output_dir: str, filepath: str) -> str:
    return os.path.join(
        output_dir,
        os.path.basename(filepath).removesuffix(".mp3") + ".txt",
    )


def transcribe(
    input_dir: str = settings.audio, output_dir: str = settings.transcriptions
) -> None:
    _log.info(f"Input dir: {input_dir}")
    _log.info(f"Output dir: {output_dir}")

    os.makedirs(output_dir, exist_ok=True)

    filenames = os.listdir(input_dir)
    filepaths = [os.path.join(input_dir, filename) for filename in filenames]
    filepaths.sort()

    _log.info("Transcribing %d files" % len(filepaths))

    for filepath in filepaths:
        try:
            transcription = transcriber_.transcribe(filepath)
            destination = get_destnation(output_dir, filepath)
            write(destination, transcription)
        except Exception as e:
            _log.error("Error transcribing %s: %s" % (filepath, e))


transcribe(input_dir=args.input_dir, output_dir=args.output_dir)
