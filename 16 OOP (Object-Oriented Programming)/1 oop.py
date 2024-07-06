### Duck Typing

'''Konsep duck typing tidak berkaitan langsung dengan dynamic typing atau loosely typed, ini merupakan konsep yang lebih erat dengan materi kita kali ini, yaitu pemrograman berorientasi objek (object-oriented programming). Duck typing menjelaskan bahwa sebuah tipe atau class dari sebuah object tidak lebih penting daripada method yang menjadi perilakunya. '''

### Class, Object, dan Method
'''anggaplah kita memiliki mobil sebagai kelas dasar dengan method maju, mundur, berbelok, dan berhenti. Selain itu, kelas dasar mobil memiliki atribut warna dan kecepatan.

Ketika membuat kelas baru, seperti Mobil Sport, kita dapat menggunakan kelas yang sudah ada (mobil sebagai kelas dasar) untuk mewarisi beberapa hal, mulai dari atribut warna, kecepatan hingga beberapa perilakunya, yakni maju, mundur, berbelok, dan berhenti. Namun, kita ingin menambahkan metode baru karena ini adalah mobil sport. Metode baru tersebut adalah turbo yang meningkatkan kecepatan secara signifikan.'''

'''Secara umum, konsep OOP dalam pemrograman sangat mirip seperti ilustrasi-ilustrasi di atas. Object-oriented programming adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atributdan perilaku (method). Objek merupakan perwujudan dari class dengan anggapan bahwa kelas adalah cetakan yang memungkinkan kita dapat membuat banyak objek berdasarkan cetakan tersebut.'''

'''Method adalah perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Sebagaimana halnya maju, mundur, berbelok, dan berhenti pada contoh sebelumnya. Atribut adalah variabel yang menjadi identitas dari objek atau kelas, seperti warna dan kecepatan pada contoh sebelumnya.'''

# Class
'''Pembuatan class dalam Python mirip seperti fungsi, yakni perlu menggunakan keyword untuk bisa membuatnya. Keyword atau kata kunci untuk membuat kelas dalam Python adalah "class".'''

class Mobil:
    
    # atribut
    warna = "Merah"


# Object (Objek)
'''Untuk memanggil kelas yang telah dibuat, kita membuat sebuah objek. Berdasarkan KBBI dari kemendikbud, objek merupakan benda, hal, dan sebagainya yang dijadikan sasaran untuk diteliti, diperhatikan, dan sebagainya. Keterkaitan antara objek dan class sangat erat. Contohnya, jika Anda membuat kelas bernama manusia, objeknya adalah manusia dengan nama yang berbeda.'''

'''Anda bisa umpamakan kelas adalah bentuk abstrak dari objek, layaknya cetakan atau blueprint. Saat kelas diwujudkan menjadi bentuk yang lebih nyata, proses ini disebut sebagai instansiasi. Itulah sebabnya objek disebut juga sebagai instance atau instance of the class.'''\

class Mobil:
    # Atribut
    warna = "Merah"
 
mobil_1 = Mobil()

