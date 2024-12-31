<img alt="Github License" src="https://img.shields.io/github/license/J0a00liveira/audio-transcritor" />  <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/J0a00liveira/audio-transcritor" />
# Transcritor de áudio com OpenAI Whisper           

Este script realiza a transcrição automática de arquivos de áudio (MP3, MP4, M4A) para texto, utilizando o modelo Whisper da OpenAI. Ele suporta transcrição com marcação de tempo, o que permite identificar em qual parte do áudio cada segmento de texto foi falado. O script salva as transcrições em arquivos de texto com informações de tempo para cada palavra ou segmento. Resolvi fazer este projeto por conta de uma necessidade em transcrever áudios para um trabalho, porem a maioria dos sites exige pagamento para áudios relativamente curtos, com isso, resolvi desenvolver e adaptar a minha necessidade aproveitando este modelo da OpenAI.

- Utilize da maneira que precisar, os únicos pontos de atenção que preciso levantar são:
  - É uma transcrição feita por IA, podem e vão existir erros, sempre confira o arquivo gerado.
  - É um processo normalmente pesado, exige de recursos da sua máquina, de preferência que possua uma gpu, caso contrario será feito com a cpu e pode levar mais tempo. (mas funciona, eu acho 🙃)
 
[Confira a documentação do whisper aqui](https://github.com/openai/whisper) e veja idiomas disponíveis e os tamanhos para cada tipo de modelo.

---

### Requisitos

Antes de rodar o script, você precisa instalar as dependências listadas no arquivo requirements.txt. O arquivo contém as bibliotecas necessárias para a execução do código. Para instalar basta executar o comando abaixo no terminal do projeto, recomendo que utilize um ambiente virtual para executar, caso queira utilizar deixarei abaixo um passo a passo.

<code>pip install -r requirements.txt</code>

---
<details>
  <summary> como criar ambiente virtual </summary>

- Para criar um ambiente virtual com venv:

<code>python -m venv nome_do_ambiente</code>

- Para ativar o ambiente
  - No Linux:
    <code>source nome_do_ambiente/bin/activate</code>
  - No Windows:
    <code>nome_do_ambiente\Scripts\activate</code>

Após ativar o ambiente, basta rodar o comando `pip install -r requirements.txt` para instalar as bibliotecas.  
</details>

---

### Como executar

após executar o script para o requirements.txt, inclua seus arquivos na pasta **audio_file** e rode o arquivo principal: 

- linux: python3 transcrever.py
- windows: python transcrever.py (ou outra versão do python que possa estar instalada, como a própria python3)

---

### Exemplo de Transcrição

O conteúdo do arquivo de transcrição será formatado da seguinte forma:

[00:00:01.00 - 00:00:05.00] Olá, bem-vindo ao tutorial de transcrição.

[00:00:05.00 - 00:00:10.00] Neste áudio, vamos aprender como usar o Whisper.

---

### Estrutura de Diretórios

`audio_files/` - Diretório onde os arquivos de áudio devem ser armazenados.

`transcriptions/` - Diretório onde as transcrições serão salvas.

`requirements.txt` - Arquivo com as dependências necessárias.

`transcribe.py` - O script Python responsável pela transcrição.

---

### Detalhes de Implementação

- O modelo Whisper é carregado usando `whisper.load_model("base")`, que oferece uma boa relação entre precisão e performance. Outros modelos maiores podem ser usados, mas podem exigir mais recursos computacionais, consulte a documentação.
- o colorama é utilizado para melhorar a visibilidade do processo no terminal
- warnings para ignorar alguns avisos, como no meu caso que utilizei uma máquina sem gpu, para que ele não fique sempre me alertando, mas você pode comentar as linhas 20 e 21 se quiser ver os alertas.
- O nltk é utilizado para garantir que os dados de tokenização necessários sejam baixados, evitando erros durante a execução, e também auxilia na segmentação do texto.
- O script detecta automaticamente o sistema operacional e ajusta o local onde os dados do NLTK serão armazenados.
- Os arquivos de áudio são processados em ordem, e a transcrição é salva com as marcas de tempo de início e fim de cada segmento falado.
- Durante a execução, o script mostra mensagens no terminal com feedback sobre o progresso da transcrição, incluindo tempo de transcrição e sucesso da operação.
