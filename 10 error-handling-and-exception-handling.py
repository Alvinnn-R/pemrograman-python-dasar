### Penanganan Kesalahan (Error Handling and Exception Handling)

'''Saat Anda membuat program, sering kali menemukan setidaknya dua jenis kesalahan berdasarkan kejadiannya.

- Kesalahan sintaks (syntax errors) atau sering disebut juga sebagai kesalahan penguraian (parsing errors). 
- Pengecualian (exceptions) atau sering disebut juga sebagai kesalahan saat beroperasi (runtime errors). '''

## Kesalahan Sintaks (Syntax Errors)
'''Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda.
Ini mengakibatkan pesan kesalahan muncul sebelum program tersebut berjalan.
Salah satu tipe kesalahan sintaks yang sering ditemui adalah kesalahan indentasi (IndentationError).'''

# IndentationError
# if 9>10:
# print("Hello World!")

"""
Output:
File "/home/glot/main.py", line 2
    print("Hello World!")
    ^
IndentationError: expected an indented block
"""

# SyntaxErrors
# i = 1
# while i<3
#     print("Dicoding")
#     i+=1

"""
Output:
  File "/home/glot/main.py", line 2
    while i<3
             ^
SyntaxError: invalid syntax
"""

## Pengecualian (Exceptions)
'''Pengecualian adalah kesalahan yang terjadi ketika Python mengerti perintah Anda, tetapi mendapatkan masalah saat mengikutinya.
Umumnya, pengecualian bisa terjadi ketika aplikasi sudah mulai beroperasi.'''

# print(angka)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 1, in <module>
    print(angka)
NameError: name 'angka' is not defined
"""

# contoh pengecualian selanjutnya.
# bukan_angka = '1'
# bukan_angka + 2


"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    bukan_angka + 2
TypeError: can only concatenate str (not "int") to str
"""

# Penanganan Pengecualian
'''Lalu, bagaimana menangani kesalahan atau pengecualian tersebut? Program Python yang Anda bangun dapat dilengkapi penanganan terhadap 
pengecualian dari tipe kesalahan yang Anda tentukan. Konsep ini dikenal dengan exceptions handling yang menggunakan 
pernyataan try-except untuk menangani pengecualian tersebut.

Mari lihat jenis pengecualian yang berbeda dari contoh sebelumnya. Kali ini, pengecualiannya adalah kesalahan pembagian angka dengan nol.'''

# z = 0
# print(1/z)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    print(1/z)
ZeroDivisionError: division by zero
"""

# Penerapan try-except
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")


## struktur lengkap pernyataan try.
'''
try:
    # Blok kode Anda yang mungkin terjadi pengecualian.
except:
    # Pernyataan yang dioperasikan jika terjadi pengecualian.
else:
    # Pernyataan yang dioperasikan jika TIDAK terjadi pengecualian.
finally:
    # Pernyataan yang dioperasikan setelah semua pernyataan diatas terjadi.
'''

""" Mari lihat contoh penerapannya di bawah ini, contoh tersebut merupakan program untuk menampilkan key dalam tipe data dictionary. 
Jenis pengecualian yang akan dilakukan adalah KeyError dan TypeError. Kita akan coba untuk mengakses value dictionary dari key yang tidak ada 
dan mencoba mengoperasikan value dictionary tersebut yang termasuk string dengan operasi aritmetika. 
Untuk pengingat, dictionary merupakan tipe data yang melibatkan key-value. """

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

'''Pada contoh di atas, langkah pertama yang dilakukan adalah melakukan inisialisasi variable "var_dict" dengan nilai dictionary. 
Lalu, kita mencoba mengakses value dari key "rata_rata". Program di atas tidak menimbulkan error karena kita memberikan sintaks yang 
benar untuk mengakses value berdasarkan key, yakni var_dict['rata_rata'].'''

"""
Perlu diperhatikan bahwa else statement ikut dieksekusi disebabkan pengecualian tidak terjadi (Error Exception tidak ada). Selain itu, finally statement akan selalu dieksekusi baik jika ada pengecualian ataupun tidak.

Bagaimana membangkitkan KeyError dan TypeError? Perhatikan langkah berikut.

1. Untuk membangkitkan KeyError, ubah kode "print(f"rata-rata adalah {var_dict['rata_rata']}") " 
dengan kode " print(f"rata-rata adalah {var_dict['ratarata']}")  ". Anda bisa langsung copy-paste kode tersebut.

    1. Dengan mengubah kode tersebut, program akan menampilkan KeyError. Hal ini terjadi karena kita mengakses key "ratarata", 
    padahal seharusnya adalah "rata_rata". 
    2. Perhatikan bahwa else statement tidak dieksekusi, karena exception atau pengecualian terjadi. 
    Hal ini dibuktikan dengan tidak adanya teks "Kode ini dieksekusi jika tidak ada exception".

2. Untuk membangkitkan TypeError, ubah kode "print(f"rata-rata adalah {var_dict['rata_rata']}") " 
dengan kode " print(f"rata-rata adalah {var_dict['rata_rata']/2}")  ". Anda bisa langsung copy-paste kode tersebut.

    1. Dengan mengubah kode tersebut, program akan menampilkan TypeError. Hal ini terjadi karena kita melakukan operasi aritmetika
    terhadap value dari key "rata_rata" yang merupakan tipe data string.
    2. Perhatikan bahwa else statement tidak dieksekusi, karena exception atau pengecualian terjadi. 
    Hal ini dibuktikan dengan tidak adanya teks "Kode ini dieksekusi jika tidak ada exception".
"""

## Raise Exception

'''
Jika sebelumnya kita menangani kesalahan yang TIDAK DISENGAJA, kali ini kita akan mempelajari cara menangani kesalahan yang DISENGAJA. Umumnya, ketika membuat kode program kita ingin membatasi program tersebut dengan kondisi tertentu.

Perlu diingat bahwa umumnya, raise digunakan bersamaan dengan if-else statement.

Misalnya, Anda ingin membuat kode program untuk menampilkan angka dari 1 hingga 10 berdasarkan input atau masukan pengguna. 
Namun, dalam program tersebut kita ingin mengontrol dengan cara berikut: jika user memberikan input berupa bilangan negatif, 
program akan memunculkan pesan error dengan keterangan "Bilangan negatif tidak diperbolehkan".
'''

# var = -1
# if var < 0:
#     raise ValueError("Bilangan negatif tidak diperbolehkan")
# else:
#     for i in range(var):
#         print(i+1)

for i in range(1, 3):    
    for j in range(1, 3):    
        print(i,j)

i = 9 
if i<10:    
    print(i)

lulus = True 
print("Dicoding Indonesia") if lulus else print("Python")