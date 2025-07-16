import requests
import random
import time

questions = [
    "Apa manfaat membaca buku setiap hari?",
    "Apa manfaat membaca buku setiap hari? Jelaskan dengan contoh.",
    "Apa manfaat membaca buku setiap hari? Berikan penjelasan sederhana.",
    "Apa manfaat membaca buku setiap hari? Apa pendapat Anda?",
    "Apa manfaat membaca buku setiap hari? Apa tantangan terbesarnya?",
    "Apa manfaat membaca buku setiap hari? Apakah ada sisi negatifnya?",
    "Apa manfaat membaca buku setiap hari? Bagaimana hal ini memengaruhi generasi muda?",
    "Apa manfaat membaca buku setiap hari? Apa solusi terbaik menurut Anda?",
    "Apa manfaat membaca buku setiap hari? Jelaskan menurut sudut pandang ilmiah.",
    "Apa manfaat membaca buku setiap hari? Berikan analogi sehari-hari.",
    "Bagaimana cara meningkatkan konsentrasi saat belajar?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Jelaskan dengan contoh.",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Berikan penjelasan sederhana.",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Apa pendapat Anda?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Apa tantangan terbesarnya?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Apakah ada sisi negatifnya?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Bagaimana hal ini memengaruhi generasi muda?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Apa solusi terbaik menurut Anda?",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Jelaskan menurut sudut pandang ilmiah.",
    "Bagaimana cara meningkatkan konsentrasi saat belajar? Berikan analogi sehari-hari.",
    "Apa itu kecerdasan buatan (AI)?",
    "Apa itu kecerdasan buatan (AI)? Jelaskan dengan contoh.",
    "Apa itu kecerdasan buatan (AI)? Berikan penjelasan sederhana.",
    "Apa itu kecerdasan buatan (AI)? Apa pendapat Anda?",
    "Apa itu kecerdasan buatan (AI)? Apa tantangan terbesarnya?",
    "Apa itu kecerdasan buatan (AI)? Apakah ada sisi negatifnya?",
    "Apa itu kecerdasan buatan (AI)? Bagaimana hal ini memengaruhi generasi muda?",
    "Apa itu kecerdasan buatan (AI)? Apa solusi terbaik menurut Anda?",
    "Apa itu kecerdasan buatan (AI)? Jelaskan menurut sudut pandang ilmiah.",
    "Apa itu kecerdasan buatan (AI)? Berikan analogi sehari-hari.",
    "Mengapa penting menjaga kesehatan mental?",
    "Mengapa penting menjaga kesehatan mental? Jelaskan dengan contoh.",
    "Mengapa penting menjaga kesehatan mental? Berikan penjelasan sederhana.",
    "Mengapa penting menjaga kesehatan mental? Apa pendapat Anda?",
    "Mengapa penting menjaga kesehatan mental? Apa tantangan terbesarnya?",
    "Mengapa penting menjaga kesehatan mental? Apakah ada sisi negatifnya?",
    "Mengapa penting menjaga kesehatan mental? Bagaimana hal ini memengaruhi generasi muda?",
    "Mengapa penting menjaga kesehatan mental? Apa solusi terbaik menurut Anda?",
    "Mengapa penting menjaga kesehatan mental? Jelaskan menurut sudut pandang ilmiah.",
    "Mengapa penting menjaga kesehatan mental? Berikan analogi sehari-hari."
] + [f"Pertanyaan tambahan nomor {i}" for i in range(41, 501)]

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
