#!/usr/bin/python
# -*- coding: <encoding name> -*-
from cProfile import label
from os import stat
from tkinter import *
from tkinter import font
from tkinter import messagebox
from criptografia import criptografar, descriptografar
import Janela_cript



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
                    messagebox.showerror("","Mensagem inválida!")
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



    janela.geometry("500x500")
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

    entry_mensagem =Entry(janela,background="#8B4513",fg="#E0FFFF")
    entry_mensagem.place(relx=0.3,rely=0.22,relwidth=0.5)
    #BT colar
    bt_copiar = Button(frame1,text="Colar",background="#E0FFFF",command=Rotas.chamar_bt_colar)
    bt_copiar.place(relx=0.82,rely=0.22,relwidth=0.1,relheight=0.04)

    lb_senha =Label(janela,text="Senha: ",font=({35}),background="#FFDAB9")
    lb_senha.place(relx=0.08,rely=0.3)

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



