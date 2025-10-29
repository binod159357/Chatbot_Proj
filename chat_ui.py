# chat_ui.py
import tkinter as tk
from response import get_response
from nlp1 import clean_text
import nlp1

def send_message():
    user_input = entry_box.get()
    chat_log.insert(tk.END, f"You: {user_input}\n")
    response = get_response(user_input)
    chat_log.insert(tk.END, f"Bot: {response}\n\n")
    entry_box.delete(0, tk.END)

root = tk.Tk()
root.title("Rule-Based Chatbot")

chat_log = tk.Text(root, bg="white", fg="black", wrap="word")
chat_log.pack(padx=10, pady=10)

entry_box = tk.Entry(root, width=80)
entry_box.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
