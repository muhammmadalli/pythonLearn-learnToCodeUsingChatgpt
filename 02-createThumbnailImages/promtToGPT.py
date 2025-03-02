import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def create_thumbnails(input_dir: str, output_dir: str, size: tuple = (50, 50)):
    """
    Creates 50x50 pixel thumbnails for all image files in the specified directory.
    
    :param input_dir: Directory containing image files.
    :param output_dir: Directory to save thumbnails.
    :param size: Tuple indicating the size of thumbnails. Defaults to (50, 50).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        try:
            with Image.open(file_path) as img:
                img.thumbnail(size)
                thumbnail_path = os.path.join(output_dir, file_name)
                img.save(thumbnail_path, format=img.format)
        except Exception as e:
            print(f"Skipping {file_name}: {e}")
    
    messagebox.showinfo("Success", "Thumbnails created successfully!")

def select_input_directory():
    directory = filedialog.askdirectory()
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(0, directory)

def select_output_directory():
    directory = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, directory)

def start_thumbnail_creation():
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    
    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both input and output directories.")
        return
    
    create_thumbnails(input_dir, output_dir)

# GUI Setup
root = tk.Tk()
root.title("Thumbnail Creator")
root.geometry("400x200")

tk.Label(root, text="Select Input Directory:").pack(pady=5)
input_dir_entry = tk.Entry(root, width=50)
input_dir_entry.pack()
tk.Button(root, text="Browse", command=select_input_directory).pack()

tk.Label(root, text="Select Output Directory:").pack(pady=5)
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.pack()
tk.Button(root, text="Browse", command=select_output_directory).pack()

tk.Button(root, text="Create Thumbnails", command=start_thumbnail_creation).pack(pady=10)

root.mainloop()