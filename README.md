# VozParaTexto

**VozParaTexto** é uma aplicação simples desenvolvida em Python que converte arquivos de áudio `.mp3` para texto utilizando a biblioteca [Vosk](https://alphacephei.com/vosk/). A aplicação oferece uma interface gráfica amigável criada com `Tkinter`, permitindo aos usuários selecionar arquivos `.mp3`, transcrevê-los e salvar o resultado em um arquivo de texto.

## Funcionalidades

- **Conversão de Áudio para Texto**: Suporta arquivos `.mp3` e realiza a conversão automática para o formato necessário (mono, 16-bit, 16kHz) antes da transcrição.
- **Barra de Progresso em Pop-up**: Mostra o progresso da transcrição em uma janela modal que aparece centralizada na tela, proporcionando uma experiência visual clara.
- **Interface Gráfica Simples**: Interface construída com `Tkinter`, fácil de usar e intuitiva.
- **Suporte a Português Brasileiro**: Utiliza o modelo Vosk otimizado para o português brasileiro.

## Tecnologias Utilizadas

- **Python 3.12**
- **Vosk** para reconhecimento de fala
- **Pydub** para manipulação de áudio
- **Tkinter** para a interface gráfica

## Requisitos

- **Python 3.12**
- Bibliotecas Python necessárias:
  - `vosk`
  - `pydub`
  - `tkinter` (geralmente incluído no Python)

## Como Usar (Windows)

### 1. Clone o Repositório

No Windows, abra o Prompt de Comando ou o PowerShell, e execute os seguintes comandos:

```bash
git clone https://github.com/waldirjr94/VozParaTexto.git
cd VozParaTexto
```

### 2. Instale o Ambiente Virtual e as Dependências
```bash
python -m venv venv
venv\Scripts\activate
pip install vosk pydub
```

### 3. Execute a Aplicação
```bash
python VozParaTexto.py
```

## Como Usar (Ubuntu/Linux)

### 1. Instale o Python 3 e o pip, se ainda não estiverem instalados.

No Ubuntu, use o terminal:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Clone o Repositório
```bash
git clone https://github.com/waldirjr94/VozParaTexto.git
cd VozParaTexto
```

### 3. Instale o Ambiente Virtual e as Dependências
```bash
python3 -m venv venv
source venv/bin/activate
pip install vosk pydub
```

### 4. Execute a Aplicação
```bash
python3 VozParaTexto.py
```

## Como Usar (macOS)

### 1. Instale o Python 3 e o pip, se ainda não estiverem instalados.

No macOS, você pode usar o Homebrew:

```bash
brew install python
```

### 2. Clone o Repositório
```bash
git clone https://github.com/waldirjr94/VozParaTexto.git
cd VozParaTexto
```

### 3. Instale o Ambiente Virtual e as Dependências
```bash
python3 -m venv venv
source venv/bin/activate
pip install vosk pydub
```

### 4. Execute a Aplicação
```bash
python3 VozParaTexto.py
```

## Créditos
### © Criado Por Waldir Donatti Junior
