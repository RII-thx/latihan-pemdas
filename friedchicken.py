print("GEROBAK FRIED CHICKEN")
print("----------------------------")
print("Kode   Jenis Potong    Harga")
print("----------------------------")
print("D      Dada            Rp 2500")
print("P      Paha            Rp 2000")
print("S      Sayap           Rp 1500")
print("----------------------------")

banyak_jenis = int(input("Masukkan banyak jenis ayam yang dibeli: "))

total_bayar = 0

for i in range(banyak_jenis):
    print("\nJenis ke-", i+1)
    kode = input("Masukkan kode potong [D/P/S]: ").upper()
    banyak_beli = int(input("Masukkan banyak potong: "))

    if kode == "D":
        harga = 2500
        jenis = "Dada"
    elif kode == "P":
        harga = 2000
        jenis = "Paha"
    elif kode == "S":
        harga = 1500
        jenis = "Sayap"
    else:
        print("Kode tidak valid!")
        continue

    jumlah = harga * banyak_beli
    total_bayar = total_bayar + jumlah

    print("Jenis:", jenis)
    print("Harga Satuan: Rp", harga)
    print("Jumlah Harga: Rp", jumlah)

pajak = total_bayar * 0.10
total_akhir = total_bayar + pajak

print("\n----------------------------")
print("Jumlah Bayar  : Rp", total_bayar)
print("Pajak 10%     : Rp", int(pajak))
print("Total Bayar   : Rp", int(total_akhir))
print("----------------------------")
print("Terima kasih telah membeli di Gerobak Fried Chicken!")
