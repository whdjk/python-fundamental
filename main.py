
# PERCABANGAN
jumlah_botol_susu = 123
jumlah_telur = 1453
print(f"Jumlah botol susu yang ada {jumlah_botol_susu} botol")
print(f"Jumlah telur yang ada {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangya cukup")
    print("Budi membeli 1 botol susu")
    if jumlah_telur > 5:
        print("Budi membeli 6 butir telur")
    else:
        print("Budi membeli 1 botol susu")

else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya ke Ibu")