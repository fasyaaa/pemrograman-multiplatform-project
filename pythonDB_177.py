import sqlite3 
import tkinter as tk
from tkinter import messagebox 
"import sqlite3, tkinter digunakan untuk memanggil library."

def tambah_data():
    "def tambah_data merupakan fungsi"

    nama = entry_list[0].get()
    "code di atas merupakan sebuah variable untuk memasukan nama yang ingin di data."

    nilai_list = [float(entry.get()) for entry in entry_list[1:]]
    '''code di atas digunakan untuk mengisi nilai dari mata pelajaran yang ada, nilai list bersifat float, dan
    terdapat [1:] digunakan agar variable nama tidak termasuk ke dalam format float dan tetap di text.'''

    prodi_list = ['Kedokteran', 'Teknik', 'Bahasa', 'Matematika', 'Kimia', 'Ekonomi', 'Seni', 'Sejarah', 'Geografi', 'Nuklir']
    "code di atas digunakan untuk mengeluarkan pilihan setelah peng-inputan nilai."

    prediksi = prodi_list[nilai_list.index(max(nilai_list))]
    "code di atas digunakan untuk membuat prediksi berdasarkan list prodi yang tersedia dan list nilai yang sudah di inputkan."

    hasil_prediksi.config(text=f"Prodi Pilihan : {prediksi}")
    "untuk menampilkan prediksi program studi berdasarkan skor tertinggi yang diberikan pengguna pada kolom input"

    conn = sqlite3.connect('percobaan3.db')
    "code di atas digunakan untuk melakukan penyambungan ke sqlite dengan menggunakan nama database percobaan3."

    cursor = conn.cursor()
    "code di atas digunakan untuk membuat objek kursor menggunakan connection"

    cursor.execute('''CREATE TABLE IF NOT EXISTS NilaiSiswa (
                   NamaSiswa TEXT,
                   Biologi REAL,
                   Fisika REAL,
                   Inggris REAL,
                   Matematika REAL,
                   Kimia REAL,
                   Ekonomi REAL,
                   Seni REAL,
                   Sejarah REAL,
                   Geograsi REAL,
                   Nuklir REAL,
                   PrediksiFakultas TEXT
                )''')
    "code di atas digunakan untuk membuat table bernama NilaiSiswa."

    cursor.execute("INSERT INTO NilaiSiswa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (nama, *nilai_list, prediksi))
    "code di atas digunakan untuk menyimpan data ke dalam tabel."

    conn.commit()
    "code di atas untuk melakukan penyimpanan data di dalam sqlite"

    conn.close()
    "code di atas digunakan untuk menutup connection ke sqlite."

    for entry in entry_list:
        entry.delete(0, 'end')
    "code di atas digunakan agar ketika menginputkan data dapat ter-reset menjadi kosong lagi."

    messagebox.showinfo("Info", "Data telah disimpan dengan aman dan baik percayakan saja pada kami!!")
    "code di atas digunakan untuk memunculkan pesan box ketika meng-klik bagian submit."

root = tk.Tk()
root.title("Input Nilai Siswa")
"code di atas digunakan untuk nama program yang di buat."

labels = ['Nama Siswa: ', 'Biologi: ', 'Fisika: ', 'Inggris: ', 'Matematika: ', 'Kimia: ', 'Ekonomi: ', ' Seni: ', 'Sejarah: ', 'Geografi: ', 'Nuklir: ']
entry_list = []
"code di atas digunakan untuk membuat list berdasarkan urutan labels"

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0)
    '''code di atas digunakan unutk membuat label dan entry field sesuai dengan
    teks label yang ada dalam labels sesuai dengan persyaratan pada line 73 dan 74.'''

    entry = tk.Entry(root)
    "code di atas digunakan untuk membuat sebuah widget Entry dari Tkinter yang merupakan kotak input untuk pengguna memasukkan teks atau nilai numerik"

    entry.grid(row=i, column=1)
    "code di atas digunakan untuk menempatkan widget Entry pada jendela utama dengan menggunakan metode grid layout manager."

    entry_list.append(entry)
    '''code di atas digunakan untuk melacak semua objek 'entry' yang dibuat sehingga 
    nilai-nilai yang dimasukkan oleh pengguna ke dalam kotak input ini dapat diakses dengan mudah dari list ini.'''

button_submit = tk.Button(root, text="Submit", command=tambah_data)
"code di atas digunakan untuk menambahkan tommbol 'Submit' pada GUI"

button_submit.grid(row=len(labels), column=0, columnspan=2)
"code di atas digunakan untuk mengatur posisi dari tombol 'Submit' di jendela utama"
"columspan=2 dan column=0 artinya tombol itu akan berbentuk memanjang sepanjang 2 kolom grid"

hasil_prediksi = tk.Label(root, text="", font=("Times new roman", 14))
'''Membuat objek Label yang akan menampilkan teks kosong awalnya (text="") di jendela utama. 
Font yang digunakan adalah 'Times new roman' dengan ukuran 14.'''

hasil_prediksi.grid(row=len(labels) + 1, column=0, columnspan=2)
"Menempatkan label hasil_prediksi dalam tata letak grid pada jendela utama."

root.mainloop()
"perintah untuk menjalankan event loop utama Tkinter yang membuat GUI berjalan dan responsif terhadap interaksi pengguna."