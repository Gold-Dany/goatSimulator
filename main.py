import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1200, 900

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goat Simulator")

# Характеристики персонажа
player_width, player_height = 100, 100
player_speed = 3
player_health = 100
# Шаблон козла
goat = pygame.image.load('data/goat.png')
goat = pygame.transform.scale(goat, (player_width, player_height))
goat1 = pygame.image.load('data/goat1.png')
goat1 = pygame.transform.scale(goat1, (player_width, player_height))
goat2 = pygame.image.load('data/goat2.png')
goat2 = pygame.transform.scale(goat2, (player_width, player_height))
goat_rect = goat.get_rect()
goat_rect.center = (WIDTH // 2, HEIGHT // 2)
# Атака
goat_attack = pygame.image.load('data/cursor.png')
goat_attack = pygame.transform.scale(goat_attack, (player_width, player_height))
goat_attack_rect = goat_attack.get_rect()
goat_attack_rect.center = (-100, -100)
goat_attack_speed = 10

background = pygame.image.load('data/bg.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

play_btn = pygame.image.load('data/play_btn.png')
play_btn = pygame.transform.scale(play_btn, (100, 100))
play_btn_rect = play_btn.get_rect()
play_btn_rect.center = (WIDTH // 2, HEIGHT // 2)

# Босс №1
boss1 = pygame.image.load('data/boss1.png')
boss1 = pygame.transform.scale(boss1, (100, 100))
boss1_rect = boss1.get_rect()
boss1_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
boss1_speed = 1
boss1_health = 100

# Объекты
mill = pygame.image.load('data/mill.png')
mill = pygame.transform.scale(mill, (200, 300))

barn = pygame.image.load('data/barn.png')
barn = pygame.transform.scale(barn, (300, 300))

mill_rect = mill.get_rect(topleft=(WIDTH // 2, HEIGHT // 10))
barn_rect = barn.get_rect(topleft=(WIDTH // 10, HEIGHT // 10))

walk_right = [goat, goat1, goat2, goat2]
walk_left = [pygame.transform.flip(img, True, False) for img in walk_right]
win_blit = 'start_bg'

right = False
left = False
allow_animation = False
walk_count = 0
left_attack, right_attack = False, False
allow_walk = True

move_boss_event = None
move_boss_event_check = 'small'


def draw_mill():
    win.blit(mill, (mill_rect.x, mill_rect.y))


def draw_barn():
    win.blit(barn, (barn_rect.x, barn_rect.y))


def intro_maker():
    global win_blit, background, player_health, goat_attack, left_attack, right_attack, goat_attack_rect
    goat_attack_rect.center = (-100, -100)
    goat_attack = None
    left_attack, right_attack = False, False
    player_health = 100
    background = pygame.image.load('data/bg.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    win_blit = 'start_bg'
    image = pygame.image.load('data/goat_bg.jpg')
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    win.blit(image, (0, 0))
    win.blit(play_btn, play_btn_rect)


intro_maker()


def boss_fight1():
    global win_blit, background, move_boss_event, move_boss_event_check, boss1, boss1_health, boss1_rect
    boss1_health = 100
    move_boss_event = pygame.USEREVENT + 1
    pygame.time.set_timer(move_boss_event, 5000)
    boss1 = pygame.image.load('data/boss1.png')
    boss1 = pygame.transform.scale(boss1, (100, 100))
    boss1_rect = boss1.get_rect()
    boss1_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    move_boss_event_check = 'small'
    win_blit = 'boss_fight1'
    background = pygame.image.load('data/bg_boss_fight1.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    win.blit(background, (0, 0))


# Функция отрисовки персонажа
def draw_player(x, y):
    global walk_count, allow_animation, win_blit

    # Хп игрока
    font = pygame.font.Font(None, 50)
    text = font.render(f"Your XP: {player_health}", True, (255, 255, 0))
    text_rect = text.get_rect(center=(WIDTH // 8, HEIGHT // 16))
    win.blit(text, text_rect)

    if win_blit != 'start_bg':

        if walk_count + 1 >= 12:
            walk_count = 0
        if allow_animation:
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


running = True
clock = pygame.time.Clock()
while running:
    # Проверка локации
    if win_blit == 'main1_bg':
        win.blit(background, (0, 0))
    elif win_blit == 'boss_fight1':
        win.blit(background, (0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(f"Boss XP: {boss1_health}", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 8, HEIGHT // 8))
        win.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn_rect.collidepoint(event.pos) and win_blit == 'start_bg':
                win.blit(background, (0, 0))
                player_x, player_y = WIDTH // 2, HEIGHT // 2
                win_blit = 'main1_bg'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                player_speed = 3
            allow_animation = False

        if event.type == move_boss_event:
            if move_boss_event_check == 'big':
                x, y, = boss1_rect.x, boss1_rect.y
                boss1 = pygame.transform.scale(boss1, (100, 100))
                boss1_rect = boss1.get_rect()
                boss1_rect.move_ip(x, y)
                move_boss_event_check = 'small'
            else:
                x, y, = boss1_rect.x, boss1_rect.y
                boss1 = pygame.transform.scale(boss1, (200, 200))
                boss1_rect = boss1.get_rect()
                boss1_rect.move_ip(x, y)
                move_boss_event_check = 'big'
                boss1_speed = 2

    keys = pygame.key.get_pressed()
    # Движение персонажа
    if win_blit != 'start_bg':
        if keys[pygame.K_a]:
            goat_rect.move_ip(-player_speed, 0)
            left = True
            right = False
            allow_animation = True
        if keys[pygame.K_d]:
            goat_rect.move_ip(player_speed, 0)
            right = True
            left = False
            allow_animation = True
        if keys[pygame.K_w]:
            goat_rect.move_ip(0, -player_speed)
            allow_animation = True
        if keys[pygame.K_s]:
            goat_rect.move_ip(0, player_speed)
            allow_animation = True
        if keys[pygame.K_LSHIFT]:
            player_speed = 6
        if keys[pygame.K_f] and win_blit == 'main1_bg':
            boss_fight1()
        if keys[pygame.K_c] and win_blit != 'start_bg':
            if left_attack is False and right_attack is False:
                goat_attack = pygame.image.load('data/cursor.png')
                goat_attack = pygame.transform.scale(goat_attack, (player_width, player_height))
                goat_attack_rect = goat_attack.get_rect()
                goat_attack_rect.center = (goat_rect.x, goat_rect.y)
                left_attack = False
                right_attack = False
    # Анимация атаки
    if goat_attack:
        if left_attack is True:
            goat_attack_rect.move_ip(-goat_attack_speed, 0)
        elif right_attack is True:
            goat_attack_rect.move_ip(goat_attack_speed, 0)
        elif left is True:
            left_attack = True
            goat_attack_rect.move_ip(-goat_attack_speed, 0)
        elif right is True:
            right_attack = True
            goat_attack_rect.move_ip(goat_attack_speed, 0)
        else:
            right_attack = True
            goat_attack_rect.move_ip(goat_attack_speed, 0)

        win.blit(goat_attack, (goat_attack_rect.x, goat_attack_rect.y))
        if goat_attack_rect.x > WIDTH or goat_attack_rect.x < -100:
            left_attack = False
            right_attack = False
            goat_attack = None

    # Проверка на выход за границы карты
    goat_rect.clamp_ip(win.get_rect())

    if win_blit == 'main1_bg':
        # Проверка на столкновение с препятствием
        if goat_rect.colliderect(mill_rect) or goat_rect.colliderect(barn_rect):
            # Если столкновение произошло, возвращаем персонажа на предыдущую позицию
            if keys[pygame.K_a]:
                goat_rect.move_ip(player_speed, 0)
            if keys[pygame.K_d]:
                goat_rect.move_ip(-player_speed, 0)
            if keys[pygame.K_w]:
                goat_rect.move_ip(0, player_speed)
            if keys[pygame.K_s]:
                goat_rect.move_ip(0, -player_speed)

    # Движение босса за персонажем
    if win_blit == 'boss_fight1':
        if boss1_rect.x < goat_rect.x:
            boss1_rect.move_ip(boss1_speed, 0)
        elif boss1_rect.x > goat_rect.x:
            boss1_rect.move_ip(-boss1_speed, 0)
        if boss1_rect.y < goat_rect.y:
            boss1_rect.move_ip(0, boss1_speed)
        elif boss1_rect.y > goat_rect.y:
            boss1_rect.move_ip(0, -boss1_speed)

        # В случае столкновения, возвращаем персонажа на предыдущую позицию
        if goat_rect.colliderect(boss1_rect):
            goat_rect.move_ip(-player_speed, 0)
            player_health -= 1

        # Нанесение боссу урона аттакой
        if goat_attack_rect.colliderect(boss1_rect):
            boss1_health -= 1

        # Случай поражения
        if player_health <= 0:
            win.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render("ПОТРАЧЕНО", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            win.blit(text, text_rect)
            pygame.display.update()
            # Задержка
            pygame.time.wait(2000)
            intro_maker()

        if boss1_health <= 0:
            win.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render("ПОБЕДА", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            win.blit(text, text_rect)
            pygame.display.update()
            # Задержка
            pygame.time.wait(2000)
            intro_maker()

    # Отрисовка игровых объектов
    if win_blit != 'start_bg':
        draw_player(goat_rect[0], goat_rect[1])
    if win_blit == 'boss_fight1':
        win.blit(boss1, boss1_rect)
    if win_blit != 'start_bg' and win_blit != 'boss_fight1':
        draw_mill()
        draw_barn()
    # Обновление экрана
    pygame.display.update()
    # Ограничение скорости игры
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()
