# quiz_empresas.py
# Quiz 1 - Fundamentos de programacion (Programacion Estructurada + POO)
# Tu tarea: completar todos los bloques marcados con "# TODO".
# Cada linea de empresas.txt tiene:  nombre, sector, num_empleados, ingresos_anuales
# Para ejecutar:  python quiz_empresas.py
#
# CONSEJO: ve completando un TODO a la vez y ejecuta el archivo para ver como
#          se va llenando la salida. Al inicio veras resultados vacios o en cero.


# 1) LA CLASE: representa UNA empresa (datos + comportamiento juntos)
class Empresa:
    """Representa UNA empresa: encapsula sus datos y su comportamiento."""

    # El CONSTRUCTOR se ejecuta al crear el objeto y guarda sus datos.
    # 'self' es el propio objeto que se esta construyendo.
    def __init__(self, nombre, sector, num_empleados, ingresos_anuales):
        self.nombre = nombre
        self.sector = sector
        self.num_empleados = int(num_empleados)
        self.ingresos_anuales = int(ingresos_anuales)     
        #Comentario Juan Leal: Se guarda como atributo cada uno de los parámetros recibidos. 
        #Comentario Juan Leal: Y con int se convierte a entero los que son números.

    def obtener_informacion(self):
        """Devuelve los datos de la empresa como un texto legible."""
        #Comentario Juan Leal: Se devuelve a texto los datos, según la estructura del ejemplo.
        #Comentario Juan Leal: Se usó el f-string con los atributos de self.
        return f"{self.nombre} | {self.sector} | {self.num_empleados} empleados | ${self.ingresos_anuales}"

# 2) Leer el archivo y crear una LISTA DE OBJETOS Empresa
def leer_empresas(nombre_archivo):
    """Lee el archivo y crea un objeto Empresa por cada linea valida.

    Una linea es INVALIDA si num_empleados es menor o igual a 0:
    en ese caso NO se crea el objeto (se ignora el registro).
    """
    empresas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, sector, num_empleados, ingresos_anuales = linea.strip().split(",")
            #Comentario Juan Leal: Se añade la condición si es mayor a 0 para evitar datos inválidos.
            if int(num_empleados) > 0:
                empresa = Empresa(nombre, sector, num_empleados, ingresos_anuales)
                empresas.append(empresa)
    return empresas

# 3) Sumar los ingresos de todas las empresas
def calcular_total_ingresos(empresas):
    """Devuelve la suma de los ingresos_anuales de todas las empresas."""
    #Comentario Juan Leal: Se recorre la lista y se suma el atributo ingresos_anuales de cada empresa.
    total = 0 #Comentario Juan Leal: El acumulador arranca en 0. Para sumar los ingresos de todas las empresas.
    for empresa in empresas:
        total += empresa.ingresos_anuales
    return total

# 4) Quedarse solo con las empresas de un sector
def filtrar_por_sector(empresas, sector):
    """Devuelve una lista con las empresas cuyo sector coincide."""
    filtradas = [] #Comentario Juan Leal: Lista nueva y vacía para guardar las empresas filtradas.
    for empresa in empresas:
        if empresa.sector == sector: #Comentario Juan Leal: Para filtrar según el sector.
            filtradas.append(empresa)
    return filtradas


# 5) Encontrar la empresa con mas empleados
def empresa_con_mas_empleados(empresas):
    """Devuelve el objeto Empresa que tiene mas empleados."""
    if len(empresas) == 0: #Comentario Juan Leal: Si la lista está vacía, devuelve None.
        return None
    mayor = empresas[0] #Comentario Juan Leal: Se asume que la primera empresa es la que tiene más empleados.
    for empresa in empresas:
        if empresa.num_empleados > mayor.num_empleados: #Comentario Juan Leal: Se compara el número de empleados.
            mayor = empresa #Comentario Juan Leal: Si la empresa actual tiene más empleados, se actualiza la variable mayor.
    return mayor

# 6) Calcular el promedio de empleados
def promedio_empleados(empresas):
    """Devuelve el promedio de empleados de todas las empresas."""
    if len(empresas) == 0: #Comentario Juan Leal: Evita dividir entre cero si la lista está vacía.
        return 0
    total = 0
    for empresa in empresas:
        total += empresa.num_empleados
    return round(total / len(empresas), 2) #Comentario Juan Leal: el round se usa para redondear el promedio a 2 decimales.

# 7) Funcion principal: usa todo lo anterior y muestra los resultados
def ejecutar_quiz():
    empresas = leer_empresas("empresas.txt")

    print("--- Empresas registradas ---")
    for empresa in empresas:
        print(empresa.obtener_informacion())

    print("\nTotal de ingresos:", calcular_total_ingresos(empresas))

    print("\n--- Empresas del sector TECNOLOGIA ---")
    for empresa in filtrar_por_sector(empresas, "TECNOLOGIA"):
        print(empresa.obtener_informacion())

    mejor = empresa_con_mas_empleados(empresas)
    if mejor is not None:
        print("\nEmpresa con mas empleados:", mejor.obtener_informacion())

    print("\nPromedio de empleados:", promedio_empleados(empresas))

# Iniciar el programa
ejecutar_quiz()

#COMENTARIOS Y CONCLUSIONES JUAN LEAL:

#Se confirma la salida según lo esperado.

#Como notas personales adicionales, se tuvo presente el error de la empresa fantasma.

#Si tuviera que resaltar una traba en el desarrollo fue en el punto 6, 
#ya que tuve inicialmente el error de dejar el return dentro del for, lo que me daba un promedio incorrecto.

#Afortunadamente se revisó de forma manual y se identificó el error, corrigiéndolo y obteniendo el resultado esperado.

#En conclusión fue interesante el desarrollo de la actividad.
#Considero que aún me falta mucha práctica para poder desarrollar de forma más fluida y rápida.