### Style Guide pada Python

## Pengecekan Style Guide PEP8

# Lint
'''Lint adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), termasuk dalam proses ini adalah mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8. Aplikasi yang digunakan untuk proses ini disebut linter.

Integrasi linter dengan editor kode Anda akan membuat efisien dalam menulis kode Python. Pertimbangan ini karena keluaran atau output dari aplikasi linter hanya berupa teks singkat berupa keterangan dan kode Error atau Warning atau Kesalahan Konvensi Penamaan (Naming Conventions).

Lint atau linting akan meminimalkan kode Anda mengalami error, salah satu contohnya karena kesalahan indentasi di Python. Sebelum kode Anda diproses oleh interpreter Python dengan IndentationError, lint akan memberitahukannya lebih dahulu ke Anda.'''

# Tiga jenis aplikasi linter
"""
1. Pycodestyle (sebelumnya bernama pep8)
2. Pylint
3. Flake8
"""


### Memformat Kode
'''ika proses lint atau linting hanya melakukan pengecekan, kali ini adalah arahan gaya penulisan kode agar bisa sesuai dengan PEP8. Kita akan kembali menggunakan beberapa aplikasi yang nantinya akan diinstal. 

Proses memformat kode akan sama dengan cara melakukan proses linting, yaitu kita akan mengeksekusi script. Perbedaannya adalah output yang dihasilkan. Jika proses linting menghasilkan pesan dengan menunjukkan baris dan kode yang mengalami kesalahan, proses memformat kode akan memberikan pesan berupa kode yang telah diperbaiki. Ini artinya Anda tidak perlu mengubah kode secara manual.'''

# Tiga jenis aplikasi untuk memformat kode
"""
1. black
2. YAPF (Yet Another Python Formatter)
3. autopep8
"""


### Style Guide Statement Gabungan
'''Setelah mengetahui aplikasi untuk pengecekan dan memformat kode, kali ini kita akan belajar cara membuat kode yang baik dan benar. Perhatikan bahwa materi ini akan menunjukkan sintaks yang disarankan dan tidak disarankan.'''

## Penjalasan atau Contoh Kode Yang Disarankan 

# Statement Gabungan
'''Saat Anda membuat program dengan banyak statement, usahakan untuk tidak menggabungkan >1 statement pada baris yang sama.'''

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

'''Anda diperbolehkan untuk membuat sebuah konten/isi dari if/for/while yang cukup pendek untuk diletakkan dalam satu baris (program tetap berjalan). Namun, pastikan tidak melakukannya jika if/for/while Anda bertingkat atau bersifat multi clause, misalnya if-else, try-finally, dan sebagainya.'''

## Sangat tidak disarankan seperti ini.

if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()
try: something()
finally: cleanup()
do_one(); do_two(); do_three(long, argument,
                             list, like, this)
if foo == 'blah': one(); two(); three()


## Penggunaan Trailing Commas

'''Koma di bagian akhir (trailing commas) umumnya bersifat opsional, satu statement yang bersifat wajib adalah saat kita membuat variabel menggunakan tipe tuple dengan satu elemen. Hal ini umumnya diperjelas dengan kurung untuk menghindari penghapusan atau pembersihan.
'''

# Disarankan seperti ini.
FILES = ('setup.cfg',)

# Disarankan seperti ini.
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

## Anotasi Fungsi
'''Anotasi fungsi adalah fitur yang memungkinkan kita untuk menambahkan informasi tambahan tentang parameter dan return value dari sebuah fungsi. Jika sebelumnya kita belajar menambahkan informasi terkait fungsi dengan menambahkan docstring, anotasi fungsi lebih spesifik untuk menjelaskan parameter dan return value.

Penggunaan anotasi fungsi sebaiknya menggunakan aturan baku untuk titik dua (:) dan menggunakan spasi untuk penggunaan arah panah atau arrow (->). Hal ini disebut sebagai type hints yang merujuk pada PEP 484.'''

# Perhatikan penggunaan spasi dari kedua kode berikut.
 
# Yes:
def munge(input: str):  # Menambahkan informasi parameter bertipe string
    pass
def munge() -> str:   # Menambahkan informasi return value bertipe string
    pass
 
# No:
def munge(input:str):  # Menambahkan informasi parameter bertipe string
    pass
def munge()->str:   # Menambahkan informasi return value bertipe string
    pass


# Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
# No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas

'''Mari kita simpulkan sedikit. Jika kita membuat fungsi yang menggabungkan anotasi dengan nilai parameter, sebaiknya tetap menggunakan spasi sebelum dan sesudah tanda sama dengan (=). Namun, ketika membuat fungsi biasa tanpa adanya anotasi, sebaiknya tidak menggunakan spasi sebelum dan sesudah tanda sama dengan (=).'''

