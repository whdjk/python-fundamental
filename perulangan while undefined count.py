"""
program pengulangan baca buku menggunakan while
"""
jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')
jumlah_baca = 0
jumlah_dipahami = 0
print(f'Jumlah buku yang dipahami {jumlah_dipahami}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_dipahami == 9:
        print(f"Buku ke {jumlah_dipahami + 1} belum paham")
    else:
        jumlah_dipahami = jumlah_dipahami + 1
        print(f"Buku ke {jumlah_dipahami} sudah dipahami")
if jumlah_dipahami == jumlah_buku:
    print('Semua buku bisa dipahami')
else:
    print('tidak semua buku bisa dipahami')




