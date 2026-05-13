import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

def get_printers():
    try:
        out = subprocess.check_output(["lpstat", "-p"], text=True)
        printers = []
        for line in out.splitlines():
            if line.startswith("printer"):
                printers.append(line.split()[1])
        return printers
    except:
        return []

def print_text():
    text = text_box.get("1.0", tk.END).strip()
    printer = printer_var.get()

    if not text:
        messagebox.showerror("Hata", "Metin boş!")
        return

    if not printer:
        messagebox.showerror("Hata", "Yazıcı seç!")
        return

    try:
        p = subprocess.Popen(
            ["lp", "-d", printer],
            stdin=subprocess.PIPE,
            text=True
        )
        p.communicate(text)
        messagebox.showinfo("OK", "Yazdırıldı!")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

# UI
root = tk.Tk()
root.title("TextPrint")

tk.Label(root, text="Yazıcı:").pack()

printer_var = ttk.Combobox(root, values=get_printers())
printer_var.pack()

tk.Label(root, text="Metin:").pack()

text_box = tk.Text(root, height=10, width=40)
text_box.pack()

tk.Button(root, text="Yazdır", command=print_text).pack()

root.mainloop()
