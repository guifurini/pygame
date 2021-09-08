import pygame
pygame.init()
x = 400
y = 300
velocidade = 30

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Primeiro jogo")
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w]:
        y -= velocidade
    if comandos[pygame.K_s]:
        y += velocidade
    if comandos[pygame.K_d]:
        x += velocidade
    if comandos[pygame.K_a]:
        x -= velocidade

    janela.fill((0, 0, 0))
    pygame.draw.circle(janela, (0,255,0), (x, y),50)
    pygame.display.update()
pygame.quit()