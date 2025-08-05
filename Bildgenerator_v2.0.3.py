###################
## version 2.0.3 ##
###################

import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tempfile
import os


class QRCodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QR-Code Generator für URLs")
        self.geometry("420x560")
        self.qr_image_label = None
        self.qr_image = None
        self.temp_qr_path = None  # Pfad zur temporären Datei
        self.placeholder = "Bitte URL eingeben"
        self.init_ui()

        # Stelle sicher, dass temporäre Datei beim Schließen gelöscht wird
        self.protocol("WM_DELETE_WINDOW", self.cleanup_and_exit)

    def init_ui(self):
        # Eingabefeld
        label = tk.Label(self, text="Gib eine URL ein:", font=("Arial", 12))
        label.pack(pady=(10, 0))

        self.text_input = tk.Entry(self, width=50, fg='grey')
        self.text_input.pack(pady=10)
        self.text_input.insert(0, self.placeholder)
        self.text_input.bind("<FocusIn>", self.clear_placeholder)
        self.text_input.bind("<FocusOut>", self.add_placeholder)

        # QR-Code generieren
        generate_button = tk.Button(self, text="QR-Code generieren", command=self.generate_qr_code)
        generate_button.pack(pady=10)

        # QR-Code Vorschau (leeres Label)
        self.qr_image_label = tk.Label(self)
        self.qr_image_label.pack(pady=10)

        # Speichern
        save_button = tk.Button(self, text="QR-Code speichern", command=self.save_qr_code)
        save_button.pack(pady=10)

    def clear_placeholder(self, event):
        if self.text_input.get() == self.placeholder:
            self.text_input.delete(0, tk.END)
            self.text_input.config(fg='black')

    def add_placeholder(self, event):
        if not self.text_input.get():
            self.text_input.insert(0, self.placeholder)
            self.text_input.config(fg='grey')

    def generate_qr_code(self):
        data = self.text_input.get().strip()

        if data == self.placeholder or not data.startswith(("http://", "https://")):
            self.show_error("Bitte gib eine gültige URL mit http:// oder https:// ein.")
            return

        # Temporären Pfad definieren
        temp_dir = tempfile.gettempdir()
        self.temp_qr_path = os.path.join(temp_dir, "temp_qr_code.png")

        # QR-Code generieren und als Datei speichern
        qr = qrcode.make(data)
        qr.save(self.temp_qr_path)

        # Bild aus Datei laden
        qr_image_pil = Image.open(self.temp_qr_path)
        qr_image_pil = qr_image_pil.resize((300, 300))
        self.qr_image = ImageTk.PhotoImage(qr_image_pil)

        # Im Label anzeigen
        self.qr_image_label.configure(image=self.qr_image)
        self.qr_image_label.image = self.qr_image  # Referenz halten

    def save_qr_code(self):
        data = self.text_input.get().strip()

        if data == self.placeholder or not data.startswith(("http://", "https://")):
            self.show_error("Bitte gib eine gültige URL ein, bevor du speicherst.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[("PNG Dateien", '*.png'), ("Alle Dateien", '*.*')]
        )
        if file_path:
            qr = qrcode.make(data)
            qr.save(file_path)

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Fehler")
        error_window.geometry("300x100")
        tk.Label(error_window, text=message, fg="red").pack(pady=20)
        tk.Button(error_window, text="OK", command=error_window.destroy).pack()

    def cleanup_and_exit(self):
        # Temporäre Datei löschen (falls vorhanden)
        if self.temp_qr_path and os.path.exists(self.temp_qr_path):
            try:
                os.remove(self.temp_qr_path)
            except Exception:
                pass
        self.destroy()


if __name__ == "__main__":
    app = QRCodeGenerator()
    app.mainloop()