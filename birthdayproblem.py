import numpy as np
import pandas as pd

linkki = r"https://www.avoindata.fi/data/dataset/5121b358-8f36-41ae-9880-7438c04027a3/resource/cd6686b2-a1bc-4437-a1eb-ffa910de8d91/download/syntymapaivien_maaran_jakautuminen_kalenterivuodelle_poimittu_26062019.xlsx"
df = pd.read_excel(linkki)
print(df)

