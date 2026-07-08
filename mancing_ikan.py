# Import library yang dibutuhkan
import random
import time

# ==================================================
# CONSTANS
# ==================================================
# persentase peluang menangkap ikan
legenda_change = 10
langka_change = 40

# batas maksimal berat ikan
max_berat_countdown = 10
min_countdown = 1
max_countdown = 5

# Data Map dengan berbagai lokasi mancing
data_map = {
    "rawa hijau": {
        "ikan_biasa": ["kembung", "teri"],
        "ikan_langka": ["lemadang", "kowe gerong"],
        "ikan_legenda": ["raja laut", "hiiu paus"]
    },
    "danau biru": {
        "ikan_biasa": ["cakalang", "tongkol"],
        "ikan_langka": ["kurisi bali", "mandarin"],
        "ikan_legenda": ["napoleon", "pari hitam manta"]
    },
    "sungai abu": {
        "ikan_biasa": ["kerapu macan", "baronang"],
        "ikan_langka": ["tenggiri", "tuna sirip kuning"],
        "ikan_legenda": ["hiu gergaji", "hiu harimau"]
    }
}

# pesan hasil tangkapan
pesan_tangkapan = {
    "legenda": "Selamat!! Kamu mendapatkan Ikan {} dengan berat {} kg",
    "langka": "Hebat! Kamu mendapatkan Ikan {} dengan berat {} kg",
    "biasa": "Kamu mendapatkan Ikan {} dengan berat {} kg"
}

# ==================================================
# PLAYER DATA
# ==================================================
koleksi_ikan = {
    "koleksi_ikan_biasa": [],
    "koleksi_ikan_langka": [],
    "koleksi_ikan_legenda": []
}

dompet_player = 0

# ==================================================
# FUNCTIONS
# ==================================================
# Menu Utama

# menampilkan menu utama
def tampilkan_menu_utama():
  print("\n===== Menu Utama =====")
  print("1.Mulai Game")
  print("2.Koleksi Ikan")
  print("3.Toko Ikan")
  print("4.Keluar Game")
  print("======================")

# player memilih menu utama
def validasi_menu(pilihan):
  try:
    menu_int = int(pilihan)
    if menu_int in [1, 2, 3, 4]:
      return menu_int
    else:
      print("Pilihan harus 1, 2, 3, atau 4")
      return None
  except ValueError:
    print("Pilihan harus berupa angka")
    return None

# meminta player memilih map
def pilih_map():
    print("\n===== Selamat Datang di Game Memancing Ikan =====")
    print("Pilihan Map:")
    print("1. Rawa Hijau")
    print("2. Danau Biru")
    print("3. Sungai Abu")

    peta_pilihan = {
        "1": "rawa hijau",
        "2": "danau biru",
        "3": "sungai abu"
    }

    pilihan = input("\nPilih Map! 1/2/3:").strip()

    if pilihan in peta_pilihan:
      return peta_pilihan[pilihan]
    else:
      print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3")
      return None

def countdown_pancingan():
  print("\nSiap untuk melempar pancingan")
  for detik in range(max_countdown, min_countdown - 1, -1):
    print(f"Lempar pancingan dalam {detik} detik", end="\r")
    time.sleep(1)
  print("Pancingan terlempar\n")

def tentukan_hasil_tangkapan(persentase, peta):
  if persentase <= legenda_change:
    jenis = "legenda"
    nama = random.choice(data_map[peta]["ikan_legenda"])
  elif persentase <= langka_change:
    jenis = "langka"
    nama = random.choice(data_map[peta]["ikan_langka"])
  else:
    jenis = "biasa"
    nama = random.choice(data_map[peta]["ikan_biasa"])

  return jenis, nama

def tampilkan_hasil_tangkapan(jenis_ikan, nama_ikan, berat):
  pesan = pesan_tangkapan[jenis_ikan]
  print(pesan.format(nama_ikan.title(), berat))
  time.sleep(0.5)

def simpan_ikan(jenis_ikan, nama_ikan, berat):
  kunci_koleksi = f"koleksi_ikan_{jenis_ikan}"
  koleksi_ikan[kunci_koleksi].append({
      "nama": nama_ikan,
      "berat": berat
  })

def proses_mancing(peta):
  print(f"\n===== Selamat Datang di Map {peta.title()} =====")
  print("=" * 45)

  while True:
    input("\nTekan ENTER untuk melempar pancingan: ")

    # countdown
    countdown_pancingan()

    # tentukan hasil tangkapan
    persentase = random.randint(1, 100)
    berat = random.randint(1, max_berat_countdown)
    jenis_ikan, nama_ikan = tentukan_hasil_tangkapan(persentase, peta)

    # tampilkan hasil
    tampilkan_hasil_tangkapan(jenis_ikan, nama_ikan, berat)

    # simpan ikan
    simpan_ikan(jenis_ikan, nama_ikan, berat)

    # tanya player apakah ingin lanjut
    lanjut = input("\nApakah kamu ingin mancing lagi? (y/n): ").strip()
    if lanjut != "y":
      print("kembali ke Menu Utama...\n")
      break

