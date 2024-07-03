### Implementasi Array dengan Python

## Implementasi Array dengan Python
'''
Pada materi sebelumnya, sudah disebutkan bahwa dalam Python kita dapat mendeklarasikan array menggunakan dua cara. 
Pertama dengan memanfaatkan list dan kedua menggunakan library Python.

Perlu Anda ingat, setiap elemen yang ada pada list sebetulnya disimpan pada satu memori. 
Jika list adalah "[1, 2, 3]", sebetulnya Anda memerintahkan memori komputer untuk menyimpan integer "1" ke dalam satu tempat memori, 
begitu pun integer "2" akan disimpan dalam satu tempat memori, dan seterusnya.
'''

var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

print('\n')

'''Ketika Anda menjalankan kode di atas, ia akan menghasilkan lokasi memori setiap elemen yang berada pada list. 
Lokasi tersebut bisa berubah jika Anda menjalankan ulang program,
 tetapi perhatikan bahwa semua elemen tersebut memiliki ID lokasi penyimpanan yang berbeda.

Sekarang mari lebih detailkan cara deklarasi array dalam Python menggunakan list. 
Ada dua cara untuk melakukan deklarasi array menggunakan list, yakni berikut.'''

# Mendefinisikan Isi Array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

# Mendefinisikan Nilai Default
'''Jika tidak mengetahui nilai yang diberikan, kita dapat memberikan nilai default terlebih dahulu sebagai upaya untuk memberikan nilai awal.
Umumnya, nilai default ini ditentukan karena kita tidak tahu nilai seharusnya. '''

'''Dalam prosesnya, kita bisa secara perlahan mengganti masing-masing nilai tersebut sesuai kebutuhan. 
Misal kita memiliki array "[0,0,0,0]", yang kemudian hari kita bisa memperbaruinya menjadi "[1,2,0,4]", 
dengan begitu kita bisa mengetahui bahwa indeks ke-2 pada array tersebut belum kita perbarui. 

Nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan yang nilainya di luar dari rentang yang disepakati. 
Misalnya, tim Anda menentukan nilai dalam list harus berkisar dari 1 hingga 10. 
Kita bisa menyepakati "0" sebagai nilai default karena di luar jangkauan yang disepakati (1-10).'''

# <nama-var> = [<default-var> for in range(<n>)]
"""
Berikut adalah penjelasan lebih detail terkait struktur tersebut.

<nama-var> merupakan variabel yang Anda deklarasikan.
<default-val> merupakan nilai default yang Anda definisikan. Umumnya, programmer akan menggunakan nilai di luar range yang telah disepakati 
sebagai nilai default. Misalnya jika range nilai yang disepakati seharusnya 1 hingga 10, nilai default bisa kita definisikan dengan 0. 
<n> merupakan ukuran panjangnya array."""
print('\n')

# Contoh
var_arr = [0 for i in range(10)]
print(var_arr)

# Dari sini, Anda dapat mengubah nilai default tersebut dengan nilai yang baru berdasarkan hasil suatu operasi. Misalkan pada contoh di bawah ini.
print('\n')

for i in range(10):
    var_arr[i] = i

print(var_arr)


## Mengakses Elemen Array
'''Mengakses elemen array dalam Python tidak berbeda dengan mengakses elemen pada list. 
Hal ini karena kita menggunakan list sebagai "bentuk lain" dari array. Anda dapat melakukan metode indexing untuk mengakses elemen array. 
Berikut adalah struktur untuk melakukan hal tersebut.'''

# <namaVariabelArray> [<indeks>]
print('\n')

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])



### Pemrosesan Sekuensial pada Array
"""Pemrosesan array merujuk kepada operasi-operasi yang dilakukan pada elemen-elemen suatu array. 
Operasi ini melibatkan manipulasi hingga pengolahan elemen yang ada pada array. 

Adapun pemrosesan sekuensial adalah sebuah pemrosesan setiap elemen array yang dimulai dari elemen pada indeks terkecil hingga terbesar.
Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya."""

'''
Sebab pemrosesan sekuensial melibatkan semua elemen di dalamnya, ada beberapa hal yang perlu diperhatikan.

Setiap elemen array diakses secara langsung melalui indeksnya (metode indexing).
Elemen pertama (first element) adalah elemen array dengan indeks terkecil yang selalu dimulai dari 0. 
Elemen selanjutnya (next element) dicapai melalui suksesor indeks.
Kondisi berhenti dicapai jika indeks yang diproses adalah indeks terbesar yang sudah terdefinisi.
Suatu array tidak boleh kosong, minimal memiliki satu elemen di dalamnya.
'''

var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")


