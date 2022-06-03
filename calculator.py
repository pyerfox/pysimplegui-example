from typing import Tuple, final
import random
import PySimpleGUI as sg

def create_window(theme: str) -> sg.Window:
    sg.theme(theme)
    button_size = (4, 2)
    sg.set_options(font = '"Cascadia Mono SemiBold"', button_element_size = button_size)
    layout = [
        [sg.Text('',
            justification = 'right',
            expand_x = True,
            pad = (10, 20),
            right_click_menu = theme_menu,
            key = '-TEXT-',
        )],
        [sg.Button(k, expand_x = True) for k in ('Clear', 'Enter')],
        [sg.Button(k, size = button_size) for k in (7, 8, 9, '*')],
        [sg.Button(k, size = button_size) for k in (4, 5, 6, '/')],
        [sg.Button(k, size = button_size) for k in (3, 2, 1, '-')],
        [sg.Button(0, expand_x = True)] + [sg.Button(k, size = button_size) for k in ('.', '+')],
    ]
    return sg.Window('계산기', layout, finalize = True)

theme_menu: Tuple[str, list[str]]
theme_menu = ('menu', random.choices(list(sg.LOOK_AND_FEEL_TABLE.keys()), k = 5))
window = create_window(theme_menu[1][0])

current_num: list[str] = []
full_operation: list[str] = []
display: sg.Text = window['-TEXT-']

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        tmp = display.get()
        window.close()
        theme_menu = ('menu', random.choices(list(sg.LOOK_AND_FEEL_TABLE.keys()), k = 5))
        window = create_window(event)
        display = window['-TEXT-']
        display.update(tmp)
    
    if event in list('.0123456789'):
        current_num.append(event)
        num_string = ''.join(current_num)
        display.update(num_string)
    
    if event in list('+-/*'):
        full_operation.append(''.join(current_num))
        current_num.clear()
        full_operation.append(event)
        display.update('')
    
    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval(' '.join(full_operation))
        display.update(result)
        full_operation.clear()
    
    if event == 'Clear':
        current_num.clear()
        full_operation.clear()
        display.update('')

window.close()