# Yes:
def LuasPersegiPanjang(panjang:int = 2, lebar=None):
    pass
 
# No:
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass



### Style Guide Prinsip Penamaan pada Python
'''Saat membuat variabel, fungsi, hingga kelas, Anda dapat memberikan nama-nama yang beragam. Terkadang, keberagaman tersebut menghasilkan tidak adanya standar dalam kode yang Anda bangun.'''

## Prinsip Overriding

'''Nama yang dilihat oleh user publik sebaiknya merefleksikan penggunaan/fungsinya dan bukan implementasinya. Misalnya nama fungsi berikut.'''
cariJalan()

'''Itu akan lebih mudah dipahami dibanding berikut.'''
jalan()

## Penamaan Deskriptif
'''Penamaan deskriptif adalah cara untuk memberikan nama yang informatif, jelas, dan sesuai dengan tujuan dari elemen kode. Penamaan deskriptif ini meliputi variabel, fungsi, kelas, hingga konstanta.'''

"""
Berikut adalah beberapa cara penamaan yang umum.

Satu karakter huruf kecil: b
Satu karakter huruf besar: B
Huruf kecil: hurufkecil
Huruf kecil dengan pemisah kata garis bawah: huruf_kecil_dengan_pemisah_kata_garis_bawah
Huruf Besar: HURUFBESAR
Huruf Besar dengan pemisah garis bawah: HURUF_BESAR_DENGAN_PEMISAH_GARIS_BAWAH
Huruf Besar di Awal Kata (CapWords, CamelCase): HurufBesarDiAwalKata (pastikan semua singkatan/akronim dituliskan dengan huruf besar, misalnya HTTPServerError, bukan HttpServerError)
Huruf Campuran: hurufCampuran (mirip dengan CapWords, hanya berbeda di karakter paling awal)
Huruf Besar di Awal Kata dengan Garis Bawah: Huruf_Besar_Di_Awal_Kata_Dengan_Garis_Bawah
"""


### Hal-hal yang Harus Dipertimbangkan dalam Penamaan
'''Sebelumnya kita membahas detail terkait penamaan sebuah fungsi, method, kelas, hingga hal yang tidak dianjurkan dalam penamaannya. Pembahasan selanjutnya adalah petunjuk untuk mempertimbangkan nama yang tepat. Sekali lagi, penamaan di sini merujuk ke banyak hal, seperti penamaan variabel, fungsi, hingga kelas.'''

## Nama yang Dihindari
'''Hindari karakter l (huruf L kecil), O (huruf o besar), atau I (huruf i besar) sebagai nama variabel satu karakter karena mereka sulit dibedakan dengan angka satu dan nol. Daripada menggunakan l (huruf l kecil), menggunakan L besar akan sangat membantu.'''

## ASCII Compatibility
'''Merujuk pada PEP 3131,  suatu identifiers yang digunakan dalam Python Standard Library harus kompatibel dengan kode ASCII. ASCII adalah sebuah kode karakter yang memetakan set karakter dan umum digunakan dalam angka. Sederhananya, ASCII memetakan karakter-karakter beserta angka yang mewakilinya.

Identifiers merujuk pada nama-nama yang digunakan untuk menyebut variabel, fungsi, kelas, dan kode lainnya dalam Python. Contoh identifiers adalah nama variabel "x", nama fungsi "penjumlahan()", atau nama method "get_nama()".'''

## Nama Paket dan Nama Modul
'''Masih ingat dengan modul dan package (paket) dalam Python? Modul pada Python adalah file yang berisi kode Python, seperti fungsi, kelas, dan sebagainya. Ketika Anda membuat script atau file Python, hal itu bisa dianggap sebagai modul. Di sisi lain, paket adalah sebuah direktori yang berisi satu atau lebih modul yang terkait dan saling berhubungan.

Penamaan modul sebaiknya pendek atau singkat, menggunakan huruf kecil, dan opsional garis bawah (_) untuk meningkatkan keterbacaan. Contohnya '__init__.py' atau modul 'math_operations.py' dengan seluruh kode di dalamnya merupakan fungsi, kelas, method yang berhubungan dengan operasi matematika, seperti penjumlahan, pengurangan, dan sebagainya.

Nama paket juga sebaiknya singkat, menggunakan huruf kecil, dan hindari garis bawah(_). Contohnya, jika kita membuat paket bernama "math" yang di dalamnya ada modul 'math_operations.py", pengguna akan memahami bahwa paketnya bernama math yang memiliki banyak modul, seperti salah satunya operasi matematika.'''

