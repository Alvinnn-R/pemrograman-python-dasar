### Fundamental Array
'''Python tidak memiliki tipe data array yang sering digunakan dalam bahasa pemrograman lain. 
Sebaliknya, Python memiliki tipe data list yang dapat dikatakan mirip, tetapi tak sama dengan array. 

Perbedaan yang menonjol adalah cara array menyimpan nilai sangat berbeda dengan list. 
Pada array, nilai di dalamnya harus memiliki tipe data yang sama. 
Namun, pada list, nilai di dalamnya tidak harus memiliki tipe data yang sama. 
'''

'''Perlu diketahui oleh Anda, array bukan hanya sebuah tipe data, melainkan salah satu tipe struktur data berjenis linear. 
Array merupakan kata dalam bahasa Inggris yang jika diterjemahkan ke bahasa Indonesia memiliki arti 
"sebuah kelompok besar yang terdiri dari beberapa hal atau orang". 
Arti ini mirip dengan array atau tipe data list dalam Python, sebuah kelompok besar yang terdiri dari beberapa nilai atau data. 
Lalu, apa arti dari struktur data itu sendiri?

Struktur data adalah cara untuk mengatur dan menyimpan data sehingga data-data tersebut dapat diakses dan bekerja secara efisien. 
Dengan adanya struktur data, setiap data yang disimpan memiliki hubungan satu sama lain dan kita dapat beroperasi dengan setiap data tersebut.

Ketika mempelajari materi tipe data pada modul "Berinteraksi dengan Data", sebenarnya Anda telah mempelajari struktur data yang beragam jenisnya.
Baik tipe data primitif maupun tipe data collection yang telah dibahas sebelumnya termasuk jenis struktur data Python.'''

# Dari sini, kita harus bisa menyamakan persepsi bahwa array dan list merupakan hal yang berbeda dalam Python. 
# Kendati demikian, Anda bisa menggunakan list sebagai array dalam Python.

x = [1, 2, 3, 4, 5]
print(x)

"""Jika Anda benar-benar ingin menggunakan array, Anda pun bisa mendeklarasikan array dalam Python dengan menggunakan library atau modul Python.
Salah satunya modul bernama "array". """
print('\n')
import array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

"""Pada kode di atas, kita melakukan impor module array dengan memberikan sintaks "import array". 
Dengan mengimpor module, sekarang kita mempunyai beragam kode baru yang dapat digunakan. 
Contohnya fungsi "array()" yang digunakan untuk membuat array. 

Pada contoh di atas, kita membuat array bertipe integer dengan menyatakan "i" sebelum array. 
Sekarang, coba Anda ubah nilai array "[1, 2, 3, 4, 5]" menjadi "[1, 2, 3, 4, 5, 'Dicoding']". 
Apa yang terjadi? Jika yang terjadi adalah error, hal ini disebabkan karena nilai atau elemen dalam array harus bertipe sama atau identik."""

# List dapat dibagi kembali menjadi struktur data linear dan non-linear. 
'''Struktur data linear adalah jenis struktur data yang elemen-elemen nilai di dalamnya disusun secara berurutan atau linear. 
Sebaliknya, struktur data non-linear merupakan jenis struktur data yang elemen-elemen nilai di dalamnya tidak disusun secara linear.'''

'''Array adalah salah satu jenis dari struktur data linear. Dalam konteks ini, array terdiri dari kumpulan elemen bertipe data 
sama dengan indeks yang berurutan atau linear.'''

"""
Indeks: Posisi atau nomor yang digunakan untuk mengidentifikasi elemen-elemen dalam array. Indeks selalu dimulai dari 0.
Element: Nilai yang berada dalam suatu indeks. Elemen selalu dimulai dari 1. Contohnya jika nilai dari indeks ke-8 adalah "Dicoding",
kita bisa sebut sebagai "elemen ke-9 pada array tersebut adalah Dicoding".
Array length: Panjang dari suatu array. Dalam gambar tersebut, panjang array adalah 10."""

# Contoh
'''"Selepas berakhirnya semester genap, para guru dari SMA Dicoding perlu merekap semua nilai ujian akhir semester. 
Salah satunya adalah guru matematika, guru tersebut perlu merekap nilai dari seluruh siswa yang ada di kelas IPA 1. 
Guru tersebut membuat program menggunakan Python untuk mempermudah proses rekap nilai."'''
print('\n')

nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

print(nama_siswa1)
print(nama_siswa2)
print(nama_siswa3)
print(nama_siswa4)
print(nama_siswa5)
print(nama_siswa6)
print(nama_siswa7)
print(nama_siswa8)
print(nama_siswa9)
print(nama_siswa10)

print('\n')
# menggunakan list dalam kasus diatas
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])