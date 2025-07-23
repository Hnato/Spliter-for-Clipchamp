import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font

BG_COLOR = "#f5f3e7"     
FRAME_COLOR = "#1e3932" 
BTN_COLOR = "#6f4e37" 
BTN_TEXT_COLOR = "#fff"    
ENTRY_BG = "#fff"
ENTRY_FG = "#1e3932"
FONT_MAIN = ("Segoe UI", 12, "bold")
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_EMOJI = ("Segoe UI Emoji", 60)

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
        messagebox.showerror("Error", "Please select a valid text file.")
        return

    try:
        total_parts = split_file_by_chars(file_path)
        messagebox.showinfo("Yay!", f"File has been split into {total_parts} cute parts!\nSaved in the 'output_parts' folder.")
    except Exception as e:
        messagebox.showerror("Oh no!", f"An error occurred:\n{str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select text file",
        filetypes=[("Text file", "*.txt")]
    )
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

root = tk.Tk()
root.title("Coffee Text Splitter")
root.geometry("450x450")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

emoji_label = tk.Label(root, text="☕", font=FONT_EMOJI, bg=BG_COLOR)
emoji_label.pack(pady=(18, 5))

title_label = tk.Label(root, text="Coffee Text Splitter ☕", font=FONT_TITLE, fg=FRAME_COLOR, bg=BG_COLOR)
title_label.pack(pady=(0, 10))

main_frame = tk.Frame(root, bg=FRAME_COLOR, bd=0, relief=tk.RIDGE)
main_frame.pack(padx=24, pady=10, fill=tk.BOTH, expand=False)

label_file = tk.Label(main_frame, text="Select a text file to split:", font=FONT_MAIN, fg=BTN_TEXT_COLOR, bg=FRAME_COLOR)
label_file.pack(pady=(18, 8), padx=10, anchor="w")

frame = tk.Frame(main_frame, bg=FRAME_COLOR)
frame.pack(padx=10, pady=5, fill=tk.X)

entry_file = tk.Entry(frame, width=32, font=FONT_MAIN, bg=ENTRY_BG, fg=ENTRY_FG, relief=tk.FLAT, highlightthickness=2, highlightbackground=BTN_COLOR)
entry_file.pack(side=tk.LEFT, padx=(0, 8), ipady=4)

btn_browse = tk.Button(
    frame, text="Browse", font=FONT_MAIN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
    activebackground=FRAME_COLOR, activeforeground=BTN_TEXT_COLOR,
    command=browse_file, relief=tk.FLAT, cursor="hand2", bd=0, highlightthickness=0
)
btn_browse.pack(side=tk.LEFT, ipadx=8, ipady=2)

btn_start = tk.Button(
    main_frame, text="Split File", font=FONT_MAIN, bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
    activebackground=FRAME_COLOR, activeforeground=BTN_TEXT_COLOR,
    width=24, command=start_split, relief=tk.FLAT, cursor="hand2", bd=0, highlightthickness=0
)
btn_start.pack(pady=24, ipadx=8, ipady=4)

footer = tk.Label(
    root,
    text="Brewed with love and ☕ for you!",
    font=("Segoe UI", 10, "italic"),
    fg=FRAME_COLOR,
    bg=BG_COLOR
)
footer.pack(side=tk.BOTTOM, pady=8)

root.mainloop()
