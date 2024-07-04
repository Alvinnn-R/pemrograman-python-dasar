### Definisi Subprogram
'''Sejauh ini, Anda telah membuat program yang beragam. Setiap program yang Anda bangun, pada akhirnya akan semakin besar seiring dengan 
kompleksitas masalah yang perlu diselesaikan. Semakin besar sebuah program, bagian kode yang berulang akan bertambah sehingga tidak efisien 
jika Anda perlu mengetik ulang atau bahkan melakukan copy-paste. Salah satu kode yang sering berulang adalah rumus atau formula'''

# Luas pertama
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

'''Perhatikan bahwa kita perlu menuliskan dua rumus kode yang sama untuk mencari luas persegi panjang dengan nilai panjang dan lebar berbeda.'''

# subprogram dan salah satu jenisnya adalah fungsi
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)
print('\n')

'''Kode di atas merupakan program yang sama dengan sebelumnya dan bertujuan untuk mencari luas persegi panjang. 
Namun, kali ini kita menggunakan sebuah konsep yang disebut fungsi. Blok fungsi pada kode di atas dimulai dari "def" hingga "return".

Ini adalah tujuan akhir dari materi kali ini, Anda diharapkan memahami subprogram yang di antaranya adalah fungsi dan prosedur.'''

"""
Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. 
Hasil atau output tersebut dinyatakan dalam sebuah tipe data yang eksplisit. 
Artinya, fungsi yang dibuat dapat ditentukan untuk mengembalikan tipe data integer, string, atau lainnya.

Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state).
Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas.
"""

## Fungsi
# Fungsi dalam Matematika
'''Fungsi dalam pemrograman sebenarnya didasari oleh konsep pemetaan (asosiasi) dan fungsi dalam matematika. 
Fungsi pada matematika merupakan pemetaan antara dua himpunan nilai, yaitu domain dan range. 
Kita bisa bayangkan fungsi sebagai sebuah mesin yang memiliki input (domain) dan output (range). 
Output tersebut pasti terkait dengan input bagaimana pun kondisinya.'''

# contoh
'''
f(x) = 2.x

catatan sebagai berikut.

f = nama fungsi
x = input
2x = apa yang harus dikeluarkan (output)

mengalikan bilangan bulat dengan nilai 2, setiap elemen yang berada pada himpunan domain akan dikalikan dua 
dan hasilnya ditampung pada himpunan range. 

Notasi f(x)=2x menunjukkan bahwa fungsi "f" mengambil "x" dan mengalikannya dengan 2.

f(x) = 2.x
f(4) = 2.4 = 8
'''

## Fungsi dalam Pemrograman
'''
Fungsi dalam pemrograman didasari oleh fungsi dalam matematika. Jadi, baik fungsi pemrograman maupun fungsi matematika memiliki tujuan yang sama,
 yaitu mengubah suatu bentuk menjadi bentuk lain dengan aturan yang sama. 

 Keadaan Awal -> Fungsi -> Keadaan Akhir
Selayaknya black box, kita tidak perlu tahu tentang hal yang terjadi dalam kotak (fungsi) tersebut. 
Kita hanya perlu fokus pada keadaan awal yang merupakan himpunan nilai yang terdefinisi sebagai input (domain) dan keadaan akhir
yang merupakan himpunan nilai yang terdefinisi sebagai output (range).

'''

print('Hello World!!\n')

'''Contohnya pada gambar di atas, kita hanya perlu memasukkan teks "Hello World!" tanpa tahu proses fungsi di dalamnya.
Fungsi tersebut akan menghasilkan output dengan memunculkan teks "Hello World!" ke layar. 

fungsi dalam pemrograman adalah blok kode yang dapat digunakan kembali untuk mengeksekusi fungsionalitas tertentu saat dipanggil. 
Dalam Python, fungsi terbagi menjadi dua jenis.'''

# Built-in Functions
'''Built-in functions atau dalam bahasa Indonesia berarti fungsi bawaan adalah kumpulan fungsi yang sudah terintegrasi 
dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan. Fungsi bawaan ini menyediakan 
fungsi-fungsi inti dan dasar dari bahasa Python. Contoh dari fungsi bawaan adalah print(), len(), type(), range(), dan sebagainya.'''

