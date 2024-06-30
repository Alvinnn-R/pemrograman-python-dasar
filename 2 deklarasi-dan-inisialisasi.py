### Deklarasi dan Inisialisasi

'''Python tidak mengharuskan Anda untuk melakukan deklarasi tipe data variabel.
Hal ini disebabkan Python merupakan bahasa pemrograman yang menerapkan loosely typed.
Artinya, Anda tidak perlu mendeklarasikan tipe data variabel secara eksplisit.'''

age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

'''Python juga merupakan bahasa pemrograman yang menerapkan dynamic typing. 
Artinya, Python adalah bahasa pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan melakukan proses assignment.
Hal ini memungkinkan kita untuk mengubah tipe data dari suatu variabel seiring berjalannya program.'''

x = 6
print(type(x))

x = "6"
print(type(x))