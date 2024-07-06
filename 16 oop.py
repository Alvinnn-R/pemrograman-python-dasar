### Duck Typing

'''Konsep duck typing tidak berkaitan langsung dengan dynamic typing atau loosely typed, ini merupakan konsep yang lebih erat dengan materi kita kali ini, yaitu pemrograman berorientasi objek (object-oriented programming). Duck typing menjelaskan bahwa sebuah tipe atau class dari sebuah object tidak lebih penting daripada method yang menjadi perilakunya. '''

### Class, Object, dan Method
'''anggaplah kita memiliki mobil sebagai kelas dasar dengan method maju, mundur, berbelok, dan berhenti. Selain itu, kelas dasar mobil memiliki atribut warna dan kecepatan.

Ketika membuat kelas baru, seperti Mobil Sport, kita dapat menggunakan kelas yang sudah ada (mobil sebagai kelas dasar) untuk mewarisi beberapa hal, mulai dari atribut warna, kecepatan hingga beberapa perilakunya, yakni maju, mundur, berbelok, dan berhenti. Namun, kita ingin menambahkan metode baru karena ini adalah mobil sport. Metode baru tersebut adalah turbo yang meningkatkan kecepatan secara signifikan.'''

'''Secara umum, konsep OOP dalam pemrograman sangat mirip seperti ilustrasi-ilustrasi di atas. Object-oriented programming adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atributdan perilaku (method). Objek merupakan perwujudan dari class dengan anggapan bahwa kelas adalah cetakan yang memungkinkan kita dapat membuat banyak objek berdasarkan cetakan tersebut.'''

'''Method adalah perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Sebagaimana halnya maju, mundur, berbelok, dan berhenti pada contoh sebelumnya. Atribut adalah variabel yang menjadi identitas dari objek atau kelas, seperti warna dan kecepatan pada contoh sebelumnya.'''

## Class
'''Pembuatan class dalam Python mirip seperti fungsi, yakni perlu menggunakan keyword untuk bisa membuatnya. Keyword atau kata kunci untuk membuat kelas dalam Python adalah "class".'''

class Mobil:
    
    # atribut
    warna = "Merah"


## Object (Objek)
'''Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek. Berdasarkan KBBI dari kemendikbud, objek merupakan benda, hal, dan sebagainya yang dijadikan sasaran untuk diteliti, diperhatikan, dan sebagainya. Keterkaitan antara objek dan class sangat erat. Contohnya, jika Anda membuat kelas bernama manusia, objeknya adalah manusia dengan nama yang berbeda.'''

'''Anda bisa umpamakan kelas adalah bentuk abstrak dari objek, layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut sebagai instansiasi. Itulah sebabnya objek disebut juga sebagai instance atau instance of the class.'''\

class Mobil:
    # Atribut
    warna = "Merah"
 
mobil_1 = Mobil()

print(mobil_1.warna)
print('\n')

# Mengubah Attribut
mobil_1.warna = "Hijau"

print(mobil_1.warna)

## Atribut
'''Dalam Python, ada dua jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance. Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama.'''

'''Namun, perlu diperhatikan bahwa jenis atribut kelas memiliki kelemahan, yaitu ketika nilai atribut kelas diubah, perubahan tersebut akan memengaruhi semua objek yang dibuat berdasarkan kelas tersebut.'''

class Mobil:
    # Atribut kelas
    warna = "Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

# Mengubah atribut kelas
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)

'''Kelemahan ini akan menjadi masalah jika kita ingin setiap objek memiliki atribut masing-masing yang menjadi ciri khasnya. Sama seperti manusia yang bisa beragam dan mempunyai ciri khas walau dalam satu "blueprint" yang sama.

Jenis atribut yang kedua adalah atribut objek atau atribut instance. Jenis atribut ini memungkinkan setiap instance dari kelas memiliki atribut yang berbeda-beda sesuai dengan keinginan. 

Namun, untuk membuat atribut instance kita perlu menggunakan class constructor.'''

# Class Constructor
'''Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk menentukan nilai awal atau kondisi awal dari suatu kelas. Dengan fungsi ini, saat kita melakukan proses instansiasi atau pembuatan objek baru, hal pertama yang dilakukan adalah memanggilnya terlebih dahulu.'''

class Mobil:
    def __init__(self):
        self.warna = 'Merah'

'''Pada contoh di atas, kita membuat fungsi bernama "__init__" sebagai fungsi khusus untuk menjadi constructor. Selanjutnya, kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.

Ini artinya ketika Anda membuat instance baru bernama "mobil_1", constructor akan dipanggil pertama kali dan self akan merujuk pada instance atau objek "mobil_1" tersebut. Begitu pun kalau kita membuat instance baru lainnya bernama "mobil_2", constructor akan dipanggil pertama kali dan self akan merujuk pada instance "mobil_2". '''

