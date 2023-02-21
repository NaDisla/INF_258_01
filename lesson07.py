# TRABAJANDO CON FECHAS
import datetime

meses = {
    1:"Enero", 
    2:"Febrero", 
    3:"Marzo", 
    4:"Abril", 
    5:"Mayo", 
    6:"Junio", 
    7:"Julio", 
    8:"Agosto", 
    9:"Septiembre", 
    10:"Octubre", 
    11:"Noviembre", 
    12:"Diciembre"
}
dia = int(input("Inserte el dia: "))
mes = int(input("Inserte el mes: "))
año = int(input("Inserte el año: "))

# print(f"{dia}-{meses[mes]}-{año}")

fecha = datetime.date(año, mes, dia)
#print(fecha.month)

mes = print(meses[fecha.month])
