import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv
from openai import OpenAI

# ======================
# CARREGAR VARIÁVEIS
# ======================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ======================
# CONFIGURAÇÕES
# ======================
SAMPLE_RATE = 16000
DURATION = 5
AUDIO_INPUT = "entrada.wav"
AUDIO_OUTPUT = "resposta.mp3"

def gravar_audio():
    print("🎙️ Fale agora...")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    write(AUDIO_INPUT, SAMPLE_RATE, audio)
    print("✅ Gravação finalizada.")

def transcrever_audio():
    print("🧠 Transcrevendo...")
    with open(AUDIO_INPUT, "rb") as audio:
        resposta = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
    print("📝 Texto:", resposta.text)
    return resposta.text

def perguntar_chatgpt(pergunta):
    print("🤖 Pensando...")
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente de voz educado e objetivo."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content

def texto_para_audio(texto):
    print("🔊 Gerando áudio...")
    tts = gTTS(text=texto, lang="pt")
    tts.save(AUDIO_OUTPUT)

def main():
    gravar_audio()
    pergunta = transcrever_audio()

    if not pergunta.strip():
        print("❌ Nenhuma fala detectada.")
        return

    resposta = perguntar_chatgpt(pergunta)
    print("💬 Resposta:", resposta)

    texto_para_audio(resposta)
    playsound(AUDIO_OUTPUT)

if __name__ == "__main__":
    main()