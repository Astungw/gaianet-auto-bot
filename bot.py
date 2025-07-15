import requests
import random
import time

API_URL = "https://llama.gaia.domains/v1/chat/completions"

# Minta token dari user saat bot dijalankan
api_key = input("Masukkan Bearer Token GaiaNet kamu:\n> ").strip()
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

pertanyaan = [
    "Apa itu singularitas AI?",
    "Bagaimana AI bisa membantu manusia?",
    "Kenapa penting menjaga lingkungan?",
    "Apa itu gaya gravitasi?",
    "Apa manfaat membaca buku setiap hari?",
    "Apa peran blockchain di masa depan?",
    "Bagaimana cara kerja otak manusia?"
]

def kirim_chat(pesan):
    payload = {
        "model": "Llama-3.2-3B-Instruct",
        "messages": [
            {"role": "system", "content": "You're a helpful assistant."},
            {"role": "user", "content": pesan}
        ]
    }

    try:
        r = requests.post(API_URL, headers=headers, json=payload)
        if r.status_code == 200:
            isi = r.json()
            print(f"\n[✅] Q: {pesan}\n[🤖] A: {isi['choices'][0]['message']['content']}\n")
        else:
            print(f"\n[❌] Error {r.status_code}: {r.text}\n")
    except Exception as e:
        print(f"\n[⚠️] Gagal: {e}\n")

# Loop kirim pertanyaan acak
if __name__ == "__main__":
    while True:
        tanya = random.choice(pertanyaan)
        print(f"[📤] Kirim: {tanya}")
        kirim_chat(tanya)
        time.sleep(15)
