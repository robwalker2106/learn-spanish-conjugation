from turtle import Turtle, Screen
import pandas as pd
from verb_list import Verbs
from sheet import SheetWriter

screen = Screen()
image = 'sheet.gif'
screen.addshape(image)
screen.title("Spanish Verb Conjugation")
screen.screensize(canvwidth=800, canvheight=800)
screen.setup(width=900, height=900)
screen.tracer(0)
sheet = Turtle(image)
sheet_writer = SheetWriter()
screen.update()
verbs = Verbs(pd.read_csv('verbs.csv', encoding='mac_roman'))
screen.listen()

# def print_cood(x, y):
#     print(x, y)
#
# screen.onscreenclick(print_cood)

show_screen = True

while show_screen:
    conjugate_verb = screen.textinput("New Verb", "Do you want to conjugate a verb? (si,no)")
    screen.clearscreen()
    sheet = Turtle(image)
    sheet_writer = SheetWriter()

    if conjugate_verb.lower() == "no":
        break
    elif conjugate_verb.lower() == "si":
        verb, index = verbs.verb_challenge()

    print(verb)
    print(verbs.data)

    all_correct = True
    # Conjugate verb for yo.
    yo = screen.textinput("Yo", "Conjugate the verb for yo.")
    yo_correct = verb.iloc[0].yo
    if yo.lower() == yo_correct.lower():
        sheet_writer.print_answer('yo', yo_correct, 'correct')
    else:
        sheet_writer.print_answer('yo', yo_correct, 'incorrect')
        all_correct = False

    # Conjugate verb for tú.
    tu = screen.textinput("Yo", "Conjugate the verb for tú.")
    tu_correct = verb.iloc[0].tú
    if tu.lower() == tu_correct.lower():
        sheet_writer.print_answer('tú', tu_correct, 'correct')
    else:
        sheet_writer.print_answer('tú', tu_correct, 'incorrect')
        all_correct = False

    # Conjugate verb for él/ella/usted.
    el = screen.textinput("él/ella/usted", "Conjugate the verb for él/ella/usted.")
    el_correct = verb.iloc[0].él
    if el.lower() == el_correct.lower():
        sheet_writer.print_answer('él/ella/usted', el_correct, 'correct')
    else:
        sheet_writer.print_answer('él/ella/usted', el_correct, 'incorrect')
        all_correct = False

    # Conjugate verb for nosotros.
    nosotros = screen.textinput("Nosotros", "Conjugate the verb for nosotros.")
    nosotros_correct = verb.iloc[0].nosotros
    if nosotros.lower() == nosotros_correct.lower():
        sheet_writer.print_answer('nosotros', nosotros_correct, 'correct')
    else:
        sheet_writer.print_answer('nosotros', nosotros_correct, 'incorrect')
        all_correct = False

    # Conjugate verb for vosotros.
    vosotros = screen.textinput("Yo", "Conjugate the verb for vosotros.")
    vosotros_correct = verb.iloc[0].vosotros
    if vosotros.lower() == vosotros_correct.lower():
        sheet_writer.print_answer('vosotros', vosotros_correct, 'correct')
    else:
        sheet_writer.print_answer('vosotros', vosotros_correct, 'incorrect')
        all_correct = False

    # Conjugate verb for ellos/ellas/ustedes.
    ellos = screen.textinput("Yo", "Conjugate the verb for ellos/ellas/ustedes.")
    ellos_correct = verb.iloc[0].ellos
    if ellos.lower() == ellos_correct.lower():
        sheet_writer.print_answer('ellos/ellas/ustedes', ellos_correct, 'correct')
    else:
        sheet_writer.print_answer('ellos/ellas/ustedes', ellos_correct, 'incorrect')
        all_correct = False

    verbs.updated_verb_info(index, all_correct)


screen.mainloop()