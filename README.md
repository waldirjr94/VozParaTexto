
# VozParaTexto

**VozParaTexto** é uma aplicação em Python que converte arquivos de áudio `.mp3` para texto, utilizando a biblioteca [Vosk](https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip). A aplicação oferece uma interface gráfica simples e intuitiva, desenvolvida com `Tkinter`, que permite aos usuários selecionar arquivos de áudio, transcrevê-los e salvar o resultado em um arquivo de texto.

## Funcionalidades Principais

- **Conversão de Áudio para Texto**: Suporta arquivos `.mp3` e realiza a conversão automática para o formato necessário (mono, 16-bit, 16kHz) antes de iniciar a transcrição.
- **Barra de Progresso**: Apresenta o progresso da transcrição em uma janela modal, proporcionando uma experiência visual clara e amigável.
- **Interface Gráfica Intuitiva**: Desenvolvida com `Tkinter`, é fácil de usar e acessível mesmo para usuários sem conhecimentos técnicos.
- **Suporte ao Português Brasileiro**: Utiliza o modelo Vosk otimizado para o português do Brasil, garantindo transcrições precisas.

## Requisitos

### Software

- **Python 3.12**: Versão mínima recomendada.
- **ffmpeg**: Necessário para o `pydub` manipular arquivos de áudio.
  - **Windows**: Baixe e instale o [ffmpeg](https://ffmpeg.org/download.html).
  - **Linux**: Instale via terminal com `sudo apt install ffmpeg`.
  - **macOS**: Instale usando o Homebrew com `brew install ffmpeg`.

### Bibliotecas Python

- `vosk`: Para reconhecimento de fala.
- `pydub`: Para manipulação de arquivos de áudio.
- `tkinter`: Para criar a interface gráfica (geralmente já incluído no Python).

## Passo a Passo de Configuração

### 1. Baixe o Modelo Vosk

Antes de começar, você precisará baixar o modelo de reconhecimento de fala que o Vosk utilizará para transcrever o áudio:

1. Acesse o [link de download do modelo Vosk](https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip).
2. Extraia o conteúdo do arquivo `.zip` em uma pasta de sua escolha.
3. Certifique-se de que o caminho para essa pasta esteja corretamente configurado na aplicação.

### 2. Clonar o Repositório

#### Windows

1. Abra o Prompt de Comando ou o PowerShell.
2. Execute os seguintes comandos:

```bash
git clone https://github.com/waldirjr94/VozParaTexto.git
cd VozParaTexto
```

#### Ubuntu/Linux ou macOS

1. Abra o terminal.
2. Execute os seguintes comandos:

```bash
git clone https://github.com/waldirjr94/VozParaTexto.git
cd VozParaTexto
```

### 3. Configurar o Ambiente Virtual e Instalar Dependências

#### Windows

1. Crie e ative um ambiente virtual:
  
```bash
python -m venv venv
venv\Scripts\activate
```

2. Instale as dependências necessárias:

```bash
pip install vosk pydub
```

#### Ubuntu/Linux ou macOS

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instale as dependências necessárias:

```bash
pip install vosk pydub
```

### 4. Executar a Aplicação

#### Windows

Execute o seguinte comando no Prompt de Comando ou PowerShell:

```bash
python VozParaTexto.py
```

#### Ubuntu/Linux ou macOS

Execute o seguinte comando no terminal:

```bash
python3 VozParaTexto.py
```

## Créditos

**Criado por** Waldir Donatti Junior
