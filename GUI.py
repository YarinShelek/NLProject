import tkinter as tk
from tkinter import ttk
from main import gui_main_flow

model = gui_main_flow()


def send_message(event=None):
    message = input_box.get()
    prediction = model.predict([message])
    if 1 in prediction:
        message = "This message contains profanity."

    # Display the message in the chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + message + "\n")
    chat_window.config(state=tk.DISABLED)

    # Clear the input box
    input_box.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("ANTI PROFANITY CHAT")

# Create a style for the widgets
style = ttk.Style()

# Configure the style for the chat window
style.configure("Chat.TFrame", background="#F0F0F0")
style.configure("Chat.TLabel", background="#F0F0F0", foreground="#333333", font=("Helvetica", 12))
style.configure("Chat.TEntry", background="white", foreground="#333333", font=("Helvetica", 12))
style.configure("Chat.TButton", background="#0084FF", foreground="black", font=("Helvetica", 12), padding=5)

# Create a frame for the chat window
chat_frame = ttk.Frame(window, style="Chat.TFrame")
chat_frame.pack(pady=10)

# Create a text widget to display the chat messages
chat_window = tk.Text(chat_frame, height=20, width=50, bg="#F0F0F0", fg="#333333", font=("Helvetica", 12))
chat_window.config(state=tk.DISABLED)
chat_window.pack()

# Create a frame for the input box and send button
input_frame = ttk.Frame(window, style="Chat.TFrame")
input_frame.pack(pady=10)

# Create an input box for entering messages
input_box = ttk.Entry(input_frame, width=50, style="Chat.TEntry")
input_box.bind("<Return>", send_message)  # Bind Enter key to send message
input_box.pack(side=tk.LEFT, padx=5)

# Create a send button
send_button = ttk.Button(input_frame, text="Send", command=send_message, style="Chat.TButton")
send_button.pack(side=tk.LEFT, padx=(0, 5), pady=5)

# Set window background color
window.configure(bg="#F0F0F0")
window.mainloop()