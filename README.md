# Bingo_P 🎲📚

Mini Proyecto Final - Análisis de Algoritmos  
Aplicación de consola en Python para gestionar partidas de bingo con palabras.

---

## 📖 Descripción

**Bingo_P** es una aplicación diseñada para simular partidas de bingo con palabras en distintos idiomas.  
Cada jugador posee uno o más cartones con palabras, y un locutor anuncia palabras extraídas de un repositorio.  
El sistema marca automáticamente las coincidencias y determina si algún cartón resulta ganador.

---

## 🎯 Objetivos del Proyecto

- Aplicar conocimientos de **análisis de algoritmos** en un problema real.
- Diseñar una solución eficiente para manejar más de 200 cartones.
- Implementar y probar el sistema bajo restricciones de tiempo y recursos.
- Documentar el diseño teórico y práctico, y presentar resultados.

---

## 🧩 Reglas del Juego

- **Identificador de cartón**: 8 caracteres alfanuméricos.  
  - Prefijo de 2 letras = idioma (`SP`, `EN`, `PT`, `DT`).  
  - Sufijo de 6 dígitos = número único.  

- **Máximo de palabras por cartón**:
  - Español → 24  
  - Inglés → 14  
  - Portugués → 20  
  - Dutch → 10  

- **Orden de rondas**: aleatorio por idioma en cada partida.  
- **Entrada de cartones**:
  - Manual (teclado).  
  - Masiva (archivo `.TXT`).  
- **Salida por ronda**:
  - Identificador del cartón ganador, o  
  - Mensaje de que no hubo ganadores.

---

## ⚙️ Estructura del Sistema

1. **Cartones de jugadores**  
   - Representados con un `set` de palabras y un `contador` de palabras restantes.  
   - Ejemplo:
     ```python
     carton = {
         "id": "SP123456",
         "idioma": "SP",
         "palabras": {"CASA","PERRO","SOL","LIBRO"},
         "contador": 4
     }
     ```

2. **Repositorio de palabras (locutor)**  
   - Diccionario con sets de palabras por idioma.  
   - Ejemplo:
     ```python
     repositorio = {
         "SP": {"CASA","PERRO","SOL","LIBRO","ARBOL","MANO"},
         "EN": {"DOG","HOUSE","SUN","BOOK","TREE","SEA"},
         ...
     }
     ```

3. **Orden de rondas**  
   - Lista de idiomas mezclada con `random.shuffle()`.  

4. **Verificación de ganadores**  
   - Cada vez que se anuncia una palabra:
     - Si está en el cartón → se elimina del set y se decrementa el contador.  
     - Si `contador == 0` → el cartón es ganador.  

---

## 🚀 Ejecución

### 1. Requisitos
- Python 3.x
- Archivo `cartones.txt` con cartones y palabras.

### 2. Ejemplo de `cartones.txt`
    PT300001 CASA CAO GATO SOL LUA MAR CEU TERRA AGUA FOGO AR NUVEM CHUVA NEVE VENTO RAIO TROVAO ONDA RIO LAGO
    PT300002 MONTANHA FLOR ARVORE LIVRO CADEIRA MESA CANETA PAPEL COMPUTADOR CASA CAO GATO SOL LUA MAR CEU TERRA AGUA FOGO AR
    SP100003 NIEVE VIENTO RAYO TRUENO OLA RIO LAGO MONTAÑA FLOR ARBOL LIBRO SILLA MESA LAPIZ PAPEL COMPUTADORA TELEFONO ESCUELA AMIGO FAMILIA CIUDAD PAIS MUNDO UNIVERSO


### 3. Ejecutar el programa
```bash
python bingo_p.py
