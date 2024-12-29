import pandas as pd
import matplotlib.pyplot as plt
import math
import streamlit as st
import base64
import plotly.express as px
from diem_tuong_duong_2019 import diem_tuong_duong

# Background
df_2020 = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Title
original_title = '<p style="font-family:Arial; color:Black; font-size: 32px; text-align: center; font-weight:600">WEB TRA CỨU ĐIỂM THI CỦA THÍ SINH</p>'
st.markdown(original_title, unsafe_allow_html=True)


# Nhập thông tin
sbd_str = st.text_input("Nhập số báo danh của bạn")


# MAIN
# Khai báo
df_2020 = pd.read_csv("C:\\Users\\ADMIN\\Repo\\Web\\diem_thi_2020.csv", dtype={'sbd': str})
df_2020.columns = ['sbd','toan','van','ly','hoa','sinh','su','dia','gdcd','nn','ma_nn']
df_2020['KHTN'] = df_2020['ly'] + df_2020['hoa'] + df_2020['sinh']
df_2020['KHXH'] = df_2020['su'] + df_2020['dia'] + df_2020['gdcd']
df_2020['N1'] = df_2020[df_2020['ma_nn'] == 'N1']['nn']
df_2020['N1'] = df_2020[df_2020['ma_nn'] == 'N1']['nn']
df_2020['N2'] = df_2020[df_2020['ma_nn'] == 'N2']['nn']
df_2020['N3'] = df_2020[df_2020['ma_nn'] == 'N3']['nn']
df_2020['N4'] = df_2020[df_2020['ma_nn'] == 'N4']['nn']
df_2020['N5'] = df_2020[df_2020['ma_nn'] == 'N5']['nn']
df_2020['N6'] = df_2020[df_2020['ma_nn'] == 'N6']['nn']
df_2020['N7'] = df_2020[df_2020['ma_nn'] == 'N7']['nn']

df_2020['sbd'] = df_2020['sbd'].astype(str)
tinh = ['THÀNH PHỐ HÀ NỘI', 'THÀNH PHỐ HỒ CHÍ MINH', 'THÀNH PHỐ HẢI PHÒNG', 'THÀNH PHỐ ĐÀ NẴNG', 'TỈNH HÀ GIANG', 'TỈNH CAO BẰNG', 'TỈNH LAI CHÂU', 'TỈNH LÀO CAI', 'TỈNH TUYÊN QUANG', 'TỈNH LẠNG SƠN', 'TỈNH BẮC KẠN', 'TỈNH THÁI NGUYÊN', 'TỈNH YÊN BÁI', 'TỈNH SƠN LA', 
        'TỈNH PHÚ THỌ', 'TỈNH VĨNH PHÚC', 'TỈNH QUẢNG NINH', 'TỈNH BẮC GIANG', 'TỈNH BẮC NINH', 'TỈNH HẢI DƯƠNG', 'TỈNH HƯNG YÊN', 'TỈNH HÒA BÌNH', 'TỈNH HÀ NAM', 'TỈNH NAM ĐỊNH', 'TỈNH THÁI BÌNH', 'TỈNH NINH BÌNH', 'TỈNH THANH HÓA', 'TỈNH NGHỆ AN', 'TỈNH HÀ TĨNH', 
        'TỈNH QUẢNG BÌNH', 'TỈNH QUẢNG TRỊ', 'TỈNH THỪA THIÊN-HUẾ', 'TỈNH QUẢNG NAM', 'TỈNH QUẢNG NGÃI', 'TỈNH KON TUM', 'TỈNH BÌNH ĐỊNH', 'TỈNH GIA LAI', 'TỈNH PHÚ YÊN', 'TỈNH ĐĂK LĂK', 'TỈNH KHÁNH HÒA', 'TỈNH LÂM ĐỒNG', 'TỈNH BÌNH PHƯỚC', 'TỈNH BÌNH DƯƠNG', 
        'TỈNH NINH THUẬN', 'TỈNH TÂY NINH', 'TỈNH BÌNH THUẬN', 'TỈNH ĐỒNG NAI', 'TỈNH LONG AN', 'TỈNH ĐỒNG THÁP', 'TỈNH AN GIANG', 'TỈNH BÀ RỊA-VŨNG TÀU', 'TỈNH TIỀN GIANG', 'TỈNH KIÊN GIANG', 'THÀNH PHỐ CẦN THƠ', 'TỈNH BẾN TRE', 'TỈNH VĨNH LONG', 'TỈNH TRÀ VINH', 
        'TỈNH SÓC TRĂNG', 'TỈNH BẠC LIÊU', 'TỈNH CÀ MAU', 'TỈNH ĐIỆN BIÊN', 'TỈNH ĐĂK NÔNG', 'TỈNH HẬU GIANG']


