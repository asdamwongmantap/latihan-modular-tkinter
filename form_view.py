"""Modul tampilan: form sederhana dengan satu input dan satu tombol."""
import tkinter as tk
from tkinter import ttk, messagebox

import validator  # modul validasi input


class FormFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=16)
        self.nama = tk.StringVar()  # terhubung ke isi kolom input

        ttk.Label(self, text="Nama").grid(row=0, column=0, padx=4)
        ttk.Entry(self, textvariable=self.nama).grid(row=0, column=1, padx=4)
        ttk.Button(self, text="Kirim", command=self._on_kirim).grid(row=1, column=0, columnspan=2, pady=8)

    def _on_kirim(self):
        """Dipanggil saat tombol diklik: validasi, lalu munculkan notifikasi."""
        if not validator.nama_valid(self.nama.get()):
            messagebox.showwarning("Peringatan", "Nama tidak boleh kosong.")
            return
        messagebox.showinfo("Notifikasi", f"Halo, {self.nama.get()}!")
