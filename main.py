import streamlit as st
import time
import base64

# --- CONFIG ---
st.set_page_config(page_title="JOKO SEARCH", page_icon="🔍")

# Fungsi Audio yang lebih kuat biar bunyi
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # Pakai iframe tersembunyi supaya auto-play lebih galak di beberapa browser
        md = f"""
            <iframe src="data:audio/mp3;base64,{b64}" allow="autoplay" style="display:none" id="iframeAudio"></iframe>
            <audio autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# --- CSS TAMPILAN ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .joko-header {
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-size: 50px;
        color: #202124;
        margin-top: 20px;
    }
    /* Kotak Input & Tombol Search */
    .stTextInput > div > div > input {
        border-radius: 24px 0 0 24px !important;
        padding: 25px !important;
    }
    div.stButton > button {
        background-color: #1a73e8 !important;
        color: white !important;
        border-radius: 0 24px 24px 0 !important;
        height: 52px !important;
        width: 60px !important;
        border: none !important;
    }
    @keyframes slideFromLeft {
        0% { transform: translateX(-100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    .hasil-joko {
        animation: slideFromLeft 0.8s ease-out;
        display: block;
        margin: 30px auto;
        max-width: 400px;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- FOTO BISIK (DI PALING ATAS) ---
col_1, col_2, col_3 = st.columns([1, 2, 1])
with col_2:
    try:
        st.image("bisik.png", use_container_width=True)
    except:
        st.error("File bisik.png nggak ketemu di GitHub, Faldo!")

# --- JUDUL ---
st.markdown('<div class="joko-header">JOKO SEARCH</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5f6368; margin-bottom: 30px;'>Cari jawaban maut di sini.</p>", unsafe_allow_html=True)

# --- LAYOUT SEARCH ---
c_space, c_input, c_btn, c_space2 = st.columns([1, 4, 0.6, 1])

with c_input:
    query = st.text_input("", placeholder="Tulis rahasia negara...", label_visibility="collapsed")

with c_btn:
    search_clicked = st.button("🔍")

# --- LOGIKA ---
if search_clicked:
    if query:
        with st.spinner('Menunggu bisikan istana...'):
            time.sleep(1.2)
        
        # 1. Mainkan Suara
        try:
            play_audio("sound.mp3")
