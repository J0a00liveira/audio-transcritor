import os
import whisper
import warnings
import nltk
import platform
import time
from colorama import init, Fore

if platform.system() == 'Windows':
    nltk_data_path = os.path.join(os.getenv('APPDATA'), 'nltk_data')
else:
    nltk_data_path = os.path.expanduser("~/.nltk_data")

if not os.path.exists(os.path.join(nltk_data_path, "punkt")):
    nltk.download('punkt', quiet=True)

if not os.path.exists(os.path.join(nltk_data_path, "punkt_tab")):
    nltk.download('punkt_tab', quiet=True)

warnings.simplefilter("ignore", FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, message="FP16 is not supported on CPU")

init()

model = whisper.load_model("base")

audio_dir = "audio_files"
transcription_dir = "transcriptions"

os.makedirs(audio_dir, exist_ok=True)
os.makedirs(transcription_dir, exist_ok=True)

audio_files = [f for f in os.listdir(audio_dir) if f.lower().endswith(('.mp4', '.mp3', '.m4a'))]

if not audio_files:
    print(Fore.RED + "Nenhum arquivo de áudio válido encontrado na pasta 'audio_files'.")
else:
    total_files = len(audio_files)
    for idx, audio_file in enumerate(audio_files, 1):
        audio_path = os.path.join(audio_dir, audio_file)
        
        base_name = os.path.splitext(audio_file)[0]
        
        transcription_file = os.path.join(transcription_dir, f"{base_name}_transcription.txt")
        
        print(Fore.YELLOW + f"Transcrevendo ({idx}/{total_files}) o arquivo {audio_file}...")
        print(Fore.WHITE)
        
        start_time_transcription = time.time()  # Inicia a contagem do tempo
        
        response = model.transcribe(audio_path, word_timestamps=True)
        
        formatted_text = []

        for segment in response["segments"]:
            start_time = segment['start']
            end_time = segment['end']
            
            start_minute = int(start_time // 60)
            start_second = round(start_time % 60, 2)

            end_minute = int(end_time // 60)
            end_second = round(end_time % 60, 2)
            
            text = segment['text']

            formatted_text.append(f"[{start_minute:02}:{start_second:05.2f} - {end_minute:02}:{end_second:05.2f}] {text}\n")

        with open(transcription_file, "w") as file:
            file.writelines(formatted_text)

        end_time_transcription = time.time() 
        transcription_duration = end_time_transcription - start_time_transcription
        
        minutes_taken = int(transcription_duration // 60)
        seconds_taken = round(transcription_duration % 60, 2)

        print(Fore.GREEN + f"Transcrição do arquivo {audio_file} salva em {transcription_file}")
        print(Fore.CYAN + f"Tempo de transcrição: {minutes_taken:02}:{seconds_taken:05.2f}")