def tampilkan_koleksi():
  # menampilkan koleksi yang dimiliki player
  print("\n===== Koleksi Ikan =====\n")

  total_ikan = 0

  # tampilan ikan biasa
  ikan_biasa = koleksi_ikan["koleksi_ikan_biasa"]
  print(f"Ikan Biasa ({len(ikan_biasa)} ekor):")
  if ikan_biasa:
    for idx, ikan in enumerate(ikan_biasa, 1):
      print(f"  {idx}. {ikan['nama'].title()} - {ikan['berat']} kg")
    total_ikan += len(ikan_biasa)
  else:
    print("   (Belum ada ikan biasa)")

  # tampilan ikan langka
  ikan_langka = koleksi_ikan["koleksi_ikan_langka"]
  print(f"\nIkan Langka ({len(ikan_langka)} ekor):")
  if ikan_langka:
    for idx, ikan in enumerate(ikan_langka, 1):
      print(f"  {idx}. {ikan['nama'].title()} - {ikan['berat']} kg")
    total_ikan += len(ikan_langka)
  else:
    print("   (Belum ada ikan langka)")

  # tampilan ikan legenda
  ikan_legenda = koleksi_ikan["koleksi_ikan_legenda"]
  print(f"\nIkan Legenda ({len(ikan_legenda)} ekor):")
  if ikan_legenda:
    for idx, ikan in enumerate(ikan_legenda, 1):
      print(f"  {idx}. {ikan['nama'].title()} - {ikan['berat']} kg")
    total_ikan += len(ikan_legenda)
  else:
    print("   (Belum ada ikan legenda)")

  print(f"\n{'='*30}")
  print(f"Total ikan: {total_ikan}")
  print(f"{'='*30}\n")

  input("Tekan ENTER untuk kembali ke Menu Utama: ")

def tampilan_penjualan_ikan():
  print("\n" + "="*45)
  print("1. Jual Ikan Biasa")
  print("2. Jual Ikan Langka")
  print("3. Jual Ikan Legenda")
  print("4. Kembali")

  try:
    pilihan = int(input("Pilih opsi! "))
    if pilihan in [1, 2, 3, 4]:
      return pilihan
    else:
      print("Pilihan tidak valid!!")
      print("pilih angka 1, 2, 3, atau 4")
      return None
  except ValueError:
    print("Pilihan harus berupa angka")
    return None\

def menu_toko():
  global dompet_player

  while True:
    print("\n===== TOKO =====")
    print(f"Gold player: {dompet_player} gold\n")

    # menampilkan ikan yang dimiliki
    ikan_biasa = len(koleksi_ikan["koleksi_ikan_biasa"])
    ikan_langka = len(koleksi_ikan["koleksi_ikan_langka"])
    ikan_legenda = len(koleksi_ikan["koleksi_ikan_legenda"])
    print(f"Jumlah ikan biasa {ikan_biasa} ekor")
    print(f"Jumlah ikan langka {ikan_langka} ekor")
    print(f"Jumlah ikan legenda {ikan_legenda} ekor")

    # pilihan player untuk menjual ikan
    pilihan = tampilan_penjualan_ikan()

    if pilihan == 1:
      if ikan_biasa > 0:
        dompet_player += 100
        koleksi_ikan["koleksi_ikan_biasa"].pop()
      else:
        print("Tidak ada ikan biasa yang tersedia")

    elif pilihan == 2:
      if ikan_langka > 0:
        dompet_player += 200
        koleksi_ikan["koleksi_ikan_langka"].pop()
      else:
        print("Tidak ada ikan langka yang tersedia")

    elif pilihan == 3:
      if ikan_legenda > 0:
        dompet_player += 500
        koleksi_ikan["koleksi_ikan_legenda"].pop()
      else:
        print("Tidak ada ikan legenda yang tersedia")

    elif pilihan == 4:
      print("Kembali ke Menu Utama...\n")
      break
  
    
def main():
  """ Fungsi Utama - Loop Game """
  print("\n" + "="*45)
  print("SELAMAT DATANG DI GAME MEMANCING IKAN")
  print("="*45)

  while True:
    tampilkan_menu_utama()

    # Input dan validasi menu
    while True:
      pilihan = input("\nPilih Menu: ")
      menu = validasi_menu(pilihan)
      if menu is not None:
        break

    # Logika menu
    if menu == 1:
      # mulai game
      peta = pilih_map()
      if peta:
        proses_mancing(peta)

    elif menu == 2:
      # Koleksi ikan
      tampilkan_koleksi()

    elif menu == 3:
      # menu toko
      menu_toko()

    elif menu == 4:
      # Keluar game
      print("\n===== Terima Kasih Telah Bermain =====")
      print("Sampai Jumpa Lagi!!\n")
      break

# ==================================================
# MAIN PROGRAM
# ==================================================
if __name__ == "__main__":
  main()
