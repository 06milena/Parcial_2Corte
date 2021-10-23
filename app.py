from flask import Flask, render_template, request,redirect
from controllers import users


app = Flask(__name__)

@app.get('/')
def home():
    return render_template('crearBase.html')



@app.post('/guardar')
def guardarData(): 
    ingreso  = request.form
    if(ingreso.getlist('check')):
      print('mostrar')
      print(ingreso)
      datos = users.listarBases(ingreso)
      print(datos)
      return render_template('crearBase.html',datosDB = datos)

      


      
    else: 
      print('nochek')
      
      

      
      
      




app.run(debug=True)