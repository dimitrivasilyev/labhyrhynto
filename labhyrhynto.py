import pygame
import random
import json

pygame.init()

# CONFIGURAÇÃO DE TELA E JOGO
largura, altura = 630, 600
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
imagem_jogador = pygame.image.load('soldier.png')
imagem_jogador = pygame.transform.scale(imagem_jogador, (35, 30))
imagem_final = pygame.image.load('final.png')
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo,(80,80))
pygame.display.set_icon(logo)
pygame.display.set_caption('Labhyrhynto')
LARGURA, ALTURA = largura // 30, altura // 30
running = True
menu = True
pontuacao = 0

# CORES
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (47, 130, 38)
TERRA = (130, 70, 38)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Função para desenhar a tela do menu
def desenhar_menu(cursor_pos):
    screen.blit(wallpaper,(0,0))

    fonte = pygame.font.Font('font.ttf', 50)
    titulo = fonte.render("Labirinto", True, BRANCO)
    screen.blit(titulo, (largura // 2 - titulo.get_width() // 2, altura // 3 - 100))

    fonte_opcoes = pygame.font.Font('font.ttf', 40)
    opcao_1 = fonte_opcoes.render("Iniciar Jogo", True, BRANCO)
    opcao_2 = fonte_opcoes.render("Sair", True, BRANCO)

    # opções
    screen.blit(opcao_1, (largura // 2 - opcao_1.get_width() // 2, altura // 2))
    screen.blit(opcao_2, (largura // 2 - opcao_2.get_width() // 2, altura // 2 + 50))

    # o cursor
    if cursor_pos == 0:
        pygame.draw.rect(screen, VERDE, (largura // 2 - opcao_1.get_width() // 2 - 40, altura // 2 + 10, 30, 30))
    elif cursor_pos == 1:
        pygame.draw.rect(screen, VERDE, (181, altura // 2 + 60, 30, 30))

# Classe Jogador
class Jogador:
    def __init__(self, tamanho, posicao):
        self.tamanho = tamanho
        self.posicao = posicao

    def mover_jogador(self, dx, dy, labirinto):
        novo_x = self.posicao[0] + dx
        novo_y = self.posicao[1] + dy
        if labirinto.verificar_movimento(novo_x, novo_y):
            self.posicao[0] = novo_x
            self.posicao[1] = novo_y

    def desenhar_jogador(self):
        screen.blit(imagem_jogador, (jogador.posicao[0] * 30, jogador.posicao[1] * 30))

class Labirinto(Jogador):
    def __init__(self, largura, altura, fase=None):
        self.largura = largura
        self.altura = altura
        if fase:                # se tiver uma fase no arquivo "matrizes.json" pega ele
            self.labirinto=fase
        else:                   # senão cria um novo
            self.labirinto=[]
        self.controle = True    # pro jogador poder se mover
        self.final_pos = (0,0)  # a posição final que fica próxima no canto inferior direito
        if fase:
            self.final_pos = self.definir_ponto_final()
        self.iniciar_labirinto()

    def avancar_fase(self):
        global fase_atual, pontuacao
        fase_atual += 1
        if fase_atual < len(fases):
            jogo()  # começa a próxima fase
        else:
            labirinto.fim_de_jogo()
            fase_atual = 0
            pontuacao = 0

    def iniciar_labirinto(self):
        """Inicializa o labirinto com paredes (1) e caminhos (0)."""
        for y in range(self.altura):
            linha = []
            for x in range(self.largura):
                linha.append(1)
            self.labirinto.append(linha)

        # gera o labirinto a partir de um ponto aleatório
        inicio_x = random.randrange(1, self.largura, 2)
        inicio_y = random.randrange(1, self.altura, 2)
        self.generate_labirinto(inicio_x, inicio_y)
        self.final_pos = self.definir_ponto_final()

    def pegar_vizinhos(self, x, y):
        """Retorna os vizinhos válidos da célula (x, y)."""
        vizinhos = []
        direcao = [(2, 0), (-2, 0), (0, 2), (0, -2)]  # direita, esquerda, baixo, cima
        for dx, dy in direcao:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.largura and 0 <= ny < self.altura and self.labirinto[ny][nx] == 1:
                vizinhos.append((nx, ny))
        return vizinhos

    def generate_labirinto(self, x, y):
        """Gera o labirinto a partir da célula (x, y)."""
        self.labirinto[y][x] = 0  # marca a célula como caminho (0)
        vizinhos = self.pegar_vizinhos(x, y)
        random.shuffle(vizinhos)  # embaralha os vizinhos para criar um caminho mais aleatório

        for nx, ny in vizinhos:
            if self.labirinto[ny][nx] == 1:
                # remove a parede entre a célula atual e o vizinho
                self.labirinto[(y + ny) // 2][(x + nx) // 2] = 0
                self.generate_labirinto(nx, ny)

    def desenhar(self, screen, tamanho_celula):
        """Desenha o labirinto na tela."""
        for y in range(len(self.labirinto)):
            for x in range(len(self.labirinto[y])):
                if self.labirinto[y][x] == 1:
                    pygame.draw.rect(screen, VERDE, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))
                else:
                    pygame.draw.rect(screen, TERRA, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))

        # o ponto final, de chegada
        #pygame.draw.rect(screen, VERMELHO, (self.final_pos[0] * tamanho_celula, self.final_pos[1] * tamanho_celula, tamanho_celula, tamanho_celula))
        screen.blit(imagem_final, (self.final_pos[0] * tamanho_celula, self.final_pos[1] * tamanho_celula))

    def verificar_movimento(self, x, y):
        """Verifica se a célula na posição (x, y) é um caminho (0) ou parede (1)."""
        if 0 <= x < self.largura and 0 <= y < self.altura:
            return self.labirinto[y][x] == 0
        return False

    def fim_de_jogo(self):
        global menu
        fonte = pygame.font.Font('font.ttf', 50)
        texto = fonte.render("FIM DE JOGO!", True, VERMELHO)
        screen.blit(texto, (largura // 2 - 150, altura // 2 - 50))
        fonte_pontuacao = pygame.font.Font('font.ttf', 40)
        texto_pontuacao = fonte_pontuacao.render(f"PONTUACAO FINAL: {pontuacao}", True, VERMELHO)
        screen.blit(texto_pontuacao, (largura // 2 - texto_pontuacao.get_width() // 2, altura // 2 + 10))
        pygame.display.flip()
        pygame.time.wait(2700)
        menu = True # volta pra tela inicial do jogo

    def desenhar_timer(self, tempo_restante):
        minutos = tempo_restante // 60
        segundos = tempo_restante % 60
        tempo_formatado = f"{minutos:02}:{segundos:02}"
        
        fonte = pygame.font.Font('font.ttf', 40)
        texto = fonte.render(f"TEMPO : {tempo_formatado}", True, BRANCO)
        screen.blit(texto, (0, 0)) # canto superior esquerdo

    def desenhar_pontuacao(self):
        """Desenha a pontuação na tela."""
        fonte = pygame.font.Font('font.ttf', 40)
        texto = fonte.render(f"PONTUACAO: {pontuacao}", True, BRANCO)
        screen.blit(texto, (largura - texto.get_width() - 10, 0))  # canto superior direito

    def desenhar_fase_atual(self):
        """Desenha o texto da fase atual no meio da tela (horizontalmente)."""
        fonte = pygame.font.Font('font.ttf', 40)
        fase_texto = fonte.render(f"FASE: {fase_atual + 1}", True, BRANCO)
        texto_largura = fase_texto.get_width()
        x_pos = (largura - texto_largura) // 2  # centralizado, na mesma linha com pontuacao e tempo
        screen.blit(fase_texto, (x_pos, 0))

    def definir_ponto_final(self):
            """Define uma posição final válida no labirinto."""
            # começa a partir do canto inferior direito
            for y in range(self.altura - 1, -1, -1): # procurando um caminho
                for x in range(self.largura - 1, -1, -1):
                    if self.labirinto[y][x] == 0:  # encontrar uma célula de caminho
                        return (x, y)
            return (self.largura - 2, self.altura - 2)  # retonar o padrão se não encontrar outro caminho

def carregar_fases(arquivo): # puxando as matrizes (fases)
    with open(arquivo, 'r') as file:
        data = json.load(file)
    return data["fases"]

def jogo():
    global jogador, labirinto, tempo_inicio, fase_atual
    tempo_inicio = pygame.time.get_ticks()  # 
    labirinto = Labirinto(LARGURA, ALTURA, fases[fase_atual])  # carrega a fase atual
    jogador = Jogador(30, [1, 1])

# timer
tempo_restante = 30
tempo_total = tempo_restante
tempo_inicio = pygame.time.get_ticks()

# menu
cursor_pos = 0
wallpaper=pygame.image.load("wallpaper.png")

# fases
fases=carregar_fases("matrizes.json")
fase_atual = 0  # começando da primeira fase

# loop principal
while running:
    screen.fill(PRETO)  # limpando os frames da tela, antes de iniciar
    keys = pygame.key.get_pressed()

    if menu:
        print('no menu')
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    cursor_pos = (cursor_pos + 1) % 2
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    cursor_pos = (cursor_pos - 1) % 2
                if event.key == pygame.K_RETURN:
                    if cursor_pos == 0:  # iniciar jogo
                        menu = False
                        jogo()
                    elif cursor_pos == 1:  # sair
                        running = False
        desenhar_menu(cursor_pos)

    else:
        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000
        tempo_restante = tempo_total - tempo_decorrido

        if tempo_restante <= 0 or labirinto.controle == False: # se o tempo acabar, fim de jogo e exibe a pontuacao
            labirinto.fim_de_jogo()
        elif labirinto.controle: # movimentação do jogador
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    running = False
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                jogador.mover_jogador(-1, 0, labirinto)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                jogador.mover_jogador(1, 0, labirinto)
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                jogador.mover_jogador(0, -1, labirinto)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                jogador.mover_jogador(0, 1, labirinto)
            elif keys[pygame.K_f]:
                labirinto.avancar_fase()
            # elif keys[pygame.K_g]:  outro pra incrementar 5s de tempo
            #     tempo_total+=5

            # jogador chegou ao ponto final?
            if jogador.posicao == list(labirinto.final_pos):
                pontuacao += 100
                labirinto.avancar_fase()  # próxima fase

            labirinto.desenhar(screen, 30) # com a matriz do labirinto, desenha ele na tela
            labirinto.desenhar_pontuacao() # 
            labirinto.desenhar_timer(tempo_restante)
            labirinto.desenhar_jogador()
            labirinto.desenhar_fase_atual()

    pygame.display.flip()
    clock.tick(10)

pygame.quit()

