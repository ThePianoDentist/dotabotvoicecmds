# You need to install pyaudio to run this example
# pip install pyaudio

# When using a microphone, the AudioSource `input` parameter would be
# initialised as a queue. The pyaudio stream would be continuosly adding
# recordings to the queue, and the websocket client would be sending the
# recordings to the speech to text service
#https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/microphone-speech-to-text.py
from __future__ import print_function

import os
import re
from difflib import get_close_matches
from urllib import request

import pyaudio
import logging
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from threading import Thread
from constants import *

logger = logging.getLogger('listener')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('listener.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)

try:
    from Queue import Queue, Full
except ImportError:
    from queue import Queue, Full

###############################################
#### Initalize queue to store the recordings ##
###############################################
CHUNK = 1024
# Note: It will discard if the websocket client can't consumme fast enough
# So, increase the max size as per your choice
BUF_MAX_SIZE = CHUNK * 10
# Buffer to store audio
q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK)))

# Create an instance of AudioSource
audio_source = AudioSource(q, True, True)

###############################################
#### Prepare Speech to Text Service ########
###############################################

# initialize speech to text service
speech_to_text = SpeechToTextV1(
    iam_apikey=os.environ.get('ibmkey'),
    url='https://gateway-lon.watsonplatform.net/speech-to-text/api')

# define callback for the speech to text service
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_transcription(self, transcript):
        logger.info("transcript: {}".format(transcript))

    def on_connected(self):
        logger.info('Connection was successful')

    def on_error(self, error):
        logger.error('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        logger.error('Inactivity timeout: {}'.format(error))

    def on_listening(self):
        logger.info('Service is listening')

    def on_hypothesis(self, hypothesis):
        logger.info("hypothesis: {}".format(hypothesis))
        self.parse_hypo(hypothesis)

    def on_data(self, data):
        logger.info("data: {}".format(data))

    def on_close(self):
        logger.info("Connection closed")

    def parse_hypo(self, hypothesis):
        parts = re.sub('\s?%HESITATION\s?', ' ', hypothesis).strip(" ").split(" ")
        name = parts[0]
        name_matches = get_close_matches(name, PLAYERS_TO_HERO.keys())
        if name_matches:
            hero = PLAYERS_TO_HERO.get(name_matches[0])
            try:
                mode = self.find_mode(parts[1:])
            except IndexError:
                logger.warning("Couldnt find mode: {}".format(parts))
                return
            logger.info("\n{} NEW MODE: {}\n\n".format(hero, mode.upper()))
            req = request.Request('http://127.0.0.1:5000/{}/{}'.format(hero, mode), method="POST")
            resp = request.urlopen(req)
            print(resp)

    def find_mode(self, parts):
        return get_close_matches("".join(parts), self.strip_valid_modes())[0]

    @staticmethod
    def strip_valid_modes():
        return [vm.replace("_", "").lower() for vm in VALID_MODES]

# this function will initiate the recognize service and pass in the AudioSource
def recognize_using_weboscket(*args):
    mycallback = MyRecognizeCallback()
    speech_to_text.recognize_using_websocket(audio=audio_source,
                                             content_type='audio/l16; rate=44100',
                                             recognize_callback=mycallback,
                                             interim_results=True)

###############################################
#### Prepare the for recording using Pyaudio ##
###############################################

# Variables for recording the speech
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# define callback for pyaudio to store the recording in queue
def pyaudio_callback(in_data, frame_count, time_info, status):
    try:
        q.put(in_data)
    except Full:
        pass # discard
    return (None, pyaudio.paContinue)

# instantiate pyaudio
audio = pyaudio.PyAudio()

# open stream using callback
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    stream_callback=pyaudio_callback,
    start=False
)

#########################################################################
#### Start the recording and start service to recognize the stream ######
#########################################################################

print("Enter CTRL+C to end recording...")
stream.start_stream()

try:
    recognize_thread = Thread(target=recognize_using_weboscket, args=())
    recognize_thread.start()

    while True:
        pass
except KeyboardInterrupt:
    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_source.completed_recording()