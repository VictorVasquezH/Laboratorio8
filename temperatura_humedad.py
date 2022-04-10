from asyncore import write
import serial
import simplejson
import csv
#import time

import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600)
x = []
y = []
myData = [["X","Y"]]
#time.sleep(60)!=0
for i in range(20):
    jsonResult = ser.readline()
    try:
        jsonObject = simplejson.loads(jsonResult)
        myData.extend([[int(jsonObject["Temperatura"]), int(jsonObject["Humedad"])]])
        x.append(int(jsonObject["Temperatura"])), y.append(int(jsonObject["Humedad"]))
        print(jsonObject["Temperatura"], jsonObject["Humedad"])
    except Exception:
        pass
with open('example3.csv', 'w', newline='') as file:
            write = csv.writer(file, delimiter=';')
            write.writerows(myData)
print("Escritura Completa")

#DEFINIMOS UNA LISTA CON PAISES COMO STRING
xb = []
xb2 = []
for i in range(len(x)*2):
    if i % 2==0:
        xb.append(i)
for i in range(len(x)*2):
    if i%2 !=0:
        xb2.append(i)

fig, ax = plt.subplots()
#COLOCAMOS UNA ETIQUETA EN EL EJE Y
ax.set_xlabel('Temperatura - Humedad')
ax.set_ylabel('Temperatura - Humedad')
#COLOCAMOS UNA ETIQUETA EN EL EJE X
ax.set_title('Temperatura C - Humedad % en 20 s')
#CREAMOS LA GRAFICA DE BARRAS UTILIZANDO 'XB' COMO EJE TEMPERATURA Y 'XB2' COMO EJE HUMEDAD
plt.bar(xb, x)
plt.bar(xb2, y)
plt.savefig('Barras _ Temperatura _ Humedad.png')
#FINALMENTE MOSTRAMOS LA GRFICA CON EL METODO SHOW()
plt.show()