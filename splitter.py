import os
import tkinter as tk
from tkinter import filedialog, messagebox

def split_file_by_chars(file_path, chars_per_part=15000, output_dir="output_parts"):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    total_parts = (len(text) + chars_per_part - 1) // chars_per_part

    os.makedirs(output_dir, exist_ok=True)

    for i in range(total_parts):
        start = i * chars_per_part
        end = start + chars_per_part
        part_text = text[start:end]

        part_filename = os.path.join(output_dir, f"part_{i+1}.txt")
        with open(part_filename, "w", encoding="utf-8") as f:
            f.write(part_text)

    return total_parts

def start_split():
    file_path = entry_file.get()
    if not file_path or not os.path.isfile(file_path):
        messagebox.showerror("ERROR", "Plese select correct text file.")
        return

    try:
        total_parts = split_file_by_chars(file_path)
        messagebox.showinfo("Sukces", f"Plik podzielono na {total_parts} części.\nZapisano w folderze 'output_parts'.")
    except Exception as e:
        messagebox.showerror("error", f"error:\n{str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select text file",
        filetypes=[("text file", "*.txt")]
    )
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

# --- Budowa GUI ---
root = tk.Tk()
root.title("Spliting txt files (15000 words)")
root.geometry("500x160")
root.resizable(False, False)

label_file = tk.Label(root, text="Select file:")
label_file.pack(pady=(10, 0))

frame = tk.Frame(root)
frame.pack(padx=10, pady=5)

entry_file = tk.Entry(frame, width=50)
entry_file.pack(side=tk.LEFT, padx=(0, 5))

btn_browse = tk.Button(frame, text="Browse", command=browse_file)
btn_browse.pack(side=tk.LEFT)

btn_start = tk.Button(root, text="Split file", width=30, command=start_split)
btn_start.pack(pady=15)

root.mainloop()
