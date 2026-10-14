"""**Enunciado: Diccionario Inteligente**
Desarrolla un sistema de autocompletado y diccionario utilizando un Árbol Binario de Búsqueda. En este caso, el BST almacenará Objetos `Palabra`, los cuales contienen el texto de la palabra y su definición. 
Deberás:
1. Cargar al menos 50 palabras en el BST desde un archivo de texto o lista inicial. El ordenamiento en el árbol debe ser alfabético.
2. Permitir al usuario buscar una palabra exacta para obtener su definición.
3. Crear un método `buscar_por_prefijo(prefijo)` que retorne una lista con todas las palabras en el árbol que comiencen con ese prefijo (ej: "au" -> "auto", "autonomía", "aurora").
4. Generar una pequeña interfaz por consola donde el usuario pueda interactuar con el sistema (buscar, ver diccionario completo en orden, salir)."""
class NodoPalabra:
    def __init__(self, texto: str, definicion: str):
        self.texto = texto.lower()
        self.definicion = definicion
        self.izquierdo = None
        self.derecho = None


class DiccionarioBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, texto: str, definicion: str) -> None:
        self.raiz = self._insertar_rec(self.raiz, texto.lower(), definicion)

    def _insertar_rec(self, nodo, texto, definicion):
        if nodo is None:
            return NodoPalabra(texto, definicion)
        if texto < nodo.texto:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, texto, definicion)
        elif texto > nodo.texto:
            nodo.derecho = self._insertar_rec(nodo.derecho, texto, definicion)
        else:
            nodo.definicion = definicion
        return nodo

    def buscar(self, texto: str):
        return self._buscar_rec(self.raiz, texto.lower())

    def _buscar_rec(self, nodo, texto):
        if nodo is None or nodo.texto == texto:
            return nodo
        if texto < nodo.texto:
            return self._buscar_rec(nodo.izquierdo, texto)
        return self._buscar_rec(nodo.derecho, texto)

    def buscar_por_prefijo(self, prefijo: str) -> list:
        resultado = []
        self._prefijo_rec(self.raiz, prefijo.lower(), resultado)
        return resultado

    def _prefijo_rec(self, nodo, prefijo, resultado):
        if nodo is not None:
            if nodo.texto.startswith(prefijo):
                self._prefijo_rec(nodo.izquierdo, prefijo, resultado)
                resultado.append((nodo.texto, nodo.definicion))
                self._prefijo_rec(nodo.derecho, prefijo, resultado)
            elif prefijo < nodo.texto:
                self._prefijo_rec(nodo.izquierdo, prefijo, resultado)
            else:
                self._prefijo_rec(nodo.derecho, prefijo, resultado)

    def inorden(self) -> list:
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append((nodo.texto, nodo.definicion))
            self._inorden_rec(nodo.derecho, resultado)


