import PySimpleGUI as sg
from time import time
import base64

# img_close_str = "iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAD9ElEQVRoge3Yz28bRRTA8e/Muti4B0jSQOyUGxJ3BFJJ0iZREQQRkMqJvyCi4gIcKEmaXy5JaU/Aqf0zQKhFVFDcJiq9ceRMEhfRIhRInATvzOPg2rFj7+x6U8k++F1WXmvGn7cz82bW0I1udKMb7QwV9MXOu++/LajrwKCIgAAcXOXQZwSkfBMOXevuO9pX79e330CY6l27ebOZUwclIKhrbceX+z0pYq8HOQMTAE62+ckj5c5BeKHlBNqOF6lr23ICnYSv9tdSAp2ED/aHj0Bn4GOOQMfgHSOQCORHxPsi7BqfY0qTVCoSft8aStaSUpqEUuH4o66BIPx/Yvl34ATPrMzjv/YKRd8Pxe8aH3/kFD1Xc2xnBtizJhTvWsSBIxDlye8M9DP45RUSfb0cf/VlHuSusJNfI629pviiKcHYaQaXplGeR+qlF/n9g0/wNv8goWgZDxFGIGjO7xqfvg+nSPT1AqA8j8z8BTgzRNH4gfjsYzxA4kQf/R+dZ88aNz7WFApZsMeU5p/vvkeMqTZRnkdm4TMYHa4mEYQHEGPY+vYGCYUbHyeBsGqTVAq1ep8Hi5cbksguTsPZUbZ9v4wfHWnEW0th8Qskv0YS7cS7JpHrLBRaKtOeh7r7C4WFlbok0JrM3Kfo18fK+NxMI37hMvaHn0grLxzvGIHA4/TWG+9V1E3xtdVm1xjsyKkGKFYQBKUPnlMsvAjP/XqnqTXSCIRtUk9rjb57j8L88qGRUE8EH/MoEQ1fm4S6c4/C3DJY26Q7OQI+1kYWHV+9LwJKNf05VenK1rSLiHdtBdGqUAT8rvGR0eHyOtBNutWK7NI03pvj7PimNXy8o0RMfG21EambTkprsrkZvIlxtn2/BXycBI6Kt5bC/Arr00v1+4TWZHOzeG+dpWhMNHy8RRyOL5pSMP7xguX2KhtNkhi8NIueGGfbmFB87DcyF37fGuT0UCPeGDYvfl6tNmmt4fYqm7OXmiRxETU+zL61bny8o0QwHhFK1vLs5EQjfm4Z+TFfVyrTSmNv/czGTK7h2NFzbpKSsbHwzgScpRJIKc3Dr67hP/rLia9Um7T2kFv5uulUeviIP69+TUorNz7OUeLvsXckCF+Zr/tiKWaep//j82x9cwPJr4VuUkVrkbEhes5NlvHrBZ5CufEiDPx2v6nVkcCkuPCVP518K+xZQ0IR7VQpwr61lIwlpRVeBLwAmYAEQt/IGvAc4BFIKDiudf10C9mkkiiSng6fNrXtAiK8Ch3GN5Q8aQkfqdo0tAtWuqtQp+BjjUAH4V3vZNHfB9qJjzOFOgofbxGz0Tl4WW89AWEKkY0OwU85HnQ3utGNbrQx/geUXOzhLxT8xgAAAABJRU5ErkJggg=="
# img_close = base64.b64decode(img_close_str)
# import io
# from PIL import Image
# buffer = io.BytesIO(img_close)
# img = Image.open(buffer)
# new_img = img.resize((20, 20))
# new_img.save(buffer, format = 'png')
# new_img_close_bs = base64.b64encode(buffer.getvalue())
# print(str(new_img_close_bs))

img_close_str = "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAACT0lEQVR4nNWUz2oUQRDGf1UzswbChhyNJyU+ggcfYDGJevAi/kfEqzffIBFRDIroUY+JiIInoxgPIgo+QFAEEeNViLKJu266p8pDz+xuMPGsAwPdNVPfV/V91Q3/+iP14sexE5O5ySkvPTezFDRLL2BmYACDGGa4SVSRxfE3Tz8D5DWglpwebeyadYm4GbjjoqBerQ3UcVcQw90BpaHCt82eAHNbAMU89xjZCAHccEtAuKdkq0Dc+9/cjFFRxKyP01+YuafKKrAYsRCRPAMkgZVG2dtEVUElkUhK7ne6RdGaPUbi5F44f5JQFHiMECOhkaMXzxD378NCqCr3gabDFSY2BXfKGNGDBxi/cJaNPRN0r98CE0YuX6I53WLNnHLlPVo0cAwbqmkLYG2AZhnh4RPWJ3bTnG7hpEqa0y3az18SFh+RZzluhiM7VFi37EmOvNvj17XbYEbz8CEA2s+W6czeoAgRlwpIdgA0szQafTetkliGCBNp6kZwN9wV215DqjlLboZGI2k206K9tAxujB2ZAuDnlXnyTnfAsn3LiQ13yl6P/NxxmjMt1pde0JmbT0kOY0enCF9WCXfuoUVRdbWTKZJmUDQjvn7HWmmEhcdJMzM6V28SVr8SXr1FVdOJ+psp9UlABf34iXLlA3mWJQNUyTpd4t37Q4PtOGwZnGFTBCrWSnQtiv7ePSVJHSvr8yxgA+f6gG7ERiaMivQH3KnmTCTpS3VJUP9jjDi0S4t/AOaiC997PXezdH2ZMXyN1TFssFeMjhHybPMB/83zG5uaprjtfuZqAAAAAElFTkSuQmCC"
img_close = base64.b64decode(img_close_str)

def create_window():
    sg.theme('black')
    layout = [
        [sg.Push(), sg.Image(img_close, pad = 0, enable_events = True, key = '-CLOSE-')],
        [sg.Text('', font = '"Comic Sans MS" 50', key = '-TIME-')],
        [
            sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = '-STARTSTOP-'),
            sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = '-LAP-', visible = False)
        ],
        [sg.Column([[]], expand_x = True, expand_y = True, scrollable = True, vertical_scroll_only = True, key = '-LAPS-')],
    ]
 
    return sg.Window(
        'Stopwatch', 
        layout,
        size = (300,300),
        no_titlebar = True,
        element_justification = 'center')

window = create_window()
active = False
start_time = 0
elapsed_time = 0
lap_amount = 1

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active: # Stop
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible = False)
        else:
            if start_time > 0: # Reset
                window.close()
                window = create_window()
                start_time = 0
                elapsed_time = 0
                lap_amount = 1
            else: # Start
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'],
            [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount += 1
        window['-LAPS-'].contents_changed()
        window['-LAPS-'].Widget.canvas.yview_moveto(1)
        

window.close()