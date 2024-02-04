from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)

# Filtros personalizados

#decorador
@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

#filtro
#app.add_template_filter(today, 'today') otra forma de registrar al igual que el decorador de la linea 8 pero con filtro

# function personalizada con decorador sin enviar por vista
#con decorador
@app.add_template_global
def sum(n1:int, n2:int):
    return n1 + n2

#con filtro
#app.add_template_filter(sum, 'sum') misma accion que lina 20/21

def repeat(s, n):
    return s * n

# function personalizada
def repeat(s, n):
    return s * n

@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('code', code = 'print("Hola")'))
    #name = 'Pablo'
    name = None
    friends = ['Alexandre', 'Roel', 'Juan', 'Pedro']
    date = datetime.now()
    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        date = date,
        repeat = repeat
    )
'''
@app.route('/hello')
def hello():
    return f'<h1>Hola Mundo</h1>'
'''


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<string:name>/<int:age>')
@app.route('/hello/<string:name>/<int:age>/<email>')
def hello(name:str = None, age:int = None, email = None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data = my_data)
'''
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<string:name>/<int:age>/<email>')
def hello_dinamic(name:str = None, age:int = None, email = None):
    if name == None and age == None:
        return f'<h1>Hola Mundo</h1>'
    elif age == None:
        return f'<h1>Hola, {name}!</h1>'
    else:
        return f'<h1>Hola {name}, el doble de tu edad es {age * 2}!</h1>'
'''

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}<code>'

# Crear formulario wtform
class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario: ")
    password = PasswordField("Contraseña: ")
    submit = SubmitField("Registrar: ")


# Registrar usuario
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Nombre de usuario: {username}, Contraseña: {password}"
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
        
    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f"Nombre de usuario: {username}, Contraseña: {password}"
    #     else:
    #         error = """Nombre de usuario debe tener entre 4 y 25 caracteres y la contraseña debe tener entre 6 y 40 caracteres.
    #         """  
    #         return render_template('auth/register.html', form = form, error = error)
    # return render_template('auth/register.html', form = form)

#flask --app hello run (levantar servidor)
#flask --app hello --debug run (levantar servidor con modo debug en el navegador)
# .\env\Scripts\activate (activar entorno virtual)
