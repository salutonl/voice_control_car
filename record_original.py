import pyaudio
import wave
import os
import sys

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 30

def record(name, times):
    for i in int(times):
        WAVE_OUTPUT_FILENAME = "data/" + name + "/sample" + str(i) + ".wav"
        p = pyaudio.PyAudio()
        training_model_path = name + "/sample" + str(i) + ".wav"
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("recording...")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("done")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        with open('Speaker-Identification-Python/trainingDataPath.txt', 'a+') as f:
            f.write(training_model_path)
