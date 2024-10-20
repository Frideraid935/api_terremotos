import requests
from pprint import pprint
from tkinter import *


base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"

def obtener_datos_api():
    starttime = fecha_inicio.get()
    endtime = fecha_fin.get()
    
    url = f"{base_url}&starttime={starttime}&endtime={endtime}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            mostrar_datos(datos)
        else:
            resultado_label.config(text=f"Error al obtener datos: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        resultado_label.config(text=f"Error de conexion: {e}")

def mostrar_datos(datos):
    
    resultado_label.config(text="")
    
    lugares = [evento["properties"]["place"] for evento in datos["features"][:10]]
    
    
    resultado_label.config(text="\n".join(lugares))


ventana = Tk()
ventana.title("Consulta de Terremotos")
ventana.minsize(width=400, height=300)
ventana.config(padx=20, pady=20)

Label(ventana, text="Fecha de inicio (anio-mes-dia):").grid(row=0, column=0, sticky=W)
fecha_inicio = Entry(ventana, width=20)
fecha_inicio.grid(row=0, column=1)

Label(ventana, text="Fecha de fin (anio-mes-dia):").grid(row=1, column=0, sticky=W)
fecha_fin = Entry(ventana, width=20)
fecha_fin.grid(row=1, column=1)

boton_buscar = Button(ventana, text="Buscar", command=obtener_datos_api)
boton_buscar.grid(row=2, column=0, columnspan=2, pady=10)


resultado_label = Label(ventana, text="", justify=LEFT, wraplength=350)
resultado_label.grid(row=3, column=0, columnspan=2, pady=20)


ventana.mainloop()

