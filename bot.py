import requests
import random
import time

# List pertanyaan random
questions = [
    "Apa manfaat membaca buku setiap hari?",
    "Apa itu singularitas AI?",
    "Bagaimana AI bisa membantu manusia?",
    "Apa perbedaan antara etika dan moral?",
    "Apa itu gaya gravitasi?",
    "Bagaimana cara kerja otak manusia?",
    "Mengapa penting menjaga kesehatan mental?",
    "Apa dampak sosial media terhadap anak muda?",
    "Bagaimana cara menjadi kreatif setiap hari?",
    "Apa saja tantangan dalam era digital saat ini?"
]

# Fungsi untuk mengirim pertanyaan ke API
def ask_question(token, question):
    url = "https://llama.gaia.domains/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Llama-3.2-3B-Instruct",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 401:
            return "unauthorized"
        elif response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            return reply
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception: {e}"

# Fungsi untuk validasi token
def validate_token(token):
    test_question = "Halo!"
    result = ask_question(token, test_question)
    return result != "unauthorized"

# Main
while True:
    token = input("🔑 Masukkan Bearer Token GaiaNet kamu: ").strip()
    print("🔍 Mengecek token...")
    if validate_token(token):
        print("✅ Token valid! Bot mulai berjalan...\n")
        break
    else:
        print("❌ Token tidak valid atau expired. Coba salin ulang dari DevTools.\n")

# Jalankan loop bot
while True:
    question = random.choice(questions)
    print(f"[📤] Kirim: {question}")
    reply = ask_question(token, question)

    if reply == "unauthorized":
        print("❌ Token expired saat berjalan. Silakan jalankan ulang bot dan masukkan token baru.")
        break
    elif "Error" in reply or "Exception" in reply:
        print(reply)
    else:
        print(f"[✅] Q: {question}")
        print(f"[🤖] A: {reply}\n")

    time.sleep(10)  # jeda antar pertanyaan
