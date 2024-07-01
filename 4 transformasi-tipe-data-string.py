### Transformasi Angka, Karakter, dan String

## Mengubah Huruf Besar/Kecil
'''alam kategori ini terdapat beberapa metode yang dapat digunakan untuk mengubah string menjadi huruf kapital (UPPERCASE) 
atau huruf kecil (lowercase). Kedua metode ini, baik upper() maupun lower() adalah metode bawaan dari string Python.'''

# upper()
kata = 'dicoding'
kata = kata.upper()
print(kata)

# lower()
kata = 'DICODING'
kata = kata.lower()
print(kata)


## Awalan dan Akhiran
'''Kategori ini adalah metode dalam string yang biasanya dipergunakan untuk menghapus karakter whitespace pada suatu string. 
Namun, selain whitespace bisa juga diperuntukkan untuk menghilangkan kata yang tidak diinginkan.'''

# rstrip()
'''Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string.'''
print("Dicoding          ".rstrip())

# lstrip()
'''Kebalikan dari rstrip(), lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string.'''
print("           Dicoding".lstrip())

# strip()
'''Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string.'''
print("         Dicoding          ".strip())


kata = 'CodeCodeKevinCodeCode'
print(kata.strip("Code"))
'''Anda dapat mengganti whitespace dengan kata atau hal lainnya. 
Caranya adalah memberikan nilai pada ".strip()". Kode di atas menghapus kata "Code" pada variabel "kata".'''

# startswith()
'''Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.'''
print('Dicoding Indonesia'.startswith('Dicoding'))

# endswith()
'''Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string. Metode ini juga mengembalikan nilai True jika menemukannya,
sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.'''
print('Dicoding Indonesia'.endswith('Dicoding'))


## Memisah dan Menggabung String

# join()
print(' '.join(['Dicoding','Indonesia', '!']))
'''sintaks awal sebelum ".join()" terdapat single quotes di sana. 
Single quotes ini bermaksud untuk menentukan delimiter pada setiap kata/nilai yang ingin di gabungkan. 
Pada kode di atas, delimiter-nya adalah whitespace atau spasi.'''

print('123'.join(['Dicoding','Indonesia']))

# split()
'''Kebalikan dari metode sebelumnya, metode split() bertujuan untuk memisahkan kata/substring berdasarkan delimiter.'''
print('Dicoding Indonesia !'.split())

# delimiter newline (\n) untuk memisahkan setiap baris pada string multiline.
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))


## Mengganti Elemen String

# replace()
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))


## Pengecekan String

# isupper()
'''isupper() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase). 
Sebaliknya, jika ada satu huruf saja yang kecil/tidak uppercase, nilai False akan dikembalikan.'''
kata = 'DICODING'
print('\n',kata.isupper())

# islower()
'''Kebalikannya, islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase).'''
kata = 'dicoding'
print('\n',kata.islower())

# isalpha()
'''Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet.
Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan.'''
kata = 'dicoding'
print('\n',kata.isalpha())

# isalnum()
'''Metode isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, 
yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.'''
kata = 'dicoding123'
print('\n',kata.isalnum())

# isdecimal()
'''Metode isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik.
Jika tidak, nilai False akan dikembalikan.'''
print('123'.isdecimal())

# isspace()
'''Metode isspace() akan mengembalikan nilai True jika string hanya berisi whitespace, 
seperti spasi, tab, newline, atau karakter whitespace lainnya.'''
print('         '.isspace())

# istitle()
'''Metode istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. 
Jika tidak, nilai False dikembalikan.'''
print('Dicoding Indonesia'.istitle())


## Formatting pada String
'''Kategori terakhir yang akan kita bahas pada modul kali ini adalah formatting pada string. 
Dalam kategori ini terdapat beberapa metode, yaitu zfill(), rjust(), ljust(), center(), dll.'''

# zfill()
'''Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu.
Tujuan dari metode ini adalah membantu untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap, 
terutama ketika ingin menyimpan nilai dalam format yang konsisten.'''
teks = 'Code'
tambah_number = teks.zfill(5)
print('\n',tambah_number)

'''Metode zfill() ini berguna ketika ingin memastikan bahwa angka atau nilai dalam string memiliki panjang tetap 
dan sesuai dengan format yang diinginkan. Metode zfill() dapat diterapkan untuk menetapkan nomor nota atau nomor antrian.'''

# rjust()
'''Metode rjust() berguna untuk merapikan pencetakan teks. 
Dengan metode rjust() ini, Anda dapat membuat teks menjadi rata kanan sehingga tampilannya lebih rapi.'''
print('Dicoding'.rjust(20))

'''Angka 20 yang Anda masukkan bersifat sama seperti pada zfill(). 
Metode rjust() akan memastikan bahwa panjang teksnya adalah 20 termasuk dengan kata "Dicoding".

Anda bisa menambahkan teks lain, tidak hanya whitespace.'''
print('Dicoding'.rjust(20, '!'))

# ljust()
'''Selanjutnya adalah metode ljust(), metode ini adalah kebalikan dari metode rjust() yang bertujuan untuk membuat teks menjadi rata kiri.'''
print('Dicoding'.ljust(20))

# center()
'''Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default.
Anda juga bisa mengganti whitespace tersebut dengan karakter lain.'''
print('Dicoding'.center(10, '-'))


## String Literals
'''Umumnya, string ditulis dengan mudah di Python, diapit oleh tanda petik tunggal. 
Namun, dalam kondisi tertentu, dibutuhkan petik tunggal di tengah string (misalnya, struktur kepemilikan dalam bahasa Inggris—Amerika's 
Cat atau penyebutan Jum'at pada hari dalam bahasa Indonesia).'''
# st1 = 'Jum'at'
st1 = "Jum'at"
st1 = 'Jum\'at'

'''Python mengetahui bahwa pada Jum\'at, sebelum petik terdapat backslash (\) yang menandakan petik tunggal sebagai bagian dari string dan bukan akhir dari string. Escape character \' dan \" memungkinkan Anda untuk memasukkan karakter ' dan '' dalam bagian string. Beberapa contoh escape character lainnya sebagai berikut. 

\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash'''

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")


## Raw String
'''Python juga menyediakan cara untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan. Metode ini dinamakan raw strings'''
print(r'Dicoding\tIndonesia') 
'''Perhatikan bahwa escape character (\t) ikut tercetak pada teks tersebut. 
Hal ini karena raw string akan mencetak string sesuai dengan apa pun input atau teks yang diberikan.'''