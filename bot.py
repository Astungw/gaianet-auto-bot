import requests
import random
import time

API_URL = "https://llama.gaia.domains/v1/chat/completions"
API_KEY = "Bearer gaia-NTdjODMyM2ItMDdiNC00OTA0LThiOGEtNDQ1NTRlMGVjZGZi-3v4tDCS7I3s_I8XW"

headers = {
    "Content-Type": "application/json",
    "Authorization": API_KEY
}

pertanyaan = [
    "Apa itu singularitas AI?",
    "Bagaimana AI bisa membantu manusia?",
    "Kenapa penting menjaga lingkungan?",
    "Apa peran blockchain di masa depan?",
    "Apa itu gaya gravitasi?",
    "Jelaskan revolusi industri 4.0!",
    "Apa manfaat membaca buku setiap hari?"
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
            print(f"[✅] Q: {pesan}\n[🤖] A: {isi['choices'][0]['message']['content']}\n")
        else:
            print(f"[❌] Error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[⚠️] Gagal: {e}")

# Main loop
if __name__ == "__main__":
    while True:
        tanya = random.choice(pertanyaan)
        print(f"[📤] Kirim: {tanya}")
        kirim_chat(tanya)
        time.sleep(15)
