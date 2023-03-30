import pandas as pd

df = pd.read_csv("data/raw/auxilio_full.csv", sep=',', encoding="ISO-8859-1")

df.columns = ["month", "state", "payment_installment", "value_paid", "count"]

df['value_paid'] = df['value_paid'].str.replace(',', '.').astype(float)

#df["count"] = df["count"] / 1000

df["month"] = (pd.to_datetime(df['month'], format='%Y%m')
               .dt.strftime("%d/%m/%Y"))

df["payment_installment"] = df["payment_installment"].str.extract('(\d+)')

df["amount_paid"] = df["value_paid"] * df["count"]

df_year = (df.groupby(["month"], as_index=False, dropna=False, sort=False)
           .sum())

df_year.drop("value_paid", axis = 1, inplace=True)

df_year["average_paid"] = df_year["amount_paid"] / df_year["count"]

df_year['amount_paid_cumulative'] = df_year['amount_paid'].cumsum(axis = 0) 


df_year.to_excel("data/processing/auxilio_emergencial_by_year.xlsx", index=False)



df_states = df.groupby(["state"], as_index=False, dropna=False).sum()
df_states["state"] = df_states['state'].replace(inv_dic_states, regex=False)
inv_dic_states = {v: k for k, v in dic_states.items()}

df_states.to_excel("data/processing/auxilio_emergencial_by_states.xlsx", index=False)


df2 = pd.read_excel("data/raw/tabela4097.xlsx")

df2['state']  = df2['state'].ffill()

df2["month"] = (pd.to_datetime(df2['month'], format='%Y%m')
               .dt.strftime("%d/%m/%Y"))


dic = {"Total": "Total (across all groups)",
       #"Employed",
       "Empregado no setor privado": "Employed (private sector)",
       "Empregado no setor privado, exclusive trabalhador doméstico - com carteira de trabalho assinada":"Employed (private sector) - formal",	
       "Empregado no setor privado, exclusive trabalhador doméstico - sem carteira de trabalho assinada":"Employed (private sector) - informal",	
       "Trabalhador doméstico": "Domestic workers",	
       "Trabalhador doméstico - com carteira de trabalho assinada": "Domestic workers - formal",	
       "Trabalhador doméstico - sem carteira de trabalho assinada":"Domestic workers - informal",
       "Empregado no setor público":"Employed (public sector)",
       #"Employed (public sector) - formal",
       #"Employed (public sector) - informal",
       #"Employed (public sector), military and statutory civil servant",
       "Empregador":"Employers",
       #"Employers - formal",
       #"Employers - informal",
       "Conta própria":"Self-employed",
       #"Self-employed - formal",
       #"Self-employed - informal",
       "Trabalhador familiar auxiliar":"Family workers"
       }

dic_states = {"Acre":  "AC",
"Alagoas" : "AL",
"Amapá" : "AP",
"Amazonas" : "AM",
"Bahia" : "BA",
"Ceará" : "CE",
"Distrito Federal" : "DF",
"Espírito Santo" : "ES",
"Goiás" : "GO",
"Maranhão" : "MA",
"Mato Grosso" : "MT",
"Mato Grosso do Sul" : "MS",
"Minas Gerais" : "MG",
"Pará" : "PA",
"Paraíba" : "PB",
"Paraná" : "PR",
"Pernambuco" : "PE",
"Piauí" : "PI",
"Rio de Janeiro" : "RJ",
"Rio Grande do Norte" : "RN",
"Rio Grande do Sul" : "RS",
"Rondônia" : "RO",
"Roraima" : "RR",
"Santa Catarina" : "SC",
"São Paulo" : "SP",
"Sergipe" : "SE",
"Tocantins" : "TO"
					}	

df2 = df2.rename(columns=dic)

#df2["state"]=df2['state'].replace(dic_states, regex=False)

df2["Informal"] = df2["Employed (private sector) - informal"] + df2["Domestic workers - informal"] + df2["Family workers"]
df2["Formal"] = df2["Employed (private sector) - formal"] + df2["Domestic workers - formal"] + df2["Employed (public sector)"]
df2["Undefined (formal + informal)"] = df2["Employers"] + df2["Self-employed"]
df2 = df2[["state", "month", "Informal", "Formal", "Undefined (formal + informal)"]]

