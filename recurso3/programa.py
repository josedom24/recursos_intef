import requests
## Pedimos el nombre de la ciudad por teclado
ciudad=input("Dime el nombre de una ciudad:")
# Creamos un diccionario con los parametros de la URL
parametros={"q":ciudad,
            "units":"metric",
            "APPID":"50ff42ffd87463e3fc038c0166616d7a"}
# Realizamos la petición, indicando la URL y los parámetros
respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
# Si la respuesta devuelve eñ código 200, todo ha ido bien
if respuesta.status_code == 200:
    # La respuesta json se covierte en un diccionario
    datos = respuesta.json()
    # Se obtienen los valores del diccionario
    print("La temperatura actual es: ",datos["main"]["temp"]," ºC")
    print("La sensación térmica es: ",datos["main"]["feels_like"]," ºC")
    print("La temperatura mínima es: ",datos["main"]["temp_min"]," ºC")
    print("La temperatura máxima es: ",datos["main"]["temp_max"]," ºC")
    print("La presión es: ",datos["main"]["pressure"]," hPa")
    print("La humedad es: ",datos["main"]["humidity"]," %")
else:
    print("De esa ciudad no tengo datos.")