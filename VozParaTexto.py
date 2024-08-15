import os
import wave
import json
from tkinter import Tk, Label, Button, filedialog, Text, messagebox, Frame, Scrollbar, RIGHT, Y, END, StringVar, Toplevel, BOTTOM
from tkinter.ttk import Progressbar
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)

    # Converte o áudio para mono, 16-bit, 16kHz
    audio = audio.set_channels(1)  # Mono
    audio = audio.set_sample_width(2)  # 16-bit
    audio = audio.set_frame_rate(16000)  # 16kHz
    
    audio.export(wav_file, format="wav")

def transcribe_audio(wav_file, model_path, progress_var, progress_bar, progress_window):
    try:
        model = Model(model_path)
    except Exception as e:
        raise Exception(f"Falha ao carregar o modelo: {e}")
    
    recognizer = KaldiRecognizer(model, 16000)
    
    with wave.open(wav_file, "rb") as wf:
        total_frames = wf.getnframes()
        processed_frames = 0
        
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            recognizer.AcceptWaveform(data)
            processed_frames += 4000
            
            # Atualizar a barra de progresso
            progress_percentage = int((processed_frames / total_frames) * 100)
            progress_var.set(f"Progresso: {progress_percentage}%")
            progress_bar['value'] = progress_percentage
            progress_window.update_idletasks()

        final_result = recognizer.FinalResult()
        text = json.loads(final_result)['text']
    
    return text

def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo .mp3",
        filetypes=(("MP3 files", "*.mp3"),)
    )
    return file_path

def save_file_dialog():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"),)
    )
    return file_path

def show_progress_popup():
    progress_window = Toplevel(root)
    progress_window.title("Progresso da Transcrição")
    progress_window.geometry("300x100")
    progress_window.resizable(False, False)
    progress_window.transient(root)
    progress_window.grab_set()  # Previne interação com a janela principal

    # Centraliza a janela de progresso em relação à janela principal
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    window_width = 300
    window_height = 100
    position_right = root_x + int(root_width/2 - window_width/2)
    position_down = root_y + int(root_height/2 - window_height/2)
    progress_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    progress_var = StringVar()
    progress_var.set("Progresso: 0%")
    progress_label = Label(progress_window, textvariable=progress_var, font=("Helvetica", 10))
    progress_label.pack(pady=10)

    progress_bar = Progressbar(progress_window, orient="horizontal", length=250, mode="determinate")
    progress_bar.pack(pady=10)

    return progress_window, progress_var, progress_bar

def transcribe():
    mp3_file = open_file_dialog()
    if not mp3_file:
        return

    # Exibir pop-up de progresso
    progress_window, progress_var, progress_bar = show_progress_popup()

    # Caminho para o modelo Vosk pequeno em português brasileiro
    model_path = r"C:\Users\sn1080241\Downloads\Projetos Python\VozParaTexto\vosk-model-small-pt-0.3"
    
    # Converter o arquivo .mp3 para .wav no formato necessário
    wav_file = "temp_audio.wav"
    try:
        convert_mp3_to_wav(mp3_file, wav_file)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter áudio: {str(e)}")
        progress_window.destroy()
        return

    # Realiza a transcrição
    try:
        text = transcribe_audio(wav_file, model_path, progress_var, progress_bar, progress_window)
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")
        progress_window.destroy()
        return
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o modelo: {str(e)}")
        progress_window.destroy()
        return

    # Fechar pop-up de progresso após a transcrição
    progress_window.destroy()

    # Exibir transcrição
    transcription_text.config(state="normal")
    transcription_text.delete(1.0, END)
    transcription_text.insert(END, text)
    transcription_text.config(state="disabled")

    # Remove o arquivo temporário
    os.remove(wav_file)

def save_transcription():
    if transcription_text.get(1.0, END).strip():
        output_file = save_file_dialog()
        if output_file:
            with open(output_file, "w") as f:
                f.write(transcription_text.get(1.0, END).strip())
            messagebox.showinfo("Sucesso", f"Transcrição salva em {output_file}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma transcrição disponível para salvar.")

# Interface Gráfica com Tkinter
root = Tk()
root.title("VozParaTexto - Conversor de Fala para Texto")
root.geometry("600x550")
root.configure(bg="#f4f4f4")

# Estilo do Título
title_label = Label(root, text="VozParaTexto", font=("Helvetica", 18, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

# Instruções
instructions_label = Label(root, text="Clique no botão abaixo para selecionar um arquivo .mp3", font=("Helvetica", 12), bg="#f4f4f4", fg="#555")
instructions_label.pack(pady=5)

# Botão de Transcrição
transcribe_button = Button(root, text="Selecionar Arquivo e Transcrever", command=transcribe, bg="#007acc", fg="white", font=("Helvetica", 12), padx=10, pady=5)
transcribe_button.pack(pady=10)

# Área de Texto para a Transcrição com Scrollbar
frame = Frame(root)
frame.pack(pady=10, fill="both", expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

transcription_text = Text(frame, wrap="word", width=50, height=15, font=("Helvetica", 10), bg="#f9f9f9", fg="#333", yscrollcommand=scrollbar.set)
transcription_text.pack(fill="both", expand=True)
scrollbar.config(command=transcription_text.yview)
transcription_text.config(state="disabled")

# Botão de Salvar
save_button = Button(root, text="Salvar Transcrição", command=save_transcription, bg="#28a745", fg="white", font=("Helvetica", 12), padx=10, pady=5)
save_button.pack(pady=20)

# Marca d'Água
watermark_label = Label(root, text="© Criado Por Waldir Donatti Junior", font=("Helvetica", 10, "italic"), bg="#f4f4f4", fg="#888")
watermark_label.pack(side=BOTTOM, pady=5)

root.mainloop()
