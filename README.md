
# VozParaTexto

**VozParaTexto** é uma aplicação em Python que converte arquivos de áudio `.mp3` para texto, utilizando a biblioteca [Vosk](https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip). A aplicação oferece uma interface gráfica simples e intuitiva, desenvolvida com `Tkinter`, permitindo aos usuários converter arquivos de áudio e visualizar o progresso da transcrição em tempo real.

## Funcionalidades Principais

- **Conversão de Áudio para Texto**: Suporta arquivos `.mp3` e realiza automaticamente a conversão para o formato `.wav` com as especificações adequadas (mono, 16-bit, 16kHz) para o reconhecimento de fala.
- **Transcrição Precisa**: Utiliza o modelo Vosk otimizado para português brasileiro, garantindo transcrições de alta qualidade.
- **Interface Gráfica Amigável**: Desenvolvida com `Tkinter`, a interface permite selecionar arquivos, iniciar a transcrição e acompanhar o progresso em uma barra de progresso.
- **Suporte a Multiplataformas**: Funciona em sistemas Windows, Linux e macOS.

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

## Passo a Passo para Uso

### 1. Instale os Requisitos

Antes de iniciar a aplicação, certifique-se de que todas as dependências estão instaladas.

#### Windows

1. Baixe e instale o [ffmpeg](https://ffmpeg.org/download.html).
2. Instale as bibliotecas Python necessárias:

```bash
pip install vosk pydub
```

#### Ubuntu/Linux

1. Instale o ffmpeg via terminal:

```bash
sudo apt install ffmpeg
```

2. Instale as bibliotecas Python necessárias:

```bash
pip install vosk pydub
```

#### macOS

1. Instale o ffmpeg usando o Homebrew:

```bash
brew install ffmpeg
```

2. Instale as bibliotecas Python necessárias:

```bash
pip install vosk pydub
```

### 2. Baixe o Modelo Vosk

1. Acesse o [link de download do modelo Vosk](https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip).
2. Extraia o conteúdo do arquivo `.zip` em uma pasta de sua escolha.
3. Certifique-se de que o caminho para essa pasta esteja corretamente configurado na aplicação.

### 3. Clonar o Repositório

Baixe o código da aplicação no seu computador.

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

### 4. Configurar o Ambiente Virtual e Instalar Dependências

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

### 5. Executar a Aplicação

Agora que tudo está configurado, você pode executar a aplicação e começar a converter seus arquivos de áudio para texto.

#### Windows

1. Execute o seguinte comando no Prompt de Comando ou PowerShell:

```bash
python VozParaTexto.py
```

#### Ubuntu/Linux ou macOS

1. Execute o seguinte comando no terminal:

```bash
python3 VozParaTexto.py
```

### 6. Transcrição e Salvamento

1. Use a interface gráfica para selecionar um arquivo `.mp3` de seu computador.
2. Acompanhe o progresso da transcrição na barra de progresso exibida.
3. Ao final, o texto transcrito será salvo em um arquivo `.txt` na mesma pasta do arquivo de áudio original.

## Créditos

**Criado por** Waldir Donatti Junior
