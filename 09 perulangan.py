### Perulangan
'''Dalam pemrograman, kita juga akan sering menemui masalah serupa yang mengharuskan untuk melakukan kode berulang. 
Contohnya menampilkan angka 1 hingga 10.'''

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
'''Pada kode di atas, program menampilkan angka dari 1 hingga 10 menggunakan sintaks yang berulang. 
Terlihat tidak efektif, bukan? Itulah yang menjadi tujuan dari materi perulangan ini, 
Anda akan belajar untuk membuat kode program yang efektif dan mudah dibaca oleh programmer lain.'''

print('\n')
## For
'''For termasuk sintaks dalam Python yang bersifat definite iteration. 
Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.'''

var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

'''ita melakukan perulangan untuk menampilkan angka dari 1 hingga 10 yang sebelumnya telah diinisialisasikan pada variabel "var_list". 
Setiap iterasi atau perulangan yang berjalan, "i" akan mengambil elemen dari "var_list" satu per satu. 
Lalu, blok kode "print(i)" akan dijalankan dengan nilai "i" adalah nilai yang sudah diambil sebelumnya.'''
print('\n')
# melakukan perulangan berdasarkan panjang suatu nilai dengan menggunakan fungsi "range()".
for i in range(10):
    print(i)

# range(start, stop, step)
'''
penjelasan detail terkait fungsi "range()".

"Start" merupakan nilai awal dari urutan bilangan yang bersifat opsional, jika Anda tidak memasukkannya, nilai awal akan dianggap 0. 
"Stop" merupakan nilai batas yang wajib dimasukkan. Urutan akan berhenti sebelum mencapai nilai "stop" (eksklusif). 
"Step" merupakan nilai penambahan antara setiap dua bilangan dalam urutan yang bersifat opsional. Jika nilai tersebut tidak diberikan, 
secara default nilai yang dimasukkan adalah 1.'''
print('\n')
for i in range(1,10,2):
    print(i)


## While
'''While termasuk sintaks dalam Python yang bersifat indefinite iteration. 
Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.'''
print('\n')
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

'''Namun, Anda harus berhati-hati untuk tidak melakukan infinite loop, yakni sebuah kondisi ketika perulangan tidak berhenti 
karena tidak memenuhi kondisi yang diinginkan. Contohnya adalah ketika melakukan perulangan, kita tidak memberikan increment yang menyebabkan 
variabel atau counter tidak akan memenuhi kondisi while.'''
print('\n')
# counter = 1
# while counter <= 5:
#     print(counter)


## For Bersarang (nested loop. )
'''Anda dapat asumsikan bahwa ada dua perulangan, yakni "perulangan luar" dan "perulangan dalam". 
Program akan melakukan "perulangan luar" terlebih dahulu, lalu akan melakukan "perulangan dalam". 
"variabel_luar" akan mengambil nilai dari "iterable_luar", sedangkan "variabel_dalam" akan mengambil nilai dari "iterable_dalam".'''
print('\n')
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

'''melakukan perulangan for luar dengan variabel "i" yang mengulang dari 1 hingga 2. 
Lalu melakukan perulangan "j" yang akan mengulang dari 1 hingga 2 juga.  '''


## Kontrol Perulangan

# Break
'''Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, 
lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya.'''
print('\n')
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1
print('\n')
# contoh lain
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))


# Continue
'''Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. 
Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.'''
print('\n')
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

'''Namun, alih-alih ada spasi maka program akan berhenti, program akan mengabaikan spasi tersebut dan melanjutkannya pada perulangan selanjutnya.'''


## Else setelah For
'''Pada Python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian. 
Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.'''
print('\n')
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 5:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

'''Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali saja benar. 
Dengan kata lain, break dalam if harus tidak terjadi untuk memicu else setelah for.'''

## Else setelah While
'''Berbeda dengan else setelah for, pada statement else setelah while, 
blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah. '''
print('\n')

count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

'''Pada contoh di atas, perulangan while akan terus terjadi dan else tidak akan dieksekusi jika kondisi while benar. 
Kondisi while akan terus benar pada kode di atas ketika variabel "count" bertambah dari 1 hingga 2 
dan akan berhenti ketika variabel "count" bernilai 3 karena "3<3" adalah false atau salah.'''
print('\n')

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

'''else tidak tercetak di sini. Hal ini disebabkan while tersebut masih bernilai benar walaupun program keluar karena "break". '''


## Pass
'''Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), 
tetapi tidak ada tindakan atau program tidak melakukan apa pun.'''
print('\n')

x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

'''Statement pass digunakan dalam situasi-situasi ketika Python memerlukan adanya pernyataan, tetapi tidak memiliki tindakan yang perlu dilakukan
pada saat itu. Biasanya itu adalah kondisi ketika Anda membutuhkan placeholder untuk menunjukkan bahwa tidak ada operasi yang perlu dilakukan. 
Hal ini dapat membantu kita mengatur struktur kode secara rapi dan memungkinkan penambahan implementasi di kemudian hari.'''


## List Comprehension
'''Masih terkait perulangan, terkadang ada kalanya Anda perlu membuat sebuah list baru berdasarkan list yang sudah ada.'''
print('\n')

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

'''Pada contoh di atas, kita mencoba melakukan operasi perpangkatan dari variabel list "angka". 
Hasil dari operasi tersebut kemudian disimpan pada variabel baru bernama "pangkat". 
Anda menggunakan fungsi ".append()" untuk menambahkan nilai baru ke dalam variabel "pangkat".'''
print('\n')

# Anda dapat melakukan hal berikut.
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

'''Pada kode di atas, kita melakukan perulangan dengan memasukkan operasi perulangan tersebut ke dalam inisialisasi variabel "pangkat". 
Hal ini memudahkan kita sehingga tidak perlu menggunakan fungsi ".append()" untuk menambahkan nilai baru.'''

'''Konsep ini disebut sebagai list comprehension, sebuah cara untuk menghasilkan list baru berdasarkan list atau iterables yang telah ada 
sebelumnya. Sintaks dasarnya adalah berikut.'''

# new_list[expresion for_loop_one_or_more_conditions]

'''
new_list merupakan variabel yang dideklarasikan oleh Anda.
expression merupakan ekspresi yang akan dijalankan seiring perulangan bernilai benar.
for_loop_one_or_more_conditions merupakan perulangan for yang Anda definisikan. Misalnya "for n in angka" yang ada pada contoh sebelumnya.'''


"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.
evenNumber = []
for i in range(0,501): 
  if(i%2 == 0):
  	evenNumber.append(i)

print(evenNumber)

# Atau

evenNumber = [i for i in range(0,501) if(i%2 == 0)]
    
print(evenNumber)