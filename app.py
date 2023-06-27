#paquteria de flas
from flask import Flask,render_template,request, redirect,url_for,flash
from flask_mysqldb import MySQL

#la inicializacion del app 
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='Vunity'
app.secret_key='mysecretkey'
MySQL=MySQL(app)
#declaracion o inicializacion de las rutas y le pertenece a http://localhost:5000
@app.route('/')
def iniciio():
        return render_template('inicio.html')
@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        #pasamos a variables el contenido de los input
        Vusuario=request.form['Usuario']
        Vcontraseña=request.form['Contraseña']
    
        #conectar y ejecutar el insert
        CS= MySQL.connection.cursor()
        CS. execute('insert into usuarios(usuario,contraseña) values(%s,%s)',(Vusuario,Vcontraseña))
        MySQL.connection.commit()
    flash('EL ALBUM FUE AGREGADO EXITOSAMENTE')
    return redirect(url_for('inicio'))

#ejecucion del servidor y asignacion del puerto a trabajar
if __name__ == '__main__':
        app.run(port=5000 ,debug= True)

