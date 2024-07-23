'''
1. Interface Gráfica:
○ Criar uma janela principal.
○ Adicionar campos de entrada para o peso (em kg) e altura (em metros(exemplo:
1.70, 1.80)
○ Adicionar um botão para calcular o IMC.
○ Adicionar um campo para exibir o resultado do IMC.
○ Adicionar um campo para exibir a categoria do IMC
i. Muito abaixo do peso
ii. Abaixo do peso
iii. Peso normal
iv. Acima do peso
v. Obesidade I
vi. Obesidade II
vii. Obesidade III
○ Personalize as cores da categoria para que tudo fique mais intuitivo(coloque
cores diferentes para cada nível
i. (ex:vá de branco para vermelho, de acordo com o nível de obesidade)
'''
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Digite seu Peso: Ex:70, 80', size=(35, 1)), sg.Input(key='peso')],
    [sg.Text('Digite susa Altura: Ex:1.70, 1.80',
             size=(35, 1)), sg.Input(key='altura')],
    [sg.Button(button_text='Calcular IMC')],
    [sg.Text('Seu IMC é:', size=(9, 1)), sg.Text(key='imc')],
    [sg.Text('Categoria:', size=(9, 1)), sg.Text(key='categoria')]
]

window = sg.Window('Calculadora de IMC', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calcular IMC':
        peso = int(values['peso'])
        altura = float(values['altura'])
        imc = peso / (altura * altura)
        imc_formatado = f'{imc:.2f}'
        imc_formatado = float(imc_formatado)
        window['imc'].update(imc_formatado)
        if imc_formatado < 16:
            window['categoria'].update('Muito Abaixo do Peso')
            window['categoria'].update(text_color='grey')
        elif imc_formatado >= 17 and imc_formatado < 18.5:
            window['categoria'].update('Abaixo do Peso')
            window['categoria'].update(text_color='grey')
        elif imc_formatado >= 18.5 and imc_formatado <= 24.9:
            window['categoria'].update('Peso Normal')
            window['categoria'].update(text_color='black')
        elif imc_formatado >= 25 and imc_formatado <= 29.9:
            window['categoria'].update('Acima do Peso')
            window['categoria'].update(text_color='red')
        elif imc_formatado >= 30 and imc_formatado <= 34.9:
            window['categoria'].update('Obesidade I')
            window['categoria'].update(text_color='red')
        elif imc_formatado >= 35 and imc_formatado <= 39.9:
            window['categoria'].update('Obesidade II (Severa)')
            window['categoria'].update(text_color='red')
        elif imc_formatado >= 40:
            window['categoria'].update('Obesidade III (Mórbida)')
            window['categoria'].update(text_color='red')
