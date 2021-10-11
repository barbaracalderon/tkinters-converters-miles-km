# Anotações desse Projeto
Essas são as anotações que eu fiz enquanto criava o código e aprendia sobre Tkinter. No formato de código.

```python
import tkinter

window = tkinter.Tk()
window.title("Meu primeiro programa GUI")
window.minsize(width=500, height=300)       # --- seta tamanho mínimo pra janela --- #

# --- 1) CRIANDO COMPONENTES --- #
# Labels (componente)
my_label = tkinter.Label(text="Oi", font=("Arial", 18, "bold"))
# Labels: atualizar o conteúdo de label (usar ".config")
my_label.config(text="Agora é 'olá'")

# Buttons (componente)
def button_click():
    input_content = input.get()
    my_label.config(text=input_content)


button = tkinter.Button(text="Click Me", command=button_click)      # comando é um "event listener"
new_button = tkinter.Button(text="New Button")

# Entry (componente)
input = tkinter.Entry()


# --- 2) POSICIONANDO COMPONENTES NA JANELA --- #
# --- Como os componentes vão ficar na janela --- #
# --- Três sistemas: Pack(), Place() and Grid() --- #
# PS: tem que usar um dos três para o elemento aparecer na janela. 

# Adicionar um pouco "padding" (espaçamento interno)
# .config(padx=value, pady=value2)

# PACK Sistema
# my_label.pack()         # --> pack sozinho deixa no centro do programa
# pack("left"), pack("bottom"), etc... outras opções
# pack (expand=True)      # --> ele tenta pegar toda altura e largura disponível do tamanho da tela
# button.pack()
# input.pack()

# GRID Sistema (Adotamos esse nos arquivos de Python)
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
input.grid(column=3, row=2)

window.mainloop()          # --> fim do projeto

# Mais sobre...
# PACK(), PLACE(), GRID()
# o que fazem?

# PACK -> Ele empacota cada elemento um colado ao outro com uma lógica um pouco vaga. Por padrão, ele
# começa do topo da janela e vai descendo até o fim da janela, centralizado. Um componente debaixo do
# outro. Dá pra mudar isso usando "pack(side='left')"... se você fizer para todos os componentes, eles
# vão começar da esquerda e vão até o final da janela à direita. O problema: difícil de especificar
# posições.

# PLACE -> É todo sobre posições específicas: dá pra especificar valores no eixo X/Y. Exemplo: 
# ".place(x=0, y=0)", desse jeito ele vai colocar o componente no canto superior esquerdo da janela.
# O problema: muito específico... se a gente tem muitos componentes, precisamos coordená-los manualmente
# sabendo exatamente onde colocá-los. Pesado.

# GRID -> Ele imagina que a janela é uma tabela em que você consegue definir o número de colunas e linhas.
# Por exemplo: ".grid(column=0, row=0). O sistema grid é baseado em posições relativas: isso significa que
# mesmo que você coloque ".grid(column=5, row=5), se não houver outro componente na tela, ele vai mostrar
# o componente no canto superior esquerda da janela. Então, a melhor forma de trabalhar com o grid é colocar
# o seu primeiro componente no canto ".grid(column=0, row=0)" e a partir daí ir adicionando os outros em
# relação a esse.

# Cuidado: se você começar usando o método place, vai até o final. Se você começar com o grid, vai até
# o final. Não dá pra misturar eles ou senão vai acusar um Erro no código.
```