#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:11:30 2021

@author: d-nct
"""

# Sessão de Importações
# ---------------------
from imap_tools import MailBox, AND
import os

# Definição das Classes

class Baixador():
    """Objeto baixador de anexos no gmail.
    """
    
    def __init__(self, usr, pwd):
        self.mailbox = MailBox('imap.gmail.com').login(usr, pwd)
    
    @staticmethod
    def _baixar(arquivo, nome, path):
        """Faz o download do arquivo no devido path.
        """
        with open(f"{path}/{nome}", mode='wb') as f:
            f.write(arquivo.payload)
    
    def _baixar_se_novo(self, email, arquivo, tipo, path, verbose):
        """Faz o download do arquivo se ele não consta no path.
        """
        nome = f"{email.date.date()} - {email.subject}.{tipo}"
        baixados = os.listdir(path)
        if novo:= not nome in baixados:
            self._baixar(arquivo, nome, path)
        return nome, novo
    
    @staticmethod
    def _tipos_iguais(arquivo, tipo):
        """Compara o tipo do arquivo com o tipo alvo e retorna o resultado.
        """
        tipo_do_arquivo = arquivo.content_type.split('/')[1]
        return tipo == tipo_do_arquivo
    
    def baixar(self, remetente, tipo, path, verbose=False):
        """Checa a caixa de entrada do email e faz o download dos anexos, se houver, de todos os email do(s) remetente(s) no local indicado.
        """
        if isinstance(remetente, list):
            for rem in remetente: self.baixar(rem, tipo, path, verbose)
        
        elif isinstance(remetente, str):
            if verbose: print(f"Acessando emails de {remetente}")
            lista_emails = self.mailbox.fetch(AND(from_=remetente))
            
            for email in lista_emails:
                if verbose: print(f"  Abrindo o email {email.subject}")
                for anexo in email.attachments: # Se não houver, vai passar direto
                    if verbose: print(f"    Encontrado o anexo {anexo.filename}")
                    if self._tipos_iguais(anexo, tipo):
                        nome, novo = self._baixar_se_novo(email, anexo, tipo, path, verbose)
                        if verbose:
                            if novo: print(f"    > Baixando: {nome}")
                            else:    print(f"    > Já baixado: {nome}")
            if verbose: print("Downloads concluídos!", end='\n\n')