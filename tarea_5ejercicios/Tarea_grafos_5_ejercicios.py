"""
Unidad 9: Árboles - Árbol Binario de Búsqueda (BST)
Implementación profesional con tipado estático y resolución de la Tarea 6.
"""
from collections import deque
from typing import Optional, List, Any

class NodoArbol:
    """Clase que representa un nodo en un árbol binario."""
    def __init__(self, valor: Any):
        self.valor = valor
        self.izquierdo: Optional['NodoArbol'] = None
        self.derecho: Optional['NodoArbol'] = None


class ArbolBinarioBusqueda:
    """Clase que representa un Árbol Binario de Búsqueda (BST)."""
    
    def __init__(self):
        self.raiz: Optional[NodoArbol] = None

    # ==========================================
    # OPERACIONES BÁSICAS (Sección 3)
    # ==========================================
    def insertar(self, valor: Any) -> None:
        """Inserta un nuevo valor en el árbol de forma ordenada."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual: NodoArbol, valor: Any) -> None:
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)

    def buscar(self, valor: Any) -> bool:
        """Busca un valor en el árbol. Retorna True si existe, False si no."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual: Optional[NodoArbol], valor: Any) -> bool:
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor:
            return True
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        return self._buscar_recursivo(nodo_actual.derecho, valor)

    # ==========================================
    # RECORRIDOS (Sección 3)
    # ==========================================
    def inorden(self) -> List[Any]:
        """Recorrido Inorden: Izquierda -> Raíz -> Derecha."""
        resultado: List[Any] = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo: Optional[NodoArbol], resultado: List[Any]) -> None:
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecho, resultado)

    # ==========================================
    # RESOLUCIÓN DE LA TAREA (Sección 6)
    # ==========================================
    
    # --- TAREA 1: ELIMINAR NODO ---
    def eliminar(self, valor: Any) -> None:
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo: Optional[NodoArbol], valor: Any) -> Optional[NodoArbol]:
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_rec(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            sucesor = self._min_nodo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.valor)
        return nodo

    def _min_nodo(self, nodo: NodoArbol) -> NodoArbol:
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    # --- TAREA 2: RECORRIDO POR NIVELES (BFS) ---
    def bfs(self) -> List[Any]:
        if self.raiz is None:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado

    # --- TAREA 3: SUMA DE ELEMENTOS ---
    def sumar_elementos(self) -> Any:
        return self._sumar_rec(self.raiz)

    def _sumar_rec(self, nodo: Optional[NodoArbol]) -> Any:
        if nodo is None:
            return 0
        return nodo.valor + self._sumar_rec(nodo.izquierdo) + self._sumar_rec(nodo.derecho)

    # --- TAREA 4: ES COMPLETO ---
    def es_completo(self) -> bool:
        return self._es_completo_rec(self.raiz)

    def _es_completo_rec(self, nodo: Optional[NodoArbol]) -> bool:
        if nodo is None:
            return True
        if nodo.izquierdo is None and nodo.derecho is None:
            return True
        if nodo.izquierdo is not None and nodo.derecho is not None:
            return self._es_completo_rec(nodo.izquierdo) and self._es_completo_rec(nodo.derecho)
        return False

    # --- TAREA 5: BALANCEAR UN ÁRBOL DEGENERADO ---
    def balancear_arbol(self) -> None:
        elementos = self.inorden()
        self.raiz = self._construir_balanceado(elementos, 0, len(elementos) - 1)

    def _construir_balanceado(self, lista: List[Any], inicio: int, fin: int) -> Optional[NodoArbol]:
        if inicio > fin:
            return None
        medio = (inicio + fin) // 2
        nodo = NodoArbol(lista[medio])
        nodo.izquierdo = self._construir_balanceado(lista, inicio, medio - 1)
        nodo.derecho = self._construir_balanceado(lista, medio + 1, fin)
        return nodo

    # ==========================================
    # UTILIDADES DE VISUALIZACIÓN
    # ==========================================
    def mostrar_arbol(self) -> None:
        """Muestra el árbol rotado 90 grados en consola."""
        self._imprimir_nodo(self.raiz, "", True)

    def _imprimir_nodo(self, nodo: Optional[NodoArbol], prefijo: str, es_izquierdo: bool) -> None:
        if nodo is not None:
            self._imprimir_nodo(nodo.derecho, prefijo + ("|   " if es_izquierdo else "    "), False)
            print(prefijo + ("\\-- " if es_izquierdo else "/-- ") + str(nodo.valor))
            self._imprimir_nodo(nodo.izquierdo, prefijo + ("    " if es_izquierdo else "|   "), True)


# ==========================================
# BLOQUE DE PRUEBAS
# ==========================================
if __name__ == "__main__":
    bst = ArbolBinarioBusqueda()
    valores_prueba = [50, 30, 70, 20, 40, 60, 80]
    
    print("--- 1. INSERCIÓN E INORDEN ---")
    for val in valores_prueba:
        bst.insertar(val)
    print("Recorrido Inorden:", bst.inorden())

    print("\n--- 2. TAREA 1: ELIMINAR ---")
    print("Eliminando 20 (hoja)...")
    bst.eliminar(20)
    print("Inorden después de eliminar 20:", bst.inorden())

    print("\n--- 3. TAREA 2: BFS (RECORRIDO POR NIVELES) ---")
    print("Recorrido BFS:", bst.bfs())

    print("\n--- 4. TAREA 3: SUMA DE ELEMENTOS ---")
    print("Suma total de valores:", bst.sumar_elementos())

    print("\n--- 5. TAREA 4: ¿ES COMPLETO? ---")
    print("¿El árbol actual es completo?:", bst.es_completo())

    print("\n--- 6. TAREA 5: BALANCEAR ÁRBOL ---")
    bst_degenerado = ArbolBinarioBusqueda()
    for val in [1, 2, 3, 4, 5]:
        bst_degenerado.insertar(val)
    print("Inorden degenerado:", bst_degenerado.inorden())
    bst_degenerado.balancear_arbol()
    print("Inorden tras balancear:", bst_degenerado.inorden())
    print("BFS tras balancear:", bst_degenerado.bfs())