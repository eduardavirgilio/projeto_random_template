import random

#coisas basicas que sempre tem que ter no codigo

#importando uma parte do flask
from flask import Flask, render_template

#criando a variavel e instanciando
app = Flask(__name__)

#-----------------------------------------------------------------------------


lista_cores = ["lavanderblush", "pink", "papayawhip", "snow", "powderblue", "#BABACA", "#e1c8fd"]

@app.route("/sobre")
def pagina_sobre():
    cor_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_fundo_html = cor_fundo)



#-----------------------------------------------------------------------------

#rodar o site
app.run(debug=True)