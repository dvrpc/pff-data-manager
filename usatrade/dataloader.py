import requests
import io
import json

SQL_INSERT_USATRADE = """
        INSERT INTO usatrade(year, type, port_id, hs_group, vessel_kg, vessel_value, cont_kg, cont_value) 
        VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s
        )
    """

def get_trade(year, imex):
    import_url = 'https://api.census.gov/data/timeseries/intltrade/%s/porths?get=PORT,PORT_NAME,E_COMMODITY,VES_WGT_YR,VES_VAL_YR,CNT_VAL_YR,CNT_WGT_YR&PORT=1107&PORT=1102&PORT=1113&PORT=1105&PORT=1101&COMM_LVL=HS2&time=%s-12'
    
    data=requests.get(import_url % ie,year)

    for item in data.json():
        type = imex
        portid = item[0]
        hs_group = item[2]
        vessel_kg = item[3]
        vessel_value = item[4]
        cont_kg = item[5]
        cont_value = item[6]

        print(year, type, portid, hs_group,vessel_kg,vessel_value,cont_kg,cont_value)



if __name__ == "__main__":
    get_imports()
W