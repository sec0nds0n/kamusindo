import json
from difflib import get_close_matches

data = json.load(open('indonesia.json'))

def terjemahkan(kata):
    kata = kata.lower()
    rekomendasi_kata = get_close_matches(kata, data.keys())[0]
    if kata in data:
        return (data[kata])
    elif len(get_close_matches(kata, data.keys())) > 0:
        konfirmasi = input("Mungkin maksud anda %s? (y/n)" % rekomendasi_kata)
        konfirmasi = konfirmasi.lower()
        if konfirmasi == "y":
            return (data[rekomendasi_kata])
        elif konfirmasi == "n":
            return "Kata tidak ditemukan"
        else:
            return "Jawaban anda tidak sesuai (y/n)"
    else:
        return "Kata tidak ditemukan"
    

kata = input("Masukkan kata (Bahasa Indonesia): ")
print(terjemahkan(kata))
