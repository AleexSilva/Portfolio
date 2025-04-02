import requests
import streamlit as st



AIRTABLE_API_KEY = st.secrets.AIRTABLE_API_KEY # Crea el token en este enlace https://airtable.com/create/tokens
AIRTABLE_BASE_ID=st.secrets.AIRTABLE_BASE_ID #Copia la plantilla de este enlace https://airtable.com/appv1dCIP9oXJOXFE/shruOGxFeklRDFp0i/tblIBw5i2w5geQhQc/viwOxM9R5nUpGo3ZO?blocks=hide

TABLE_NAME = "profile"

url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_NAME}"
headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

response = requests.get(url, headers=headers)
print(response.status_code, response.json())

if response.status_code == 200:
    print("Connection successful")
else:
    print("Connection failed")