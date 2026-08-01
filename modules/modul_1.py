import streamlit as st

def render():
    st.title("📌 Modul 1: Teori Himpunan dalam Ekonomi")
    st.caption("Memahami Batas Pilihan dan Ruang Keputusan")
    
    # 1. INTUISI
    st.info("""
    💡 **Intuisi:** Himpunan pada dasarnya adalah **pagar imajiner**. 
    Sebelum mendesain kebijakan atau menghitung fungsi, ekonom harus menentukan siapa/apa saja yang ada di dalam 'pagar' analisisnya.
    """)
    
    st.markdown("---")
    
    # 2. SIMULATOR / INTERAKTIF
    st.subheader("🧪 Simulator: Himpunan Kesanggupan Belanja (Budget Set)")
    
    col_input, col_display = st.columns([1, 2])
    
    with col_input:
        pendapatan = st.slider("Pendapatan (I)", 10, 100, 50, step=10)
        p_x = st.slider("Harga Barang X (Px)", 1, 10, 2)
        p_y = st.slider("Harga Barang Y (Py)", 1, 10, 5)
        
    with col_display:
        st.write(f"**Batas Maksimum:**")
        st.latex(rf"{p_x}X + {p_y}Y \le {pendapatan}")
        st.write("Semua titik $(X, Y)$ yang memenuhi pertidaksamaan di atas adalah **anggota Himpunan Pilihan Konsumen**.")
        
        # Di sini nanti bisa ditempel grafik Plotly/Matplotlib untuk mengarsir daerah himpunannya
        
    st.markdown("---")
    
    # 3. FORMALISASI
    st.subheader("📚 Bahasa Formal Himpunan")
    st.markdown("""
    * **Notasi Pembangun Himpunan:** $S = \{ x \mid x \text{ adalah kombinasi barang yang sanggup dibeli} \}$
    * **Irisan ($\cap$):** Kombinasi yang disukai *sekaligus* sanggup dibeli.
    * **Gabungan ($\cup$):** Seluruh pilihan yang ada di Pasar A atau Pasar B.
    """)
    
    # 4. REFLEKSI
    st.subheader("🧠 Refleksi")
    st.text_area("Menurut Anda, apa yang terjadi pada 'Himpunan Pilihan Konsumen' jika terjadi inflasi hebat?", placeholder="Tuliskan pemikiran Anda...")
