import PySimpleGUI as sg
from pathlib import Path
from typing import Tuple
from functools import reduce

smileys: list[Tuple[str, list[str]]] = [
    ('happy', [':)','xD',':D','<3']),
    ('sad', [':(','T_T']),
    ('other', [':3']),
]

smiley_events: list[str] = reduce(lambda acc, cur: acc + cur[1], smileys, [])

menu_layout = [
    ('File', ['Open', 'Save', '---', 'Exit']),
    ('Tools', ['Word Count']),
    ('Add', smileys),
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline(no_scrollbar = True, expand_x = True, expand_y = True, key = '-TEXTBOX-')],
]

window = sg.Window('Text Editor', layout, size = (300, 400), resizable = True)

while True:
    evt, vals = window.read()
    if evt in [sg.WIN_CLOSED, 'Exit']:
        break
    
    if evt == 'Open':
        filepath = sg.popup_get_file('open', no_window = True)
        if filepath:
            f = Path(filepath)
            fail = False
            txt = ''
            try:
                txt = f.read_text()
            except:
                try:
                    txt = f.read_text(encoding = 'utf-8')
                except Exception as e:
                    sg.popup_error_with_traceback('Failed to read file:', e)
                    fail = True
            if not fail:
                window['-TEXTBOX-'].update(txt)
                window['-DOCNAME-'].update(filepath.split('/')[-1])
        
    if evt == 'Save':
        filepath = sg.popup_get_file('Save as', no_window = True, save_as = True, file_types = (("Text Files", "*.txt"), ("All Files", "*.* *")))
        if filepath:
            f = Path(filepath)
            f.write_text(vals['-TEXTBOX-'])
            window['-DOCNAME-'].update(filepath.split('/')[-1])
        
    if evt == 'Word Count':
        full_text = vals['-TEXTBOX-']
        clean_text: list[str] = full_text.replace('\n', ' ').split(' ')
        clean_text = list(filter(None, clean_text))
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'words {word_count}\ncharacters: {char_count}')
    
    if evt in smiley_events:
        # cur_text: str = vals['-TEXTBOX-']
        # new_text = cur_text + ' ' + evt
        pos = window['-TEXTBOX-'].Widget.index('insert')
        window['-TEXTBOX-'].Widget.insert(pos, f'{evt}')

window.close()