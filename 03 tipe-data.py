### Tipe Data

# Tipe Data Primitif
'''Tipe data primitif merupakan jenis paling dasar dalam pemrograman. 
Tipe data ini menyimpan single value. Berikut adalah berbagai tipe data primitif.'''
# int
# float
# complex
print("Tipe Data Primitif")
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))

# tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah.
'''tipe data primitif atau single-value (numbers, boolean, string) sudah dapat dipastikan adalah immutable secara natural.
(program membuat objek baru dengan nilai baru alih-alih mengubahnya.)'''
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Boolean

x = True
print(type(x))

x = False
print(type(x))

# String

x = 'Alvin'
print(type(x))

'''string Python: dapat menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).'''

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

'''String merupakan urutan karakter yang setiap karakternya memiliki indeks. 
Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing.'''

x = 'Alvin'
print(x[0])

'''Namun tidak dapat mengubah substring di dalamnya. Ini dikarenakan string pada Python bersifat immutable.'''

# x = 'Alvin'
# x[0] = 'F'

'''dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.'''

x = 'Alvin'
print(x[2:])


# Formatted String
name = "Alvin Rama Saputra"
print(f"Hello, nama saya {name}") #“f” di depan string dan menempatkan variabel di dalam kurung kurawal.

# %-formatting
print("Nama saya %s" % (name)) #menggunakan operator Modulo (%) untuk memasukkan nilai variabel ke dalam string dengan menggunakan format khusus yang ditentukan oleh tipe data variabel

# str.format()
print("Nama saya {}".format(name)) #Metode ini memungkinkan penggabungan variabel/nilai ke dalam string dengan menempatkan tanda kurung kurawal atau {} sebagai penempatan variabel.


## Tipe Data Collection
'''Tipe data collection merupakan tipe data yang menyimpan satu atau lebih data primitif sebagai satu kelompok. 
Dalam Python, berikut yang termasuk tipe data collection.'''

## List
'''List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python. 
List dalam Python ini serupa, tetapi tak sama dengan array pada bahasa pemrograman lainnya. 
List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, sedangkan array sebaliknya. '''

x = [1, 2.2, 'Alvin']
print(type(x))
print(x)

x = [1, 'Alvin', True, 1.0]
print(x[2])

'''List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.'''

x = [1, 2.2, 'Alvin', 5]
x[0] = 'Indonesia'
print(x)

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

# slicing 
# sequence[start:stop:step]

# Start merupakan indeks pertama yang Anda ambil. Stop merupakan indeks terakhir yang ingin Anda ambil.
# Step merupakan jumlah elemen yang ingin Anda lewati di antara setiap elemen slice. Secara default, nilai step adalah 1.

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

## Tuple
'''Tuple adalah jenis dari list yang tidak dapat diubah elemennya. 
Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. 
Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.'''

x = (1, "Alvin", 1+3j)
print(type(x))

'''Tuple bersifat immutable yang artinya tidak dapat diubah.'''
# x = (5, 'program', 1+3j)
# x[1] = 'Alvin'

## Set
'''Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan dapat diinisialisasikan dengan kurawal “{}” 
di mana setiap elemennya dipisahkan dengan koma.'''
'''Tidak sama seperti list, dalam set kita tidak bisa melakukan indeksing karena set tidak memiliki indeks. 
Hal ini merujuk pada definisi nya yang menyatakan bahwa set merupakan kumpulan item tanpa urutan. Perhatikan kode di bawah ini.'''

# x = {1,2,7,2,3,13,3}
# print(x[0]) # Error karena set tidak memiliki indeks

'''Selain tanpa urutan (unordered collection). Set juga bersifat unik, artinya, data yang Anda simpan pada set tidak akan ada duplikat.'''
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

'''set adalah himpunan dalam matematika. Ini maknanya Anda dapat melakukan operasi union (gabungan) dan intersection (irisan) pada set. 
Python menyediakan method “.union()” dan “.intersection()” untuk tipe data set.'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

## Dictionary
'''Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. 
Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. 
Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut.

1. Setiap elemen pasangan key-value dipisahkan dengan koma (,).
2. Key dan value dipisahkan dengan titik dua (:).
3. Key dan value dapat berupa tipe variabel/objek apa pun.'''

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(type(x))

'''Dalam mengambil setiap nilai/elemen pada dictionary, Anda harus mengetahui key (kunci) untuk mengakses setiap value-nya (nilai). 
Hal ini berbeda dengan tipe data sebelumnya yang cukup mengharuskan Anda untuk menyebutkan indeksnya saja.'''

# x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
# print(x[0]) menghasilkan error karena Anda mencoba mengakses data pada dictionary dengan menggunakan metode indexing.

d = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
print(d ['name'])

# 1. Menambah Data pada Dictionary
d = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
d ['Job'] = "Web Developer"

print(d)

# 2. Menghapus Data pada Dictionary
d = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del d['isMarried']

print(d)

# 3. Mengubah Data pada Dictionary
d = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
d ['name'] = "Alvin"

print(d)


## Konversi antara Tipe Data
'''konversi antar tipe data dengan menggunakan beberapa fungsi.'''

# Konversi Integer ke Float
print(float(5))

# Konversi Float ke Integer
print(int(5.6))
print(int(-5.6))

# Konversi dari-dan-ke String
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

## Konversi Kumpulan Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

# Konversi ke Dictionary
'''Untuk konversi ke dictionary, data harus memenuhi persyaratan key-value.
Selain itu, Anda bisa melakukan konversi ke dictionary menggunakan fungsi dict().'''

print(dict([[1,2],[3,4]]))

'''Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary.'''
print(dict([(3,26),(4,44)]))


"""
TODO:
Buatlah variabel firstName, lastName, age, isMarried dengan ketentuan:
- firstName: isi dengan nama depan Anda bertipe data string.
- lastName: isi dengan nama belakang Anda bertipe data string.
- age: isi dengan umur Anda bertipe data integer.
- isMarried: isi dengan status pernikahan Anda bertipe data boolean.

Catatan:
- Value variabel harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""
# TODO: Silakan buat kode Anda di bawah ini.
firstName = "Alvin"
lastName = "Saputra"
age = 19
isMarried = False

print(type(firstName))
print(type(lastName))
print(type(age))
print(type(isMarried))

"""
TODO:
Buatlah variabel dictionary dengan nama "data_diri",
variabel tersebut berisi identitas diri Anda berdasarkan ketentuan berikut.
- Memiliki key bernama "firstName":
    - Isi value dengan nama depan Anda, pastikan bertipe data string.
- Memiliki key bernama "lastName":
    - Isi value dengan nama terakhir Anda, pastikan bertipe data string.
- Memiliki key bernama "age":
    - Isi value dengan umur Anda, pastikan bertipe data integer.
- Memiliki key bernama "isMarried":
    - Isi value dengan status pernikahan Anda, pastikan bertipe data boolean.

Catatan:
- Value pada dictionary harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""

# TODO: Silakan buat kode Anda di bawah ini.
data_diri = {
  "firstName": "Alvin",
  "lastName": "Saputra",
  "age": 19,
  "isMarried": False
}

print(data_diri ["age"])