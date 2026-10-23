"""Modul validasi: tidak tahu apa-apa soal tampilan."""


def nama_valid(nama):
    """True jika nama tidak kosong (spasi saja dianggap kosong)."""
    return bool(nama.strip())
