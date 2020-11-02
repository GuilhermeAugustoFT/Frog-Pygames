import pygame as pg
import os
import requests
import json

print("\nBem-vindo ao Frogger Game")

def login():
    res = input ("\nJá possui conta? (S / N) ")
    if res == "S":
        print("\n----- Login -----")
        nome = input("\nDigite seu nome: ")
        senha = input("Digite sua senha: ")
        json_player = json.dumps({"nome": nome, "senha": senha})
        response = requests.post("http://localhost:5000/api/autenticatePlayer", json=json_player)
        json_string = json.dumps(response.json())
        response_dict = json.loads(json_string)
        if response_dict['message'] == 200:
            return
        else:
            print("\nNome ou senha incorretos!")
            login()
    elif res == "N":
        print("\n----- Registro de Jogador -----")
        nome = input("\nDigite um nome: ")
        nickname = input("Digite um nickname: ")
        senha = input("Digite uma senha: ")
        json_player = json.dumps({"nome": nome, "senha": senha, "nickname": nickname, "pontuacao": 100})
        response = requests.post("http://localhost:5000/api/insertPlayer", json=json_player)
        '''json_string = json.dumps(response.json())
        response_dict = json.loads(json_string)'''

        '''if response_dict['message'] == 500:
            print("\nNome de usuário já existente! Tente outro")
            login()'''

        login()
    else:
        print("\nDigite S ou N")
        login()


def main():
    ## Prepara tela
    screen = pg.display.set_mode((400, 300))
    white = (255, 255, 255)
    font = pg.font.Font(None, 32)
    pg.display.set_caption('Digite seu nome')
    input_box = pg.Rect(100, 130, 140, 32) ## Formato do input
    color_inactive = pg.Color('lightskyblue3') ## Cor padrao do input
    color_active = pg.Color('dodgerblue2') ## Cor utilizado quando usuario clicar no input
    fontTitle = pg.font.Font('machine_gunk.ttf', 40)
    title = fontTitle.render('Insira seu nome', True, white)
    titleRect = title.get_rect()
    titleRect.center = (200, 100)
    fontSubtitle = pg.font.Font('machine_gunk.ttf', 30)
    subtitle = fontSubtitle.render('Pressione [Enter] para jogar', True, white)
    subtitleRect = subtitle.get_rect()
    subtitleRect.center = (200, 200)
    color = color_inactive
    active = False
    text = '' ## Texto que o usuario digitou
    done = False

    while not done:
        screen.blit(title, titleRect)
        screen.blit(subtitle, subtitleRect)
        for event in pg.event.get():
            ## Se e um evento de fechamento de janela
            if event.type == pg.QUIT:
                done = True
            ## Usuario clicou
            if event.type == pg.MOUSEBUTTONDOWN:
                ## Usuario clicou no input especificamente
                if input_box.collidepoint(event.pos):
                    active = not active ## Boolean e setado para depois mudar cor do input
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive ## Se active e true, muda cor do input
            if event.type == pg.KEYDOWN:
                if active:
                    ## Usuario apertou enter
                    if event.key == pg.K_RETURN:
                        print(text)
                        '''requests.post("http:localhost:5000/api/insertPlayer", json={"nome": "afdsfs", "pontuacao": 1000})'''
                        pg.quit()
                        os.system('python main.py')


                    ## Usuario apagou uma letra
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        ## Usuario digitou uma letra
                        text += event.unicode

        ## txt_surface eh um componente texto com conteudo de text
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        ## Desenha o texto
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        ## Desenha o input
        pg.draw.rect(screen, color, input_box, 2)

        ## Atualizar tela
        pg.display.flip()

## Para rodar programa
if __name__ == '__main__':
    login()
    pg.init()
    main()
    pg.quit()


