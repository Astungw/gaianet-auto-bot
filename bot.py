import requests
import random
import time

# List pertanyaan random
questions = [
    "Apa dampak positif dan negatif dari penggunaan AI dalam kehidupan sehari-hari?",
    "Bagaimana cara kerja teknologi blockchain secara sederhana?",
    "Apa perbedaan antara kecerdasan buatan dan machine learning?",
    "Bagaimana teknologi dapat membantu sektor pendidikan di negara berkembang?",
    "Apa tantangan terbesar dalam menjaga keamanan data pribadi di era digital?",
    "Bagaimana perubahan iklim memengaruhi kehidupan manusia secara global?",
    "Apa itu energi terbarukan dan mengapa penting untuk masa depan?",
    "Bagaimana cara kerja panel surya dalam menghasilkan listrik?",
    "Apa manfaat membaca buku dibandingkan menonton video edukatif?",
    "Bagaimana cara kerja sistem imun tubuh manusia melawan virus?",
    "Apa saja faktor utama penyebab stres pada generasi muda?",
    "Bagaimana cara kerja otak saat seseorang sedang bermimpi?",
    "Apa saja kebiasaan kecil yang dapat meningkatkan produktivitas harian?",
    "Mengapa penting mempelajari sejarah peradaban manusia?",
    "Bagaimana teknologi internet mengubah cara kita berinteraksi sosial?",
    "Apa yang dimaksud dengan konsep 'sirkular ekonomi'?",
    "Bagaimana AI digunakan dalam bidang kesehatan saat ini?",
    "Mengapa penting bagi pelajar memahami literasi digital?",
    "Apa hubungan antara pola makan dan kesehatan mental?",
    "Bagaimana cara kerja pesawat terbang bisa tetap melayang di udara?",
    "Apa itu metaverse dan bagaimana pengaruhnya ke masa depan digital?",
    "Bagaimana teknologi memengaruhi kebiasaan membaca generasi sekarang?",
    "Mengapa penting melestarikan bahasa daerah dan budaya lokal?",
    "Apa itu big data dan bagaimana penggunaannya dalam bisnis?",
    "Apa saja dampak negatif dari terlalu lama menggunakan media sosial?",
    "Bagaimana proses terjadinya hujan secara ilmiah?",
    "Apa itu ekosistem dan mengapa penting bagi kelangsungan hidup?",
    "Bagaimana perubahan gaya hidup dapat membantu menjaga lingkungan?",
    "Mengapa banyak orang mengalami burnout dalam pekerjaan?",
    "Apa manfaat journaling untuk kesehatan mental?",
    "Bagaimana perkembangan AI di bidang seni dan musik?",
    "Apa itu quantum computing dan apa potensinya di masa depan?",
    "Bagaimana cara kerja teknologi GPS dalam navigasi?",
    "Mengapa penting untuk memiliki keterampilan berpikir kritis?",
    "Bagaimana algoritma rekomendasi bekerja di media sosial?",
    "Apa perbedaan antara resume dan CV dalam dunia kerja?",
    "Apa itu etika digital dan mengapa penting saat ini?",
    "Bagaimana peran AI dalam membantu tunanetra?",
    "Apa itu teknologi wearable dan contohnya?",
    "Bagaimana dampak pandemi COVID-19 terhadap pendidikan global?",
    "Apa yang dimaksud dengan digital detox?",
    "Mengapa penting menjaga keseimbangan antara kerja dan kehidupan pribadi?",
    "Apa manfaat belajar bahasa asing sejak dini?",
    "Bagaimana internet memengaruhi perkembangan bisnis kecil?",
    "Apa itu deepfake dan bagaimana dampaknya terhadap kepercayaan publik?",
    "Bagaimana cara kerja teknologi fingerprint pada smartphone?",
    "Apa saja ancaman siber yang sering terjadi dan cara mencegahnya?",
    "Mengapa penting memahami hak digital sebagai pengguna internet?",
    "Bagaimana robot digunakan di industri manufaktur?",
    "Apa itu augmented reality dan bagaimana cara kerjanya?",
    "Apa dampak AI terhadap lapangan pekerjaan di masa depan?",
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
