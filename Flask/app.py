from flask import Flask,request,jsonify
from flask_mysqldb import MySQL 

app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'bdflask'

mysql= MySQL(app)



# Ruta Simple
@app.route('/')
def principal():
    return 'Hola Mundo Flask'


# RutaPruebaConex
@app.route('/pruebaConexion')
def pruebaConexion():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute("Select 1")
        datos= cursor.fetchone()
        return jsonify({'status':'Conexion exitosa', 'data':datos})
    except Exception as ex:
        return jsonify({'status':'Error de Conexion', 'mensaje':str(ex)})
    

# Ruta Doble
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Ivan Isay'

# Rutas con parametros
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola '+ nombre +'!!!'

# Definicion de metodos de trabajo
@app.route('/formulario',methods=['GET','POST'] )
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar passwords por GET'
    elif request.method == 'POST':
        return 'POST si es seguro para passwords'
        
        
#Manejo de excepciones para rutas        
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontre Nada'  




if __name__ == '__main__':
    app.run(port=3000, debug= True)