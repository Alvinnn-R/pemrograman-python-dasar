### Pengenalan Library

'''
Dalam pengembangan program atau aplikasi, kita tidak akan lepas dari peran package atau library. Sebagaimana yang sudah dijelaskan dalam materi-materi sebelumnya, package adalah sebuah direktori yang berisi satu atau lebih modul yang terkait dan saling berhubungan, sedangkan library adalah koleksi dari banyaknya modul dan paket yang saling terkait dan dapat digunakan berulang kali. 

Pada materi ini, kita akan mempelajari berbagai library yang telah dikembangkan oleh banyak pengembang dan dapat digunakan kembali oleh kita. Jumlah library Python sangat banyak yang terbagi menjadi Python Standard Library dan Python External Library.

Python Standard Library adalah jenis library yang telah terinstal secara otomatis ketika kita melakukan instalasi Python. Anda tidak perlu melakukan instalasi kembali jika ingin menggunakannya. Beberapa contoh Python Standard Library adalah “os”, “datetime”, “re”, serta lainnya yang dapat Anda baca lebih lengkap pada laman berikut.

Python External Library adalah kumpulan kode yang telah dikembangkan oleh orang lain atau komunitas dan disediakan dalam bentuk paket atau modul yang dapat diimpor. Jenis library ini mengharuskan Anda untuk melakukan instalasi agar dapat digunakan. External library ini dikembangkan oleh individu atau organisasi di luar tim inti pengembang Python. '''

# PIP
'''PIP adalah package manager resmi dari Python yang dapat digunakan untuk mengunduh, menginstal, menghapus, dan mengelola package Python dari Python Package Index (PyPI) dan repositori lainnya. PyPI merupakan repositori online yang menyediakan ribuan package dari Python dan siap digunakan oleh para pengembang.'''

# Conda
'''Selain pip yang termasuk package manager resmi dari Python, ada juga conda yang merupakan package manager dan environment manager untuk Python. Conda memungkinkan kita untuk membuat dan mengelola lingkungan (environment) terisolasi atau terpisah satu sama lain. Dengan terisolasinya setiap lingkungan tersebut, kita diuntungkan untuk mencegah konflik yang terjadi antar proyek. '''

## Library Text Processing
'''Pertama adalah sekumpulan library yang bertujuan untuk melakukan pemrosesan teks dan menyederhanakan serta mempercepat tugas-tugas pemrosesan teks.'''

# String
'''String adalah salah satu modul bawaan Python yang tidak perlu dideklarasikan.'''

# Regex
'''Regex atau regular expression adalah sebuah cara untuk mencari teks berdasarkan pola tertentu. Umpamanya, ketika ingin mencari sebuah kata dalam kamus, misalnya arti dari kata parsing, kita akan mencari kata tersebut di halaman yang memiliki kata dengan awalan p, lalu pa. Regex bekerja dengan konsep yang sama.'''



### Macam" Library

## Library Matematika
'''Selanjutnya adalah library math yang termasuk salah satu modul bawaan Python dan menyediakan berbagai fungsi dan konstanta matematika. Anda hanya perlu melakukan impor untuk modul math. Berikut contoh penerapannya. '''

## Library Parser
'''Library parser pada Python menyediakan fasilitas untuk menguraikan kode Python menjadi struktur data yang dapat diproses dan dianalisis. Anda dapat menggunakan Getopt atau ArgParse. '''

## Library Pengolahan Data
'''Library pengolahan data bertujuan untuk membantu dalam manipulasi, analisis, dan pemrosesan data. Library ini menyediakan berbagai fungsi dan metode yang memudahkan pengguna untuk melakukan operasi pengolahan data dengan lebih efisien dan cepat.

Tujuan dari library ini untuk menyederhanakan tugas-tugas kompleks yang berkaitan dengan pengolahan data sehingga Anda tidak perlu mengimplementasikan semuanya dari awal. Berikut adalah beberapa library populer yang digunakan untuk pengolahan data.'''

# 1. Pandas
'''Pandas adalah library populer yang digunakan untuk pengelolaan dan analisis data. Library ini menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi, pembersihan, transformasi, dan analisis data dengan mudah dan efisien.'''

# 2. NumPy
'''Library NumPy adalah package fundamental yang sering digunakan untuk scientific computing pada Python. Library ini menyediakan objek array multidimensi, berbagai jenis objek lainnya, seperti masked array dan matrix, dan sebagainya.'''

# 3. Matplotlib
'''Selanjutnya adalah matplotlibyang merupakan library untuk melakukan visualisasi data. Matplotlib termasuk jenis library eksternal sehingga Anda perlu melakukan instalasi matplotlib terlebih dahulu.'''