mobil_1 = Mobil()
mobil_2 = Mobil()

print('\n')
print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print('\n')
print(mobil_1.warna)
print(mobil_2.warna)

print('\n')

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
        
mobil_1 = Mobil('Merah', 'DicodingCar', 160)

print(mobil_1.warna)
print(mobil_1.merek)
print(mobil_1.kecepatan)

'''Hal penting yang perlu diketahui adalah perbedaan antara kode di atas dengan kode sebelumnya. Sebelumnya, kode hanya menggunakan parameter "self". Lalu, jika kita menggunakan kode seperti berikut.'''

def __init__(self):
        self.warna = 'Merah'

'''Kode di atas berarti kita langsung menentukan nilai default terhadap suatu objek. Itulah sebabnya ketika proses instansiasi, program tidak memunculkan error walaupun kita tidak memberikan argumen apa pun.

Lain halnya pada kode di bawah ini.'''

class test:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

'''Semua atribut yang telah ditetapkan tidak memiliki nilai default. Ketika membuat sebuah objek dari kelas tersebut, kita perlu menambahkan argumen tambahan seperti yang disebutkan, yaitu warna, merek, kecepatan. Inilah sebabnya ketika proses instansiasi atau pembuatan objek, program akan memunculkan error jika tidak memberikan argumen apa pun'''

print('\n')
test.warna = "hijau"
test.merek = "Honda Civic"
print(test.warna, test.merek)

# Method
'''Setelah atribut, saatnya membahas method sebagai perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Pada pembuatan metode , sebenarnya kita membuat fungsi di dalam kelas itu sendiri. Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode. Python membagi method menjadi tiga jenis.

Metode dari object (object method).
Metode secara statis (static method).
Metode dari class (class method).
Dua metode terakhir sangat erat kaitannya dengan konsep dekorator. Kita tidak akan membahasnya lebih detail mengenai dekorator, tetapi secara umum saja. 

Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal.  Contoh sederhana dekorator sebagai berikut.'''
print('\n')
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()


# Metode dari Objek (Object Method)
'''Jenis pertama adalah method yang melekat terhadap objek. Ciri dari jenis metode ini adalah adanya parameter self yang merujuk pada objek saat ini. Perhatikan contoh di bawah ini, asumsikan bahwa kita membuat kelas mobil yang sama seperti sebelumnya. Namun, kita menambahkan metode bernama "tambah_kecepatan" dan setiap metode ini dipanggil maka kecepatan mobil akan bertambah 10.'''
print('\n')

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)

'''Selain itu, saat kode di bawah ini dieksekusi,

mobil_1.tambah_kecepatan()
ia setara dengan kita melakukan kode berikut.

Mobil.tambah_kecepatan(mobil_1)
Hal inilah yang dimaksud dengan self pada object method karena ketika kita memanggil object method, argumen pertamanya adalah objek dia sendiri (self).

Namun, object method adalah metode yang melekat terhadap suatu objek dan menggunakan parameter self. Jadi, kita tidak bisa memanggil metode ini langsung melalui kelasnya.'''

'''class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

hh = Mobil("Merah", "Civic", 123)
print(hh.kecepatan)
hh.tambah_kecepatan()
print(hh.kecepatan)'''

'''Pada contoh di atas, kita perlu membuat kelas yang sama seperti sebelumnya. Namun kali ini, kita memanggil object method melalui kelasnya secara langsung. Hal ini menyebabkan error karena kita mendefinisikan fungsi tambah_kecepatan sebagai object method. Artinya, metode ini memerlukan parameter self dan merujuk pada objek yang dibuat, sedangkan kita memanggilnya melalui kelas tanpa membuat objek.

Jika ingin membuat metode yang tidak melekat pada objek, kita bisa menggunakan class method atau static method.'''

# Metode secara Statis (Static Method)
'''Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.'''
print('\n')
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("Hei Alvin")
mobil_1.intro_mobil()
print(mobil_1.merek)

# Metode dari Kelas (Class Method)
'''Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas. Mari buat contoh yang sama dengan sebelumnya, tetapi kali ini menggunakan class method.'''
print('\n')

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

'''ketika menggunakan class method, kita akan menambahkan argumen tambahan pada posisi pertama berupa kelas itu sendiri. Perhatikan kode berikut.'''
print('\n')
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

'''Pada contoh kode di atas, fungsi intro_mobil() menggunakan variadic positional parameter, yakni *args untuk melihat argumen yang diterima oleh fungsi tersebut. Perhatikan lebih baik output-nya, kode di atas menerima sebuah parameter, yakni kelas Mobil walaupun ketika pemanggilan fungsi intro_mobil() kita tidak memberikan argumen apa pun.'''