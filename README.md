# Calculadora de Regresión Lineal Simple - Flask

Esta aplicación web permite calcular la ecuación de regresión lineal simple a partir de dos conjuntos de datos (X e Y).

## Estructura del Proyecto

```
RegresionLineal/
├── .venv/              # Entorno virtual de Python
├── app.py              # Aplicación Flask principal
├── main.py             # Script original de consola
├── templates/
│   └── index.html      # Plantilla HTML de la aplicación web
└── README.md           # Este archivo
```

## Características

- ✅ Interfaz web moderna y responsive
- ✅ Cálculo de regresión lineal simple
- ✅ Muestra todos los resultados intermedios (∑x, ∑y, ∑xy, ∑x², ∑y²)
- ✅ Validación de datos de entrada
- ✅ Manejo de errores
- ✅ Diseño atractivo con gradientes

## Requisitos

- Python 3.7 o superior
- Flask

## Instalación y Uso

El entorno virtual ya está creado y Flask ya está instalado. Para ejecutar la aplicación:

1. Asegúrate de estar en el directorio del proyecto
2. Ejecuta la aplicación Flask:
   ```bash
   .venv/bin/python app.py
   ```
3. Abre tu navegador y ve a: `http://127.0.0.1:5000`

## Cómo Usar la Aplicación

1. Ingresa los valores de X separados por comas (ejemplo: 1, 2, 3, 4, 5)
2. Ingresa los valores de Y separados por comas (ejemplo: 2, 4, 6, 8, 10)
3. Haz clic en "Calcular Regresión"
4. Los resultados se mostrarán en la misma página, incluyendo:
   - Todas las sumatorias necesarias
   - Los coeficientes a (intercepto) y b (pendiente)
   - La ecuación final de la recta: y = a + bx

## Notas

- Los valores de X e Y deben tener la misma cantidad de elementos
- Se deben ingresar valores numéricos válidos
- La aplicación maneja errores y muestra mensajes informativos

## Archivos

- `app.py`: Contiene la lógica del servidor Flask y los cálculos de regresión
- `templates/index.html`: Interfaz de usuario con estilos CSS incluidos
- `main.py`: Script original de línea de comandos (aún funcional)
