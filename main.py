import streamlit as st
import time
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="JOKO SEARCH", page_icon="🔍", layout="centered")

# Fungsi untuk memutar audio otomatis saat tombol ditekan
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# --- CSS CUSTOM (Biar Tampilan Elegan & Minimalis) ---
st.markdown("""
    <style>
    .main {
        background-color: #fcfcfc;
    }
    .title-text {
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 55px;
        font-weight: 800;
        letter-spacing: -2px;
        color: #1a1a1a;
        margin-bottom: 10px;
    }
    .subtitle-text {
        text-align: center;
        color: #666;
        margin-bottom: 40px;
        font-style: italic;
    }
    .stTextInput > div > div > input {
        border-radius: 30px;
        padding: 25px;
        border: 2px solid #eee;
        transition: 0.3s;
    }
    .stTextInput > div > div > input:focus {
        border: 2px solid #1a1a1a;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    @keyframes slideIn {
        0% { transform: translateX(-120%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    .sticker-anim {
        animation: slideIn 0.8s ease-out forwards;
        width: 100%;
        max-width: 450px;
        display: block;
        margin: 30px auto;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- TAMPILAN UTAMA ---
st.markdown('<div class="title-text">JOKO SEARCH</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Pusat Informasi Terpercaya (Mungkin)</div>', unsafe_allow_html=True)

# Input pencarian (bisa sepanjang
