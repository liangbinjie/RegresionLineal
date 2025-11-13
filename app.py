from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/regresion-lineal')
def regresion_lineal():
    return render_template('regresion_lineal.html')

@app.route('/regresion-lineal/calcular', methods=['POST'])
def calcular_regresion():
    try:
        # Obtener los valores de X y Y del formulario
        array_x_str = request.form.get('array_x', '')
        array_y_str = request.form.get('array_y', '')
        
        # Convertir las cadenas a listas de números
        array_x = [float(i.strip()) for i in array_x_str.split(",") if i.strip()]
        array_y = [float(i.strip()) for i in array_y_str.split(",") if i.strip()]
        
        # Validar que tengan la misma longitud
        if len(array_x) != len(array_y):
            return render_template('regresion_lineal.html', 
                                 error="Error: Los arreglos deben tener la misma longitud.")
        
        if len(array_x) == 0:
            return render_template('regresion_lineal.html', 
                                 error="Error: Debe ingresar al menos un par de valores.")
        
        # Realizar los cálculos de regresión lineal
        n = len(array_x)
        sum_x = sum(array_x)
        sum_y = sum(array_y)
        sum_xy = sum(x * y for x, y in zip(array_x, array_y))
        sum_x2 = sum(x ** 2 for x in array_x)
        sum_y2 = sum(y ** 2 for y in array_y)
        
        # Calcular los coeficientes a y b
        b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        a = (sum_y - b * sum_x) / n
        
        # Calcular medias
        mean_x = sum_x / n
        mean_y = sum_y / n
        
        # Calcular Sxx, Syy, Sxy
        Sxx = sum_x2 - (sum_x ** 2) / n
        Syy = sum_y2 - (sum_y ** 2) / n
        Sxy = sum_xy - (sum_x * sum_y) / n
        
        # Calcular valores predichos y residuos
        y_pred = [a + b * x for x in array_x]
        residuos = [y - y_p for y, y_p in zip(array_y, y_pred)]
        
        # Calcular SCE (Suma de Cuadrados del Error)
        SCE = Syy - b * Sxy
        
        # Calcular S^2 (varianza del error) y s (desviación estándar del error)
        S2 = SCE / (n - 2) if n > 2 else 0
        s = S2 ** 0.5
        
        # Preparar los resultados
        resultados = {
            'n': n,
            'sum_x': sum_x,
            'sum_y': sum_y,
            'sum_xy': sum_xy,
            'sum_x2': sum_x2,
            'sum_y2': sum_y2,
            'mean_x': mean_x,
            'mean_y': mean_y,
            'Sxx': Sxx,
            'Syy': Syy,
            'Sxy': Sxy,
            'SCE': SCE,
            'S2': S2,
            's': s,
            'a': a,
            'b': b,
            'ecuacion': f"y = {a:.8f} + {b:.8f}x",
            'array_x': array_x_str,
            'array_y': array_y_str
        }
        
        return render_template('regresion_lineal.html', resultados=resultados)
        
    except ValueError:
        return render_template('regresion_lineal.html', 
                             error="Error: Por favor ingrese valores numéricos válidos.")
    except ZeroDivisionError:
        return render_template('regresion_lineal.html', 
                             error="Error: No se puede calcular la regresión con estos datos (división por cero).")
    except Exception as e:
        return render_template('regresion_lineal.html', 
                             error=f"Error inesperado: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
