import pandas as pd
import os

# import chardet
# with open("data/raw/202110_AuxilioEmergencial.csv", 'rb') as file:
#     print(chardet.detect(file.read()))

df_full = pd.DataFrame()

for filename in os.listdir("data/raw/"):
    if filename.endswith("AuxilioEmergencial.csv"):

        df = pd.read_csv(("data/raw/" + filename), sep=';', encoding="ISO-8859-1")
        df_clean = (df
                    .drop_duplicates()[["MÊS DISPONIBILIZAÇÃO", "UF", "PARCELA", "VALOR BENEFÍCIO"]]
                    .groupby(["MÊS DISPONIBILIZAÇÃO", "UF", "PARCELA", "VALOR BENEFÍCIO"], as_index=False, dropna=False).size()
                    )
        
        df_full = df_full.append(df_clean)

df_full.to_csv("data/raw/auxilio_full.csv", index=False)

df.shape[0]
print(df.columns)

df_full.groupby(["MÊS DISPONIBILIZAÇÃO"], as_index=False, dropna=False).sum()

(df
.drop_duplicates()[["MÊS DISPONIBILIZAÇÃO", "UF", "PARCELA", "VALOR BENEFÍCIO"]])

###################################################################################


df_full = pd.DataFrame()

for filename in os.listdir("data/raw/"):
    if filename.endswith("AuxilioEmergencial.csv"):
        print(filename)

        df = pd.read_csv(("data/raw/" + filename), sep=';', encoding="ISO-8859-1")
        df_clean = (df
                    #.drop_duplicates()[["MÊS DISPONIBILIZAÇÃO", "UF", "PARCELA", "VALOR BENEFÍCIO"]]
                    .groupby(["MÊS DISPONIBILIZAÇÃO", "CPF BENEFICIÁRIO", "NOME BENEFICIÁRIO"], as_index=False, dropna=False).size()
                    )
        
        df_full = df_full.append(df_clean)

df_full.to_csv("data/raw/auxilio_full_unique.csv", index=False)

df_full = df_full.groupby(["MÊS DISPONIBILIZAÇÃO"], as_index=False, dropna=False).size()
df_full.to_csv("data/raw/auxilio_full_unique_permonth.csv", index=False)


##################################################################################


df_full = pd.DataFrame()

for filename in os.listdir("data/raw/"):
    if filename.endswith("AuxilioEmergencial.csv"):
        print(filename)

        df = pd.read_csv(("data/raw/" + filename), sep=';', encoding="ISO-8859-1")
        df['VALOR BENEFÍCIO'] = df['VALOR BENEFÍCIO'].str.replace(',', '.').astype(float)

        df_clean = (df
                    #.drop_duplicates()[["MÊS DISPONIBILIZAÇÃO", "UF", "PARCELA", "VALOR BENEFÍCIO"]]
                    .groupby(["PARCELA"], as_index=False, dropna=False).sum()
                    )
        
        df_full = df_full.append(df_clean)

df_full = df_full.groupby(["PARCELA"], as_index=False, dropna=False).sum()

df_full.to_csv("data/raw/auxilio_full_parcela.csv", index=False)




##################################################################################

df_test = pd.read_csv(("data/raw/202110_AuxilioEmergencial.csv"), sep=';', encoding="ISO-8859-1")
df_test = df_test.groupby(["CPF BENEFICIÁRIO", "NOME BENEFICIÁRIO"], as_index=False, dropna=False).size()

##################################################################################

df_raw = pd.read_csv(("data/raw/202007_AuxilioEmergencial.csv"), sep=';', encoding="ISO-8859-1", nrows=10000)
df_raw['VALOR BENEFÍCIO'] = df_raw['VALOR BENEFÍCIO'].str.replace(',', '.').astype(float)
df_test = df_raw.groupby(["PARCELA"], as_index=False, dropna=False).sum()
df_test = df_test.groupby(["MÊS DISPONIBILIZAÇÃO"], as_index=False, dropna=False).size()
