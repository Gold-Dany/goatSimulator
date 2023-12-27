import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goat Simulator")

player_x, player_y = WIDTH // 2, HEIGHT // 2
player_width, player_height = 100, 100
player_speed = 3

background = pygame.image.load('data/bg.jpg')
background = pygame.transform.scale(background, (800, 600))

goat = pygame.image.load('data/goat.png')
goat = pygame.transform.scale(goat, (player_width, player_height))
goat1 = pygame.image.load('data/goat.png')
goat1 = pygame.transform.scale(goat1, (player_width + 2, player_height + 2))

mill = pygame.image.load('data/mill.png')
mill = pygame.transform.scale(mill, (200, 300))

barn = pygame.image.load('data/barn.png')
barn = pygame.transform.scale(barn, (300, 300))

play_btn = pygame.image.load('data/play_btn.png')
play_btn = pygame.image.load('data/play_btn.png')
play_btn = pygame.transform.scale(play_btn, (100, 100))
play_btn_rect = play_btn.get_rect()
# коордианты кнопки
play_btn_rect.topleft = (WIDTH // 2, HEIGHT // 2)

walk_right = [goat, goat, goat1, goat1]
walk_left = [pygame.transform.flip(img, True, False) for img in walk_right]
win_blit = False

right = False
left = False
allow_walk = False
walk_count = 0


def intro_maker():
    image = pygame.image.load('data/goat_bg.jpg')
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    win.blit(image, (0, 0))
    win.blit(play_btn, play_btn_rect)


intro_maker()

def draw_mill():
    if win_blit:
        win.blit(mill, (0, 300))


def draw_barn():
    if win_blit:
        win.blit(barn, (500, 0))

# Функция отрисовки персонажа
def draw_player(x, y):
    global walk_count, allow_walk, win_blit
    if win_blit:

        if walk_count + 1 >= 12:
            walk_count = 0
        if allow_walk:
            if left:
                win.blit(walk_left[walk_count // 3], (x, y))
                walk_count += 1
            elif right:
                win.blit(walk_right[walk_count // 3], (x, y))
                walk_count += 1
            else:
                win.blit(walk_right[walk_count // 3], (x, y))
                walk_count += 1
        else:
            if left:
                win.blit(walk_left[0], (x, y))
            elif right:
                win.blit(walk_right[0], (x, y))
            else:
                win.blit(walk_right[0], (x, y))

def check_collision(obj1, obj2):
    if obj1.colliderect(obj2):
        return True
    return False

running = True
clock = pygame.time.Clock()
while running:
    if win_blit:
        win.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn_rect.collidepoint(event.pos) and win_blit is False:
                win.blit(background, (0, 0))
                player_x, player_y = WIDTH // 2, HEIGHT // 2
                win_blit = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                player_speed = 3
            allow_walk = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
        left = True
        right = False
        allow_walk = True
    if keys[pygame.K_d]:
        player_x += player_speed
        right = True
        left = False
        allow_walk = True
    if keys[pygame.K_w]:
        player_y -= player_speed
        allow_walk = True
    if keys[pygame.K_s]:
        player_y += player_speed
        allow_walk = True
    if keys[pygame.K_LSHIFT]:
        player_speed = 6

    # Проверка на выход за границы карты
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - player_height:
        player_y = HEIGHT - player_height
    
    # проверка на пересечение с др предметами(я тут гетрект поставила тк по другому не получалось чета)
    mill_rect = mill.get_rect(topleft=(0, 300))
    barn_rect = barn.get_rect(topleft=(500, 0))
    goat_rect = goat.get_rect(topleft=(player_x, player_y))

    if check_collision(goat_rect, mill_rect):
        if player_y > 300:
            player_x += player_speed
        elif 250 < player_y < 300:
            player_y -= player_speed

    # Отрисовка игровых объектов
    draw_player(player_x, player_y)
    draw_mill()
    draw_barn()
    # Обновление экрана
    pygame.display.update()
    # Ограничение скорости игры
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()
