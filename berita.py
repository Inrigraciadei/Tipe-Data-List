with open("berita.txt", "r") as file:
       isi_dalam_file = file.read()
       print("=====ISI BERITA=====")
       print(isi_dalam_file)

kata_unik = []

kumpulan_kata = isi_dalam_file.split()
for kata in kumpulan_kata:
      if kata not in kata_unik:
            kata_unik.append(kata.strip(',?!.'))

print("\n=====Kata Unik Pada Berita=====")
print(kata_unik)