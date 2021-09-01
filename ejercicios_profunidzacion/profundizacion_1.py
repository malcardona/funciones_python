# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira la dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números.
Esa lista de datos se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos vistos en clase en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamada "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para buscar sacar generala.
Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo canto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tira los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
def ramdom_list(n_try_1):
    try_1 = []
    for n in range(n_try_1):
        dice_r = random.randint(1, 6)
        try_1.append(dice_r)
    return try_1


def max_rep(list):
    if len(list) > 0:
        max_rep = max(list, key=list.count)
    else:
        print('Lista vacia')
        max_rep = 0
    return max_rep

def save_chosen(list, m_r):
    n_list = []
    for n in list:
        if n == m_r:
            n_list.append(n)
    return n_list




# todas las funciones que utilice


# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

## --- Inicio del juego ---
dices_ini = int(input('Cuantos Dados quieres lanzar:\n'))

if dices_ini <= 2:
    print('Muy pocos!')
    dices_ini = 3
elif dices_ini > 6:
    print('6 es el número máxino de dados')
    dices_ini = 6

print('Jugaremos Generala con {} dados'.format(dices_ini))

## --- Ronda 1 --- 
try_1 = ramdom_list(dices_ini)

print('Ronda 1: {}'.format(try_1))   

#Eleccion del número que mas se repite
choosen = max_rep(try_1)

# Guardar el numero mas repetido en una nueva lista
result = []
save = save_chosen(try_1, choosen)
result += save
n_result = len(result)
#print(result)

#########################################
if n_result == dices_ini:
    print('Generala! {}'.format(result))
#########################################
    
print('Deberas completar {} dados con el número {} para ganar!'.format(dices_ini, choosen))

## --- Ronda 2 ---
n_t2 = dices_ini - len(save)

print('Se guardaran {} dados se lanzaran {} dados'.format(n_result, n_t2))

try_2 = ramdom_list(n_t2)
print('Ronda 2: {}'.format(try_2))  

save = save_chosen(try_2, choosen)
result += save
n_result = len(result)
#print(result)

#########################################
if n_result == dices_ini:
    print('Generala! {}'.format(result))
#########################################

# --- Ronda Final ---
n_t3 = n_t2 - len(save)

print('Se guardaran {} dados se lanzaran {} dados'.format(n_result, n_t3))

try_3 = ramdom_list(n_t3)
print('Ronda Final: {}'.format(try_3))  

save = save_chosen(try_3, choosen)
result += save
n_result = len(result)
#print(result)

#####################################################################
if n_result == dices_ini:
    print('Generala! {}'.format(result))
else:
    print('Resultado Final: {} suerte a la próxima!'.format(result))
######################################################################

