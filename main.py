import tkinter as tk
from tkinter import ttk, messagebox

# =====================================
#      APLIKASI KASIR SUPERMARKET
# =====================================

class Produk:

    def __init__(self, nama, harga, jumlah):

        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def total(self):

        return self.harga * self.jumlah


# ===============================
# DATA
# ===============================

keranjang = []

nomor_transaksi = 1


# ===============================
# FUNGSI
# ===============================

def tampil_data():

    tree.delete(*tree.get_children())

    total = 0

    jumlah = 0

    for i, barang in enumerate(keranjang, start=1):

        tree.insert(
            "",
            tk.END,
            values=(
                i,
                barang.nama,
                barang.harga,
                barang.jumlah,
                barang.total()
            )
        )

        total += barang.total()

        jumlah += barang.jumlah

    labelJumlah.config(
        text=f"Jumlah Barang : {jumlah}"
    )

    labelTotal.config(
        text=f"Total Belanja : Rp {total:,}"
    )

    if total >= 1000000:

        diskon = total * 0.15

    elif total >= 500000:

        diskon = total * 0.10

    elif total >= 200000:

        diskon = total * 0.05

    else:

        diskon = 0

    labelDiskon.config(
        text=f"Diskon : Rp {int(diskon):,}"
    )


def tambah_barang():

    nama = entryNama.get()

    if nama == "":

        messagebox.showwarning(
            "Peringatan",
            "Nama barang kosong!"
        )

        return

    try:

        harga = int(entryHarga.get())

        jumlah = int(entryJumlah.get())

    except:

        messagebox.showerror(
            "Error",
            "Harga dan jumlah harus angka!"
        )

        return

    barang = Produk(
        nama,
        harga,
        jumlah
    )

    keranjang.append(barang)

    entryNama.delete(0, tk.END)

    entryHarga.delete(0, tk.END)

    entryJumlah.delete(0, tk.END)

    tampil_data()

# ===============================
# PILIH DATA
# ===============================
def pilih_barang(event):

    data = tree.focus()

    if data == "":
        return

    isi = tree.item(data)

    baris = isi["values"]

    if len(baris) == 0:
        return

    entryNama.delete(0, tk.END)
    entryHarga.delete(0, tk.END)
    entryJumlah.delete(0, tk.END)

    entryNama.insert(0, baris[1])
    entryHarga.insert(0, baris[2])
    entryJumlah.insert(0, baris[3])

# ===============================
# EDIT BARANG
# ===============================
def edit_barang():

    data = tree.focus()

    if data == "":
        messagebox.showwarning(
            "Peringatan",
            "Pilih barang terlebih dahulu!"
        )
        return

    index = tree.index(data)

    try:

        keranjang[index].nama = entryNama.get()
        keranjang[index].harga = int(entryHarga.get())
        keranjang[index].jumlah = int(entryJumlah.get())

    except:

        messagebox.showerror(
            "Error",
            "Input salah!"
        )
        return

    tampil_data()
    
    # ===============================
# HAPUS BARANG
# ===============================
def hapus_barang():

    data = tree.focus()

    if data == "":
        messagebox.showwarning(
            "Peringatan",
            "Pilih barang!"
        )
        return

    index = tree.index(data)

    del keranjang[index]

    tampil_data()

    entryNama.delete(0, tk.END)
    entryHarga.delete(0, tk.END)
    entryJumlah.delete(0, tk.END)
    
    

# ===============================
# WINDOW
# ===============================

root = tk.Tk()

root.title("Aplikasi Kasir Supermarket")

root.geometry("1000x650")

root.resizable(False, False)

judul = tk.Label(
    root,
    text="APLIKASI KASIR SUPERMARKET",
    font=("Arial",18,"bold")
)

judul.pack(pady=10)

frame = tk.Frame(root)

frame.pack()

tk.Label(frame,text="Nama Barang").grid(row=0,column=0,padx=5,pady=5)

entryNama = tk.Entry(frame,width=30)

entryNama.grid(row=0,column=1)

tk.Label(frame,text="Harga").grid(row=1,column=0)

entryHarga = tk.Entry(frame,width=30)

entryHarga.grid(row=1,column=1)

tk.Label(frame,text="Jumlah").grid(row=2,column=0)

entryJumlah = tk.Entry(frame,width=30)

entryJumlah.grid(row=2,column=1)

tk.Button(
    frame,
    text="Tambah Barang",
    command=tambah_barang,
    width=20
).grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10
)

tk.Button(
    frame,
    text="Edit Barang",
    width=20,
    command=edit_barang
).grid(
    row=4,
    column=0,
    pady=5
)

tk.Button(
    frame,
    text="Hapus Barang",
    width=20,
    command=hapus_barang
).grid(
    row=4,
    column=1,
    pady=5
)

kolom = (
    "No",
    "Nama",
    "Harga",
    "Jumlah",
    "Total"
)

tree = ttk.Treeview(
    root,
    columns=kolom,
    show="headings",
    height=15
)

for item in kolom:

    tree.heading(item,text=item)

    tree.column(item,width=180)

tree.pack(pady=10)

tree.bind(
    "<<TreeviewSelect>>",
    pilih_barang
)

labelTotal = tk.Label(
    root,
    text="Total Belanja : Rp 0",
    font=("Arial",12,"bold")
)

labelTotal.pack()

labelDiskon = tk.Label(
    root,
    text="Diskon : Rp 0"
)

labelDiskon.pack()

labelJumlah = tk.Label(
    root,
    text="Jumlah Barang : 0"
)

labelJumlah.pack()

root.mainloop()