## Nama Kelas
'''Saat menamai kelas, gunakan CamelCase atau CapWords. Pastikan semua akronim (misal HTTP) ditulis keseluruhan dengan huruf besar.'''

## Penulisan Tipe Variabel
'''Untuk penamaan variabel, umumnya menggunakan CamelCase atau CapWords, lebih pendek lebih baik.

T, AnyStr, Num'''

## Nama Exception
'''Untuk pengecualian (exception), Anda juga menerapkan konvensi penamaan kelas pada exception karena ia seharusnya bertipe kelas. Bedanya, tambahkan "Error" atau nama deskriptif lain pada nama exception Anda. Contoh kodenya sebagai berikut.'''

class DivideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)

def divide_numbers(a, b):
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
except DivideByZeroError as e:
    print(f"Error: {e}")

## Nama Variabel Global
'''Dalam variabel global, penamaannya bisa mengikuti fungsi/modul yang bersifat publik. Anda bisa menggunakan garis bawah untuk menghindari variabel tersebut diimpor jika ia termasuk modul non-publik.'''

## Nama Fungsi, Parameter, dan Variabel
'''Nama fungsi, parameter, dan variabel sebaiknya menggunakan huruf kecil dengan pemisahan menggunakan garis bawah untuk meningkatkan keterbacaan. mixedCase dapat digunakan jika ada dependensi dengan pustaka menggunakan style tertentu.'''

## Argumen Fungsi dan Method
'''Dalam pembuatan fungsi dan method pada suatu kelas, ada beberapa hal yang perlu dipertimbangkan.

Gunakan self sebagai argumen pertama jika Anda membuat instance method.
Gunakan cls sebagai argumen pertama ketika Anda membuat class method.
Jika nama argumen fungsi adalah reserved keyword, tambahkan garis bawah di akhir nama argumen. Jangan mengorbankan keterbacaan nama dengan menyingkatnya. Mengganti argumen bernama class dengan class_ atau kelas, lebih baik daripada clss.'''

## Nama Method dan Variabel Instance
'''Saat membuat method dan variabel dalam suatu kelas, gunakan standar penamaan fungsi, yaitu gunakan huruf kecil dengan pemisah kata garis bawah untuk meningkatkan keterbacaan. Tambahkan garis bawah sebagai awalan untuk method non-publik dan variabel internal pada fungsi.

Untuk menghindari kesamaan dengan subkelas, gunakan __dimulai_dua_garis_nama_method untuk memanggil proses yang tepat. Python menggabungkan nama modul dengan nama kelas. Misal ada suatu kelas bernama Foo, jika kelas Foo memiliki atribut __a, kita tidak dapat mengaksesnya melalui Foo.__a, tetapi Foo._Foo__a. Mulai dengan dua garis bawah hanya digunakan jika terjadi konflik dengan atribut di kelas atau subkelas lainnya.'''

## Konstanta
'''Dalam memberikan nama variabel bertipe konstanta, umumnya didefinisikan pada bagian atas modul dengan huruf besar semuanya, misalnya 'PI = 3,14'  atau  'TOTAL = 4.14213'.'''

## Selalu Persiapkan untuk Inheritance
'''Saat membangun metode dan variabel dalam sebuah kelas, sebaiknya Anda dapat langsung mengetahui atribut pada metode dan variabel tersebut, entah publik atau non-publik. Jika Anda ragu, jadikan atributnya non-publik. Sebab, lebih mudah menjadikan sebuah variabel/method bersifat non-publik menjadi publik, dibandingkan sebaliknya.

Variabel atau method bersifat non-publik adalah suatu variabel atau method yang hanya digunakan untuk lingkup tertentu dan tidak diakses secara langsung di luar. Contohnya berikut.'''

class MyClass:
    def __init__(self):
        self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

    def _private_method(self):
        print("Ini adalah method non publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non publik

'''
Saat mendeklarasikan variabel/method tersebut, ikuti panduan Pythonic berikut.

Atribut publik tidak menggunakan awalan garis bawah.
Jika nama sebuah method/variabel publik sama dengan reserved keyword, tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf.
Pada data publik yang bersifat simpel, hindari nama yang terlalu panjang. Cukup dengan nama atribut sependek mungkin. Ingatlah bahwa pada masa depan Anda akan mungkin mengembangkan skema atau data ini sehingga nama sependek apa pun mungkin akan menguntungkan Anda.
Jika Anda berniat untuk mewariskan atau membuat subclass dari kelas dan menginginkan sebuah variabel hanya digunakan di kelas utama saja, tambahkan awalan dua garis bawah. Ini akan memudahkan Anda karena Python mengenalinya sebagai konvensi kelas, untuk menghindari kemungkinan kesamaan nama atau implementasi.
'''