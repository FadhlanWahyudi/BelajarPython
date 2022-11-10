
#Soal 1 Perbedaan Data Structure
# List       = Tipe data yang terbentuk dari beberapa objek int dan float
# Dictionary = Memiliki key-value dan diawali dengan {}
# Tuple      = Tipe data ordered yang tidak bisa diubah objectnya
# Set        = tipe data yang tidak memiliki ordered, untuk cirinya bisa diubah untuk objeknya namun diuntuk objeknya harus berupa unique selain itu tandanya ialah menggunakan {}

#Soal 2 Akses List
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print(a[1 : 5])

#Soal 3 Akses Nested List

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

print(a[1][1 : 3])
 

 # Soal 4 List Manipulation

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

a[0][2] = 10
a[1][0] = 11
print(a)

# Soal 5 Delete Element List
# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

areas.remove("bathroom"),(10.50)
print(areas)

# Soal 6 List Comprehension
# Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x % 2 == 0]

print(T)

# [0, 4, 16, 36, 64]


#Soal 8: Menambahkan key-value baru ke Dictionary

#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'itali' : 'roma' }
print(europe['itali'])

#Soal 9: Boolean Comparison

#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
#- Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'

print(3 > 1) and (2 < 3)
print(4 == 4) or (5 != 5)
print(not(3 > 4))

# Soal 10: If-Else Statement
# Lengkapi kode untuk menghasilkan suatu output yang di harapkan
# - Bualah sebuah if-else statement yang dimana akan mem-print 'High' jika grade adalah 'A' dan price lebih dari 100000, kemudian mem-print 'Medium' jika grade adalah 'A' dan price lebih dari 50000 dan memprint 'low' jika grade adalah 'A' dan price lebih kecil dan sama dengan 50000.

a = 100022

if a > 100000 :
    print('High')
elif a > 50000 :
    print('Medium')
elif a < 50000 :
    print('Low')