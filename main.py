
import tkinter
from tkinter import Tk, messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk

# FUNCOES


def gerarCronograma():
    tempo = 0
    atrasoMaximoTotal = 0
    for child in tree.get_children():
        valor = tree.item(child)["values"]
        inicio = tempo
        final = tempo + valor[1]
        tempo = tempo + valor[1]
        AtrasoMaximo = final - valor[2]
        if AtrasoMaximo > atrasoMaximoTotal:
            atrasoMaximoTotal = AtrasoMaximo
        estudosList.insert('', 'end', text="1", values=(
            valor[0], valor[1], valor[2], inicio, final))
    messagebox.showinfo(title="Atraso Maximo",
                        message=f"Seu atraso Máximo é de:{atrasoMaximoTotal}")


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(key=lambda t: int(t[0]), reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col,
               command=lambda: treeview_sort_column(tv, col, not reverse))


def addComent():
    if inputEvent.get() == "" or inputDeadLine == "" or inputDuration == "":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    try:
        title = inputEvent.get()
        termino = int(inputDeadLine.get())
        duracao = int(inputDuration.get())
        tree.insert('', 'end', text="1", values=(title, duracao, termino))
        inputEvent.delete(0, tkinter.END)
        inputDuration.delete(0, tkinter.END)
        inputDeadLine.delete(0, tkinter.END)
    except ValueError:
        messagebox.showinfo(title="ERRO", message="Dados incorretos")


def delComent():
    try:
        selected_item = tree.selection()[0]  # get selected item
        tree.delete(selected_item)
    except:
        messagebox.showinfo(
            title="ERRO", message="Selecione um elemento a ser deletado!")


def Clear():
    estudosList.delete(*estudosList.get_children())


# MAIN FRAME

root = tkinter.Tk()
root.geometry("1000x600")
root.wm_title("Minha Agenda")

s = ttk.Style()


# LIST BOX FRAME
notebookRoot = ttk.Notebook(root)
notebookRoot.pack()


eventsFrame = tkinter.LabelFrame(
    notebookRoot)
eventsFrame.place(relwidth=1, relheight=0.5)
notebookRoot.add(eventsFrame, text="Trabalhos")


tree = ttk.Treeview(eventsFrame)
tree.grid(sticky='news')

ft_columns = ('Titulo', 'Duracao', 'DeadLine')
tree.configure(columns=ft_columns)

for heading in ft_columns:
    tree.heading(heading, text=heading)

tree.configure(show='headings')
for col in ft_columns:
    tree.heading(col, text=col, command=lambda _col=col:
                 treeview_sort_column(tree, _col, False))

# Frame Estudos
estudosFrame = tkinter.LabelFrame(
    notebookRoot)
estudosFrame.place(relwidth=1, relheight=0.5)
notebookRoot.add(estudosFrame, text="Estudos")

estudosList = ttk.Treeview(estudosFrame)
estudosList.grid(sticky='news')

estude_columns = ('Titulo', 'Duracao', 'DeadLine', 'Inicio', 'Fim')
estudosList.configure(columns=estude_columns)

for heading in estude_columns:
    estudosList.heading(heading, text=heading)

estudosList.configure(show='headings')


# OPCOES DE FRAME
optionsFrame = tkinter.LabelFrame(root, text="Adicione seu evento")
optionsFrame.place(relwidth=1, relheight=0.5, rely=0.5)

inputEventtFrame = tkinter.LabelFrame(optionsFrame, text="Titulo do Evento ")
inputEventtFrame.place(relwidth=1, relheight=0.21, rely=0)

inputEvent = tkinter.Entry(inputEventtFrame)
inputEvent.place(relwidth=0.75, relheight=1)

inputDurationFrame = tkinter.LabelFrame(optionsFrame, text="Duracao do evento")
inputDurationFrame.place(relwidth=1, relheight=0.21, rely=0.22)

inputDuration = tkinter.Entry(inputDurationFrame)
inputDuration.place(relwidth=0.75, relheight=1)

inputDeadLineFrame = tkinter.LabelFrame(
    optionsFrame, text="Dead Line do Evento")
inputDeadLineFrame.place(relwidth=1, relheight=0.2, rely=0.45)

inputDeadLine = tkinter.Entry(inputDeadLineFrame)
inputDeadLine.place(relwidth=0.75, relheight=1)

# BOTOES

btnComent = tkinter.Button(
    inputDeadLineFrame, text="Agendar", command=addComent)
btnComent.place(relwidth=0.25, relheight=1, relx=0.75)

btnClear = tkinter.Button(
    inputDurationFrame, text="Limpar", command=Clear)
btnClear.place(relwidth=0.25, relheight=1, relx=0.75)

btnOrganizar = tkinter.Button(
    optionsFrame, text="Organizar", command=gerarCronograma)
btnOrganizar.place(relwidth=0.4, relheight=0.2, relx=0.55, rely=0.8)

btnDelete = tkinter.Button(optionsFrame, text="Deletar", command=delComent)
btnDelete.place(relwidth=0.4, relheight=0.2, relx=0.05, rely=0.8)

# START APP
root.mainloop()
