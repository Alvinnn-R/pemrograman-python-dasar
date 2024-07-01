### Operasi pada List, Set, dan String
'''Dalam modul ini, Anda akan belajar mengenai contoh-contoh operasi pada list, set ,dan string.
Banyak fungsi dalam Python yang dapat digunakan untuk melakukan operasi pada list, set, dan string.'''

# len()
'''Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.
Khusus pada string, program akan menghitung jumlah karakternya.'''
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

'''mengonversi list menjadi set terlebih dahulu. Hal ini menyebabkan anggota list berubah menjadi anggota set yang tidak memiliki duplikat.'''
contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

# min() dan max()
'''Selain menghitung panjang atau banyaknya elemen, 
Anda juga dapat mengetahui berapa nilai minimum dan maksimum dari suatu list menggunakan fungsi min() dan max().'''

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

# Count
'''Fungsi count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.'''
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

'''program akan menghitung banyaknya substring/huruf "a" dalam string.'''
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# In dan Not In
'''In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list. 
Anda bisa menggunakan operator ini untuk memastikan suatu nilai ada dalam list bahkan dalam string. 
Operator in dan not in akan mengembalikan nilai boolean True atau False.'''

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

print('\n')
## Memberikan Nilai untuk Multiple Variable
'''Dalam list atau tuple, terkadang Anda perlu memberikan nilai pada variabel-variabel tersebut.
Secara konvensional, Anda bisa melakukan hal tersebut dengan menandai indeks yang diinginkan dan memberikan nilai satu per satu sesuai keinginan.'''

data = ['Alvin', 'Rama', 'S']
apparel = data[0]
color = data[1]
size = data[2]

print(data)
print(apparel)
print(color)
print(size)

'''Dalam kode di atas, Anda mengakses indeks pertama pada variabel "data" yang merupakan list, 
lalu menyimpannya pada variabel baru bernama "apparel". Lalu, berlaku seterusnya, 
Anda mengakses indeks kedua serta ketiga dan menyimpannya pada variabel baru, masing-masing bernama "color" dan "size".'''

data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# Sort
'''fungsi sort() untuk mengurutkan angka atau urutan huruf.'''
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

# membalikkan urutan
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

'''Pada kode di atas, mengurutkan variabel "kendaraan" secara descending atau menurun. 
Hal ini membuktikan bahwa secara default fungsi sort() akan mengurutkan secara ascending atau menaik.'''
# urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
# urutan.sort()

# print(urutan)

'''Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).'''
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)

'''ASCII (American Standard Code for Information Interchange) table merupakan sebuah kode karakter yang memetakan set karakter 
yang umum digunakan ke dalam angka. Sederhananya, tabel ini menampilkan karakter-karakter ASCII beserta nilai angka yang mewakilinya.
Metode sort() mengurutkan berdasarkan angka pada ASCII ini.'''

'''Untuk mengatasi masalah ini, Anda dapat memasukkan keyword "str.lower" pada parameter metode sort(). 
Jadi, sort() akan menganggap semua objek menggunakan huruf kecil, tanpa mengubah kondisi asli dari objek tersebut.'''

kendaraan.sort(key=str.lower)

print(kendaraan)