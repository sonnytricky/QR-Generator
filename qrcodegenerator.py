#################
## version=1.0 ##
#################

import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

class QRCodeGenerator(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("QR-Code Generator")
    self.geometry("405x450")
    self.qr_image_label = None
    self.init_ui()

  def init_ui(self):
    self.text_input = tk.Entry(self, width=50)
    self.text_input.pack(pady=20)
    self.text_input.bind("<Return>", self.generate_qr_code)

    generate_button = tk.Button(self, text="Generieren", 
                                command=self.generate_qr_code)
    generate_button.pack(pady=10)

    save_button = tk.Button(self, text="Speichern", 
                            command=self.save_qr_code)
    save_button.pack(pady=10)

  def generate_qr_code(self, event=None):
    qr_data = self.text_input.get()
    qr = qrcode.make(qr_data)
    qr = qr.resize((300, 300))

    self.qr_image = ImageTk.PhotoImage(qr)
    if self.qr_image_label is None:
      self.qr_image_label = tk.Label(self, image=self.qr_image)
      self.qr_image_label.pack(pady=20)
    else:
      self.qr_image_label.configure(image=self.qr_image)
 
  def save_qr_code(self):
    file_path = filedialog.asksaveasfilename(
      defaultextension='.png',
      filetypes=[
        ("PNG files", '*.png'), 
        ("All files", '*.*')
      ])
    if file_path:
      qr_data = self.text_input.get()
      qr = qrcode.make(qr_data)
      qr.save(file_path)

if __name__ == "__main__":
  app = QRCodeGenerator()
  app.mainloop()