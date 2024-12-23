import argparse
import os
from argparse import Namespace

from setting import settings


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Audio Transcriber")
    parser.add_argument(
        "-v", dest="verbose", action="store_true", help="verbose output"
    )

    # TODO add model size

    parser.add_argument(
        "input_dir",
        type=str,
        nargs="?",
        default=settings.audio,
        help=f"Directory containing audio files (default: {settings.audio})",
    )
    parser.add_argument(
        "output_dir",
        type=str,
        nargs="?",
        default=settings.transcription,
        help=f"Directory to write transcriptions to (default: {settings.transcription})",
    )

    args = parser.parse_args()

    os.path.exists(args.input_dir) or parser.error(
        f"Input directory not found: {args.input_dir}"
    )
    os.path.isdir(args.input_dir) or parser.error(
        f"Input path is not a directory: {args.input_dir}"
    )

    return args
