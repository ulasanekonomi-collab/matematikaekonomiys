import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render():
    st.title("📌 Modul 1: Teori Himpunan dalam Ekonomi & Sosial")
    st.caption("Mendefinisikan Batas Pilihan, Struktur Sosial, dan Kebijakan Publik")
    
    st.info("""
    💡 **Intuisi Utama:** Dalam ilmu sosial dan ekonomi, **Himpunan adalah alat pembatas (boundary maker)**. 
    Sebelum menghitung rumus atau mengukur statistik, ekonom harus menentukan siapa/apa saja yang masuk ke dalam 'pagar' analisisnya—baik itu batasan anggaran konsumen, kriteria penerima bantuan, hingga batas daya dukung lingkungan.
    """)
    
    # 3 Tab Utama
    tab_mikro, tab_makro, tab_lingkungan = st.tabs([
        "🛒 1. Mikro: Budget & Choice Set", 
        "🌐 2. Makro: Ketenagakerjaan & Kebijakan",
        "🍃 3. Lingkungan: Batas Ekologis"
    ])
    
    # ==========================================
    # TAB 1: MIKROEKONOMI
    # ==========================================
    with tab_mikro:
        st.subheader("1. Himpunan Kesanggupan Belanja (*Budget Set*)")
        st.markdown("""
        Keputusan konsumsi tidak pernah bebas tanpa batas. Konsumen dibatasi oleh **Budget Set ($B$)**, 
        yaitu himpunan semua kombinasi barang $(X, Y)$ yang sanggup dibeli dengan pendapatan $I$.
        """)
        
        st.latex(r"B = \{ (X, Y) \mid P_x X + P_y Y \le I, \quad X \ge 0, Y \ge 0 \}")
        
        col_in, col_graph = st.columns([1, 2])
        
        with col_in:
            st.markdown("**Parameter Konsumen:**")
            I = st.slider("Pendapatan / Budget (I)", 100, 1000, 500, step=50, key="b_I")
            Px = st.slider("Harga Barang X (Px)", 10, 100, 50, step=5, key="b_Px")
            Py = st.slider("Harga Barang Y (Py)", 10, 100, 25, step=5, key="b_Py")
            
            max_x = I / Px
            max_y = I / Py
            
            st.markdown("---")
            st.write(f"* Konsumsi Maksimum X: **{max_x:.1f}** unit")
            st.write(f"* Konsumsi Maksimum Y: **{max_y:.1f}** unit")
            
        with col_graph:
            fig, ax = plt.subplots(figsize=(6, 4))
            
            x_vals = np.linspace(0, max_x, 100)
            y_vals = (I - Px * x_vals) / Py
            
            ax.plot(x_vals, y_vals, color='#d62728', linewidth=2, label='Garis Anggaran (Px.X + Py.Y = I)')
            ax.fill_between(x_vals, 0, y_vals, color='#2ca02c', alpha=0.3, label='Himpunan Terjangkau / Budget Set (B)')
            
            ax.set_xlim(0, max(max_x * 1.2, 5))
            ax.set_ylim(0, max(max_y * 1.2, 5))
            ax.set_xlabel("Barang X")
            ax.set_ylabel("Barang Y")
            ax.set_title("Daerah Feasible Konsumen")
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.legend(fontsize=8)
            
            st.pyplot(fig)

    # ==========================================
    # TAB 2: MAKROEKONOMI & KEBIJAKAN
    # ==========================================
    with tab_makro:
        st.subheader("2. Partisi Himpunan Ketenagakerjaan & Kebijakan Publik")
        st.markdown("""
        Dalam makroekonomi, indikator nasional dihitung dengan melakukan **partisi himpunan**—membagi himpunan semesta populasi menjadi subset-subset yang saling lepas (*disjoint*).
        """)
        
        col_m1, col_m2 = st.columns([1, 2])
        
        with col_m1:
            pop_kerja = st.number_input("Penduduk Usia Kerja (W) [Juta Jiwa]", value=200, key="pop_w")
            tpak = st.slider("TPAK (%) - Proporsi L terhadap W", 50, 90, 70, key="tpak")
            tpt = st.slider("TPT (%) - Proporsi U terhadap L", 1.0, 15.0, 5.0, step=0.5, key="tpt")
            
            L = pop_kerja * (tpak / 100)
            U = L * (tpt / 100)
            E = L - U
            N = pop_kerja - L 
            
        with col_m2:
            st.markdown("### 📊 Operasi & Struktur Himpunan:")
            st.write(f"* **Semesta Usia Kerja ($W$):** {pop_kerja:.2f} Juta Jiwa")
            st.write(f"* **Angkatan Kerja ($L \\subset W$):** {L:.2f} Juta Jiwa")
            st.write(f"* **Bekerja ($E \\subset L$):** {E:.2f} Juta Jiwa")
            st.write(f"* **Pengangguran ($U = L \\setminus E$):** {U:.2f} Juta Jiwa")
            st.write(f"* **Bukan Angkatan Kerja ($N = W \\setminus L$):** {N:.2f} Juta Jiwa")
            
            fig2, ax2 = plt.subplots(figsize=(6, 3))
            categories = ['Bukan Angkatan Kerja (N)', 'Bekerja (E)', 'Pengangguran (U)']
            values = [N, E, U]
            
            ax2.barh(categories, values, color=['#7f7f7f', '#2ca02c', '#d62728'])
            ax2.set_xlabel("Juta Jiwa")
            ax2.set_title("Partisi Himpunan Ketenagakerjaan")
            ax2.grid(axis='x', linestyle='--', alpha=0.5)
            
            st.pyplot(fig2)

    # ==========================================
    # TAB 3: EKONOMI LINGKUNGAN
    # ==========================================
    with tab_lingkungan:
        st.subheader("3. Batas Ekologis & Himpunan Aktivitas Ekonomi")
        st.markdown("""
        Prinsip **"Bersahabat dengan Alam"** dapat diartikan secara sistematis melalui teori himpunan: 
        Aktivitas ekonomi manusia ($E$) harus berada di dalam batas Himpunan Daya Dukung Ekosistem ($S$).
        """)
        
        st.latex(r"\text{Sustainabilitas} \iff E \subseteq S")
        
        skala_ekonomi = st.slider("Skala Aktivitas Ekonomi (E)", 10, 150, 80)
        kapasitas_alam = st.slider("Batas Kapasitas Alam / Carrying Capacity (S)", 50, 100, 100)
        
        if skala_ekonomi <= kapasitas_alam:
            st.success(f"🌱 **Sistem Berkelanjutan:** $E \\subseteq S$. Seluruh aktivitas ekonomi ({skala_ekonomi}) berada dalam daya dukung alam ({kapasitas_alam}).")
        else:
            eksploitasi = skala_ekonomi - kapasitas_alam
            st.error(f"🚨 **Overshoot / Himpunan Pelanggaran:** $E \\setminus S \\neq \\emptyset$. Terjadi defisit ekologis sebesar {eksploitasi} unit!")

    st.markdown("---")
    
    # REFLEKSI
    st.subheader("🧠 Diskusikan & Refleksikan")
    st.text_area(
        "Bagaimana pendefinisian batas/kriteria keanggotaan suatu himpunan (seperti batas kriteria kemiskinan atau status angkatan kerja) dapat memengaruhi bentuk kebijakan yang dikeluarkan pemerintah?",
        placeholder="Tuliskan gagasan atau catatan Anda di sini..."
    )
