import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import soundfile as sf
from threading import Thread
import os
import time

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Recorder")

        self.record_button = ttk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack(pady=20)

        self.status_label = ttk.Label(self.master, text="")
        self.status_label.pack()

        self.output_filename = "output.wav"

    def start_recording(self):
        self.record_button.config(state=tk.DISABLED)
        self.status_label.config(text="Recording...")

        record_thread = Thread(target=self._record_audio_thread)
        record_thread.start()

    def _record_audio_thread(self):
        sample_rate = 44100
        channels = 2  # Stereo

        duration = 10  # Recording duration in seconds
        recording = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=channels, dtype='int16')
        sd.wait()  # Wait for the recording to complete

        self.status_label.config(text="Recording complete")
        self.record_button.config(state=tk.NORMAL)

        # Save the recorded audio to a WAV file
        sf.write(self.output_filename, recording, sample_rate, format='wav', subtype='PCM_24')

    def play_recorded_audio(self):
        os.system(f'start {self.output_filename}')

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)

    play_button = ttk.Button(root, text="Play Recorded Audio", command=app.play_recorded_audio)
    play_button.pack(pady=10)

    root.mainloop()