# User-defined Functions
'''User-defined functions atau dalam bahasa Indonesia berarti fungsi yang didefinisikan pengguna adalah jenis fungsi 
yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. 
Contoh dari user-defined functions adalah fungsi yang telah kita buat di awal materi ini tentang mencari luas persegi panjang.'''

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print('\n', persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

'''
Library dalam Python terdiri dari dua jenis.

Python Standard Library
Python Standard Library adalah jenis library yang telah terpasang secara otomatis ketika Anda melakukan instalasi Python. 
Python Standard Library berisi kumpulan modul dan paket yang disertakan secara default oleh Python. 
Paket (package) merupakan sebuah direktori berisi satu atau lebih modul yang terkait dan saling berhubungan.

Anda tidak perlu melakukan instalasi untuk menggunakan Python Standard Library. 
Contoh Python Standard Library adalah "os", "datetime", "re", dan sebagainya. 

External Library
Jika sebelumnya impor library tidak perlu dilakukan untuk Python Standard, 
berbeda halnya dengan external library yang mengharuskan Anda mengimpor library untuk bisa menggunakannya. 
External Library adalah jenis library yang dikembangkan oleh individu atau organisasi di luar tim inti pengembang Python.

Sederhananya, di luar sana banyak developer yang turut membuat kode untuk diri mereka sendiri dan pada akhirnya disebarluaskan 
untuk digunakan oleh developer lainnya. Contoh dari external library adalah TensorFlow yang merupakan library populer 
untuk menyelesaikan permasalahan pemelajaran mesin (machine learning). 
'''

## Kegunaan Fungsi 
'''
- Program dapat dipecah menjadi bagian yang lebih kecil (sub).
- Penggunaan ulang kode alih-alih menulis ulang kode
- Setiap fungsi bersifat independen dan dapat diuji secara terpisah.
'''

print('\n')
## Membuat dan Memanggil Fungsi
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

mencari_luas_persegi_panjang(10,5)   # Ini adalah pemanggil fungsi
print(persegi_panjang_pertama)

# Docstring
'''
Untuk membuat fungsi lebih mudah dipahami oleh programmer lain, kita bisa membuat dokumentasi berupa docstring.
Docstring adalah akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat.
Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.
'''
print('\n')

def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)


## Argumen dan Parameter
'''parameter seperti black box yang akan menampung nilai dan nilai tersebut adalah argumen.'''

def fungsiku(a,b,c):
    # Function Body
    print(a,b,c)

'''Ketika Anda membuat fungsi di atas, a, b, c merupakan parameter. 
Namun pada saat Anda memanggilnya, nilai 1, b=50,  c='Alvin' menjadi argumen.'''

testfungsiku = fungsiku(1, b=50, c="Alvin")
print(testfungsiku)

print('\n')
# Argumen

# Keyword Argument
'''Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan. 
Ketika nama parameter dalam sebuah argumen secara langsung disebutkan, artinya kita menggunakan keyword argument.
'''

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)

'''Kelebihan dari jenis argumen ini adalah walaupun kita harus menuliskan lebih banyak kata, urutan parameter fungsi tidak perlu dipikirkan.'''

# Positional Argument
'''Kebalikan dari keyword adalah positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit. 
Ketika memanggil fungsi, Anda hanya harus memasukkan nilai yang ingin diberikan. 
Namun, Anda harus mengikuti urutan dari parameter fungsi tersebut.'''
print('\n')
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama)


# Parameter
# Positional-or-Keyword
'''Jenis ini merupakan parameter default dalam Python. 
Dengan jenis ini, kita dapat menggunakan positional maupun keyword argument ketika memanggil fungsi.'''
print('\n')
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))


# Positional-Only
'''Parameter ini hanya dapat dimanfaatkan dengan menggunakan jenis argumen posisi saat pemanggilan fungsi. 
Parameter ini ditentukan menggunakan sintaks "/".'''
print('\n')
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))

'''
Pada contoh di atas, kita memanggil fungsi yang telah didefinisikan menggunakan positional argument. Perhatikan juga bahwa kita mendefinisikan parameter fungsi dengan sintaks "/".

Silakan ganti kode pemanggil fungsi dengan kode berikut untuk mengetahui hal yang terjadi jika kita menggunakan keyword argument.
print(penjumlahan(a=3, b=5)) #eror
'''

# Keyword-Only
'''Jenis ketiga adalah kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis parameter ini.
Ia ditentukan dengan sintaks "*" (asterisk).'''
print('\n')
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))

'''
kita menggunakan keyword argument untuk memanggil fungsi yang telah dibuat. 
Perhatikan bahwa kita menggunakan sintaks "*" untuk mendefinisikan bahwa parameter fungsi ini hanya bisa dipanggil menggunakan keyword argument.

Silakan ganti baris pemanggil kode dengan kode di bawah ini untuk mengetahui hal yang terjadi jika kita menggunakan positional argument.

print(greeting("Selamat sore!","Dicoding")) #Error '''

