"""
program pengulangan baca buku menggunakan while
"""
jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

jumlah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_dibaca}')

while jumlah_dibaca < jumlah_buku:
    jumlah_dibaca = jumlah_dibaca + 1
    print(f"Buku ke {jumlah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_dibaca}")