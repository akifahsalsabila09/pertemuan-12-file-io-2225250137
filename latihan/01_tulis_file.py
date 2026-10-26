
# Latihan 1: Menulis File
# Menggunakan mode w untuk menulis data ke file

with open("data/catatan.txt", "w", encoding="utf-8") as file:
    file.write("Ini adalah latihan menulis file menggunakan Python.\n")
    file.write("Data berhasil disimpan ke dalam file catatan.txt.\n")

print("Data berhasil ditulis ke file catatan.txt.")
