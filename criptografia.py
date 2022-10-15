#!/usr/bin/python
# -*- coding: <encoding name> -*-
import cryptocode


def criptografar(mensagem,chave):

    

    dado_criptografado = cryptocode.encrypt(mensagem, chave)
    
    return dado_criptografado

def descriptografar(dado_criptografado,chave):

    dado_descriptografado = cryptocode.decrypt(dado_criptografado, chave)
 
    return dado_descriptografado



