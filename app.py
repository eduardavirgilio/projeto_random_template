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


lista_imagens = ["taylor_ttpd.jpg", "taylor_swift.png"]
letras_musica = ["'E quando eu senti como se eu fosse um cardigã velho, debaixo da cama de alguém, você me vestiu e disse que eu era seu favorito' (Cardigan)", "'Todas as minhas manhãs são segundas-feiras' (Fortnight)"]

@app.route("/home")
def pagina_inicial():
    lista_imagens = random.choice(lista_imagens)
    letras_musica = random.choice(letras_musica)
    return render_template("home.html", lista_imagens_html = lista_imagens, letras_musica_html = letras_musica)

#-----------------------------------------------------------------------------

#rodar o site
app.run(debug=True)