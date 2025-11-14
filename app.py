from flask import Flask, render_template, request
import math

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
        
        # Obtener valores adicionales para intervalos
        x0 = float(request.form.get('x0', 0))
        t_value = float(request.form.get('t_value', 0))
        delta = float(request.form.get('delta', 0.05))
        
        # Obtener coeficientes de la función de salario
        a_S = float(request.form.get('a_S', 0))
        b_S = float(request.form.get('b_S', 0))
        
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
        s = math.sqrt(S2) if S2 >= 0 else 0
        
        # Calcular coeficiente de correlación
        r = Sxy / math.sqrt(Sxx * Syy) if Sxx * Syy > 0 else 0
        r2 = r ** 2
        
        # CÁLCULOS DE INTERVALOS DE CONFIANZA Y PREDICCIÓN PARA Y
        # Estimación puntual para x0
        y_hat_x0 = a + b * x0
        
        # Término común para intervalos
        term_comun = (1/n) + ((x0 - mean_x) ** 2) / Sxx
        
        # CORRECCIÓN: Calcular correctamente el error de confianza
        error_conf = t_value * s * math.sqrt(term_comun)
        
        # Intervalo de confianza para E(Y|x0)
        li_conf = y_hat_x0 + error_conf
        ls_conf = y_hat_x0 - error_conf
        
        # Intervalo de predicción para Y|x0
        error_pred = t_value * s * math.sqrt(1 + term_comun)
        li_pred = y_hat_x0 + error_pred
        ls_pred = y_hat_x0 - error_pred
        
        # CÁLCULOS DE INTERVALOS PARA EL SALARIO S = a_S + b_S * Y
        # Estimación puntual del salario para x0
        s_hat_x0 = a_S + b_S * y_hat_x0
        
        # CORRECCIÓN: Transformar correctamente los intervalos para el salario
        # Para el intervalo de confianza de E(S|x0)
        li_conf_s = a_S + b_S * li_conf
        ls_conf_s = a_S + b_S * ls_conf
        
        # Para el intervalo de predicción de S|x0
        li_pred_s = a_S + b_S * li_pred
        ls_pred_s = a_S + b_S * ls_pred
        
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
            'r': r,
            'r2': r2,
            'ecuacion': f"y = {a:.5f} + {b:.5f}x",
            'array_x': array_x_str,
            'array_y': array_y_str,
            'x0': x0,
            't_value': t_value,
            'delta': delta,
            'y_hat_x0': y_hat_x0,
            'li_conf': li_conf,
            'ls_conf': ls_conf,
            'li_pred': li_pred,
            'ls_pred': ls_pred,
            # Resultados para el salario
            'a_S': a_S,
            'b_S': b_S,
            's_hat_x0': s_hat_x0,
            'li_conf_s': li_conf_s,
            'ls_conf_s': ls_conf_s,
            'li_pred_s': li_pred_s,
            'ls_pred_s': ls_pred_s,
            'ecuacion_S': f"S = {a_S:.5f} + {b_S:.5f}·Y",
            # Agregar valores para depuración
            'term_comun': term_comun,
            'error_conf': error_conf,
            'error_pred': error_pred
        }
        
        return render_template('regresion_lineal.html', resultados=resultados)
        
    except ValueError as e:
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