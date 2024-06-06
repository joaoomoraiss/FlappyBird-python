import pygame
import os
import random

#tela do jogo

TELA_LARGURA = 500
TELA_ALTURA = 800

#imagens do jogo

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'bg.png')))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img', 'bird3.png')))]

#font da pontuação
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = IMAGEM_PASSARO
    #ANIMAÇÃO DO PASSARO
    ROTAÇAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        #angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTAÇAO_MAXIMA:
                self.angulo = self.ROTAÇAO_MAXIMA
        else:
            if self.angulo < -90:
                self.angulo -= self.VELOCIDADE_ROTACAO
        
    def desenhar(self, tela):
        #Imagem do passaro
        self.contagem_imagem += 1

        if self.contagem_imagem > self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.image = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.image = self.IMG[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4 + 1:
            self.image = self.IMGS[0]
            self.contagem_imagem = 0

        #passaro caindo não bate a asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        #desenhar imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        posicao_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=posicao_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

class Cano:
    pass


class Chao:
    pass

