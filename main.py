import streamlit as st
import time
import base64

# --- SETUP TAMPILAN ---
st.set_page_config(page_title="JOKO SEARCH", page_icon="🔍")

# Fungsi rahasia buat muter suara otomatis
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

# CSS buat Animasi Sticker Geser & Tampilan Ala Google
st.markdown("""
    <style>
    @keyframes slideIn {
        0% { transform: translateX(-100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    .sticker-anim {
        animation: slideIn 1.2s ease-out forwards;
        width: 100%;
        max-width: 400px;
        display: block;
        margin: 20px auto;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
    }
    .logo-text {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

# --- FOTO PRABOWO BISIK-BISIK ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("bisik.png", use_container_width=True)

# --- LOGO JOKO SEARCH WARNA-WARNI ---
st.markdown('<div class="logo-text">'
            '<span style="color: #4285F4;">J</span><span style="color: #EA4335;">O</span>'
            '<span style="color: #FBBC05;">K</span><span style="color: #34A853;">O</span>'
            ' <span style="color: #4285F4;">S</span><span style="color: #EA4335;">E</span>'
            '<span style="color: #FBBC05;">A</span><span style="color: #34A853;">R</span>'
            '<span style="color: #4285F4;">C</span><span style="color: #EA4335;">H</span>'
            '</div>', unsafe_allow_html=True)

# --- KOTAK PENCARIAN ---
query = st.text_input("", placeholder="Tanyakan apa saja ke Pak Joko...", label_visibility="collapsed")

if st.button("Joko Search"):
    if query:
        with st.spinner('Menghubungi Istana Bogor...'):
            time.sleep(1.5)
        
        # Mainkan Suara
        play_audio("sound.mp3")

        # Munculkan Sticker dengan Animasi Geser
        with open("sticker.png", "rb") as f:
            img_data = f.read()
            img_b64 = base64.b64encode(img_data).decode()
            st.markdown(f'<img src="data:image/png;base64,{img_b64}" class="sticker-anim">', unsafe_allow_html=True)
            
        st.balloons()
    else:
        st.warning("Isi dulu pertanyaannya, Mas!")

st.markdown("<br><p style='text-align: center; color: gray; font-size: 10px;'>© 2026 JOKO SEARCH - Yo Ndak Tau Kok Tanya Saya</p>", unsafe_allow_html=True)
