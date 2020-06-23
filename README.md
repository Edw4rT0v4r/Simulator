# Simulador para `MT` y `AFD`

Este es un simulador para ejecutar programas
de `Maquinas de Turing` y `Autómatas Finitos Deterministas`

## Instalación

Utiliza la versión de `Python 3.8.2`
es necesario descargar una librería con el siguiente comando `pip install colorama`
si no cuentan con `pip` es necesario descargarlo para la versión de `Python 3.8.2`
Puede utilizar este comando también `python3 -m pip install --upgrade pip colorama`

## Funcionamiento

Dentro de la carpeta `examples` 
existen ejemplos para ejecutar el simulador, 
se subdividen en `afd` y `mt`.

En los nombres de los ejemplos los programas
se identifican con el prefijo `p_` 
y las cintas con prefijo `t_`

Para su ejecución debe correr por `consola`
el archivo llamado `simulator.py`

La estructura de ejecución es la siguiente
`python .\simulator.py <<programa>> <<cinta>>`
Tener en cuenta la version de `python` para que funcione correctamente

Para el caso práctico este es un ejemplo:

* `python .\simulator.py .\examples\afd\p_3_1_multiple.txt .\examples\afd\t_3_1_multiple.txt`
* `python .\simulator.py .\examples\mt\p_find_1.txt .\examples\afd\t_find_1.txt`
