import random

menu_tebakan = "GAME TEBAKAN YGY"
tebakan = random.randint(1, 4)

print(f'''
####################
# {menu_tebakan} #
####################
''')

nama_user = str(input("Hai user! Masukan nama mu dulu: "))

print(f'''
Hai {nama_user}, Coba perhatikan Kotak dibawah ini.
[_] [_] [_] [_]
''')

answer = int(input("Menurut kamu, kelinci itu di kotak nomor berapa? Ketik (1/2/3/4) : "))
confirm = str(input(f"Apakah kamu yakin dengan jawaban nomor {answer}?, ketik (y/n) : "))
if confirm == "n":
  print("Program di hentikan.")
  exit()
elif confirm == "y":
  if answer > 4:
    print("Hanya dapat memilih angka (1/2/3/4) saja, Silahkan ulangi lagi!")
  else:
    if answer == tebakan:
      print(f"Selamat {nama_user}, Kamu menang!, Kotak itu berada di nomor {tebakan}")
    else:
      print(str(f"Tebakan mu salah, Kotak itu berada di nomor {tebakan}"))
else:
  print("Game berakhir.")