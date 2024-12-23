import os
from datetime import datetime

import whisper

folder = "/home/Audio/"
filenames = os.listdir(folder)
filepath = os.path.join(folder, filenames[0])
print(filepath)

models = whisper.available_models()
print(models)

model = whisper.load_model("base")

start = datetime.now()
result = model.transcribe(filepath)
end = datetime.now()
print("Time: ", (end - start))
print(result["text"])
