# Import library yang dibutuhkan
import random
import time

# Data Map
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

# penyimpanan player
koleksi_ikan = {
    "koleksi_ikan_biasa": [],
    "koleksi_ikan_langka": [],
    "koleksi_ikan_legenda": []
}

# Mulai Game
# Menu Utama
while True:
  print("===== Menu Utama =====")
  print("1.Mulai Game\n2.Koleksi Ikan\n3.Keluar Game")
  print("======================")
  try:
    menu = int(input("Pilih Menu : "))
  except ValueError:
    print("Pilihan Tidak Valid")
    continue

  # Logika Game
  if menu == 1:
    print("===== Selamat Datang Di Game Memancing Ikan =====")
    print("Rawa Hijau\nDanau Biru\nSungai Abu")
    # Pemilihan map
    map = input("Pilih Map!").lower()
    if map not in ["rawa hijau", "danau biru", "sungai abu"]:
      print("Pilihan Tidak Valid")
      continue
    if map in data_map:
      print(f"===== Selamat Datang Di Map {map.title()} =====")
      print("============================================")

      # Proses mancing
      mancing = "x"
      while mancing == "x":
       input("Tekan x Untuk Lempar Pancingan! ").lower()
       for i in range(5, 0, -1):
        print(f"Lempar Pancingan Dalam {i} Detik")
        time.sleep(1)

    # persentasi ikan legenda
       persentasi = random.randint(1, 100)
       berat = random.randint(1, 10)
       if persentasi <= 10:
        strike = random.choice(data_map[map]["ikan_legenda"])
        print(f"Selamat!! Kamu mendapatkan Ikan {strike.title()} dengan berat {berat} kg")
        koleksi_ikan["koleksi_ikan_legenda"].append({"nama": strike, "berat": berat})
        time.sleep(0.5)

       # persentasi ikan langka
       elif persentasi <= 40:
        strike = random.choice(data_map[map]["ikan_langka"])
        print(f"Hebat!! Kamu mendapatkan Ikan {strike.title()} dengan berat {berat} kg")
        koleksi_ikan["koleksi_ikan_langka"].append({"nama": strike, "berat": berat})
        time.sleep(0.5)

       # persentasi ikan biasa
       else:
        strike = random.choice(data_map[map]["ikan_biasa"])
        print(f"Kamu mendapatkan Ikan {strike.title()} dengan berat {berat} kg")
        koleksi_ikan["koleksi_ikan_biasa"].append({"nama": strike, "berat": berat})
        
        time.sleep(0.5)

       clear = input("Apakah kamu ingin mancing lagi? (x/y)")
       if clear == "x":
        break

  # Koleksi Ikan player
  elif menu == 2:
    print("===== Koleksi Ikan Anda =====")
    print(koleksi_ikan)
    keluar = input("Tekan ENTER untuk keluar")

  # Keluar game
  else:
    print("===== Terima Kasih Telah Bermain =====")
    break