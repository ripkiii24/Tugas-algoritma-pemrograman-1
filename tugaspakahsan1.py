hargapasar = float(input("harga pasar sekarang berapa?.."))
hasilpanen = float(input("berapa hasil panen musim ini?(tolong konversi ke satuan kg).."))
biayatanam = float(input("berapa biaya tanamnya?.."))
biayapanen = float(input("panenya habis berapa?.."))
biayaperawatan = float(input("perawatannya?.."))
targetmargin = float(input("target margin berapa?(%)"))
pendapatan = hargapasar * hasilpanen
totalbiaya = biayatanam + biayapanen + biayaperawatan
keuntugan = pendapatan - totalbiaya
margin = (keuntugan / pendapatan)*100
if margin >= targetmargin:
    print("target tercapai! congrats")
else:
    print("target tidak tercapai")

print ("rinciannya gini:")
print ("pendapatan: ",pendapatan)
print ("Total Biaya: ",totalbiaya) 
print ("keuntungan: ",keuntugan) 
print ("margin (%)",margin)  