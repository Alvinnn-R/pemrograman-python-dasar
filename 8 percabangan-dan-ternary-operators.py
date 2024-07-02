### Percabangan dan Ternary Operators
'''Control flow adalah sebuah cara untuk memberi tahu program mengenai instruksi yang harus dijalankan dan di mana harus memulai dan berakhir.
Python akan menjalankan kode Anda berdasarkan deretan instruksi yang dibuat secara sekuensial.'''

'''Dalam Python, program dapat berupa blok kode. Python sangat memperhatikan indentasi untuk membangun sebuah blok kode. 
Salah satu blok pemrograman adalah perulangan. Perulangan adalah satu dari beberapa control flow. '''

'''Control flow memungkinkan program untuk berjalan berdasarkan jalur eksekusi. Control flow terbagi menjadi beberapa jenis, 
yakni kondisi tertentu (percabangan), mengulang blok kode secara berulang (perulangan), melewati sebagian kode dan berhenti di kode tertentu, 
hingga mendefinisikan fungsi.'''

## Percabangan
'''Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. 
Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else). '''

'''Hal lain yang perlu diperhatikan adalah Python menganggap setiap nilai kosong (zero) dan null sebagai False. 
Sebaliknya, nilai yang tidak kosong (non-zero) dan tidak null (non-null) akan bernilai True.'''
x = ""

if x:
    print("Ini True")

''' if statement memiliki versi one-liner-nya. Ini memungkinkan Anda untuk membuat kode if dalam bentuk single statement atau satu baris, 
tanpa perlu memperhatikan indentasi dan membuat blok kode.'''

score = 100

if score == 100: print("\nNilai Anda sempurna!\n")

penjual_kfc = "Masih"


if penjual_kfc == "Masih":
    print("Yeay, Makan Ayam KFC\n")
else:
    print("Yah, Ayam KFC Habisss. G jdi makan deh\n")

score = 54

if score >= 85:
    print("Nilai Anda sempurna!")
elif score >= 75:
    print("Nilai Anda Baik")
elif score >= 55:
    print("Nilai Anda Kurang Baik")
else:
    print("Nilai Jelek. Tidak LULUS")

# menambahkan 'and' atau 'or' operator dalam kondisi percabangan

nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")


## Ternary Operators
'''Ternary operators termasuk conditional expressions pada Python. 
Conditional expressions adalah bentuk ekspresi yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya. 
Anda bisa asumsikan bahwa ternary operators ini merupakan versi one-liner dari if dan else. '''

lulus = True
print("selamat") if lulus else print("perbaiki")

# Not ternary
lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")

# Opsi lain dari ternary operators adalah melibatkan tuple.
'''ternary tuples kita menggunakan indeks ke-0 tuples sebagai kode jika kondisi salah, sedangkan indeks ke-1 sebagai kode jika kondisi benar. '''

lulus = True
kelulusan = ("\nPerbaiki, Anda belum lulus.","\nSelamat, Anda lulus!")[lulus]
print(kelulusan)

'''Kode program di atas menampilkan pesan teks "Selamat, Anda lulus!" jika kondisi bernilai true dan menampilkan pesan teks "Perbaiki, Anda belum lulus." 
jika kondisi bernilai false. Jika kita ubah menjadi blok kode IF, berikut penerapannya.'''

lulus = True
if lulus:
    print("\nSelamat, Anda lulus!") 
else:
    print("\nPerbaiki, Anda belum lulus.")