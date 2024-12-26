import logging
import logging.config

from argparser import parse_args
from setting import settings
from transcriber import Transcriber

args = parse_args()
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)

logging.config.dictConfig(settings.logging)  # type: ignore[arg-type]

transcriber_ = Transcriber(model=args.model)
transcriber_.transcribe_files(input_dir=args.input_dir, output_dir=args.output_dir)
