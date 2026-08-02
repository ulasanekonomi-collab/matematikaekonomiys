import streamlit as st

def render():
    st.title("📌 Modul 1: Teori Himpunan (Set Theory)")
    st.caption("Fondasi Matematika Ekonomi berdasarkan Pendekatan Alpha C. Chiang")
    
    # BANNER MOTIVASI / URGENSI
    st.info("""
    💡 **Pertanyaan Mendasar:** *Mengapa Ekonom Harus Memahami Teori Himpunan?*
    
    Teori himpunan bukan sekadar topik matematika murni, melainkan **bahasa dasar untuk membangun kerangka berpikir ekonomi**. Sebelum ekonom bisa mengukur ($quantitative$), ia harus mampu mendefinisikan dan mengelompokkan ($qualitative/logical$).
    """)
    
    # EXPANDER: KEGUNAAN PENELITIAN & DECISION MAKING
    with st.expander("🎯 **Mengapa Teori Himpunan Penting dalam Penelitian & Decision Making? (Klik untuk membuka)**", expanded=True):
        col_res, col_dec = st.columns(2)
        
        with col_res:
            st.markdown("### 🔬 1. Dalam Penelitian (*Research*)")
            st.markdown("""
            * **Mendefinisikan Ruang Analisis (*Domain*):** Menentukan batas nilai variabel yang valid (misal: investasi $I \ge 0$, konsumsi $C \ge 0$).
            * **Partisi Data Sosial-Ekonomi:** Membagi data populasi besar menjadi *subset-subset* saling lepas untuk menghitung tingkat kemiskinan, kemiskinan ekstrem, atau ketimpangan.
            * **Aksioma Teori Ekonomi:** Landasan teori preferensi konsumen dan teori permainan (*Game Theory*) sepenuhnya dibangun dari aksioma himpunan.
            """)
            
        with col_dec:
            st.markdown("### 🎯 2. Dalam Pengambilan Keputusan (*Decision Making*)")
            st.markdown("""
            * **Memetakan Batas Pilihan (*Feasible Set*):** Keputusan optimal adalah memilih elemen terbaik dari himpunan yang sanggup dijangkau ($x \in X$).
            * **Targeting Kebijakan Publik:** Menentukan kriteria keanggotaan penerima subsidi/bansos. Kesalahan targeting secara matematis adalah kekeliruan menentukan *subset* dan *komplemen*.
            * **Ruang Strategi & Risiko:** Memetakan seluruh kemungkinan aksi lawan dan variabel luar dalam pemodelan kebijakan/bisnis.
            """)

    st.markdown("---")

    # TAB UTAMA CHIANG
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Definisi & Notasi", 
        "2. Hubungan Antar Himpunan", 
        "3. Operasi Himpunan", 
        "4. Aturan / Hukum Himpunan"
    ])
    
    # ==========================================
    # TAB 1: DEFINISI & NOTASI
    # ==========================================
    with tab1:
        st.subheader("1. Penulisan Himpunan & Jenis Sifatnya")
        st.markdown("""
        Alpha Chiang menjelaskan dua cara utama menuliskan himpunan:
        1. **Cara Enumerasi / Roster Method:** Menyebutkan seluruh anggotanya satu per satu.
           * *Contoh:* S = {Rupiah, Dollar, Yen, Euro}
        2. **Cara Deskripsi / Set-Builder Method:** Menyebutkan syarat keanggotaannya.
           * *Contoh:* S = {x | x adalah mata uang utama dunia}
        """)
        
        st.markdown("---")
        st.subheader("Finite Set vs. Infinite Set")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("🔢 **Himpunan Terhingga (Finite Set)**")
            st.write("Jumlah anggotanya terbatas dan dapat dihitung pasti.")
            st.latex(r"A = \{ x \mid x \text{ adalah BUMN di Indonesia} \}")
            st.caption("Jumlah perusahaan BUMN terbatas.")
            
        with col2:
            st.warning("♾️ **Himpunan Tak Hingga (Infinite Set)**")
            st.write("Jumlah anggotanya tidak terbatas/kontinu.")
            st.latex(r"P = \{ p \mid p > 0 \}")
            st.caption("Himpunan harga p yang mungkin bernilai kontinu dari 0 hingga tak terhingga.")

    # ==========================================
    # TAB 2: HUBUNGAN ANTAR HIMPUNAN
    # ==========================================
    with tab2:
        st.subheader("2. Hubungan Antar Himpunan (Set Relations)")
        st.markdown("""
        * **Subset (A ⊆ B):** Setiap elemen A juga merupakan elemen B.
        * **Proper Subset (A ⊂ B):** A adalah subset B, dan A ≠ B.
        * **Equal Sets (A = B):** A ⊆ B dan B ⊆ A.
        * **Disjoint Sets (A ∩ B = ∅):** Dua himpunan yang tidak memiliki satu pun anggota yang sama.
        """)
        
        st.markdown("---")
        st.subheader("🧪 Uji Hubungan Ekonomi:")
        opsi_relasi = st.selectbox(
            "Pilih Contoh Hubungan Himpunan Ekonomi:",
            [
                "Himpunan Mobil Listrik vs Himpunan Otomotif (Subset)",
                "Himpunan Barang Normal vs Himpunan Barang Inferior (Disjoint)"
            ]
        )
        
        if "Subset" in opsi_relasi:
            st.info("💡 **Penjelasan:** Semua produsen mobil listrik (A) adalah produsen otomotif (B), maka A ⊂ B.")
        else:
            st.info("💡 **Penjelasan:** Suatu barang tidak bisa menjadi barang normal sekaligus inferior pada tingkat pendapatan yang sama, maka A ∩ B = ∅.")

    # ==========================================
    # TAB 3: OPERASI PADA HIMPUNAN
    # ==========================================
    with tab3:
        st.subheader("3. Operasi pada Himpunan (Set Operations)")
        st.markdown("""
        Untuk membangun **familiarisasi**, mari kita bedah operasi himpunan menggunakan contoh kasus nyata di tingkat regional:
        * **Semesta Pembicaraan (S):** Seluruh UMKM terdaftar = `{A, B, C, D, E, F}`
        * **Himpunan A (Penerima Subsidi Modal):** `{A, B, C, D}`
        * **Himpunan B (Adopsi Digital / E-Commerce):** `{C, D, E}`
        """)
        
        st.markdown("---")
        st.markdown("### ✍️ Contoh Kerja & Proses Analisis:")
        
        # Penjelasan langkah kerja
        st.markdown("""
        1. **Gabungan (Union: A ∪ B)**
           * *Makna Ekonomi:* Seluruh UMKM yang tersentuh program (baik subsidi modal *atau* digitalisasi).
           * *Proses:* Menggabungkan seluruh anggota tanpa duplikasi $\to$ `{A, B, C, D, E}`.
           
        2. **Irisan (Intersection: A ∩ B)**
           * *Makna Ekonomi:* UMKM unggulan yang **sekaligus** menerima subsidi **dan** sudah go-digital.
           * *Proses:* Mencari anggota yang muncul di kedua himpunan $\to$ `{C, D}`.
           
        3. **Selisih (Difference: A \\ B)**
           * *Makna Ekonomi:* UMKM yang hanya menerima subsidi modal, **tetapi belum** mengadopsi digital.
           * *Proses:* Anggota Himpunan A yang dibuang elemennya jika ada di B $\to$ `{A, B}`.
           
        4. **Komplemen (Complement: Aᶜ)**
           * *Makna Ekonomi:* UMKM di kota tersebut yang **tidak** tersentuh sama sekali oleh program subsidi modal.
           * *Proses:* Anggota Semesta $S$ yang tidak ada di A $\to$ `{E, F}`.
        """)
        
        st.markdown("---")
        st.markdown("### 🧪 Simulator Interaktif Operasi")
        
        # Variabel interaktif praktis
        set_S = {"UMKM-A", "UMKM-B", "UMKM-C", "UMKM-D", "UMKM-E", "UMKM-F"}
        set_A = {"UMKM-A", "UMKM-B", "UMKM-C", "UMKM-D"}
        set_B = {"UMKM-C", "UMKM-D", "UMKM-E"}
        
        st.write(f"* **Himpunan Semesta (S):** `{set_S}`")
        st.write(f"* **Himpunan A (Subsidi):** `{set_A}`")
        st.write(f"* **Himpunan B (Digital):** `{set_B}`")
        
        op = st.radio("Pilih Operasi untuk Dilihat Hasilnya:", [
            "Gabungan (A ∪ B)", 
            "Irisan (A ∩ B)", 
            "Selisih (A \\ B)",
            "Komplemen A (Aᶜ)"
        ])
        
        if "Gabungan" in op:
            res = set_A.union(set_B)
            st.success(f"**Hasil Gabungan (A ∪ B):** `{res}`")
        elif "Irisan" in op:
            res = set_A.intersection(set_B)
            st.success(f"**Hasil Irisan (A ∩ B):** `{res}`")
        elif "Selisih" in op:
            res = set_A.difference(set_B)
            st.success(f"**Hasil Selisih (A \\ B):** `{res}`")
        else:
            res = set_S.difference(set_A)
            st.success(f"**Hasil Komplemen A (Aᶜ):** `{res}`")

    # ==========================================
    # TAB 4: ATURAN / HUKUM HIMPUNAN
    # ==========================================
    with tab4:
        st.subheader("4. Aturan & Hukum Operasi Himpunan (Laws of Set Operations)")
        st.markdown("""
        Hukum-hukum ini memastikan logika berpikir ekonom tetap konsisten saat mengolah data atau memetakan ruang pilihan kebijakan.
        
        | Nama Hukum | Operasi Gabungan (∪) | Operasi Irisan (∩) |
        | :--- | :--- | :--- |
        | **Komutatif** | A ∪ B = B ∪ A | A ∩ B = B ∩ A |
        | **Asosiatif** | (A ∪ B) ∪ C = A ∪ (B ∪ C) | (A ∩ B) ∩ C = A ∩ (B ∩ C) |
        | **Distributif** | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
        | **De Morgan** | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ | (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ |
        """)
        
        st.markdown("---")
        st.subheader("✍️ Contoh Kerja Familiarisasi Hukum De Morgan")
        st.markdown("""
        Mari kita buktikan **Hukum De Morgan Pertama: $(A \\cup B)^c = A^c \\cap B^c$** menggunakan data simulasi pasar kerja:
        * **Semesta ($S$):** Seluruh Angkatan Kerja = `{Karyawan A, Karyawan B, Karyawan C, Karyawan D, Karyawan E}`
        * **Himpunan A (Punya Sertifikasi Digital):** `{Karyawan A, Karyawan B}`
        * **Himpunan B (Punya Gelar Sarjana):** `{Karyawan B, Karyawan C}`
        """)
        
        col_ruas_kiri, col_ruas_kanan = st.columns(2)
        
        with col_ruas_kiri:
            st.info("👈 **Sisi Kiri: $(A \\cup B)^c$**")
            st.markdown("""
            1. Cari Gabungan $(A \\cup B)$: `{A, B, C}`
            2. Cari Komplemennya $((A \\cup B)^c)$: Ambil anggota $S$ yang tidak ada di gabungan.
            * **Hasil Sisi Kiri:** `{Karyawan D, Karyawan E}`
            * *Makna:* Pekerja yang **TIDAK** memiliki sertifikasi digital *maupun* gelar sarjana.
            """)
            
        with col_ruas_kanan:
            st.success("👉 **Sisi Kanan: $A^c \\cap B^c$**")
            st.markdown("""
            1. Cari $A^c$ (Tidak sertifikasi): `{C, D, E}`
            2. Cari $B^c$ (Tidak sarjana): `{A, D, E}`
            3. Cari Irisannya ($A^c \\cap B^c$): Cari anggota yang sama.
            * **Hasil Sisi Kanan:** `{Karyawan D, Karyawan E}`
            * *Makna:* Pekerja yang tidak sertifikasi **SEKALIGUS** tidak sarjana.
            """)
            
        st.warning("✅ **Kesimpulan:** Ruas Kiri = Ruas Kanan (`{Karyawan D, Karyawan E}`). Hukum De Morgan terbukti sahih secara eksplisit!")

        st.markdown("---")
        st.subheader("🧪 Pembukti Logika Interaktif")
        
        pilihan_hukum = st.selectbox(
            "Pilih Hukum Himpunan yang Ingin Diuji Logikanya:",
            [
                "Hukum Komutatif (A ∪ B = B ∪ A)",
                "Hukum Distributif: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
                "Hukum De Morgan: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ"
            ]
        )
        
        # Set Data Simulasi Interaktif
        S = {"1", "2", "3", "4", "5", "6"}
        A = {"1", "2", "3"}
        B = {"3", "4"}
        C = {"4", "5"}
        
        if "Komutatif" in pilihan_hukum:
            kiri = A.union(B)
            kanan = B.union(A)
            st.write(f"* **Ruas Kiri (A ∪ B):** `{kiri}`")
            st.write(f"* **Ruas Kanan (B ∪ A):** `{kanan}`")
            st.success("🎉 Hasil kedua ruas SAMA KANONIK. Komutatif berlaku!")
            
        elif "Distributif" in pilihan_hukum:
            kiri = A.intersection(B.union(C))
            kanan = A.intersection(B).union(A.intersection(C))
            st.write(f"* **Ruas Kiri `A ∩ (B ∪ C)`:** `{kiri}`")
            st.write(f"* **Ruas Kanan `(A ∩ B) ∪ (A ∩ C)`:** `{kanan}`")
            st.success("🎉 Hasil kedua ruas SAMA KANONIK. Distributif berlaku!")
            
        else:
            kiri = S.difference(A.union(B))
            Ac = S.difference(A)
            Bc = S.difference(B)
            kanan = Ac.intersection(Bc)
            st.write(f"* **Ruas Kiri `(A ∪ B)ᶜ`:** `{kiri}`")
            st.write(f"* **Ruas Kanan `Aᶜ ∩ Bᶜ`:** `{kanan}`")
            st.success("🎉 Hasil kedua ruas SAMA KANONIK. De Morgan berlaku!")

        st.markdown("---")
        st.subheader("🧠 Refleksi Sederhana")
        st.text_area(
            "Mengapa saat membuat program Bantuan Sosial (Bansos), pemerintah lebih efisien menggunakan formula De Morgan (mendaftar syarat yang TIDAK berhak) dibanding mendaftar satu per satu orang yang berhak?",
            height=100,
            placeholder="Tuliskan gagasan Anda di sini..."
        )
