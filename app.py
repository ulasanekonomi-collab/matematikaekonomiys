import streamlit as st
from modules import modul_0

# 1. Konfigurasi Halaman (Lebar Layar & Icon)
st.set_page_config(
    page_title="Matematika Ekonomi Interaktif",
    page_icon="📐",
    layout="wide", # Pakai "wide" agar ruang simulasi lebih lega
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Sedikit biar Tampilan Enakeun
st.markdown("""
    <style>
    /* Merapikan jarak padding atas */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    /* Warna aksen kartu/info box */
    .stAlert {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigasi
with st.sidebar:
    st.title("📐 Matek Ekonomi")
    st.caption("Berdasarkan Pendekatan Alpha Chiang")
    st.markdown("---")
    
    st.subheader("📚 Daftar Modul")
    pilihan_modul = st.radio(
        "Pilih Materi:",
        [
            "0.1 Realita & Model",
            "1.1 Teori Himpunan (Draft)",
            "2.1 Fungsi & Pemetaan (Draft)"
        ],
        index=0
    )
    
    st.markdown("---")
    st.caption("🚀 *Dikembangkan untuk Pembelajaran Interaktif*")

# 4. Main Area Router
if pilihan_modul == "0.1 Realita & Model":
    modul_0.render()
elif pilihan_modul == "1.1 Teori Himpunan (Draft)":
    st.title("🛠️ Modul 1.1: Teori Himpunan")
    st.info("Modul ini sedang dalam tahap pengembangan.")
elif pilihan_modul == "2.1 Fungsi & Pemetaan (Draft)":
    st.title("🛠️ Modul 2.1: Fungsi & Pemetaan")
    st.info("Modul ini sedang dalam tahap pengembangan.")
