#esto es un proyecto que usa otro modulo

#estoy importando informacion del archivo Modulos.py

from Modulos import suma_resta

resultado = suma_resta(a=10, b=3, c=2) #gerarquia por la letra, sin ellas hayq ue saber el orden

print(resultado)
#archivos, imprimir letras, no espacios
#los modulos hacen mas eficiente y ordenado la informacion.


#import pueden estar en cualquier lugar no es necesario que sea de primero


from archivo2 import mi_lista
from archivo2 import mi_diccionario

#from archivo2 import mi_lista, mi_diccionario  #los dos anteriores en una sola linea #usamos la cucaracha para ver la informacion


print('Esto es un ejemplo')
from subfolder.archivo_3 import pato

donald = pato()
p = donald.camina()

mi_lista.append(7)
pass