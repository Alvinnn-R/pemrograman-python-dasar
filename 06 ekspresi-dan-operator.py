### Ekspresi

'''Data yang Anda simpan pada suatu variabel umumnya akan dioperasikan untuk menghasilkan suatu nilai sesuai keinginan. 
Masih ingat ekspresi pada matematika? Ekspresi pada matematika adalah kombinasi dari simbol-simbol matematika, seperti angka, variabel, 
operasi matematika, dan sebagainya. Contohnya dibawah ini.'''

# 4x - 7 = 5
'''"4x-7" merupakan ekspresi, sedangkan "4x", "7", dan "5" merupakan suku bilangan. Apabila kita mengingat kembali, 
operasi pada matematika ataupun pemrograman merupakan suatu proses yang dilakukan untuk mendapatkan hasil nilai tertentu.'''

'''Ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan 
fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.
'''

## Penerapan ekspresi pada Python

x = 10
y = 2
result = x - y

print(result)

print('\n')

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

print('\n')

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

print(replikasi)


## Jenis-Jenis Ekspresi

# Ekspresi Menurut Arity dari Operator
'''
Biner
 (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

Uner
 (x += 1), (x-=1), (not x).
'''

'''Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), perkalian (*), 
pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), 
lebih besar dari sama dengan (>=), modulus (%), sama dengan (==), dan tidak sama dengan (!=).

Namun, ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), 
decrement (x-=1), dan negasi (not x).'''

a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

'''Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.'''

print(2+2)
print(3<10)
print(True or False)



## Jenis-Jenis Operator

'''ekspresi dengan beragam jenis, operator pun memiliki berbagai jenis yang dikelompokkan menjadi operator aritmatika, 
operator relational, operator logika, dan operator assignment.'''

# Operator Aritmetika
x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

# Operator Relasional
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Asumsikan x bernilai "Dicoding" dan y bernilai "Indonesia".
'''
Operator	            Deskripsi	                                                                    Contoh
Sama dengan (==)        Menghasilkan True, jika kedua string memiliki nilai yang identik/sama persis.   x == y, menghasilkan False.

Tidak Sama dengan (!=)  Menghasilkan True, jika kedua string memiliki nilai yang tidak sama.            x != y, menghasilkan True.

Lebih Besar dari (>)    Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai 
unicode dengan urutan yang lebih tinggi dibandingkan huruf pertama pada string kedua.                   x > y, menghasilkan False.

Kurang dari (<)         Menghasilkan True, jika huruf pertama pada string pertama memiliki nilai 
unicode dengan urutan yang lebih rendah dibandingkan huruf pertama pada string kedua.                   x < y, menghasilkan True.

Lebih Besar dari Sama dengan (>=) Menghasilkan True, jika huruf pertama pada string pertama memiliki 
nilai unicode dengan urutan yang lebih tinggi atau sama dibandingkan huruf pertama pada string kedua.   x >= y, menghasilkan False.

Kurang dari Sama dengan (<=)    Menghasilkan True, jika huruf pertama pada string pertama memiliki 
nilai unicode dengan urutan yang lebih rendah atau sama dibandingkan huruf pertama pada string kedua.   x <= y, menghasilkan True.
'''

x = "Dicoding"
y = "Indonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

'''Nilai unicode adalah standar internasional yang menetapkan kode numerik untuk setiap karakter dari hampir semua 
sistem tulisan dan simbol-simbol yang digunakan oleh manusia.'''


## Operator Logika
'''Operator AND hanya akan menghasilkan nilai True jika kedua operannya bernilai True. 
Operator OR akan menghasilkan nilai True jika salah satunya bernilai True. Operator NOT hanya akan membalikkan nilai logika; 
jika True, False yang akan dikembalikan, begitupun sebaliknya.'''

print('\n AND')
# Operator AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('\nOR')
# Operator OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('\nNOT')
# Operator NOT
print(not True)
print(not False)


print('\nAssignment')
## Operator Assignment
# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)

print('\n')


"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
diskon = 0.1 * dico
total_harga = dico - diskon
print(total_harga)



# test 1
x = "Belajar" 
y = "Python" 
result = x > y 
print(result) 

# test 2
x = 10 
y = 999 
result = x > y 
print(result)