# 🤖 Gaianet Auto Bot

Bot Python otomatis untuk mengirim pertanyaan acak ke GaiaNet dan menerima balasan AI dari model `llama.gaia.domains`. Dirancang untuk farming XP node.

---

## 📦 Cara Pakai

```bash
git clone https://github.com/Astungw/gaianet-auto-bot.git
cd gaianet-auto-bot
pip install requests
python bot.py
```

## 📌 Catatan

Saat menjalankan `python bot.py`, kamu akan diminta memasukkan Bearer Token seperti ini:

Masukkan Bearer Token GaiaNet kamu:

```
gaia-xxxxx-yyyyyyyyyy
```

### 🔑 Cara mendapatkan token:
1. Buka https://www.gaianet.ai
2. Login seperti biasa
3. Tekan `Ctrl + Shift + I` (buka Developer Tools)
4. Masuk ke tab **Network**
5. Filter: `Fetch/XHR`
6. Kirim satu chat di web GaiaNet
7. Klik request ke `/v1/chat/completions`
8. Cek tab **Headers** → cari `Authorization`
9. Salin token yang diawali `Bearer gaia-...`

> ⚠️ Token ini bersifat sementara dan bisa berubah saat login ulang.

---

## 👓 Contoh Output

```
[📤] Kirim: Apa itu singularitas AI?
[✅] Q: Apa itu singularitas AI?
[📥] A: Singularitas AI adalah titik ketika AI melampaui manusia dan...
```