print('\n')
# Var-Positional (Variadic Positional Parameter)
'''Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi.
Parameter ini ditentukan dengan menggunakan sintaks *args'''

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

'''
Pada contoh di atas, parameter *args mengumpulkan semua argumen posisi yang diberikan saat pemanggilan fungsi dan membungkusnya 
menjadi tuple "args". Dalam situasi ini, Anda bisa memasukkan angka sebanyak apa pun dalam argumen fungsi.

Silakan tambahkan integer lainnya sebanyak yang Anda mau pada kode pemanggil fungsi di atas untuk mengetahui perbedaannya. 
Contohnya Anda bisa memasukan kode berikut.
'''
print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))

# Var-Keyword (Variadic Keyword Parameter)
'''Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. 
Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). 
Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.'''
print('\n')
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

'''
Pada contoh di atas, parameter **kwargs akan mengumpulkan semua pasangan key-value yang diberikan sebagai keyword argument. 
Dalam situasi ini, Anda bisa menambahkan parameter dan argumen sejumlah yang diinginkan.

Silakan tambahkan keyword argument tambahan pada saat pemanggilan fungsi, seperti alamat, tempat tanggal lahir, dan sebagainya. 
Contohnya Anda bisa memasukan kode berikut.
'''
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer", tempat_lahir="Bandung", lulusan="ITB"))


## Fungsi Anonim (Lambda Expression)
'''Terakhir, mari kita pelajari cara membuat fungsi tanpa mendeklarasikan def. 
Cara ini dikenal dengan ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya. 
Anda bisa mengasumsikan fungsi anonim ini sebagai fungsi one-liner. Secara umum, struktur fungsi anonim sebagai berikut.'''

#  func = lambda args: ret_val
'''Nama fungsi (func) setara dengan nama variabel yang digunakan untuk menyimpan ekspresi lambda,
args adalah argumen yang dibutuhkan untuk dioperasikan, dan ret_val merupakan nilai yang kita kembalikan (return).'''

# Contoh
print('\n')
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

'''Pada contoh kode di atas, kita membuat fungsi dengan nama "mencari_luas_persegi_panjang" yang menjadi nama variabel. 
Argumen yang digunakan adalah panjang dan lebar, kita mendefinisikan ini tepat setelah pernyataan lambda. 
Lalu, kita menambahkan isi fungsi, yaitu panjang*lebar dan hasilnya merupakan return value. 
Terakhir, pemanggilan pada fungsi anonim sama seperti biasanya.

Isi fungsi dalam lambda dapat Anda ganti menjadi sebuah nilai, alih-alih variabel. 
Hal ini karena umumnya bertujuan untuk melakukan operasi sederhana dan perlu melibatkan fungsi 
yang tidak terlalu kompleks hingga perlu menggunakan def.

Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun, tetapi hanya mengembalikan satu nilai ekspresi. 
Dalam contoh di atas, Anda bisa menambahkan argumen selain panjang dan lebar, tetapi hanya bisa menggunakan satu operasi, yaitu panjang*lebar.'''
print('\n')

## Variabel Global dan Lokal
'''Dalam Python, ada konsep "scope" yang mengatur jangkauan variabel dan fungsi dalam suatu program. 
Konsep ini lebih dikenal sebagai scope variable yang mengacu pada wilayah di dalam program tempat variabel dapat diakses dan digunakan.'''

# dua jenis scope yang umum dijumpai

# Variabel Global
'''Suatu variabel yang didefinisikan di luar fungsi atau blok kode apa pun dan dapat diakses dari seluruh bagian program.'''

a = 10

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)
print('\n')

# Variabel Lokal
'''Variabel ini didefinisikan dalam suatu fungsi atau blok kode tertentu. 
Jenis ini hanya dapat diakses dari dalam fungsi atau blok kode tempat variabel tersebut didefinisikan.'''

def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)
print('\n')

# print(lokal_var)

## Menulis Modul pada Python
'''setiap file berekstensi .py dapat direferensikan sebagai modul, Anda bisa melakukan impor file dari satu file ke yang lainnya. 
Layaknya ketika Anda menggunakan library, modul, dan sebagainya.'''

# saya sudah membuat sebuah file bernama main.py berisi fungsi yang ingin kita impor.
from main import mencari_luas_persegi_panjang1, nama
# import main

# test = main.mencari_luas_persegi_panjang1(10,2)
# print(test)

print(mencari_luas_persegi_panjang1(5,5))

print(nama)
print('\n')
"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.
def minimal(a,b):
  return b if b < a else a
test = minimal(5, 6)
print(test)

print('\n')
# Atau

def minimal(a,b):
  return a if a <= b else b

test = minimal(5, 5)
print(test)

