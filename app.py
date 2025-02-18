import random

from .data import listas_configuracao as listas

#coisas basicas que sempre tem que ter no codigo

#importando uma parte do flask
from flask import Flask, render_template, request, redirect

#criando a variavel e instanciando
app = Flask(__name__)

#-----------------------------------------------------------------------------



@app.route("/sobre")
def pagina_sobre():
    cor_fundo = random.choice(listas.lista_cores)
    return render_template("sobre.html", cor_fundo_html = cor_fundo)

@app.route("/home", methods = ["GET"])

def pagina_principal():
    imagem_aleatoria = random.choice(listas.lista_imagens)

    frase_aleatoria = random.choice(listas.letras_musica)

    return render_template("home.html", 
                           frase_aleatoria_html = frase_aleatoria, 
                           imagem_aleatoria_html = imagem_aleatoria)

@app.route("/cadastro", methods = ["GET"])

def pagina_cadastro():
    return render_template("cadastro.html",  frases = listas.letras_musica)

@app.route("/post/cadastrarfrase", methods = ["POST"])
def post_cadastrarfrase():
    frase_vinda_do_html = request.form.get("frase")
    listas.letras_musica.append (frase_vinda_do_html)
    return redirect("/cadastro")

@app.route("/cadastro-frases/delete/<indice_frase>", methods = ["GET"])
def delete_frases(indice_frase):

    #converte o indice para inteiro pois ele vem como string
    indice_frase = int(indice_frase)

    #exclui a cor da lista atraves do indice
    listas.letras_musica.pop(indice_frase)

    #redireciona para a rota cadastro frases
    return redirect("/cadastro")

@app.route("/cadastro-cores", methods = ["GET"])
def pagina_cadastro_cores():
    return render_template("cadastro-cores.html",  cores = listas.
                           lista_cores)

@app.route("/post/cadastrarcores", methods = ["POST"])
def post_cadastrarcores():
    cor_vinda_do_html = request.form.get("cor")
    listas.lista_cores.append (cor_vinda_do_html)
    return redirect("/cadastro-cores")

@app.route("/cadastro-cores/delete/<indice_cor>", methods = ["GET"])
def delete_cores(indice_cor):

    #converte o indice para inteiro pois ele vem como string
    indice_cor = int(indice_cor)

    #exclui a cor da lista atraves do indice
    listas.lista_cores.pop(indice_cor)

    #redireciona para a rota cadastro cores
    return redirect("/cadastro-cores")

# lista_imagens_html = lista_imagens, 

#-----------------------------------------------------------------------------

#post - enviar uma informação 
#get pegar uma informação

#rodar o site
app.run(debug=True)