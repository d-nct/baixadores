# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:07:31 2020

@author: danieln
"""
from urllib.request import urlretrieve

def baixar_xkcd (num_tirinha, onde_salvar='D:\Imagens\XKCD\Charge -'):
#    endereço_base = 'https://imgs.xkcd.com/comics/meteor_showers.png'
#    endereço = num_tirinha + endereço_base
    nome_do_arquivo = num_tirinha.split('/')[-1]
    urlretrieve (num_tirinha, onde_salvar + nome_do_arquivo)


def interação_com_usuário():
#    num_tirinha = input('Digite o número da tirinha: \n->')
    num_tirinha = input('Cole a URL da imagem: \n->')
    print()
    onde_salvar = input("Digite o caminho do sistema em que os arquivos serão salvos (<enter> para D:\Imagens\XKCD):\n->")
    if onde_salvar == '':
        onde_salvar = 'D:\Imagens\XKCD\Charge -'
    print()
    
    print("Baixando a tirinha " + num_tirinha + "...")
    print(onde_salvar)
    baixar_xkcd (num_tirinha, onde_salvar)
    print("Download concluído!")

#interação_com_usuário()