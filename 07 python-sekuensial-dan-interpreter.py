### Aksi Sekuensial
'''Dalam bahasa pemrograman Python, program yang Anda buat akan dijalankan secara sekuensial. 
Apa maksudnya? Kode yang Anda bangun akan berjalan sesuai dengan urutan perintahnya. 
Aksi sekuensial sendiri memiliki makna sebagai sederetan instruksi yang akan dijalankan oleh komputer berdasarkan urutan penulisannya.'''
'''Dengan kata lain, program yang Anda bangun haruslah memiliki awal dan akhir. 
Jadi, ketika program tersebut dijalankan, bisa diketahui waktu berakhirnya. Simak kode di bawah ini untuk melihat implementasinya.'''
c = 3
a = 1
e = 5
b = 2
d = 4

print(a)
print(b)
print(c)
print(d)
print(e,'\n')


### Python Interpreter
'''Kode dari program Python yang Anda bangun akan ditransformasi menjadi kode yang mudah dimengerti oleh mesin menggunakan 
program compiler atau interpreter. Compiler merupakan program yang akan menerjemahkan bahasa pemrograman menjadi bahasa mesin 
sebelum dijalankan dan menghasilkan output. Ini artinya program yang Anda bangun secara keseluruhan akan diubah terlebih dahulu 
semuanya menjadi bahasa mesin.'''

'''Hal berbeda terjadi pada interpreter, yang akan menerjemahkan bahasa Python satu per satu dan menghasilkan output secara langsung. 
Hal ini memungkinkan Anda untuk melihat hasil program segera setelah satu baris kode dieksekusi hingga selesai.'''

## Block Code
'''Sebuah program Python dapat berupa pernyataan atau statement, bisa juga terdiri atas blok kode. 
Sebuah blok merujuk pada potongan kode program Python yang dijalankan sebagai satu unit. 
Kode blok dapat berupa modul, fungsi, kelas, control flow, dan sebagainya.'''

for i in range(10):
    print(i)

'''Anda harus membuat kode yang mudah dimengerti oleh Anda dan orang lain sebagai seorang programmer. 
Selain itu, kode blok yang baik dan benar akan memudahkan interpreter atau compiler untuk berjalan dengan baik dan tidak menghasilkan error. '''

#Error: expected an indented block
# for i in range(10):
# print(i)

## Case-sensitive
'''Python termasuk bahasa pemrograman case-sensitive. Ini artinya Python memperlakukan huruf besar dan kecil sebagai karakter 
yang berbeda dalam penamaan variabel, nama fungsi, atau penulisan kode secara umum.'''

teks = "Dicoding"
Teks = "Indonesia"

print('\n' + teks)
print(Teks)
# Error: "TEks" is not defined
# print(TEks)


### One-liner
'''One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode hanya dalam satu baris. 
One-liner adalah salah satu keunggulan dalam Python yang susah untuk diimplementasikan bagi beberapa bahasa pemrograman lainnya.'''

'''Tujuan dari one-liner ini adalah membuat satu baris kode yang singkat dan jelas. 
Perlu diingat bahwa tidak semua kode blok dapat dijadikan one-liner, seperti deklarasi fungsi, modul, dan kelas. '''

x = 1
y = 2
print('\nx = ',x)
print('y = ', y)

temp = x
x = y
y = temp

print("\nSetelah pertukaran: ")
print("x = ", x)
print("y =",  y)

# kode one-liner
x = 1
y = 2

x, y = y, x    # One-liner

print('\nSetelah pertukaran: ')
print('x =', x)
print('y =', y)

'''Pada kode di atas, Anda seolah-olah menginisialisasikan ulang variabel x dengan nilai variabel y di sebelah kanan. 
Anda juga menginisialisasikan ulang variabel y dengan nilai variabel x yang ada di sebelah kanan. 
Sederhana, bukan? Dengan menginisialisasikan ulang variabel masing-masing, nilai tersebut pada akhirnya bisa saling bertukar.'''

# contoh lain one-liner : Cek Palindrome
phrase = 'kasurrusak'

print(phrase.find(phrase[::-1]))