## Library File Management
'''Library file management adalah kumpulan library yang dirancang untuk membantu pengguna dalam mengelola dan berinteraksi dengan berkas dan direktori pada sistem file. Beberapa library file management adalah berikut.'''

# 1. OS
'''Modul OS pada Python berguna untuk fungsi-fungsi yang berkaitan dengan sistem operasi, misalnya open(), path(), getcwd(), dan fungsi lainnya. Modul ini memungkinkan Anda untuk memanfaatkan fungsi yang sama dan mengeksekusi fungsi terkait OS yang mungkin berbeda dalam setiap sistem operasi. Ada beberapa fitur yang hanya bekerja pada sistem operasi tertentu.'''

# 2. JSON
'''Untuk serialization dengan bahasa lain, umumnya kita menggunakan JSON(JavaScript Object Notation) yang memiliki beberapa perbedaan karakteristik dengan pickle'''

# 3. Pickle
'''Jika Anda memiliki sebuah list yang ingin disimpan atau ditransmisikan tanpa khawatir bentuknya akan rusak atau kacau, fungsi dari library pickle dapat dimanfaatkan. Pickle termasuk fungsi Object Serialization pada Python. Pickling adalah istilah untuk mengubah objek menjadi byte stream, sedangkan unpickling adalah perlakuan sebaliknya.'''

## Library Web Scraping
'''Library web scraping adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web. Proses ini disebut sebagai “web scraping” atau “web crawling”. Anda bisa menggunakan fungsi dan metode pada library ini untuk mengekstraksi informasi dari situs web dan menyimpannya dalam format yang dapat diakses dan digunakan dalam analisis atau aplikasi lainnya. '''

# 1. Beautifulsoup
'''Beautifulsoup adalah library untuk mengambil data dari halaman web dan mengekstrak informasi yang diperlukan.'''

# 2. Urllib
'''Urllib adalah library bawaan dari Python yang bertujuan untuk scraping konten dari sebuah website. Penggunaan urllib berbeda dengan beautifulsoup. Bisa dikatakan bahwa cara penggunaan urllib sedikit kompleks dibandingkan beautifulsoup.'''

## Library Machine Learning
'''Selanjutnya adalah library yang digunakan untuk melakukan pemelajaran mesin. Anda dapat menggunakan library berikut untuk membantu Anda menyelesaikan permasalahan machine learning. Berikut adalah beberapa library populer untuk machine learning.'''

# 1. scikit-learn
'''Pertama adalah scikit-learn yang menyediakan berbagai algoritma pemelajaran mesin siap pakai untuk membantu dalam pengembangan model pemelajaran mesin, pemrosesan data, dan evaluasi kinerja model.
Scikit-learn termasuk library eksternal sehingga Anda perlu menginstalnya terlebih dahulu untuk bisa menggunakannya.'''

# 2. TensorFlow
'''Selanjutnya adalah TensorFlow sebagai salah satu library paling populer terkait machine learning. Dengan menggunakan TensorFlow, Anda bisa mengembangkan machine learning hingga tahap deployment.'''

# 3. PyTorch
'''Terakhir ada PyTorch, yakni library machine learning yang dikembangkan oleh Facebook’s AI Research lab (FAIR). PyTorch menyediakan alat dan kerangka kerja yang kuat untuk mengembangkan model pemelajaran mesin, terutama dalam konteks jaringan saraf tiruan (neural networks).'''

## Library Web Development
'''Terakhir, ada library yang bertujuan untuk pengembangan aplikasi web. Sebagaimana yang sudah dijelaskan dalam materi-materi sebelumnya, Python dapat digunakan untuk pengembangan aplikasi web pada sisi server. Berikut adalah library yang dapat digunakan untuk membantu Anda mengembangkan web.'''

# 1. Django
'''Django adalah high-level Python web framework yang mendukung pengembangan secara cepat, bersih, serta pragmatis.'''

# 2. Flask
'''Flask adalah web framework dalam Python yang ditujukan untuk membangun aplikasi web. Flask dirancang dengan tujuan menjadi ringan, fleksibel, dan sederhana. Dengan Flask, Anda bisa merancang aplikasi web dari yang sederhana hingga kompleks.'''

# 3. Fast API
'''FastAPI adalah web framework untuk Python yang tujuannya merancang dan membangun API dengan cepat, efisien, dan aman. FastAPI memberikan kinerja yang tinggi, sintaks yang intuitif, serta dukungan otomatisasi dokumentasi yang kuat. Jadi, ia cocok untuk pengembangan mikroservis, layanan web responsif, dan sebagainya.'''

