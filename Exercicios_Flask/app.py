
from fileinput import filename
from flask import Flask 
from flask import render_template
from flask import url_for, redirect
from flask import request # Log do site 
import pandas as pd

# pd.read_csv('produtos.csv', header=None, names=['produtos', 'valores'], index_col='produtos')

app = Flask(__name__, template_folder='Exercicios_flask') # Caminho para executar o programa 

@app.route('/home') # Pode ter duas rotas para o mesmo lugar
@app.route('/') # Primeira rota- HOME 

def index(): 
    print("Hello print") # Aparece no terminal
    return "Hello return" # Aparece no Site

# @app.route('/rota2') # Segunda rota 
# def rota2(): 
#     return "Rota - 2"

# @app.route('/rotaoi/<nome>') # Interação - Parametros na URL
# def hello(nome):
#     print("Saudação!")
#     return f'Olá {nome} !!!!' 

# # CADASTRAR PRODUTOS / LISTA ##############################################################

# lista=[]

# @app.route('/listar') # LISTAR
# def listar():
#     return lista

# @app.route('/adicionarlista/<produtos>') # adicionar
# def adicionarlista(produtos):
#     lista.append(produtos)
#     return f'''
#     Produto adicionado:

#     {lista}
#     '''

# @app.route('/removerlista/<produtos>') # Remover
# def removelista(produtos):
#     lista.remove(produtos)
#     return f'''
#     Produto removido:

#     {lista}
#     '''

# CADASTRAR PRODUTOS / DICIONARIO ########################################################

# produtos = {} #{produto: valor}
dicio={}

@app.route('/dicionario') # LISTAR
def lisdic():
    return dicio

@app.route('/add_dic/<produtos>/<valor>') # adicionar
def adi(produtos,valor):
    dicio [produtos] = float(valor)
    # dicio.add(produtos, valor)
    # dicio.add()
    return f'''
    Produto adicionado:
    {dicio}
    '''

    # Acessar pasta ou pagina
    # para proteger arquivo e pasta crie uma rota 

@app.route('/cadastrar')
def cadastrar():
    argumentos = request.args.to_dict() # variavel local
    print(argumentos)
    return redirect('/static/formulario.html') # facil
    # return url_for('static',filename("formulario.html")) -  DIFICIL

# pd.Series(produtos).to_csv('produtos.csv', header=False)


# rodar o App quando exercutar os peograma no app.py
if __name__ == "__main__":
    app.run(debug=True)