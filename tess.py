import streamlit as st
import pandas as pd

st.header("|-----------------------------------------------------------|")
st.title("                 TUGAS BESAR ALGORITMA                         ")
st.title("\t\t                   PEMOGRAMAN                             ")
st.header("|-----------------------------------------------------------|")
st.write()
st.write("PROGRAM STUDI SAINS DATA ")
st.write("kelas RC ")
st.write("========================================================================================")
st.write(" Anggota kelompok         ")
st.write(" Ahmad Rizqi              : 122450138 ")
st.write(" David Boby C. Nainggolan : 122450048 ")
st.write(" Diana Syafithri          : 122450141 ")
st.write(" Jaclin Alcavella         : 122450015 ")
st.write(" Siti Nur Aarifah         : 122450006 ")
st.write("========================================================================================")

d = st.date_input("Tanggal pemesanan", value=None)
st.write('Tanggal pemesanan:', d)
st.write("========================================================================================")

st.write("1. List bibit buah dan pembelian")
st.write("2. Total pembelian")
st.write("3. Keluar aplikasi")
list_menu = st.radio('Select one:', [1, 2, 3])

# Initialize session state variables
if 'Data' not in st.session_state:
    st.session_state.Data = []
    st.session_state.Total = []

if list_menu == 1:
    data = {
        'nama buah': ['apel', 'semangka', 'singkong'],
        'harga buah': [12000, 13000, 20000]
    }
  #  st.session_state.sum_harga = sum(data['harga buah'])
    data_frame = pd.DataFrame(data)
    st.table(data_frame)

    st.session_state.selected_option = st.multiselect('Pilih buah yang ingin dipesan', data['nama buah'])
    if st.session_state.selected_option:
        st.session_state.Data
        st.session_state.Data.extend(st.session_state.selected_option)
        st.write('You selected:', st.session_state.selected_option)

    if st.session_state.selected_option:
        st.session_state.jumlah = st.slider('Berapa kilo?', 0, 130, 25)
        st.write("Pesan", st.session_state.jumlah, 'KG')

elif list_menu == 2:
    if st.button("Total"):
        if 'apel' in st.session_state.Data:
            st.session_state.total1 = st.session_state.jumlah * 12000
            if st.session_state.total1 not in st.session_state.Total:
                st.session_state.Total.append(st.session_state.total1)
            st.write(f"Total pembelian dan pembayaran, Rp.{st.session_state.total1}")
        if 'semangka' in st.session_state.Data:
            st.session_state.total2 = st.session_state.jumlah * 13000
            if st.session_state.total2 not in st.session_state.Total:
                st.session_state.Total.append(st.session_state.total2)
            st.session_state.Total.append(st.session_state.total2)
            st.write(f"Total pembelian dan pembayaran, Rp.{st.session_state.total2}")
        if 'singkong' in st.session_state.Data:
            st.session_state.total3 = st.session_state.jumlah * 20000
            if st.session_state.total3 not in st.session_state.Total:
                st.session_state.Total.append(st.session_state.total3)
            st.write(f"Total pembelian dan pembayaran, Rp.{st.session_state.total3}")
            st.session_state.Total.append(st.session_state.total3)
        if len(st.session_state.selected_option) > 1:
            st.write("Total Pembayaran = ", st.session_state.sum_harga)

        st.write(st.session_state.Total)

        st.write("Total Pembayaran = ", sum(st.session_state.Total))
    
elif list_menu == 3:
    st.write("Keluar aplikasi")
    st.stop()
else:
    st.write("Pilihan tidak valid")
