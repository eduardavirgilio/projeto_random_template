import random

#coisas basicas que sempre tem que ter no codigo

#importando uma parte do flask
from flask import Flask, render_template

#criando a variavel e instanciando
app = Flask(__name__)

#-----------------------------------------------------------------------------

@app.route("/")
def pagina_principal():
    return  """
            <H1>bosta seca</H1>
            <BR>
            <H2>eu adorei o flask</H2>
            """

#-----------------------------------------------------------------------------

#rodar o site
app.run(debug=True, host="0.0.0.0", port="8080")