### Implementasi Matriks pada Python
'''elemen matriks dideklarasikan memiliki tipe homogen, yang artinya elemen tersebut harus memiliki tipe data yang sama. 
Jika Anda mendeklarasikan suatu elemen bertipe data float, elemen lainnya pun adalah float.'''

## Deklarasi Matriks

# Deklarasi sekaligus inisialisasi nilai matriks
'''Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan nilainya dengan ukuran N baris dan M Kolom (NxM).
Cara ini dilakukan jika kita telah mengetahui nilai yang perlu diberikan.'''

matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
     
print(matriks)

print('\n')
# Deklarasi dengan nilai default.
'''Cara kedua adalah mendeklarasikan matriks dengan nilai default.
Sebagaimana materi array, nilai default ditentukan oleh kesepakatan bersama sesuai kebutuhan dengan nilainya di luar rentang yang ditentukan.'''

# <nama-var> = [[<default-val> for j in range(<m>)] for i in range(<n>)]
'''Terlihat pada struktur tersebut, cara kedua ini menggunakan dua metode sekaligus, yakni nested list dan nested for.
Nilai dari <default-val> ditentukan kesepakatan bersama, misalnya jika range yang disepakati adalah 1 hingga 10, kita bisa memilih 0 untuk 
nilai default-nya. Ada pula <n> sebagai jumlah baris matriks yang ingin dibuat dan <m> sebagai jumlah kolom matriks yang diinginkan.'''

matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)


print('\n')
## Akses Elemen Matriks
'''Sekarang, mari pelajari cara mengakses elemen pada matriks. Ingat bahwa matriks merupakan tabel data yang terdiri dari baris dan kolom.
Jadi, jika Anda ingin mengakses elemen dari matriks, perlu mengetahui indeks dari baris dan kolom.'''

# <namamatriks>[<nbrs>][<nkol>]

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])
"""
Output:
12
"""
print('\n')


### Operasi Matriks pada Python

"""
a. Operasi 1 matriks.
    Menghitung total semua elemen matriks.
    Mengalikan elemen matriks dengan konstanta.
    Transpose matriks.
    Inverse matriks.
    Menentukan determinan, dan sebagainya.

b. Operasi 2 matriks:
    Menambahkan dua matriks.
    Mengalikan dua matriks.
    Pembagian dua matriks, dan sebagainya.

mengalikan elemen matriks dengan konstanta.
"""

# 2 x [5 0, 1 -2] = [10 0, 2 -4]
'''kita mengalikan matriks "[5, 0], [1, -2]" dengan konstanta "2". Nilai konstanta tersebut kemudian dikalikan dengan setiap elemen matriks. 
Kalkulasinya dapat kita urai seperti berikut. 

Pertama, konstanta "2" akan dikalikan dengan elemen 5 yang menghasilkan nilai 10 (2 X 5 = 10).
Kedua, konstanta "2" akan dikalikan dengan elemen 0 yang menghasilkan nilai 0 (2 X 0 = 0).
Ketiga, konstanta "2" akan dikalikan dengan elemen 1 yang menghasilkan nilai 2 (2 X 1 = 2).
Terakhir, konstanta "2" akan dikalikan dengan elemen -2 yang menghasilkan nilai -4 (2x-2 = -4).'''

## Membuat matriks 2x2
var_mat = [[5,0],[1,-2]]
def_mat = [[0 for i in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat)):
        def_mat[i][j] = var_mat[i][j] * 2

print(var_mat)
print(def_mat)

#  cara yang lebih efektif, yaitu dengan menggunakan library NumPy
'''import numpy as np

var_mat = np.array([[5, 0],
                    [1, -2]])

result = var_mat * 2

print(result)'''

