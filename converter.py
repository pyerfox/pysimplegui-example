from typing import Any, Union, Literal
import PySimpleGUI as sg

layout: list[list[sg.Element]] = [
    [
        sg.Input(key='-INPUT-'),
        sg.Combo(['km to mile', 'kg to pound', 'sec to min'], default_value='km to mile', key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [
        sg.Text('Output', key='-OUTPUT-')
    ]
]

window = sg.Window('Converter', layout)

def convert(lval: str, conv: str) -> str:
    rval: float
    if conv == 'km to mile':
        rval = round(float(lval) * 0.6214, 2)
        return f'{lval} km are {rval} miles.'
    if conv == 'kg to pound':
        rval = round(float(lval) * 2.20462, 2)
        return f'{lval} kg are {rval} pounds.'
    if conv == 'sec to min':
        rval = round(float(lval) / 60, 2)
        return f'{lval} seconds are {rval} minutes.'
    return f'unknown conversion: {conv}'

while True:
    event, values = window.read()
    # print(values)

    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        input_value: str = values['-INPUT-']
        output_elem: sg.Text = window['-OUTPUT-']
        output_value: str
        if input_value.isnumeric():
            output_value = convert(input_value, values['-UNITS-'])
        else:
            output_value = 'please enter a number'
        output_elem.update(output_value)

window.close()
