<img alt="Github License" src="https://img.shields.io/github/license/J0a00liveira/audio-transcritor" />  <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/J0a00liveira/audio-transcritor" />
# Audio Transcritor

Ferramenta de linha de comando em Python que transcreve arquivos de áudio e vídeo para texto usando o [Whisper](https://github.com/openai/whisper), modelo de reconhecimento de fala da OpenAI. Cada trecho transcrito vem com a marcação de tempo de início e fim.

<!-- Coloque aqui um print do terminal durante a transcrição ou de um arquivo gerado -->

## Funcionalidades

- Transcreve arquivos `.mp3`, `.mp4` e `.m4a`
- Processa em lote todos os arquivos da pasta `audio_files`
- Gera um arquivo `.txt` por áudio, com marcação de tempo em cada trecho
- Mostra no terminal o progresso e o tempo de cada transcrição
- Cria as pastas necessárias e baixa os recursos do NLTK automaticamente na primeira execução

## Exemplo de saída

Arquivo `transcriptions/reuniao_transcription.txt`:

```text
[00:00.00 - 00:04.52] Bom dia a todos, vamos começar a reunião.
[00:04.52 - 00:09.10] O primeiro ponto da pauta é o planejamento da sprint.
```

## Pré-requisitos

- Python 3
- [FFmpeg](https://ffmpeg.org/download.html) instalado e disponível no PATH (o Whisper usa o FFmpeg para ler os arquivos)

Instalação do FFmpeg:

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Windows (com Chocolatey)
choco install ffmpeg

# macOS (com Homebrew)
brew install ffmpeg
```

## Instalação

```bash
git clone https://github.com/J0a00liveira/audio-transcritor.git
cd audio-transcritor

# Recomendado: criar um ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

## Como usar

1. Coloque os arquivos de áudio na pasta `audio_files` (ela é criada na primeira execução, se ainda não existir).
2. Execute o script:

```bash
python3 transcrever.py   # Linux/macOS
python transcrever.py    # Windows
```

3. As transcrições são salvas na pasta `transcriptions`, com o nome `<nome_do_arquivo>_transcription.txt`.

## Estrutura do projeto

```text
audio-transcritor/
├── audio_files/        # Áudios de entrada
├── transcriptions/     # Transcrições geradas
├── transcrever.py      # Script principal
├── requirements.txt
└── LICENSE
```

## Observações

- O projeto usa o modelo `base` do Whisper, que equilibra velocidade e precisão. Na primeira execução o modelo é baixado automaticamente.
- A transcrição é feita por IA e pode conter erros. Revise o texto gerado antes de usá-lo.
- O processamento exige bastante da máquina. Uma GPU acelera bastante, mas o script também funciona só com CPU, de forma mais lenta.

## Tecnologias

- [Python](https://www.python.org/)
- [OpenAI Whisper](https://github.com/openai/whisper): reconhecimento de fala
- [NLTK](https://www.nltk.org/): processamento de texto
- [Colorama](https://pypi.org/project/colorama/): cores na saída do terminal
