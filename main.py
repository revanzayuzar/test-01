# Program Perulangan
# -------------------------

"""
>> Dibuat Oleh :

Nama : M. Revanza Yuzar (Revan)
Bahasa Pemrograman : Python
"""

# --------------------------------------------------------------------------

# Kode Program :

print("-------------------------------------------------------------------")
print("# Program Perulangan")
print("-------------------------------------------------------------------")

print("""
>> Dibuat Oleh :

Nama : M. Revanza Yuzar (Revan)
Bahasa Pemrograman : Python
""")

print("___________________________________________________________________")

print("""
>> Deskripsi Program :

- Nilai Awal : Nilai mula-mula / Nilai awal.
- Pertambahan Nilai : Banyaknya pertambahan nilai per perulangan.
- Target Nilai : Nilai yang ingin di capai / ditargetkan.
- Nilai dapat diisi dalam bentuk Desimal.
- Gunakan tanda titik (.) untuk menuliskan koma.
- Nilai & Target pada tabel hasil ditulis dengan 4 angka dibelakang koma.
""")

print("___________________________________________________________________")

print("""
>> Tujuan Program :

Untuk mencari total perulangan yang diperlukan agar nilai awal dapat mencapai target nilai berdasarkan pertambahan nilai yang telah ditentukan.
""")

print("___________________________________________________________________")

print("\nProgram Dimulai! Silakan Mengisi ... \n")

nilai = float(input("Nilai Awal \t\t : "))
print()

pertambahan = float(input("Pertambahan Nilai \t : "))
print()

target = float(input("Target Nilai \t\t : "))
print()

perulangan = 0

print("-------------------------------------------------------------------")
print("|    Perulangan    |         Nilai         |        Target        |")
print("-------------------------------------------------------------------")

while True :
	nilai = nilai + pertambahan
	perulangan = perulangan + 1
	cek = nilai - pertambahan
	
	if cek >= target :
		nilai = nilai - pertambahan
		
		print(">> Nilai Awal Telah Mencapai Target!")
		print("-------------------------------------------------------------------")
		
		print()
		
		print(">> Tidak memerlukan perulangan!")
		print('>> Karena Nilai Awal telah mencapai Target Nilai.')
		
		print()
		
		if nilai == target :
			print(">> (Nilai Awal = Target Nilai)")
			
		else :
			print(">> (Nilai Awal > Target Nilai)")
			
		print()
		
		selisih = nilai - target
		
		print(f">> Selisih antara Nilai Awal dengan Target Nilai = {selisih:.4f}")
		break
		
	if pertambahan <= 0 :
		print(">> Pertambahan Nilai Harus Bernilai Positif!")
		print("-------------------------------------------------------------------")
		break
	
	if nilai < target :
		print("| Ke:{:>13} | {:>21.4f} | {:>20.4f} |".format(perulangan, nilai, target))

	if nilai >= target :
		print("-------------------------------------------------------------------")
		print("| Ke:{:>13} | {:>21.4f} | {:>20.4f} |".format(perulangan, nilai, target))
		print("-------------------------------------------------------------------")
		
		print()
		
		print("-------------------------------------------------------------------")
		print(f">> Perulangan Ke-{perulangan}, Nilai Telah Mencapai Target!")
		print("-------------------------------------------------------------------")
		
		print()
		
		print(f">> Total Perulangan yang diperlukan : {perulangan} Kali")
		
		print()

		if nilai == target :
			print(">> (Nilai Akhir = Target Nilai)")
	
		else :
			print(">> (Nilai Akhir > Target Nilai)")
			
		print()

		selisih = nilai - target

		print(f">> Selisih antara Nilai Akhir dengan Target Nilai = {selisih:.4f}")
		break

print("\n\n")

print("___________________________________________________________________")
print()
print("Program Selesai ...")
print()
print("Copyright© 2023 @revanzayuzar")
print("___________________________________________________________________")
print()

# Copyright© 2023 @revanzayuzar