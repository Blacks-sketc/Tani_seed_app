import streamlit as st
import pandas as pd

# Initialize session state variables
if 'alamat' not in st.session_state:
    st.session_state.alamat = ""
if 'no_telepon' not in st.session_state:
    st.session_state.no_telepon = ""
if 'metode_pembayaran' not in st.session_state:
    st.session_state.metode_pembayaran = ""
if 'tanggal_pemesanan' not in st.session_state:
    st.session_state.tanggal_pemesanan = None
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = []
if 'jumlah' not in st.session_state:
    st.session_state.jumlah = 0
if 'Total' not in st.session_state:
    st.session_state.Total = []

def main():
    st.set_page_config(page_title="Tani Seed", page_icon="logo.jpg")
    st.sidebar.title("TUGAS BESAR ALGORITMA")
    st.sidebar.title("PEMOGRAMAN")
    st.sidebar.write()
    st.sidebar.write("PROGRAM STUDI SAINS DATA")
    st.sidebar.write("kelas RC")
    st.sidebar.write("-------------------------")
    st.sidebar.write(" Anggota kelompok         ")
    st.sidebar.write(" Ahmad Rizqi              : 122450138 ")
    st.sidebar.write(" David Boby C. Nainggolan : 122450048 ")
    st.sidebar.write(" Diana Syafithri          : 122450141 ")
    st.sidebar.write(" Jaclin Alcavella         : 122450015 ")
    st.sidebar.write(" Siti Nur Aarifah         : 122450006 ")

    st.header("🍎---------------------------------------------------🍎")
    st.title("TaniSeed: Platform Penjualan Bibit Buah ")
    st.header("🍎---------------------------------------------------🍎")

    st.session_state.tanggal_pemesanan = st.date_input("Tanggal pemesanan", value=None)
    st.write('Tanggal pemesanan:', st.session_state.tanggal_pemesanan)

    st.session_state.alamat = st.text_area("Alamat Pengiriman", st.session_state.alamat)
    st.session_state.no_telepon = st.text_input("Nomor Telepon", st.session_state.no_telepon)
  
    st.session_state.metode_pembayaran = st.radio('Pilih metode pembayaran:', [ 'OVO', 'GoPay', 'Dana'])

    st.write("========================================================================================")

    list_menu = st.radio('Select one:', ["list buah dan harga", "total dan pembayaran", "keluar aplikasi"])

    if list_menu == "list buah dan harga":
        list_buah()

    elif list_menu == "total dan pembayaran":
        total()

    elif list_menu == "keluar aplikasi":
        save_to_excel()
        st.write("TERIMA KASIH TELAH BERBELANJA DI TOKO KAMI 😁")
        st.image('logo.jpg')
        st.write("UNTUK INFO LEBIH LANJUT AKAN DIINFOKAN LANGSUNG KE PEMBELI")
        st.stop()

    else:
        st.write("Pilihan tidak valid")

def list_buah():
    data = {
        'nama buah': ['apel', 'jeruk purut', 'jeruk', 'mangga', 'strowberi', 'pepaya', 'alpukat mentega', 'manggis ungu', 'rambutan rapiah', 'apel india', 'delima turki', 'red raspberry', 'srikaya jumbo', 'rambutan binjai', 'belimbing madu', 'jambu bji merah', 'kiwi'],
        'harga per 30 biji': [12000, 13000, 20000, 32000, 10000, 30000, 40000, 30000, 100000, 70000, 115000, 85000, 105000, 55000, 55000, 52000, 12000]
    }

    data_frame = pd.DataFrame(data)
    st.table(data_frame)

    st.session_state.selected_option = st.multiselect('Pilih bibit buah yang ingin dipesan', data['nama buah'])

    if st.session_state.selected_option:
        st.session_state.jumlah = st.slider('Berapa pcs?', 0, 100, 2)
        st.write("Pesan", st.session_state.jumlah, 'pcs')

def total():
    if st.button("Total"):
        st.session_state.Total = []

        for buah in st.session_state.selected_option:
            total_pembelian = st.session_state.jumlah * get_harga_buah(buah)
            st.session_state.Total.append(total_pembelian)
            st.write(f"Total pembelian dan pembayaran {buah.capitalize()}, Rp.{total_pembelian}")
        st.write('---------------------------------------------')
        st.write('Tanggal pemesanan:', st.session_state.tanggal_pemesanan)
        st.write("Total Pembayaran = ", sum(st.session_state.Total))
        st.write("Alamat Pengiriman:", st.session_state.alamat)
        st.write("Nomor Telepon:", st.session_state.no_telepon)
        st.write(f"Metode Pembayaran: {st.session_state.metode_pembayaran}")
        st.image('bayar.jpg')

def get_harga_buah(nama_buah):
    data = {
        'nama buah': ['apel', 'jeruk purut', 'jeruk', 'mangga', 'strowberi', 'pepaya', 'alpukat mentega', 'manggis ungu', 'rambutan rapiah', 'apel india', 'delima turki', 'red raspberry', 'srikaya jumbo', 'rambutan binjai', 'belimbing madu', 'jambu bji merah', 'kiwi'],
        'harga per 30 biji': [12000, 13000, 20000, 32000, 10000, 30000, 40000, 30000, 100000, 70000, 115000, 85000, 105000, 55000, 55000, 52000, 12000]
    }

    return data['harga per 30 biji'][data['nama buah'].index(nama_buah)]

def save_to_excel():
    df = pd.DataFrame({
        'Tanggal Pemesanan': [st.session_state.tanggal_pemesanan],
        'Alamat Pengiriman': [st.session_state.alamat],
        'Nomor Telepon': [st.session_state.no_telepon],
        'Metode Pembayaran': [st.session_state.metode_pembayaran],
        'Total Pembayaran': [sum(st.session_state.Total)]
    })

    df.to_excel('data_pembelian.xlsx', index=False)

if __name__ == "__main__":
    main()
