import PySimpleGUI as sg
import main

def iniciar():
    sg.change_look_and_feel('Default')
    FILENAME = r'./assets/robot.gif'
    DISPLAY_TIME_MILISSECONDS = 5000 # 5 segundos

    # Criando splash screen
    sg.Window('',
                [[sg.Image(FILENAME)]],
                transparent_color=sg.theme_background_color(),
                no_titlebar=True,
                keep_on_top=True
            ).read(timeout=DISPLAY_TIME_MILISSECONDS, close=True)
    
    layout = [
        [sg.Text('Seja bem-vindo(a)! É um prazer imenso recebê-lo(a) aqui!')],
        [sg.HorizontalSeparator()],
        [sg.Text('Executar RPA Exercise                                   '),
            sg.Button('Ok', key="ini_rpa")],
        [sg.HorizontalSeparator()],
        [sg.Button('Sair', key="sair")]
    ]

    tela = sg.Window(" Meu primeiro RPA ").layout(layout)

    while True:
        event, values = tela.Read()
        if event in ('sair', sg.WIN_CLOSED):
            break
        elif event == 'ini_rpa':
            if(main.ini()):
                alerta(tela)
                
        
def alerta(tela):
    sg.change_look_and_feel('Green')
    alert = [
        [sg.HorizontalSeparator()],
        [sg.Text('Uhuuuuuuul, parabéns você chegou ao fim :)')],
        [sg.HorizontalSeparator()],
    ]

    telinha = sg.Window('Estás de parabuens!').layout(alert)

    while True:
        event, values = telinha.Read()
        if event in (None , sg.WIN_CLOSED) or (event == 'Ok'):
            break
    return tela.close()


iniciar()
