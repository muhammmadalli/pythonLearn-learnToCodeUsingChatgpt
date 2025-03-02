import tkinter as tk
from tkinter import messagebox
import subprocess

def install_package():
    package_name = entry.get()
    if package_name:
        try:
            subprocess.check_call(["pip", "install", package_name])
            messagebox.showinfo("Success", f"{package_name} installed successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input required", "Please enter a package name")

root = tk.Tk()
root.title("Pip GUI Installer")

tk.Label(root, text="Enter package name:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

install_button = tk.Button(root, text="Install", command=install_package)
install_button.pack(pady=20)

root.mainloop()
