import random

#coisas basicas que sempre tem que ter no codigo

#importando uma parte do flask
from flask import Flask, render_template

#criando a variavel e instanciando
app = Flask(__name__)

#-----------------------------------------------------------------------------


lista_cores = ["lavanderblush", "pink", "papayawhip", "snow", "powderblue", "#BABACA", "#e1c8fd"]

lista_imagens = ["taylor_ttpd.jpg", "taylor-swift-ttpd-album-review.png", "taylor-lencol-ttpd.jpg", "clipe-fortnight.jpg", "taylor-shot-ttpd.jpg", "taylor-01.jpg", "taylor-01.jpg","taylor-02.jpg", "taylor-03.jpg", "taylor-04.jpg", "taylor-05.jpg", "taylor-06.jpg", "taylor-07.jpg"]

letras_musica = ["'E quando eu senti como se eu fosse um cardigã velho, debaixo da cama de alguém, você me vestiu e disse que eu era seu favorito' (Cardigan)", 
                 "'Todas as minhas manhãs são segundas-feiras' (Fortnight)", 
                 "'Você sabe, os melhores filmes de todos os tempos nunca foram feitos' (The 1)", 
                 "'Eu olho direto para o Sol, mas nunca para o espelho.' (Anti-Hero)", 
                 "'Você não sabe o que tem até que tenha perdido' (You're losing me)", 
                 "'Eu estou tão cansada de correr o mais rápido que consigo, imaginando se eu chegaria lá mais rápido se eu fosse um homem' (The man)", 
                 "'E se você nunca sangrar, você nunca vai crescer' (The 1)"]

@app.route("/sobre")
def pagina_sobre():
    cor_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_fundo_html = cor_fundo)

@app.route("/home")

def pagina_principal():
    imagem_aleatoria = random.choice(lista_imagens)

    frase_aleatoria = random.choice(letras_musica)

    return render_template("home.html", 
                           frase_aleatoria_html = frase_aleatoria, 
                           imagem_aleatoria_html = imagem_aleatoria)

@app.route("/cadastro")

def pagina_cadastro():
    return render_template("cadastro.html",  frases = letras_musica)



# lista_imagens_html = lista_imagens, 

#-----------------------------------------------------------------------------

#rodar o site
app.run(debug=True)