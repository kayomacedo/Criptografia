#!/usr/bin/python
# -*- coding: <encoding name> -*-
import base64
from cProfile import label
from os import stat

from tkinter import *
from tkinter import font
from tkinter import messagebox
from criptografia import criptografar, descriptografar
import Janela_cript

seta_base64 ="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"

 


def Chamar_Janela_decriptpgrafia():
    janela = Tk()

    #Rotas
    class Rotas():
        def chamarBotão():
            
            
            if (entry_mensagem.get()==""):
                messagebox.showerror("","Preencha o campo de mensagem!")
                entry_mensagem_cod.delete("0.1",END)
            else:
                msg_descript = descriptografar(entry_mensagem.get(),entry_senha.get())
                if(msg_descript == False):
                    messagebox.showerror("","Mensagem ou Senha inválida!")
                    entry_mensagem_cod.delete("0.1",END)
                else:
                    entry_mensagem_cod["state"]="normal"
                    entry_mensagem_cod.delete("0.1",END)
                    entry_mensagem_cod.insert(END,msg_descript)
                    entry_mensagem.delete(0,END)

        def chamar_bt_colar():
            if(len(janela.clipboard_get())<76):
                messagebox.showerror("","Não há criptografia válida copiada!")
                entry_mensagem_cod.delete("0.1",END)
                entry_mensagem.delete(0,END)
            else:
                entry_mensagem.insert(0,janela.clipboard_get())
        
        def chamar_janela_cript():
            
            janela.destroy()
            Janela_cript.Chamar_Janela_criptografia()
            
            

    #Largura Janela
    w = 500
    #Altura Janela
    h =500
    #Altura do display (pixel)
    monitor_height = janela.winfo_screenheight()
    #Largura do display (pixel)
    monitor_width = janela.winfo_screenwidth()

    #Posicionando no meio
    posx = int((monitor_height/2) - (h/2))
    posy = int((monitor_width/2 )- (w/2))

    #Criando e posicionando no tkinter
    janela.geometry(f"{w}x{h}+{posy}+{posx}")
    janela.resizable(False,False)
    janela.title("Programa de Mensagens")
    #frame

    frame1 = Frame(janela,background= "#FFDAB9")
    frame1.place(relx=0,rely=0,relheight=1,relwidth=1)

    #Botões Menu

    bt_cript = Button(frame1,text="Criptografar",background="#E0FFFF",command=Rotas.chamar_janela_cript)

    bt_cript.place(relx=0,rely=0.08,relwidth=0.5)
    bt_desccript = Button(frame1,text="Descriptografar",background="#E0FFFF",state="disable")
    bt_desccript.place(relx=0.5,rely=0.08,relwidth=0.5)

    #Labels e Entrys

    titulo_Programa =Label(janela,text="Criptografia de Mensagens",font=({35}),background="#8B4513",fg="#E0FFFF")
    titulo_Programa.place(relx=0,rely=0.03,relwidth=1)

    titulo_Programa_cript =Label(janela,text="Mensagem Criptografada",font=({35}),background="#FFDAB9")
    titulo_Programa_cript.place(relx=0.3,rely=0.15)

    #Imagem
    photo = PhotoImage(data=base64.b64decode(seta_base64))
    entry_mensagem2=Label(janela,image=photo,background="#FFDAB9")
    entry_mensagem2.place(relx=0.1,rely=0.17,relwidth=0.2)
   

    entry_mensagem =Entry(janela,background="#8B4513",fg="#E0FFFF")
    entry_mensagem.place(relx=0.3,rely=0.22,relwidth=0.5)
    #BT colar
    bt_copiar = Button(frame1,text="Colar",background="#E0FFFF",command=Rotas.chamar_bt_colar)
    bt_copiar.place(relx=0.82,rely=0.22,relwidth=0.1,relheight=0.04)

    lb_senha =Label(janela,text="Senha: ",font=({35}),background="#FFDAB9")
    lb_senha.place(relx=0.18,rely=0.3)

    entry_senha =Entry(janela,background="#8B4513",fg="#E0FFFF")
    entry_senha.place(relx=0.3,rely=0.3,relwidth=0.5)

    #====================================================

    lb_mensagem_cod =Label(janela,text="Mensagem Codificada: ",font=({35}),background="#FFDAB9")
    lb_mensagem_cod.place(relx=0,rely=0.6,relwidth=1)

    entry_mensagem_cod=Text(janela,background="#8B4513",fg="#E0FFFF",state="disable")
    entry_mensagem_cod.place(relx=0.1,rely=0.7,relwidth=0.8, relheight=0.2)


    bt = Button(janela,text="Decodificar Mensagem",background="#E0FFFF",command=Rotas.chamarBotão)
    bt.place(relx=0.2,rely=0.4,relwidth=0.6)

    lb_nozes= Label(frame1,text="Dev: Kayo & Kesya",background="#FFDAB9")
    lb_nozes.place(relx=0,rely=0.96,relwidth=1)




    janela.mainloop()


