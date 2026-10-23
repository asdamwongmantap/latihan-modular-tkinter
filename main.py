"""Entry point aplikasi: hanya merakit modul, tanpa logika sendiri."""
import tkinter as tk

from form_view import FormFrame


def main():
    root = tk.Tk()                   # jendela utama
    root.title("Form Data Diri")
    root.resizable(False, False)     # ukuran jendela dikunci
    FormFrame(root).pack()           # pasang form ke jendela
    root.mainloop()                  # jalankan event loop (aplikasi tetap terbuka)


# Blok ini hanya jalan jika file dieksekusi langsung (python3 main.py),
# bukan saat di-import dari file lain
if __name__ == "__main__":
    main()
