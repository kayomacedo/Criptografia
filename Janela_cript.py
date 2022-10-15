#!/usr/bin/python
# -*- coding: <encoding name> -*-
from tkinter import *
from tkinter import messagebox
from criptografia import criptografar, descriptografar
import Janela_descrip
#FFDAB9



def Chamar_Janela_criptografia():
    janela = Tk()

    #Rotas
    class Rotas():
        def chamarBotão():
            
            
            try:
                if(entry_mensagem.get()==""):
                    messagebox.showerror("","Preencha o campo de mensagem!")
                
                else:
                    msg_cript = criptografar(entry_mensagem.get(),entry_senha.get())
            except:
                pass
            
            

            
            entry_mensagem_cod["state"]="normal"
            entry_mensagem_cod.delete("0.1",END)
            try:
                entry_mensagem_cod.insert(END,msg_cript)
            except:
                pass
            messagebox.showinfo("", "Criptografia gerada!")

        def chamar_bt_copiar():
            try:
                msg = entry_mensagem_cod.get('1.0', 'end')
                janela.clipboard_clear()
                janela.clipboard_append(msg)

                if(len(janela.clipboard_get()) <76):
                    messagebox.showerror("","Criptografia precisa ser gerada!")
                
            except:
                print("Deu errado!")

        def pag_descript():
            janela.destroy()
            Janela_descrip.Chamar_Janela_decriptpgrafia()
        


    janela.geometry("500x500")
    janela.resizable(False,False)
    janela.title("Programa de Mensagens")
    #frame

    frame1 = Frame(janela,background= "#FFDAB9")
    frame1.place(relx=0,rely=0,relheight=1,relwidth=1)

    #Botões Menu

    bt_cript = Button(frame1,text="Criptografar",background="#E0FFFF",state="disable")

    bt_cript.place(relx=0,rely=0.08,relwidth=0.5)
    bt_cript = Button(frame1,text="Descriptografar",background="#E0FFFF",command=Rotas.pag_descript)
    bt_cript.place(relx=0.5,rely=0.08,relwidth=0.5)

    #Labels e Entrys

    titulo_Programa =Label(janela,text="Criptografia de Mensagens",font=({35}),background="#8B4513",fg="#E0FFFF")
    titulo_Programa.place(relx=0,rely=0.03,relwidth=1)

    lb_mensagem =Label(janela,text="Sua Mensagem: ",font=({35}),background="#FFDAB9")
    lb_mensagem.place(relx=0.029,rely=0.2)

    entry_mensagem =Entry(janela,background="#8B4513",fg="#E0FFFF")
    entry_mensagem.place(relx=0.3,rely=0.2,relwidth=0.5)

    lb_senha =Label(janela,text="Senha: ",font=({35}),background="#FFDAB9")
    lb_senha.place(relx=0.08,rely=0.3)

    entry_senha =Entry(janela,background="#8B4513",fg="#E0FFFF")
    entry_senha.place(relx=0.3,rely=0.3,relwidth=0.5)

    #====================================================

    lb_mensagem_cod =Label(janela,text="Mensagem Codificada: ",font=({35}),background="#FFDAB9")
    lb_mensagem_cod.place(relx=0,rely=0.6,relwidth=1)

    entry_mensagem_cod=Text(janela,background="#8B4513",fg="#E0FFFF",state="disable")
    entry_mensagem_cod.place(relx=0.1,rely=0.68,relwidth=0.8, relheight=0.2)


    bt = Button(janela,text="Codificar Mensagem",background="#E0FFFF",command=Rotas.chamarBotão)
    bt.place(relx=0.2,rely=0.4,relwidth=0.6)

    bt_copiar = Button(janela,text="Copiar Mensagem",background="#E0FFFF",command=Rotas.chamar_bt_copiar)
    bt_copiar.place(relx=0.2,rely=0.90,relwidth=0.6)

    lb_nozes= Label(frame1,text="Dev: Kayo & Kesya",background="#FFDAB9")
    lb_nozes.place(relx=0,rely=0.96,relwidth=1)


    janela.mainloop()
