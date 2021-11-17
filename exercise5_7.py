products = [
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2",
]
# VALMISTAJA_TUOTENIMI_MALLI_VUOSI_KUUKAUSI_PAIVA_C_KATEGORIA

categories = [
    "Muut",
    "Pienlaitteet",
    "Kylmälaitteet",
    "Sekoittimet"
]


for product in products:
    details = product.split("_")
    #print(details)
    for term in details:
        print(term)
        pass
