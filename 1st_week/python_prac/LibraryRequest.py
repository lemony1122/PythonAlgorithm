from pprint import pprint

import requests # requests 라이브러리 설치 필요

# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()

# print(rjson)
# pprint(rjson)

# rows = rjson["RealtimeCityAir"]['row']
# pprint(rows)

# for row in rows:
# #     print(row['MSRSTE_NM'], row["IDEX_MVL"])
# gus = rjson["RealtimeCityAir"]["row"]
# for gu in gus:
#     gu_name = gu["MSRSTE_NM"]
#     gu_mise = gu["IDEX_MVL"]
#     if gu_mise < 0:
#         print(gu_name, gu_mise)



def get_gu_mise(name):
    r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
    rjson = r.json()

    gus = rjson["RealtimeCityAir"]["row"]
    for gu in gus:
        gu_name = gu["MSRSTE_NM"]
        gu_mise = gu["IDEX_MVL"]
        if gu_name == name:
            return gu_mise

    return "수치가 없습니다"

print(get_gu_mise("중구"))
print(get_gu_mise("종로구"))
print(get_gu_mise("수지구"))