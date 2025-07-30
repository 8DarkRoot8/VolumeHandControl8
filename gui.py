# gui.py

import tkinter as tk
import threading
import VolumeHandControl

def start_volume_control():
    threading.Thread(target=VolumeHandControl.main).start()

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Volume Control by DARKROOT")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="🎛️ Hand Volume Control", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=30)

start_button = tk.Button(root, text="▶ Start", font=("Helvetica", 14), bg="#0984e3", fg="white", command=start_volume_control)
start_button.pack(pady=10)

exit_button = tk.Button(root, text="❌ Exit", font=("Helvetica", 14), bg="#d63031", fg="white", command=close_app)
exit_button.pack(pady=10)

root.mainloop()
