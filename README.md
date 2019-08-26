Derivar Contraseña (Ethical Hacking)
==========================

La prueba consiste en encontrar la **contraseña más corta** para la cual todas las secuencias 
proporcionadas en el archivo **keylog.txt** sean correctas.

Para ello, se realizó previamente un acercamiento al problema por medios de pruebas de escritorio, 
cuyas capturas se encuentran anexadas en la carpeta static. Una vez depurado, se construyó el algoritmo 
que da solución a este problema, cuyos pasos se ilustran en el siguiente diagrama de flujo.

![image](/static/flowchart.svg)


Demostración y solución
-----------------------
Se toman las siguientes combinaciones al azar de keylog.txt: **620**, **762**, **689**.

**Valor inicial de la contraseña**

Cadena de texto vacía


**Iteración #1** (620)

El dígito 6 no existe en la contraseña. Lo añadimos al final.

Contraseña: 6

El dígito 2 no existe en la contraseña. Lo añadimos al final.

Contraseña: 62

El dígito 0 no existe en la contraseña. Lo añadimos al final.

Contraseña: 620

**Iteración #2** (762)

El dígito 7 no existe en la contraseña. Lo añadimos al final.

Contraseña: 6207

El dígito 6 existe en la contraseña, pero en el orden incorrecto. Lo reubicamos justo después del 7.

Contraseña: 2076

El dígito 0 existe en la contraseña, pero en el orden incorrecto. Lo reubicamos justo después del 6.

Contraseña: 2760

**Iteración #3** (689)

El dígito 6 existe en la contraseña y en el orden correcto.

Contraseña: 2760

El dígito 8 no existe en la contraseña. Lo añadimos al final.

Contraseña: 27608

El dígito 9 no existe en la contraseña. Lo añadimos al final.

Contraseña: 276089


Al continuar con las iteraciones sucesivas para el resto de combinaciones, el algoritmo obtiene como 
solución del problema la contraseña **73162890**, siendo la más corta posible.

El resto de iteraciones pueden ser visualizadas al momento de ejecutar el test verbose.


Uso
------------
De acuerdo a las instrucciones del documento recibido, el proyecto contiene un Dockerfile basado en Python3.

Para construir localmente la imagen docker del proyecto:
```.bash
docker build -t credyty/pwdfinder:1.0 .

```

Para ejecutar la imagen docker:
```.bash
docker run -ti credyty/pwdfinder:1.0 .

```

Clases
------------
El programa consiste en una única clase llamada **PasswordFinder**. Hereda implícitamente a la clase **object** 
de Python.

Contiene los métodos
- **__init__**: Constructor de la clase
- **load_samples**: Carga y preprocesa la lista de combinaciones, desde un archivo de texto.
- **compute_password**: Implementación del algoritmo. Retorna la contraseña calculada.

Decoradores
- **measure_time**: Añade a cada método la medición del tiempo de ejecución.

Variables de clase
- **sequences**: Almacena la lista de combinaciones previamente cargada.
- **messages**: Almacena la lista de mensages para debbugging.

![image](/static/classes.png)


Notas
------------
-   Se incluyen dos tests para la clase construida.
-   El test verbose está destinado a mostrar paso a paso la ejecución y progreso del algoritmo. Se estableció el nivel 
    de logging a DEBUG.
-   El test estándar está destinado a medir el tiempo de ejecución aproximado y evaluar la eficiencia del algoritmo. 
    Se estableció el nivel de logging a INFO para obtener una mayor exactitud en dicha medición y no incluir el tiempo 
    que toma el sistema para imprimir la gran cantidad de mensajes de debugging.
