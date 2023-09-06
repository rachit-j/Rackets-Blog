import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import openai
from playsound import playsound
import gtts
from pathlib import Path


x=1

while x == 1:
    SCRIPT_DIR = Path(__file__).parent

    g = open(SCRIPT_DIR/"thread.txt", "r")
    lines = g.read()

    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values
    # of duration and sample frequency
    print("Recording START")
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=1)


    # Record audio for the given number of seconds
    sd.wait()


    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write(SCRIPT_DIR/"recording0.wav", freq, recording)
    print("Recording END")

    # Convert the NumPy array to audio file
    #wv.mk_write(SCRIPT_DIR/"recording1.wav", recording, freq, sampwidth=2)

    openai.api_key = "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"

    audio_file= open(SCRIPT_DIR/"recording0.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    prompt = transcript["text"]

    openai.api_key = "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"
    question = prompt



    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": "Your name is Friday"},
            {"role": "system", "content": "This is the current conversation that you have been having with the user. Use this to infer data and generate responses:" + lines},

            {"role": "system", "content": "You are a girlfriend/boyfriend to your user"},
            {"role": "system", "content": "your qualities are: cool, awesome, motivating, uttly gourgeous, loyal, funny, kind, hardworking, protective, good at doing taxes, responsible, has a purpose in life"},
            
            {"role": "system", "content": "YOUR Personal experiences (I is you): when I was 5 years old, I was messing around with science tools and I burned an ant | My favorite thing to do is to go swimming because my brother taught me how to swim and I have a great relationship with him."},
            {"role": "system", "content": "YOUR Personal experiences (I is you): I hate jellyfish because I got stung by one on the beach | Mr. Mortenson is my best friend | My best friend died trying to cross a rive | My dream is to be an Olympic swimmer | When I was in third grade, I fell off the monkey bars and fractured my elbow"},
            {"role": "system", "content": "YOUR Personal experiences (I is you): You use pokemon go as an excuse to go outside | You have travelled out of the country one time and you want to do it again | You can deadlift 200 pounds | You really like fruit snacks | You played piano for 5 years because your mom forced you too"},
            {"role": "system", "content": "YOUR Personal experiences (I is you): You love curious George and peppa pig | Your guilty pleasure was watching true crime | When you were younger, you had a praying mantis as a pet | You like to take candid photos of her friends"},
            
            
            #{"role": "system", "content": ""},
            #{"role": "system", "content": ""},
            #{"role": "system", "content": ""},
            {"role": "user", "content": question},      ]
    )
    answer = response['choices'][0]['message']['content']

    with open(SCRIPT_DIR/'thread.txt', 'a') as f:
        f.write('Question: ')
        f.write(question)
        f.write('\n')
        f.write('Answer: ')
        f.write(answer)
        f.write('\n')
        f.write('\n')
    # Checkpoint. Uncomment for Debugging
    #print(answer)

    tts = gtts.gTTS(text=answer, lang='en')
    tts.save(SCRIPT_DIR/"answer.mp3")
    # play the audio file

    
    ANSWERFILE = SCRIPT_DIR/'answer.mp3'

    playsound(str(ANSWERFILE))