sbd = df_2020['sbd'].to_list()

for i in range(len(sbd)):
    if sbd_str == sbd[i]:
        index = i
        break



try:
    # Tránh in xấu
    if sbd_str != "":
        tmp = index
        st.write("Điểm thi thành phần của bạn là:")
        m1, m2, m3, m4, m5, m6, m7, m8, m9 = st.columns(9)
        with m1:
            st.write("Toán")
            st.write(df_2020['toan'].iloc[index])
        with m2:
            st.write("Ngữ văn")
            st.write(df_2020['van'].iloc[index])
        with m3:
            st.write("Ng.ngữ")
            st.write(df_2020['nn'].iloc[index])
        with m4:
            st.write("Vật lý")
            st.write(df_2020['ly'].iloc[index])
        with m5:
            st.write("Hóa học")
            st.write(df_2020['hoa'].iloc[index])
        with m6:
            st.write("Sinh học")
            st.write(df_2020['sinh'].iloc[index])
        with m7:
            st.write("Lịch sử")
            st.write(df_2020['su'].iloc[index])
        with m8:
            st.write("Địa lý")
            st.write(df_2020['dia'].iloc[index])
        with m9:
            st.write("GDCD")
            st.write(df_2020['gdcd'].iloc[index])

        khoi = ""
        khoi = st.text_input("Nhập khối thi của bạn. Cần nhập đúng dạng (A00, A01,..., B00, B01,...)")

        # Tránh in xấu
        if khoi != "":
            # Check điểm các khối
            if khoi == 'A00':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['hoa'].loc[index]
                df_2020['A00'] = df_2020['toan'] + df_2020['ly'] + df_2020['hoa']
            elif khoi == 'A01':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['N1'].loc[index]
                df_2020['A01'] = df_2020['toan'] + df_2020['ly'] + df_2020['N1']
            elif khoi == 'A02':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['sinh'].loc[index]
                df_2020['A02'] = df_2020['toan'] + df_2020['ly'] + df_2020['sinh']
            elif khoi == 'A03':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['su'].loc[index]
                df_2020['A03'] = df_2020['toan'] + df_2020['ly'] + df_2020['su']
            elif khoi == 'A04':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['dia'].loc[index]
                df_2020['A04'] = df_2020['toan'] + df_2020['ly'] + df_2020['dia']
            elif khoi == 'A05':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['su'].loc[index]
                df_2020['A05'] = df_2020['toan'] + df_2020['hoa'] + df_2020['su']
            elif khoi == 'A06':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['dia'].loc[index]
                df_2020['A06'] = df_2020['toan'] + df_2020['hoa'] + df_2020['dia']
            elif khoi == 'A07':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['su'].loc[index] + df_2020['dia'].loc[index]
                df_2020['A07'] = df_2020['toan'] + df_2020['su'] + df_2020['dia']
            elif khoi == 'A08':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['su'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['A08'] = df_2020['toan'] + df_2020['su'] + df_2020['gdcd']
            elif khoi == 'A09':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['A09'] = df_2020['toan'] + df_2020['dia'] + df_2020['gdcd']
            elif khoi == 'A10':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['A10'] = df_2020['toan'] + df_2020['ly'] + df_2020['gdcd']
            elif khoi == 'A11':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['A11'] = df_2020['toan'] + df_2020['hoa'] + df_2020['gdcd']
            elif khoi == 'A12':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['KHXH'].loc[index]
                df_2020['A12'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['KHXH']
            elif khoi == 'A14':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['dia'].loc[index]
                df_2020['A14'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['dia']
            elif khoi == 'A15':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['A15'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['gdcd']
            elif khoi == 'A16':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['van'].loc[index]
                df_2020['A16'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['van']
            elif khoi == 'A17':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['KHXH'].loc[index]
                df_2020['A17'] = df_2020['toan'] + df_2020['ly'] + df_2020['KHXH']
            elif khoi == 'A18':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['KHXH'].loc[index]
                df_2020['A18'] = df_2020['toan'] + df_2020['hoa'] + df_2020['KHXH']
            elif khoi == 'B00':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['hoa'].loc[index]
                df_2020['B00'] = df_2020['toan'] + df_2020['sinh'] + df_2020['hoa']
            elif khoi == 'B01':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['su'].loc[index]
                df_2020['B01'] = df_2020['toan'] + df_2020['sinh'] + df_2020['su']
            elif khoi == 'B02':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['dia'].loc[index]
                df_2020['B02'] = df_2020['toan'] + df_2020['sinh'] + df_2020['dia']
            elif khoi == 'B03':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['van'].loc[index]
                df_2020['B03'] = df_2020['toan'] + df_2020['sinh'] + df_2020['van']
            elif khoi == 'B04':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['B04'] = df_2020['toan'] + df_2020['sinh'] + df_2020['gdcd']
            elif khoi == 'B05':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['KHXH'].loc[index]
                df_2020['B05'] = df_2020['toan'] + df_2020['sinh'] + df_2020['KHXH']
            elif khoi == 'B08':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N1'].loc[index]
                df_2020['B08'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N1']
            elif khoi == 'C00':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['dia'].loc[index]
                df_2020['C00'] = df_2020['van'] + df_2020['su'] + df_2020['dia']
            elif khoi == 'C01':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['ly'].loc[index]
                df_2020['C01'] = df_2020['van'] + df_2020['toan'] + df_2020['ly']
            elif khoi == 'C02':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['hoa'].loc[index]
                df_2020['C02'] = df_2020['van'] + df_2020['toan'] + df_2020['hoa']
            elif khoi == 'C03':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['su'].loc[index]
                df_2020['C03'] = df_2020['van'] + df_2020['toan'] + df_2020['su']
            elif khoi == 'C04':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['dia'].loc[index]
                df_2020['C04'] = df_2020['van'] + df_2020['toan'] + df_2020['dia']
            elif khoi == 'C05':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['hoa'].loc[index]
                df_2020['C05'] = df_2020['van'] + df_2020['ly'] + df_2020['hoa']
            elif khoi == 'C06':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['sinh'].loc[index]
                df_2020['C06'] = df_2020['van'] + df_2020['ly'] + df_2020['sinh']
            elif khoi == 'C07':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['su'].loc[index]
                df_2020['C07'] = df_2020['van'] + df_2020['ly'] + df_2020['su']
            elif khoi == 'C08':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['hoa'].loc[index] + df_2020['sinh'].loc[index]
                df_2020['C08'] = df_2020['van'] + df_2020['hoa'] + df_2020['sinh']
            elif khoi == 'C09':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['dia'].loc[index]
                df_2020['C09'] = df_2020['van'] + df_2020['ly'] + df_2020['dia']
            elif khoi == 'C10':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['hoa'].loc[index] + df_2020['su'].loc[index]
                df_2020['C10'] = df_2020['van'] + df_2020['hoa'] + df_2020['su']
            elif khoi == 'C12':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['sinh'].loc[index] + df_2020['su'].loc[index]
                df_2020['C12'] = df_2020['van'] + df_2020['sinh'] + df_2020['su']
            elif khoi == 'C13':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['sinh'].loc[index] + df_2020['dia'].loc[index]
                df_2020['C13'] = df_2020['van'] + df_2020['sinh'] + df_2020['dia']
            elif khoi == 'C14':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['C14'] = df_2020['van'] + df_2020['toan'] + df_2020['gdcd']
            elif khoi == 'C15':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['KHXH'].loc[index]
                df_2020['C15'] = df_2020['van'] + df_2020['toan'] + df_2020['KHXH']
            elif khoi == 'C16':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['C16'] = df_2020['van'] + df_2020['ly'] + df_2020['gdcd']
            elif khoi == 'C17':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['hoa'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['C17'] = df_2020['van'] + df_2020['hoa'] + df_2020['gdcd']
            elif khoi == 'C19':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['C19'] = df_2020['van'] + df_2020['su'] + df_2020['gdcd']
            elif khoi == 'C20':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['gdcd'].loc[index]
                df_2020['C20'] = df_2020['van'] + df_2020['dia'] + df_2020['gdcd']
            elif khoi == 'D01':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D01'] = df_2020['van'] + df_2020['toan'] + df_2020['N1']
            elif khoi == 'D02':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D02'] = df_2020['van'] + df_2020['toan'] + df_2020['N2']
            elif khoi == 'D03':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D03'] = df_2020['van'] + df_2020['toan'] + df_2020['N3']
            elif khoi == 'D04':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D04'] = df_2020['van'] + df_2020['toan'] + df_2020['N4']
            elif khoi == 'D05':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D05'] = df_2020['van'] + df_2020['toan'] + df_2020['N5']
            elif khoi == 'D06':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['toan'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D06'] = df_2020['van'] + df_2020['toan'] + df_2020['N6']
            elif khoi == 'D07':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D07'] = df_2020['toan'] + df_2020['hoa'] + df_2020['N1']
            elif khoi == 'D08':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D08'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N1']
            elif khoi == 'D09':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['su'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D09'] = df_2020['toan'] + df_2020['su'] + df_2020['N1']
            elif khoi == 'D10':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D10'] = df_2020['toan'] + df_2020['dia'] + df_2020['N1']
            elif khoi == 'D11':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D11'] = df_2020['van'] + df_2020['ly'] + df_2020['N1']
            elif khoi == 'D12':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D12'] = df_2020['van'] + df_2020['hoa'] + df_2020['N1']
            elif khoi == 'D13':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D13'] = df_2020['van'] + df_2020['sinh'] + df_2020['N1']
            elif khoi == 'D14':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D14'] = df_2020['van'] + df_2020['su'] + df_2020['N1']
            elif khoi == 'D15':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D15'] = df_2020['van'] + df_2020['dia'] + df_2020['N1']
            elif khoi == 'D16':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D16'] = df_2020['toan'] + df_2020['dia'] + df_2020['N5']
            elif khoi == 'D17':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D17'] = df_2020['toan'] + df_2020['dia'] + df_2020['N2']
            elif khoi == 'D18':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D18'] = df_2020['toan'] + df_2020['dia'] + df_2020['N6']
            elif khoi == 'D19':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D19'] = df_2020['toan'] + df_2020['dia'] + df_2020['N3']
            elif khoi == 'D20':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['dia'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D20'] = df_2020['toan'] + df_2020['dia'] + df_2020['N4']
            elif khoi == 'D21':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D21'] = df_2020['toan'] + df_2020['hoa'] + df_2020['N5']
            elif khoi == 'D22':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D22'] = df_2020['toan'] + df_2020['hoa'] + df_2020['N2']
            elif khoi == 'D23':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D23'] = df_2020['toan'] + df_2020['hoa'] + df_2020['N6']
            elif khoi == 'D24':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D24'] = df_2020['toan'] + df_2020['hoa'] + df_2020['N3']
            elif khoi == 'D25':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['hoa'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D25'] = df_2020['toan'] + df_2020['hoa'] + df_2020['N4']
            elif khoi == 'D26':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D26'] = df_2020['toan'] + df_2020['ly'] + df_2020['N5']
            elif khoi == 'D27':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D27'] = df_2020['toan'] + df_2020['ly'] + df_2020['N2']
            elif khoi == 'D28':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D28'] = df_2020['toan'] + df_2020['ly'] + df_2020['N6']
            elif khoi == 'D29':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D29'] = df_2020['toan'] + df_2020['ly'] + df_2020['N3']
            elif khoi == 'D30':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['ly'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D30'] = df_2020['toan'] + df_2020['ly'] + df_2020['N4']
            elif khoi == 'D31':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D31'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N5']
            elif khoi == 'D32':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D32'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N2']
            elif khoi == 'D33':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D33'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N6']
            elif khoi == 'D34':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D34'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N3']
            elif khoi == 'D35':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['sinh'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D35'] = df_2020['toan'] + df_2020['sinh'] + df_2020['N4']
            elif khoi == 'D41':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D41'] = df_2020['van'] + df_2020['dia'] + df_2020['N5']
            elif khoi == 'D42':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D42'] = df_2020['van'] + df_2020['dia'] + df_2020['N2']
            elif khoi == 'D43':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D43'] = df_2020['van'] + df_2020['dia'] + df_2020['N6']
            elif khoi == 'D44':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D44'] = df_2020['van'] + df_2020['dia'] + df_2020['N3']
            elif khoi == 'D45':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['dia'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D45'] = df_2020['van'] + df_2020['dia'] + df_2020['N4']
            elif khoi == 'D52':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D52'] = df_2020['van'] + df_2020['ly'] + df_2020['N2']
            elif khoi == 'D54':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D54'] = df_2020['van'] + df_2020['ly'] + df_2020['N3']
            elif khoi == 'D55':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['ly'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D55'] = df_2020['van'] + df_2020['ly'] + df_2020['N4']
            elif khoi == 'D61':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D61'] = df_2020['van'] + df_2020['su'] + df_2020['N5']
            elif khoi == 'D62':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D62'] = df_2020['van'] + df_2020['su'] + df_2020['N2']
            elif khoi == 'D63':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D63'] = df_2020['van'] + df_2020['su'] + df_2020['N6']
            elif khoi == 'D64':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D64'] = df_2020['van'] + df_2020['su'] + df_2020['N3']
            elif khoi == 'D65':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['su'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D65'] = df_2020['van'] + df_2020['su'] + df_2020['N4']
            elif khoi == 'D66':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D66'] = df_2020['van'] + df_2020['gdcd'] + df_2020['N1']
            elif khoi == 'D68':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D68'] = df_2020['van'] + df_2020['gdcd'] + df_2020['N2']
            elif khoi == 'D69':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D69'] = df_2020['van'] + df_2020['gdcd'] + df_2020['N6']
            elif khoi == 'D70':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D70'] = df_2020['van'] + df_2020['gdcd'] + df_2020['N3']
            elif khoi == 'D72':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D72'] = df_2020['van'] + df_2020['KHTN'] + df_2020['N1']
            elif khoi == 'D73':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D73'] = df_2020['van'] + df_2020['KHTN'] + df_2020['N5']
            elif khoi == 'D74':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D74'] = df_2020['van'] + df_2020['KHTN'] + df_2020['N2']
            elif khoi == 'D75':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D75'] = df_2020['van'] + df_2020['KHTN'] + df_2020['N6']
            elif khoi == 'D76':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D76'] = df_2020['van'] + df_2020['KHTN'] + df_2020['N3']
            elif khoi == 'D77':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D77'] = df_2020['van'] + df_2020['KHTN'] + df_2020['N4']
            elif khoi == 'D78':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D78'] = df_2020['van'] + df_2020['KHXH'] + df_2020['N1']
            elif khoi == 'D79':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D79'] = df_2020['van'] + df_2020['KHXH'] + df_2020['N5']
            elif khoi == 'D80':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D80'] = df_2020['van'] + df_2020['KHXH'] + df_2020['N2']
            elif khoi == 'D81':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D81'] = df_2020['van'] + df_2020['KHXH'] + df_2020['N6']
            elif khoi == 'D82':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D82'] = df_2020['van'] + df_2020['KHXH'] + df_2020['N3']
            elif khoi == 'D83':
                diem_cua_thi_sinh = df_2020['van'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D83'] = df_2020['van'] + df_2020['KHXH'] + df_2020['N4']
            elif khoi == 'D84':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D84'] = df_2020['toan'] + df_2020['gdcd'] + df_2020['N1']
            elif khoi == 'D85':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D85'] = df_2020['toan'] + df_2020['gdcd'] + df_2020['N5']
            elif khoi == 'D86':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D86'] = df_2020['toan'] + df_2020['gdcd'] + df_2020['N2']
            elif khoi == 'D87':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D87'] = df_2020['toan'] + df_2020['gdcd'] + df_2020['N3']
            elif khoi == 'D88':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['gdcd'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D88'] = df_2020['toan'] + df_2020['gdcd'] + df_2020['N6']
            elif khoi == 'D90':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D90'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['N1']
            elif khoi == 'D91':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D91'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['N3']
            elif khoi == 'D92':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D92'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['N5']
            elif khoi == 'D93':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D93'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['N2']
            elif khoi == 'D94':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N6'].loc[index]
                df_2020['D94'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['N6']
            elif khoi == 'D95':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHTN'].loc[index] + df_2020['N4'].loc[index]
                df_2020['D95'] = df_2020['toan'] + df_2020['KHTN'] + df_2020['N4']
            elif khoi == 'D96':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N1'].loc[index]
                df_2020['D96'] = df_2020['toan'] + df_2020['KHXH'] + df_2020['N1']
            elif khoi == 'D97':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N3'].loc[index]
                df_2020['D97'] = df_2020['toan'] + df_2020['KHXH'] + df_2020['N3']
            elif khoi == 'D98':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N5'].loc[index]
                df_2020['D98'] = df_2020['toan'] + df_2020['KHXH'] + df_2020['N5']
            elif khoi == 'D99':
                diem_cua_thi_sinh = df_2020['toan'].loc[index] + df_2020['KHXH'].loc[index] + df_2020['N2'].loc[index]
                df_2020['D99'] = df_2020['toan'] + df_2020['KHXH'] + df_2020['N2']
            else:
                st.write("Khối thi của bạn không được hỗ trợ tính toán hoặc bạn nhập sai khối thi. Bạn hãy chọn khối thi khác.")



            df_2020 = df_2020[['sbd', khoi]]

            vi_tri_dau_tien =  [0,102095,186946,209669,222802,229088,234134,237972,245838,80000,99999,266500,282653,290888,302661,318535,332577,348602,369682,386406,408340,423726,433416,443051,463456,484301,495450,531930,186946,586065,
                                597233,605646,618675,635872,649742,654770,673667,688528,209669,720236,734723,749410,760340,774558,780679,790908,803808,836966,222802,868297,888239,901164,916619,931042,943103,955220,965655,974851,229088,
                                991278,1001054,1007739,1015123,1022060] # vị trí (số báo danh) đầu tiên theo tỉnh thành

            # Xác định mã tỉnh
            if len(sbd_str) == 7:
                mt = int(sbd_str[0]) - 1  # mã tỉnh
            elif len(sbd_str) == 8:
                mt = int(sbd_str[:2]) - 2     # mã tỉnh
            else:
                st.write("Bạn nhập sai số báo danh!")


            # Xác định tỉnh của thí sinh
            if mt in [i for i in range(1, 20)]:
                tinh_cua_thi_sinh = tinh[mt]
            else:
                tinh_cua_thi_sinh = tinh[mt]



            if math.isnan(diem_cua_thi_sinh):
                st.write("Bạn không đủ điểm thành phần để tính điểm khối", khoi)

            else:
                diem_cua_thi_sinh = round(diem_cua_thi_sinh, 2)
                st.write("Điểm khối", khoi, "của bạn là: ", diem_cua_thi_sinh)
                
                # Tỉnh thành
                df_2020_tinh = df_2020.loc[vi_tri_dau_tien[mt]:vi_tri_dau_tien[mt+1]-1]
                df_2020_tinh_cleaned = df_2020_tinh.dropna()
                count_tinh = len(df_2020_tinh_cleaned)
                sort_tinh = sorted(df_2020_tinh_cleaned[khoi].to_list(), reverse = True)
                st.write("Xếp hạng điểm khối", khoi, "của bạn tại", tinh_cua_thi_sinh, "là:", sort_tinh.index(diem_cua_thi_sinh), "trên tổng số", count_tinh, "thí sinh, bạn thuộc top", round(sort_tinh.index(diem_cua_thi_sinh)/count_tinh*100, 2), "%")
                
                # Toàn quốc
                df_2020_toan_quoc_cleaned = df_2020.dropna()
                count_toan_quoc = len(df_2020_toan_quoc_cleaned)
                sort_toan_quoc = sorted(df_2020_toan_quoc_cleaned[khoi].to_list(), reverse = True)
                st.write("Xếp hạng điểm khối", khoi, "của bạn trên toàn quốc là:", sort_toan_quoc.index(diem_cua_thi_sinh), "trên tổng số", count_toan_quoc, "thí sinh, bạn thuộc top", round(sort_toan_quoc.index(diem_cua_thi_sinh)/count_toan_quoc*100, 2), "%")

                # Điểm tương đương với năm 2019
                st.write("Điểm số của bạn tương đương với mức điểm", diem_tuong_duong(khoi, sort_toan_quoc.index(diem_cua_thi_sinh)/count_toan_quoc), " năm 2019 (dựa trên top điểm thi trên toàn quốc là ", round(sort_toan_quoc.index(diem_cua_thi_sinh)/count_toan_quoc*100, 2), "%)")
except:
    st.write("Bạn nhập sai số báo danh hoặc số báo danh không tồn tại trong dữ liệu của Bộ GD&ĐT. Mời bạn nhập lại.")

