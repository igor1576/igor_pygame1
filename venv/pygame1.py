import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True


circle_radius = 10

circle = []
speed = []
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())

while running:
     # Получаем рандомный цвет для круга
    circle_color = pygame.Color(random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Сохраяем координаты курсора в массив координат (это будет стартовые кооры для круга)
            inner_list = list(event.pos)
            inner_list.append(circle_color)
            circle.append(inner_list)
            speed.append(1)

    # Чистим второй холст
    screen2.fill(pygame.Color('black'))
    # Перерисовываем круги
    for i in range(len(circle)):
        # Проверяем Y кородинату круга
        if circle[i][1] >= size[1] - circle_radius:
            speed[i] = 0

        circle[i][1] += speed[i]

        circle_pos = [circle[i][0], circle[i][1]]
        pygame.draw.circle(screen2, circle[i][2], circle_pos, circle_radius, 0)


    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
