# Dashboard KPI IAS 2025

Streamlit app sederhana untuk dashboard KPI.

## Menjalankan lokal
```
pip install -r requirements.txt
streamlit run app/main.py
```

## Deploy ke EasyPanel (Docker)
1) Pastikan file `Dockerfile` dan `.dockerignore` ada (sudah disediakan).
2) Buat app baru di EasyPanel dengan source repo ini.
3) Set port ke `8501`.
4) Deploy.

Catatan: Streamlit harus bind ke `0.0.0.0` di port `8501`, sudah diatur di `Dockerfile`.
