import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render():
    st.title("📌 Modul 1: Aplikasi Teori Himpunan dalam Ekonomi")
    st.caption("Memetakan Batas Pilihan Mikroekonomi & Struktural Makroekonomi")
    
    st.info("""
    💡 **Intuisi Utama:** Dalam ekonomi, himpunan digunakan untuk **mendefinisikan batas (boundary)**. 
    Di Mikro, himpunan membatasi apa yang *sanggup dibeli* konsumen. Di Makro, himpunan membagikan populasi ke dalam *kategori struktural* (misal: Angkatan Kerja).
    """)
    
    # Tab Navigasi Aplikasi Mikro vs Makro
    tab_mikro, tab_makro = st.tabs(["🛒 Aplikasi Mikroekonomi", "🌐 Aplikasi Makroekonomi"])
    
    # ==========================================
    # TAB 1: MIKROEKONOMI (BUDGET SET)
    # ==========================================
    with tab_mikro:
        st.subheader("1. Himpunan Kesanggupan Belanja (*Budget Set*)")
        st.markdown("""
        Seorang konsumen menghadapi kombinasi barang $X$ dan $Y$. **Budget Set** adalah himpunan semua titik $(X, Y)$ 
        yang memenuhi syarat pertidaksamaan anggaran:
        """)
        
        st.latex(r"B = \{ (X, Y) \mid P_x X + P_y Y \le I, \quad X \ge 0, Y \ge 0 \}")
        
        col_in, col_graph = st.columns([1, 2])
        
        with col_in:
            st.markdown("**Parameter Konsumen:**")
            I = st.slider("Pendapatan / Budget (I)", 100, 1000, 500, step=50)
            Px = st.slider("Harga Barang X (Px)", 10, 100, 50, step=5)
            Py = st.slider("Harga Barang Y (Py)", 10, 100, 25, step=5)
            
            # Max units
            max_x = I / Px
            max_y = I / Py
            
            st.write(f"* Max Barang X: **{max_x:.1f}** unit")
            st.write(f"* Max Barang Y: **{max_y:.1f}** unit")
            
        with col_graph:
            # Plotting Budget Set using Matplotlib
            fig, ax = plt.subplots(figsize=(6, 4))
            
            x_vals = np.linspace(0, max_x, 100)
            y_vals = (I - Px * x_vals) / Py
            
            # Draw Budget Line
            ax.plot(x_vals, y_vals, color='red', linewidth=2, label='Garis Anggaran (Px.X + Py.Y = I)')
            
            # Fill Budget Set (Feasible Region)
            ax.fill_between(x_vals, 0, y_vals, color='green', alpha=0.3, label='Himpunan Terjangkau (Budget Set)')
            
            ax.set_xlim(0, max(max_x * 1.2, 5))
            ax.set_ylim(0, max(max_y * 1.2, 5))
            ax.set_xlabel("Kuantitas Barang X")
            ax.set_ylabel("Kuantitas Barang Y")
            ax.set_title("Daerah Feasible (Budget Set) Konsumen")
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.legend(fontsize=8)
            
            st.pyplot(fig)

    # ==========================================
    # TAB 2: MAKROEKONOMI (LABOR MARKET SETS)
    # ==========================================
    with tab_makro:
        st.subheader("2. Himpunan Ketenagakerjaan Makro (*Labor Market Sets*)")
        st.markdown("""
        Dalam indikator makroekonomi, status ketenagakerjaan didefinisikan menggunakan hierarki **Himpunan Bagian (*Subset*)**:
        * $W$ = Total Penduduk Usia Kerja
        * $L$ = Angkatan Kerja ($L \subset W$)
        * $E$ = Himpunan Bekerja ($E \subset L$)
        * $U$ = Himpunan Pengangguran ($U = L \setminus E$)
        """)
        
        col_m1, col_m2 = st.columns([1, 2])
        
        with col_m1:
            pop_kerja = st.number_input("Penduduk Usia Kerja (W) [Juta]", value=200)
            tpt_pct = st.slider("Tingkat Partisipasi Angkatan Kerja / TPAK (%)", 50, 90, 70)
            unemp_pct = st.slider("Tingkat Pengangguran Terbuka / TPT (%)", 1.0, 15.0, 5.0, step=0.5)
            
            # Calculations
            L = pop_kerja * (tpt_pct / 100)
            U = L * (unemp_pct / 100)
            E = L - U
            N = pop_kerja - L # Bukan angkatan kerja
            
        with col_m2:
            st.markdown("### 📊 Struktur Elemen Himpunan:")
            st.write(f"* **Total Angkatan Kerja ($L$):** {L:.2f} Juta Jiwa")
            st.write(f"* **Bekerja ($E$):** {E:.2f} Juta Jiwa")
            st.write(f"* **Pengangguran ($U = L \\setminus E$):** {U:.2f} Juta Jiwa")
            st.write(f"* **Bukan Angkatan Kerja ($W \\setminus L$):** {N:.2f} Juta Jiwa")
            
            # Simple bar structure
            fig2, ax2 = plt.subplots(figsize=(6, 3))
            categories = ['Bukan Angkatan Kerja', 'Bekerja (E)', 'Pengangguran (U)']
            values = [N, E, U]
            colors = ['#gray', '#2ca02c', '#d62728']
            
            ax2.barh(categories, values, color=['#8c564b', '#2ca02c', '#d62728'])
            ax2.set_xlabel("Jumlah (Juta Jiwa)")
            ax2.set_title("Pembagian Himpunan Ketenagakerjaan")
            ax2.grid(axis='x', linestyle='--', alpha=0.5)
            
            st.pyplot(fig2)

    st.markdown("---")
    
    # 3. REFLEKSI
    st.subheader("🧠 Refleksi")
    st.text_area(
        "Bagaimana perubahan definisi 'himpunan angkatan kerja' (misal: memasukkan pekerja gig/freelance) dapat mengubah statistik pengangguran suatu negara?",
        placeholder="Tuliskan pemikiran kritis Anda di sini..."
    )
