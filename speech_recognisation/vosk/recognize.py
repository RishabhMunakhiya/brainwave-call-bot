import json
import vosk
import sys
import wave

model = vosk.Model("speech_recognition/vosk_model")
wf = wave.open(sys.argv[1], "rb")
rec = vosk.KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print("Recognized Text:", result['text'])
