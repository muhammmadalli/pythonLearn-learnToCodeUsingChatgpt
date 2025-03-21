import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading

def install_package():
    package_name = entry.get().strip()
    
    if not package_name:
        messagebox.showwarning("Input required", "Please enter a package name")
        return
    
    output_text.insert(tk.END, f"Installing {package_name}...\n")
    output_text.yview(tk.END)  # Auto-scroll to the latest output

    def run_install():
        try:
            process = subprocess.Popen(
                ["pip", "install", package_name, "--timeout", "100"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            for line in process.stdout:
                output_text.insert(tk.END, line)
                output_text.yview(tk.END)

            process.wait()

            if process.returncode == 0:
                messagebox.showinfo("Success", f"{package_name} installed successfully")
            else:
                error_message = process.stderr.read()
                output_text.insert(tk.END, f"\nError: {error_message}\n")
                messagebox.showerror("Error", f"Failed to install {package_name}")

        except Exception as e:
            messagebox.showerror("Exception", str(e))
    
    threading.Thread(target=run_install, daemon=True).start()


def show_installed_packages():
    output_text.insert(tk.END, "\nFetching installed packages...\n")
    output_text.yview(tk.END)

    def run_list():
        try:
            process = subprocess.Popen(
                ["pip", "list", "--format=freeze"],  # Get package names only
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            output_text.insert(tk.END, "Installed Packages:\n")
            for line in process.stdout:
                if "==" in line:
                    package_name = line.split("==")[0]  # Extract package name only
                    output_text.insert(tk.END, f"{package_name}\n")
                    output_text.yview(tk.END)

        except Exception as e:
            output_text.insert(tk.END, f"\nError: {str(e)}\n")
            messagebox.showerror("Exception", str(e))

    threading.Thread(target=run_list, daemon=True).start()


# GUI Setup
root = tk.Tk()
root.title("Pip GUI Installer")
root.geometry("500x450")

tk.Label(root, text="Enter package name:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

install_button = tk.Button(root, text="Install", command=install_package)
install_button.pack(pady=5)

show_packages_button = tk.Button(root, text="Show Installed Packages", command=show_installed_packages)
show_packages_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, height=15, width=60, wrap=tk.WORD)
output_text.pack(padx=10, pady=5)

root.mainloop()