def cargar_datos(diccionario):
    datos = [
        ("algoritmo", "Secuencia de instrucciones finitas para resolver un problema."),
        ("altura", "Distancia desde la raíz hasta la hoja más profunda."),
        ("ancho", "Medida horizontal."),
        ("archivo", "Conjunto de datos almacenados en un medio."),
        ("arista", "Conexión entre vértices de un grafo."),
        ("árbol", "Estructura de datos no lineal."),
        ("autómata", "Modelo matemático para una máquina de estados."),
        ("balanceado", "Árbol con alturas de subárboles equilibradas."),
        ("binario", "Sistema numérico base 2."),
        ("bucle", "Estructura de control que repite un bloque de código."),
        ("búsqueda", "Proceso de localizar un elemento."),
        ("camino", "Secuencia de vértices conectados."),
        ("ciclo", "Camino cerrado en un grafo."),
        ("clase", "Plantilla para crear objetos en programación orientada a objetos."),
        ("cola", "Estructura FIFO."),
        ("compilador", "Traductor de código fuente a código de máquina."),
        ("consulta", "Solicitud de información a un sistema o base de datos."),
        ("costo", "Peso asignado a una arista."),
        ("depurar", "Encontrar y corregir errores en el software."),
        ("diccionario", "Estructura de datos clave-valor."),
        ("encapsulamiento", "Ocultamiento del estado interno de un objeto."),
        ("enlace", "Conexión entre nodos o referencias."),
        ("grafo", "Estructura con vértices y aristas."),
        ("hoja", "Nodo sin hijos."),
        ("índice", "Estructura para acelerar búsquedas en bases de datos."),
        ("matriz", "Arreglo bidimensional."),
        ("nodo", "Unidad básica de un árbol o grafo."),
        ("orden", "Disposición de elementos."),
        ("pila", "Estructura LIFO."),
        ("puntero", "Variable que almacena la memoria de otra."),
        ("raíz", "Nodo superior del árbol."),
        ("rama", "Camino de nodos."),
        ("recorrido", "Visita sistemática a los nodos."),
        ("recursividad", "Función que se llama a sí misma."),
        ("registro", "Estructura que agrupa datos relacionados."),
        ("servidor", "Computadora que provee servicios en una red."),
        ("sintaxis", "Reglas formales de un lenguaje de programación."),
        ("socket", "Extremo de una comunicación de red bidireccional."),
        ("subárbol", "Árbol formado por un nodo y sus descendientes."),
        ("tabla", "Estructura tabular de filas y columnas."),
        ("tupla", "Estructura de datos inmutable en Python."),
        ("variable", "Espacio de memoria para almacenar valores."),
        ("vector", "Arreglo unidimensional."),
        ("vértice", "Nodo de un grafo."),
        ("versión", "Estado específico de un software en desarrollo."),
        ("virtual", "Simulado por software."),
        ("web", "Sistema de documentos interconectados por internet."),
        ("xml", "Lenguaje de marcado extensible."),
        ("yaml", "Formato de serialización de datos legible."),
        ("zona", "Región específica de red o memoria.")
    ]
    for texto, defn in datos:
        diccionario.insertar(texto, defn)


def iniciar_interfaz():
    dic = DiccionarioBST()
    cargar_datos(dic)

    print("=== 50 palabras disponibles ===")
    palabras_disp = [p for p, d in dic.inorden()]
    print(", ".join(palabras_disp))
    print(f"\nTotal de palabras cargadas: {len(palabras_disp)}")
    print("=============================================")

    while True:
        print("\n--- DICCIONARIO INTELIGENTE ---")
        print("1. Buscar palabra exacta")
        print("2. Buscar por prefijo")
        print("3. Ver diccionario completo (50 palabras y definiciones)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ter = input("Ingrese la palabra a buscar: ").strip()
            res = dic.buscar(ter)
            if res:
                print(f"-> {res.texto}: {res.definicion}")
            else:
                print("-> Palabra no encontrada.")
        elif opcion == "2":
            print("\nGuía de letras iniciales disponibles:")
            print(" - 'a': algoritmo, altura, ancho, archivo, arista, árbol, autómata")
            print(" - 'b': balanceado, binario, bucle, búsqueda")
            print(" - 'c': camino, ciclo, clase, cola, compilador, consulta, costo")
            print(" - 'd': depurar, diccionario")
            print(" - 'e': encapsulamiento, enlace")
            print(" - 'g'-'h'-'i'-'m'-'n'-'o'-'p'-'r'-'s'-'t'-'v'-'xml'-'yaml'-'z'")
            
            pref = input("Ingrese el prefijo: ").strip()
            res = dic.buscar_por_prefijo(pref)
            if res:
                print(f"Se encontraron {len(res)} coincidencias:")
                for p, d in res:
                    print(f" - {p}: {d}")
            else:
                print("-> No hay palabras con ese prefijo.")
        elif opcion == "3":
            print("\nListado completo de las 50 palabras y definiciones:")
            for p, d in dic.inorden():
                print(f" - {p}: {d}")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    iniciar_interfaz()