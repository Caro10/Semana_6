
#por defecto el modulo es de lectura: r

f = open('mis_datos4.txt')

pass


#f.readlines() con esto se ven  la informacion en el evaluador de expresiones


#paquete para tejer rutas path, crea ruta compatible con sistemas operativos
#ruta_archivo = path.join('diccionario', 'archivo.text')
"""
archivo = open(ruta_archivo)
contenido = archivo.read()
archivo.close()
contenido

archivo = open('text.txt,'w') # modo de escritura 'w'
#se escriben algunas lineas
archivo.write('primera linea\n')
archivo.write('segund linea\n')
#y se cierrael archivo para que el sistema actualice
archivo.close() #salva el archivo hace un clon

siempre hay que cerrar para que no hayan dos recursos compitiendo por el mismo archivo. 


se recomienda usar contexto 'with'

with open('data.txt, 'w') as f:
    f.write('Hello\n')