barang = input('Masukkan nama barang: ')
harga = int(input('Masukkan harga barang: '))
jumlah_barang = int(input('Masukkan jumlah barang: '))


total_harga = harga * jumlah_barang

#ujang abdul rohman
#20230040144

text = f'''=== NOTA KASIR ===
Barang        : {barang}
Harga         : {harga}
Jumlah Barang : {jumlah_barang}
Total Harga   : {total_harga}
'''


try:
    with open('nota.txt', 'a') as file:
        file.write(text)
        file.write('\n')  
    print("Nota telah dicetak ke file nota.txt.")
except IOError:
    print("Terjadi kesalahan saat menulis ke file.")