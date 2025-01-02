import pandas as pd
import pymysql

# Kết nối tới MySQL
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='MySQL123@@',
    database='big_data'
)


def diem_tuong_duong(khoi, phan_tram):
    # Khai báo
    query = "SELECT sbd, toan, ngu_van, vat_ly, hoa_hoc, sinh_hoc, lich_su, dia_ly, gdcd, ngoai_ngu,  FROM diem_thi_2017_2020 WHERE nam_thi = 2019"
    df_2019 = pd.read_sql(query, connection)
    # df_2019 = pd.read_csv("C:\\Users\\ADMIN\\Repo\\Web\\diem_thi_2019.csv", dtype={'sbd': str})
    df_2019.columns = ['sbd','toan','van','ly','hoa','sinh','su','dia','gdcd','nn','ma_nn']
    df_2019['KHTN'] = df_2019['ly'] + df_2019['hoa'] + df_2019['sinh']
    df_2019['KHXH'] = df_2019['su'] + df_2019['dia'] + df_2019['gdcd']
    df_2019['N1'] = df_2019[df_2019['ma_nn'] == 'N1']['nn']
    df_2019['N1'] = df_2019[df_2019['ma_nn'] == 'N1']['nn']
    df_2019['N2'] = df_2019[df_2019['ma_nn'] == 'N2']['nn']
    df_2019['N3'] = df_2019[df_2019['ma_nn'] == 'N3']['nn']
    df_2019['N4'] = df_2019[df_2019['ma_nn'] == 'N4']['nn']
    df_2019['N5'] = df_2019[df_2019['ma_nn'] == 'N5']['nn']
    df_2019['N6'] = df_2019[df_2019['ma_nn'] == 'N6']['nn']
    df_2019['N7'] = df_2019[df_2019['ma_nn'] == 'N7']['nn']


    if khoi != "":
        # Check điểm các khối
        if khoi == 'A00':
            df_2019['A00'] = df_2019['toan'] + df_2019['ly'] + df_2019['hoa']
        elif khoi == 'A01':
            df_2019['A01'] = df_2019['toan'] + df_2019['ly'] + df_2019['N1']
        elif khoi == 'A02':
            df_2019['A02'] = df_2019['toan'] + df_2019['ly'] + df_2019['sinh']
        elif khoi == 'A03':
            df_2019['A03'] = df_2019['toan'] + df_2019['ly'] + df_2019['su']
        elif khoi == 'A04':
            df_2019['A04'] = df_2019['toan'] + df_2019['ly'] + df_2019['dia']
        elif khoi == 'A05':
            df_2019['A05'] = df_2019['toan'] + df_2019['hoa'] + df_2019['su']
        elif khoi == 'A06':
            df_2019['A06'] = df_2019['toan'] + df_2019['hoa'] + df_2019['dia']
        elif khoi == 'A07':
            df_2019['A07'] = df_2019['toan'] + df_2019['su'] + df_2019['dia']
        elif khoi == 'A08':
            df_2019['A08'] = df_2019['toan'] + df_2019['su'] + df_2019['gdcd']
        elif khoi == 'A09':
            df_2019['A09'] = df_2019['toan'] + df_2019['dia'] + df_2019['gdcd']
        elif khoi == 'A10':
            df_2019['A10'] = df_2019['toan'] + df_2019['ly'] + df_2019['gdcd']
        elif khoi == 'A11':
            df_2019['A11'] = df_2019['toan'] + df_2019['hoa'] + df_2019['gdcd']
        elif khoi == 'A12':
            df_2019['A12'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['KHXH']
        elif khoi == 'A14':
            df_2019['A14'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['dia']
        elif khoi == 'A15':
            df_2019['A15'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['gdcd']
        elif khoi == 'A16':
            df_2019['A16'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['van']
        elif khoi == 'A17':
            df_2019['A17'] = df_2019['toan'] + df_2019['ly'] + df_2019['KHXH']
        elif khoi == 'A18':
            df_2019['A18'] = df_2019['toan'] + df_2019['hoa'] + df_2019['KHXH']
        elif khoi == 'B00':
            df_2019['B00'] = df_2019['toan'] + df_2019['sinh'] + df_2019['hoa']
        elif khoi == 'B01':
            df_2019['B01'] = df_2019['toan'] + df_2019['sinh'] + df_2019['su']
        elif khoi == 'B02':
            df_2019['B02'] = df_2019['toan'] + df_2019['sinh'] + df_2019['dia']
        elif khoi == 'B03':
            df_2019['B03'] = df_2019['toan'] + df_2019['sinh'] + df_2019['van']
        elif khoi == 'B04':
            df_2019['B04'] = df_2019['toan'] + df_2019['sinh'] + df_2019['gdcd']
        elif khoi == 'B05':
            df_2019['B05'] = df_2019['toan'] + df_2019['sinh'] + df_2019['KHXH']
        elif khoi == 'B08':
            df_2019['B08'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N1']
        elif khoi == 'C00':
            df_2019['C00'] = df_2019['van'] + df_2019['su'] + df_2019['dia']
        elif khoi == 'C01':
            df_2019['C01'] = df_2019['van'] + df_2019['toan'] + df_2019['ly']
        elif khoi == 'C02':
            df_2019['C02'] = df_2019['van'] + df_2019['toan'] + df_2019['hoa']
        elif khoi == 'C03':
            df_2019['C03'] = df_2019['van'] + df_2019['toan'] + df_2019['su']
        elif khoi == 'C04':
            df_2019['C04'] = df_2019['van'] + df_2019['toan'] + df_2019['dia']
        elif khoi == 'C05':
            df_2019['C05'] = df_2019['van'] + df_2019['ly'] + df_2019['hoa']
        elif khoi == 'C06':
            df_2019['C06'] = df_2019['van'] + df_2019['ly'] + df_2019['sinh']
        elif khoi == 'C07':
            df_2019['C07'] = df_2019['van'] + df_2019['ly'] + df_2019['su']
        elif khoi == 'C08':
            df_2019['C08'] = df_2019['van'] + df_2019['hoa'] + df_2019['sinh']
        elif khoi == 'C09':
            df_2019['C09'] = df_2019['van'] + df_2019['ly'] + df_2019['dia']
        elif khoi == 'C10':
            df_2019['C10'] = df_2019['van'] + df_2019['hoa'] + df_2019['su']
        elif khoi == 'C12':
            df_2019['C12'] = df_2019['van'] + df_2019['sinh'] + df_2019['su']
        elif khoi == 'C13':
            df_2019['C13'] = df_2019['van'] + df_2019['sinh'] + df_2019['dia']
        elif khoi == 'C14':
            df_2019['C14'] = df_2019['van'] + df_2019['toan'] + df_2019['gdcd']
        elif khoi == 'C15':
            df_2019['C15'] = df_2019['van'] + df_2019['toan'] + df_2019['KHXH']
        elif khoi == 'C16':
            df_2019['C16'] = df_2019['van'] + df_2019['ly'] + df_2019['gdcd']
        elif khoi == 'C17':
            df_2019['C17'] = df_2019['van'] + df_2019['hoa'] + df_2019['gdcd']
        elif khoi == 'C19':
            df_2019['C19'] = df_2019['van'] + df_2019['su'] + df_2019['gdcd']
        elif khoi == 'C20':
            df_2019['C20'] = df_2019['van'] + df_2019['dia'] + df_2019['gdcd']
        elif khoi == 'D01':
            df_2019['D01'] = df_2019['van'] + df_2019['toan'] + df_2019['N1']
        elif khoi == 'D02':
            df_2019['D02'] = df_2019['van'] + df_2019['toan'] + df_2019['N2']
        elif khoi == 'D03':
            df_2019['D03'] = df_2019['van'] + df_2019['toan'] + df_2019['N3']
        elif khoi == 'D04':
            df_2019['D04'] = df_2019['van'] + df_2019['toan'] + df_2019['N4']
        elif khoi == 'D05':
            df_2019['D05'] = df_2019['van'] + df_2019['toan'] + df_2019['N5']
        elif khoi == 'D06':
            df_2019['D06'] = df_2019['van'] + df_2019['toan'] + df_2019['N6']
        elif khoi == 'D07':
            df_2019['D07'] = df_2019['toan'] + df_2019['hoa'] + df_2019['N1']
        elif khoi == 'D08':
            df_2019['D08'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N1']
        elif khoi == 'D09':
            df_2019['D09'] = df_2019['toan'] + df_2019['su'] + df_2019['N1']
        elif khoi == 'D10':
            df_2019['D10'] = df_2019['toan'] + df_2019['dia'] + df_2019['N1']
        elif khoi == 'D11':
            df_2019['D11'] = df_2019['van'] + df_2019['ly'] + df_2019['N1']
        elif khoi == 'D12':
            df_2019['D12'] = df_2019['van'] + df_2019['hoa'] + df_2019['N1']
        elif khoi == 'D13':
            df_2019['D13'] = df_2019['van'] + df_2019['sinh'] + df_2019['N1']
        elif khoi == 'D14':
            df_2019['D14'] = df_2019['van'] + df_2019['su'] + df_2019['N1']
        elif khoi == 'D15':
            df_2019['D15'] = df_2019['van'] + df_2019['dia'] + df_2019['N1']
        elif khoi == 'D16':
            df_2019['D16'] = df_2019['toan'] + df_2019['dia'] + df_2019['N5']
        elif khoi == 'D17':
            df_2019['D17'] = df_2019['toan'] + df_2019['dia'] + df_2019['N2']
        elif khoi == 'D18':
            df_2019['D18'] = df_2019['toan'] + df_2019['dia'] + df_2019['N6']
        elif khoi == 'D19':
            df_2019['D19'] = df_2019['toan'] + df_2019['dia'] + df_2019['N3']
        elif khoi == 'D20':
            df_2019['D20'] = df_2019['toan'] + df_2019['dia'] + df_2019['N4']
        elif khoi == 'D21':
            df_2019['D21'] = df_2019['toan'] + df_2019['hoa'] + df_2019['N5']
        elif khoi == 'D22':
            df_2019['D22'] = df_2019['toan'] + df_2019['hoa'] + df_2019['N2']
        elif khoi == 'D23':
            df_2019['D23'] = df_2019['toan'] + df_2019['hoa'] + df_2019['N6']
        elif khoi == 'D24':
            df_2019['D24'] = df_2019['toan'] + df_2019['hoa'] + df_2019['N3']
        elif khoi == 'D25':
            df_2019['D25'] = df_2019['toan'] + df_2019['hoa'] + df_2019['N4']
        elif khoi == 'D26':
            df_2019['D26'] = df_2019['toan'] + df_2019['ly'] + df_2019['N5']
        elif khoi == 'D27':
            df_2019['D27'] = df_2019['toan'] + df_2019['ly'] + df_2019['N2']
        elif khoi == 'D28':
            df_2019['D28'] = df_2019['toan'] + df_2019['ly'] + df_2019['N6']
        elif khoi == 'D29':
            df_2019['D29'] = df_2019['toan'] + df_2019['ly'] + df_2019['N3']
        elif khoi == 'D30':
            df_2019['D30'] = df_2019['toan'] + df_2019['ly'] + df_2019['N4']
        elif khoi == 'D31':
            df_2019['D31'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N5']
        elif khoi == 'D32':
            df_2019['D32'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N2']
        elif khoi == 'D33':
            df_2019['D33'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N6']
        elif khoi == 'D34':
            df_2019['D34'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N3']
        elif khoi == 'D35':
            df_2019['D35'] = df_2019['toan'] + df_2019['sinh'] + df_2019['N4']
        elif khoi == 'D41':
            df_2019['D41'] = df_2019['van'] + df_2019['dia'] + df_2019['N5']
        elif khoi == 'D42':
            df_2019['D42'] = df_2019['van'] + df_2019['dia'] + df_2019['N2']
        elif khoi == 'D43':
            df_2019['D43'] = df_2019['van'] + df_2019['dia'] + df_2019['N6']
        elif khoi == 'D44':
            df_2019['D44'] = df_2019['van'] + df_2019['dia'] + df_2019['N3']
        elif khoi == 'D45':
            df_2019['D45'] = df_2019['van'] + df_2019['dia'] + df_2019['N4']
        elif khoi == 'D52':
            df_2019['D52'] = df_2019['van'] + df_2019['ly'] + df_2019['N2']
        elif khoi == 'D54':
            df_2019['D54'] = df_2019['van'] + df_2019['ly'] + df_2019['N3']
        elif khoi == 'D55':
            df_2019['D55'] = df_2019['van'] + df_2019['ly'] + df_2019['N4']
        elif khoi == 'D61':
            df_2019['D61'] = df_2019['van'] + df_2019['su'] + df_2019['N5']
        elif khoi == 'D62':
            df_2019['D62'] = df_2019['van'] + df_2019['su'] + df_2019['N2']
        elif khoi == 'D63':
            df_2019['D63'] = df_2019['van'] + df_2019['su'] + df_2019['N6']
        elif khoi == 'D64':
            df_2019['D64'] = df_2019['van'] + df_2019['su'] + df_2019['N3']
        elif khoi == 'D65':
            df_2019['D65'] = df_2019['van'] + df_2019['su'] + df_2019['N4']
        elif khoi == 'D66':
            df_2019['D66'] = df_2019['van'] + df_2019['gdcd'] + df_2019['N1']
        elif khoi == 'D68':
            df_2019['D68'] = df_2019['van'] + df_2019['gdcd'] + df_2019['N2']
        elif khoi == 'D69':
            df_2019['D69'] = df_2019['van'] + df_2019['gdcd'] + df_2019['N6']
        elif khoi == 'D70':
            df_2019['D70'] = df_2019['van'] + df_2019['gdcd'] + df_2019['N3']
        elif khoi == 'D72':
            df_2019['D72'] = df_2019['van'] + df_2019['KHTN'] + df_2019['N1']
        elif khoi == 'D73':
            df_2019['D73'] = df_2019['van'] + df_2019['KHTN'] + df_2019['N5']
        elif khoi == 'D74':
            df_2019['D74'] = df_2019['van'] + df_2019['KHTN'] + df_2019['N2']
        elif khoi == 'D75':
            df_2019['D75'] = df_2019['van'] + df_2019['KHTN'] + df_2019['N6']
        elif khoi == 'D76':
            df_2019['D76'] = df_2019['van'] + df_2019['KHTN'] + df_2019['N3']
        elif khoi == 'D77':
            df_2019['D77'] = df_2019['van'] + df_2019['KHTN'] + df_2019['N4']
        elif khoi == 'D78':
            df_2019['D78'] = df_2019['van'] + df_2019['KHXH'] + df_2019['N1']
        elif khoi == 'D79':
            df_2019['D79'] = df_2019['van'] + df_2019['KHXH'] + df_2019['N5']
        elif khoi == 'D80':
            df_2019['D80'] = df_2019['van'] + df_2019['KHXH'] + df_2019['N2']
        elif khoi == 'D81':
            df_2019['D81'] = df_2019['van'] + df_2019['KHXH'] + df_2019['N6']
        elif khoi == 'D82':
            df_2019['D82'] = df_2019['van'] + df_2019['KHXH'] + df_2019['N3']
        elif khoi == 'D83':
            df_2019['D83'] = df_2019['van'] + df_2019['KHXH'] + df_2019['N4']
        elif khoi == 'D84':
            df_2019['D84'] = df_2019['toan'] + df_2019['gdcd'] + df_2019['N1']
        elif khoi == 'D85':
            df_2019['D85'] = df_2019['toan'] + df_2019['gdcd'] + df_2019['N5']
        elif khoi == 'D86':
            df_2019['D86'] = df_2019['toan'] + df_2019['gdcd'] + df_2019['N2']
        elif khoi == 'D87':
            df_2019['D87'] = df_2019['toan'] + df_2019['gdcd'] + df_2019['N3']
        elif khoi == 'D88':
            df_2019['D88'] = df_2019['toan'] + df_2019['gdcd'] + df_2019['N6']
        elif khoi == 'D90':
            df_2019['D90'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['N1']
        elif khoi == 'D91':
            df_2019['D91'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['N3']
        elif khoi == 'D92':
            df_2019['D92'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['N5']
        elif khoi == 'D93':
            df_2019['D93'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['N2']
        elif khoi == 'D94':
            df_2019['D94'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['N6']
        elif khoi == 'D95':
            df_2019['D95'] = df_2019['toan'] + df_2019['KHTN'] + df_2019['N4']
        elif khoi == 'D96':
            df_2019['D96'] = df_2019['toan'] + df_2019['KHXH'] + df_2019['N1']
        elif khoi == 'D97':
            df_2019['D97'] = df_2019['toan'] + df_2019['KHXH'] + df_2019['N3']
        elif khoi == 'D98':
            df_2019['D98'] = df_2019['toan'] + df_2019['KHXH'] + df_2019['N5']
        elif khoi == 'D99':
            df_2019['D99'] = df_2019['toan'] + df_2019['KHXH'] + df_2019['N2']
    else:
        return "Khối thi của bạn không được hỗ trợ tính toán hoặc bạn nhập sai khối thi. Bạn hãy chọn khối thi khác."


    # Tính toán và trả về kết quả
    lst_khoi = df_2019[khoi].to_list()
    lst_khoi_loai_bo_nan = [x for x in lst_khoi if str(x) != 'nan']
    lst_sorted = sorted(lst_khoi_loai_bo_nan, reverse=True)
    diem_tuong_duong_2019 = lst_sorted[int(len(lst_sorted)*phan_tram)]
    return diem_tuong_duong_2019


print(diem_tuong_duong("A00", 0.0291))  # 24.2
