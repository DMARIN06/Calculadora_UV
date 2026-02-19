from flask import Flask, request
from 

app = Flask (__name__)

@app.route("/")
def home():
    return '''

<h1> Aplicación Calculadora </h1>

<p> Opciones disponibles </p>

<ul>

    <li><a href="suma?a=8&b=12"> Suma </a>  </li>
    <li><a href="resta?a=12&b=8"> Resta </a> </li>
    <li><a href= "multiplicacion?a=8&b=12"> multiplicacion </a> </li>
    <li><a href= "division?a=8&b=2"> division </a> </li>
    <li><a href= "division_?a=5&b=2"> division_ </a> </li>

</ul>

'''

#esta es una ruta adicional en la aplicación
@app.route("/suma")
def ruta_suma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a+b
    return f'''
    "La suma de los numeros {a} y {b} es: {resultado} "
    <a href="/"> 
    volver al inicio<a/>
    '''
    
@app.route("/resta")
def ruta_resta():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a-b 
    return f'''
      "La resta de los numeros {a} y {b} es: {resultado} "
      <a href="/"> 
    volver al inicio<a/>
    '''

@app.route("/multiplicacion")
def ruta_multiplicacion():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a*b 
    return f"La multiplicacion de los numeros {a} y {b} es: {resultado} "

@app.route("/division")
def ruta_division():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a//b 
    return f"La division de los numeros {a} y {b} es: {resultado} "

@app.route("/division_")
def ruta_division_():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado= round(a//b) 
    return f"La division_ de los numeros {a} y {b} es: {resultado} "



#esto nos permite actualizar rápidamente los cambios
if __name__=="main_":
    app.run(debug=True)
