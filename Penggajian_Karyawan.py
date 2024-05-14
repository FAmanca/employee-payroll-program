print("+=====================================================================================+")
print("|                  APLIKASI PENGGAJIAN KARYAWAN PT.SEJAHTERA MULIA                    |")
print("+-------------------------------------------------------------------------------------+")
print("|                     DAFTAR JABATAN GAJI DAN TUNJANGAN KARYAWAN                      |")
print("+-----+--------------+----------------+--------------+---------------------+----------+")
print("|     |              |                |              |        STATUS       | ASURANSI |")
print("|  NO |   JABATAN    |   GAJI POKOK   |   TUNJANGAN  |---------------------|----------|")
print("|     |              |                |              |   MENIKAH   | BELUM |   BPJS   |")
print("+-----+--------------+----------------+--------------+-------------+-------+----------+")
print("|  1  | Direktur     |Rp. 15.000.000  |Rp.10.000.000 |Rp.1.000.000 |   0   |    10%   |")
print("|  2  | Manager      |Rp. 8.000.000   |Rp.5.000.000  |Rp.750.000   |   0   |    8%    |")
print("|  3  | Supervisor   |Rp. 5.000.000   |Rp.3.000.000  |Rp.500.000   |   0   |    5%    |")
print("|  4  | Operator     |Rp. 3.000.000   |Rp.1.000.000  |Rp.250.000   |   0   |    3%    |")
print("+=====+==============+================+==============+=============+=======+==========+")

namaKaryawan = input("Masukan Nama Karyawan : ")
#* VALIDASI JABATAN
while True:
  jenisJabatan = int(input("Masukan Jenis Jabatan (1/2/3/4) : "))
  if (
    jenisJabatan != 1
    and jenisJabatan != 2
    and jenisJabatan != 3
    and jenisJabatan != 4
  ):
    print("INPUT INVALID !")
    print("HARAP ISI KEMBALI")
    continue
  else:
    break
tunjangan_anak = 0
print("1. Menikah")
print("2. Belum Menikah")
status = int(input("Pilih Status : "))
if status == 1:
    anak = int(input("Masukan Jumlah Anak : "))
    if anak > 3:
      bonus = 3
      tunjangan_anak = 100000 * bonus
    else:
      bonus = anak
      tunjangan_anak = 100000 * bonus

#* VALIDASI UNTUK HARI KERJA JIKA LEBIH 30 HARI
while True:
  JumlahHariKerja = int(input("Masukan Jumlah Hari kerja (Maksimal 30 hari) : "))
  if JumlahHariKerja > 30 and JumlahHariKerja <0:
    print("Maksimum Hari Kerja adalah 30 Hari !")
    print("Harap Isi ulang kembali !!")
    continue
  else:
    break

tunjangan_nikah = 0
match jenisJabatan:
  case 1:
      jabatan = "Direktur"
      gajiPokok = 15000000
      Tunjangan = 10000000
      AsuransiBPJS = 0.1 * gajiPokok
      if status == 1:
        tunjangan_nikah = 1000000
  case 2:
      jabatan = "Manager"
      gajiPokok = 8000000
      Tunjangan = 5000000
      AsuransiBPJS = 0.08 * gajiPokok
      if status == 1:
          tunjangan_nikah = 750000
  case 3:
      jabatan = "Supervisor"
      gajiPokok = 5000000
      Tunjangan = 3000000
      AsuransiBPJS = 0.05 * gajiPokok
      if status == 1:
          tunjangan_nikah = 500000
  case 4:
      jabatan = "Operator"
      gajiPokok = 3000000
      Tunjangan = 1000000
      AsuransiBPJS = 0.03 * gajiPokok
      if status == 1:
          tunjangan_nikah = 250000

#* PERHITUNGAN TOTAL GAJI DAN POTONGAN
HariTidakKerja = 30 - JumlahHariKerja
potongan = HariTidakKerja * 15000
Total_gaji = (gajiPokok + Tunjangan + tunjangan_nikah + tunjangan_anak + JumlahHariKerja * 10000) - (potongan + AsuransiBPJS)

print("+=====================================================================================+")
print("                                      SLIP GAJI")
print("+=====================================================================================+")
print(f"Nama Karyawan    : {namaKaryawan}")
print(f"Jabatan          : {jabatan}")
print("+-------------------------------------------------------------------------------------+")
print(f"Gaji Pokok       : Rp.{gajiPokok}")
print(f"Tunjangan        : Rp.{Tunjangan}")
print(f"Tunjangan Nikah  : Rp.{tunjangan_nikah}")
print(f"Tunjangan Anak   : Rp.{tunjangan_anak}")
print(f"Potongan BPJS    : Rp.{AsuransiBPJS}")
print("+-------------------------------------------------------------------------------------+")
print(f"Hari Tidak Kerja : {HariTidakKerja} Hari")
print(f"Potongan         : Rp.{potongan}")
print("+-------------------------------------------------------------------------------------+")
print(f"Total Gaji       : Rp.{Total_gaji}")
print("+=====================================================================================+")