perbandingan = "saya suka perbandingan,saya suka belajar pyton"
print (perbandingan)
# Daftar umur
umur_siswa = [18, 21, 17, 20, 22]

# Memeriksa apakah ada siswa yang berumur lebih dari 21
if any(umur > 21 for umur in umur_siswa):
    print("Ada siswa yang berumur lebih dari 21.")
else:
    print("Tidak ada siswa yang berumur lebih dari 21.")