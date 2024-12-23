import logging
import os

_log = logging.getLogger(__name__)


def write(filepath: str, text: str) -> None:
    _log.info("Writing transcription to %s" % filepath)
    with open(filepath, "w") as f:
        f.write(text)


def get_destnation(input_dir: str, output_dir: str, filepath: str) -> str:
    destination = (
        output_dir + filepath.removeprefix(input_dir).removesuffix(".mp3") + ".txt"
    )
    folder = os.path.dirname(destination)
    os.makedirs(folder, exist_ok=True)
    return destination


def get_filepaths(input_dir: str) -> list[str]:
    filepaths = []
    for root, _, files in os.walk(input_dir):
        for file_name in files:
            filepaths.append(os.path.join(root, file_name))
    filepaths.sort()
    return filepaths
