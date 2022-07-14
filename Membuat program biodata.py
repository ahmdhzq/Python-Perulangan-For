# Membuat Program Biodata

# Membuat variabel nama_saya yang menerima inputan
nama_lengkap = input("Masukan Nama Lengkap : ")

# Membuat variabel asal_daerah yang menerima inputan
asal_daerah = input("Masukan Asal Daerah : ")

# Membuat array biodata untuk mengumpulkan hasil inputan
biodata = [ nama_lengkap, asal_daerah ]

no = 0
for isi_biodata in biodata :
    print(biodata[no])
    no = no + 1