"""
Pertama-tama, kita menginisialisasi variabel "var_arr" dengan nilai "[1, 2, 3, 4, 5]". 
Perulangan for digunakan untuk melakukan iterasi melalui setiap elemen array. 
Variabel "i" bertindak sebagai indeks saat ini yang digunakan untuk mengakses elemen dalam setiap iterasi atau perulangan.

Kemudian, setiap proses perulangan berlangsung, kita mengambil elemen saat ini menggunakan "var_arr[i]" dan menyimpannya 
pada variabel "current_element". Selanjutnya adalah mencari indeks berikutnya dengan cara menambahkan nilai "1" pada indeks saat ini atau "i". 

Hasil dari operasi penjumlahan nilai "1" dengan indeks saat ini akan disimpan pada variabel "next_index". 
"next_index" berperan sebagai "suksesor indeks" yang merujuk pada indeks berikutnya berdasarkan indeks saat ini dengan menambahkan nilai "1". 

Kemudian kita memeriksa "next_index" berada dalam rentang indeks yang valid dalam array atau tidak. 
Jika iya, artinya masih ada elemen berikutnya, dan kita ambil elemen berikutnya tersebut menggunakan "var_arr[next_index]" 
serta menyimpannya dalam variabel "next_element". Sebaliknya, jika "next_index" tidak valid atau melebihi rentang array, 
artinya tidak ada elemen berikutnya sehingga kita menetapkan "next_element" sebagai "None".

Pada langkah terakhir, kita mencetak nilai "current_element" dan "next_element" untuk menunjukkan perbedaan 
antara elemen sekarang dan selanjutnya.

Mencetak setiap elemen array menggunakan perulangan adalah satu di antara banyaknya contoh-contoh persoalan pemrosesan sekuensial pada array. 
Contoh lain dari pemrosesan array adalah berikut.

Mengisi array secara sekuensial.
Menghitung nilai rata-rata elemen array.
Mengalikan elemen array dengan suatu nilai.
Mencari nilai terbesar atau terkecil pada array.
Mencari indeks letak suatu nilai ditemukan pertama kali dalam array, dan sebagainya.

"""


# Latihan Array
# Mencari nilai terbesar dalam array
print('\n')

var_arr = [1, 7, 2, 89, 3]
print(var_arr[0])
left_pointer = var_arr[0]

for i in range(0, len(var_arr)):
    right_pointer = var_arr[i]
    print(right_pointer)
    
    if(right_pointer > left_pointer):
        left_pointer = right_pointer
        print('perbandingan:',left_pointer)

print('Nilai terbesar: ', left_pointer)


"""Pada program di atas, hal pertama yang dilakukan adalah menginisialisasi variabel "var_arr" dengan array "[1, 7, 2, 89, 3]". 
Kedua, kita menginisialisasi variabel "left_pointer" dengan nilainya adalah indeks pertama variabel "var_arr" (var_arr[0]).  

Kita menggunakan perulangan "for" untuk mengakses semua indeks dari indeks ke-1 hingga panjang array. Untuk mengetahui panjang array, 
kita menggunakan fungsi "len()", yang  bertujuan menghitung panjang atau banyaknya elemen dari list, set, dan string. 

Dalam perulangan "for" tersebut kita mendeklarasikan variabel "right_pointer" yang akan terus berpindah dari indeks ke-1 
hingga indeks terakhir (akhir panjang array). Setelah memiliki "left_pointer" dan "right_pointer", kita membandingkan nilai keduanya. 
Jika "right_pointer" lebih besar dari "left_pointer", kita akan memperbarui nilai "left_pointer" dengan nilai "right_pointer".

Proses tersebut terjadi secara berulang sampai nilai yang tersimpan dalam "left_pointer" dijadikan sebagai nilai maksimal dari array. 
Lalu, kita mencetak nilai tersebut dengan perintah "print(left_pointer)"."""



"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""

# TODO: Silakan buat kode Anda di bawah ini.
print('\n')
# Jangan ubah kode ini
var_array = [i for i in range(101)]
total_nilai = var_array[0]
result = 0
# total_nilai = [0]
print(len(var_array))

for i in range(len(var_array)):
      total_nilai += var_array[i]
      if var_array[i] >= len(var_array) - 1:
          result = total_nilai / var_array[i]
          print(total_nilai)
          print(var_array[i])

print(result)


# Done

total_nilai = var_array[0]

for i in range(len(var_array)):
      total_nilai += var_array[i]
      if var_array[i] >= len(var_array) - 1:
          result = total_nilai / len(var_array)

print(result)

# Menggunakan konsep One Liner
result = sum(var_array)/ len(var_array)

print(result)