import requests

months = ["04","05","06","07","08","09","10","11","12"]

for month in months:
    url = "https://www.portaltransparencia.gov.br/download-de-dados/auxilio-emergencial/2020" + month
    print(url)

    r = requests.get(url, allow_redirects=True, verify=False)
    filepath = "../data/raw/2021" + month + "_AuxilioEmergencial.zip"
    with open(filepath, 'wb') as f:
        f.write(r.content)
