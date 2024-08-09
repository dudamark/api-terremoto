import requests

def obter_dados_terremotos():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "limit": 50,  # Número de resultados
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["features"]
