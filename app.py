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


def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    imc_formatado = f'{imc:.2f}'
    imc_formatado = float(imc_formatado)
    return imc_formatado


def categoria():
    if calculo_imc(peso, altura) < 16:
        categoria = 'Muito Abaixo do Peso'
    elif calculo_imc(peso, altura) >= 17 and calculo_imc(peso, altura) < 18.5:
        categoria = 'Abaixo do Peso'
    elif calculo_imc(peso, altura) >= 18.5 and calculo_imc(peso, altura) <= 24.9:
        categoria = 'Peso Normal'
    elif calculo_imc(peso, altura) >= 25 and calculo_imc(peso, altura) <= 29.9:
        categoria = 'Acima do Peso'
    elif calculo_imc(peso, altura) >= 30 and calculo_imc(peso, altura) <= 34.9:
        categoria = 'Obesidade I'
    elif calculo_imc(peso, altura) >= 35 and calculo_imc(peso, altura) <= 39.9:
        categoria = 'Obesidade II (Severa)'
    elif calculo_imc(peso, altura) >= 40:
        categoria = 'Obesidade III (Mórbida)'
    return categoria


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Calcular IMC':
        peso = int(values['peso'])
        altura = float(values['altura'])

        window['imc'].update(calculo_imc(peso, altura))

        if 'Muito Abaixo do Peso' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='grey')

        elif 'Abaixo do Peso' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='grey')

        elif 'Peso Normal' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='black')

        elif 'Acima do Peso' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='red')

        elif 'Obesidade I' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='red')

        elif 'Obesidade II (Severa)' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='red')

        elif 'Obesidade III (Mórbida)' in categoria():
            window['categoria'].update(categoria())
            window['categoria'].update(text_color='red')
