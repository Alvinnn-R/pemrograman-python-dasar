# Prosedur
'''
Dalam KBBI, kata prosedur memiliki makna sebagai tahap kegiatan untuk menyelesaikan suatu aktivitas. 
Hal ini sama seperti prosedur sebagai subprogram yang merupakan pengelompokan instruksi-instruksi yang sering dipakai dalam program. 

Berbeda dengan fungsi, prosedur tidak mengharuskan adanya parameter input atau output dan dapat dipandang sebagai fungsi 
yang tidak menghasilkan nilai. Dalam Python, prosedur didefinisikan dengan return tanpa ekspresi atau nilai yang dihasilkan di akhir fungsi.
'''

# def nama_prosedur(param1, param2, ....)
#     Blok kode prosedur
#     Tindakan atau perintah yang ingin dilakukan
#     ...

# Memanggil prosedur
# nama_prosedur(nilai_param1, nilai_param2, ...)
'''Secara konsep, gambar di atas merupakan kerangka dasar prosedur pada Python. \
Sekilas memang sangat mirip dengan fungsi, hanya saja kita tidak mendefinisikan return dan bahkan return value. '''

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
print('\n')

'''Perhatikan bahwa kita tidak mendefinisikan return dan membuat return value. Konsep ini disebut sebagai prosedur, 
yakni fungsi Python yang kita buat tidak mengeluarkan nilai dari fungsi tersebut.

Kita sebenarnya bisa menambahkan pernyataan return, tetapi kita tidak menyertakan return value setelahnya.'''

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
    return
print('\n')

# Contoh 

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Alvin R.S")
print('\n')

def greeting():
    print("Halo Selamat Datang!")

greeting()