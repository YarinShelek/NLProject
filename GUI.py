import tkinter as tk
from tkinter import ttk
from main import gui_main_flow

def send_message(input_box, chat_window):
    message = input_box.get()
    prediction = model.predict([message])
    if 1 in prediction:
        message = "This message contains profanity."

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + message + "\n")
    chat_window.config(state=tk.DISABLED)

    input_box.delete(0, tk.END)

def open_gui():
    global model

    model = gui_main_flow()

    window = tk.Tk()
    window.title("ANTI PROFANITY CHAT")

    style = ttk.Style()

    style.configure("Chat.TFrame", background="#F0F0F0")
    style.configure("Chat.TLabel", background="#F0F0F0", foreground="#333333", font=("Helvetica", 12))
    style.configure("Chat.TEntry", background="white", foreground="#333333", font=("Helvetica", 12))
    style.configure("Chat.TButton", background="#0084FF", foreground="black", font=("Helvetica", 12), padding=5)

    chat_frame = ttk.Frame(window, style="Chat.TFrame")
    chat_frame.pack(pady=10)

    chat_window = tk.Text(chat_frame, height=20, width=50, bg="#F0F0F0", fg="#333333", font=("Helvetica", 12))
    chat_window.config(state=tk.DISABLED)
    chat_window.pack()

    input_frame = ttk.Frame(window, style="Chat.TFrame")
    input_frame.pack(pady=10)

    input_box = ttk.Entry(input_frame, width=50, style="Chat.TEntry")
    input_box.bind("<Return>", lambda event: send_message(input_box, chat_window))
    input_box.pack(side=tk.LEFT, padx=5)

    send_button = ttk.Button(input_frame, text="Send", command=lambda: send_message(input_box, chat_window), style="Chat.TButton")
    send_button.pack(side=tk.LEFT, padx=(0, 5), pady=5)

    window.configure(bg="#F0F0F0")
    window.mainloop()

if __name__ == "__main__":
    model = None
    open_gui()
