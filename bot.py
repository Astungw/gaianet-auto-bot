import requests
import random
import time

questions = [
    "Apa manfaat membaca buku setiap hari?",
    "Bagaimana cara menjadi orang yang lebih disiplin?",
    "Apa itu singularitas AI?",
    "Apa perbedaan antara etika dan moral?",
    "Bagaimana cara kerja otak manusia?",
    "Apa dampak sosial media terhadap remaja?",
    "Bagaimana teknologi mempengaruhi kehidupan modern?",
    "Apa pentingnya menjaga kesehatan mental?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar?",
    "Apa saja tantangan di era digital saat ini?",
    # Pertanyaan 11 s/d 500 berikutnya:
] + [f"Pertanyaan tambahan nomor {i}" for i in range(11, 501)]

def ask_question(token, question):
    url = "https://llama.gaia.domains/v1/chat/completions"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"model": "Llama-3.2-3B-Instruct", "messages": [{"role": "user", "content": question}]}
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code == 401: return "unauthorized"
    if r.status_code == 200: return r.json()["choices"][0]["message"]["content"]
    return f"Error {r.status_code}: {r.text}"

def validate_token(token):
    return ask_question(token, "Halo!") != "unauthorized"

# Main init
while True:
    token = input("🔑 Masukkan Bearer Token GaiaNet kamu: ").strip()
    print("🔍 Mengecek token...")
    if validate_token(token):
        print("✅ Token valid! Mulai bot...\n"); break
    print("❌ Token salah atau expired. Coba lagi.\n")

while True:
    ques = random.choice(questions)
    print(f"[📤] Kirim: {ques}")
    reply = ask_question(token, ques)
    if reply == "unauthorized":
        print("❌ Token expired. Restart bot dan masukkan token baru.")
        break
    print(f"[✅] Q: {ques}\n[🤖] A: {reply}\n")
    time.sleep(10)
