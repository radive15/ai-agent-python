# AI Agent Python

Aplikasi chatbot sederhana berbasis AI yang dibangun menggunakan Python, LangChain, dan model Google Gemini. Agent ini mampu menjawab pertanyaan umum dan mengetahui tanggal hari ini secara real-time.

---

## Fungsi Aplikasi

- Menerima pertanyaan dari user melalui terminal
- Menjawab pertanyaan umum menggunakan model AI Google Gemini
- Mengetahui tanggal hari ini secara akurat melalui tool `get_date`
- Menggunakan pola **ReAct** (Reasoning + Acting) — agent berpikir dulu sebelum menjawab

---

## Teknologi yang Digunakan

| Library | Fungsi |
|---|---|
| `langchain` | Framework utama untuk membangun AI agent |
| `langchain-google-genai` | Koneksi ke model Google Gemini |
| `langgraph` | Membuat alur kerja agent (ReAct) |
| `python-dotenv` | Membaca API key dari file `.env` |

---

## Cara Instalasi

### 1. Clone atau download project ini

### 2. Buat virtual environment (opsional tapi disarankan)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install semua dependency
```bash
pip install -r requirements.txt
```

### 4. Buat file `.env` di folder project
```
GOOGLE_API_KEY=isi_dengan_api_key_kamu
```

> API key Google Gemini bisa didapat gratis di [Google AI Studio](https://aistudio.google.com)

---

## Cara Menjalankan

```bash
python main.py
```

Setelah dijalankan, ketik pertanyaan di terminal lalu tekan Enter.

```
Masukan pertanyaan: Apa ibu kota Jepang?
Ibu kota Jepang adalah Tokyo.
```

---

## Contoh Pertanyaan

```
Masukan pertanyaan: Hari ini tanggal berapa?
Masukan pertanyaan: Siapa presiden Indonesia?
Masukan pertanyaan: Jelaskan apa itu fotosintesis
```

---

## Struktur Project

```
ai-agent-python/
├── main.py          # File utama aplikasi
├── requirements.txt # Daftar library yang dibutuhkan
├── .env             # API key (buat sendiri, jangan di-upload ke GitHub)
└── README.md        # Dokumentasi ini
```

---

## Catatan

- File `.env` berisi API key yang bersifat rahasia, **jangan pernah di-upload ke GitHub**
- Pastikan koneksi internet aktif karena model Gemini berjalan di server Google
