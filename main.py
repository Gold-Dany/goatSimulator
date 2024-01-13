import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1300, 900

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goat Simulator")

lines = []

# Характеристики персонажа
player_width, player_height = 100, 100
player_health = 100
player_max_health = 0
player_speed = 0
player_super_speed = 0
player_strength = 0

# Шаблон козла
goat = pygame.image.load('data/goat.png')
goat = pygame.transform.scale(goat, (60, 60))
goat = pygame.transform.scale(goat, (player_width, player_height))
goat1 = pygame.image.load('data/goat1.png')
goat1 = pygame.transform.scale(goat1, (60, 60))
goat1 = pygame.transform.scale(goat1, (player_width, player_height))
goat2 = pygame.image.load('data/goat2.png')
goat2 = pygame.transform.scale(goat2, (60, 60))
goat2 = pygame.transform.scale(goat2, (player_width, player_height))
goat_rect = goat.get_rect()
goat_rect.center = (WIDTH // 2, HEIGHT / 1.5)
# Атака
goat_attack = pygame.image.load('data/horn.png')
goat_attack = pygame.transform.scale(goat_attack, (50, 50))
goat_attack_rect = goat_attack.get_rect()
goat_attack_rect.center = (-100, -100)
goat_attack_speed = 10

background = pygame.image.load('data/bg.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

charact_menu = pygame.image.load('data/charact_menu.png')
charact_menu = pygame.transform.scale(charact_menu, (750, 750))
charact_menu_rect = charact_menu.get_rect()
charact_menu_rect.center = (WIDTH // 2, HEIGHT // 2)

# Кнопки
play_btn = pygame.image.load('data/play_btn.png')
play_btn = pygame.transform.scale(play_btn, (100, 100))
play_btn_rect = play_btn.get_rect()
play_btn_rect.center = (WIDTH // 2, HEIGHT // 2)

characteristic_btn = pygame.image.load('data/characteristic_btn.png')
characteristic_btn = pygame.transform.scale(characteristic_btn, (100, 100))
characteristic_btn_rect = characteristic_btn.get_rect()
characteristic_btn_rect.center = (WIDTH / 1.036, HEIGHT // 20)

charact_esc_btn = pygame.image.load('data/characteristic_btn.png')
charact_esc_btn = pygame.transform.scale(charact_esc_btn, (50, 50))
charact_esc_btn_rect = charact_esc_btn.get_rect()
charact_esc_btn_rect.center = (WIDTH / 1.65, HEIGHT // 3)

speed_btn = pygame.image.load('data/characteristic_btn.png')
speed_btn = pygame.transform.scale(speed_btn, (50, 50))
speed_btn_rect = speed_btn.get_rect()
speed_btn_rect.center = (WIDTH / 2.8, HEIGHT // 2)

attack_speed_btn = pygame.image.load('data/characteristic_btn.png')
attack_speed_btn = pygame.transform.scale(attack_speed_btn, (50, 50))
attack_speed_btn_rect = attack_speed_btn.get_rect()
attack_speed_btn_rect.center = (WIDTH / 2.08, HEIGHT // 2)

strength_btn = pygame.image.load('data/characteristic_btn.png')
strength_btn = pygame.transform.scale(strength_btn, (50, 50))
strength_btn_rect = strength_btn.get_rect()
strength_btn_rect.center = (WIDTH / 1.63, HEIGHT // 2)

new_game_btn = pygame.image.load('data/new_game_btn.png')
new_game_btn = pygame.transform.scale(new_game_btn, (100, 100))
new_game_btn_rect = new_game_btn.get_rect()
new_game_btn_rect.center = (WIDTH / 2, HEIGHT / 1.5)

# Босс №1
boss1 = pygame.image.load('data/boss1.png')
boss1_rect = boss1.get_rect()
boss1_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
boss1_speed = 1
boss1_health = 100
# Босс №2
boss2 = pygame.image.load('data/boss2.png')
boss2_rect = boss2.get_rect()
boss2_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
boss2_speed = 1
boss2_health = 150
# Босс №3
boss3 = pygame.image.load('data/boss3_1.png')
boss3 = pygame.transform.scale(boss3, (150, 150))
boss3_rect = boss3.get_rect()
boss3_rect.center = (WIDTH // 2, HEIGHT // 2)
boss3_health = 1000
boss3_2 = pygame.image.load('data/boss3_2.png')
boss3_2 = pygame.transform.scale(boss3_2, (150, 150))

# Объекты
mill = pygame.image.load('data/mill.png')
mill = pygame.transform.scale(mill, (200, 300))

barn = pygame.image.load('data/barn.png')
barn = pygame.transform.scale(barn, (300, 300))

anvil = pygame.image.load('data/anvil.png')
anvil = pygame.transform.scale(anvil, (40, 40))
anvil = pygame.transform.scale(anvil, (100, 100))

black_window = pygame.image.load('data/black.jpg')
black_window = pygame.transform.scale(black_window, (50, 50))

mill_rect = mill.get_rect(topleft=(WIDTH // 10, HEIGHT // 10))
barn_rect = barn.get_rect(topleft=(WIDTH // 2, HEIGHT // 10))
anvil_x, anvil_y = 1.2, 3.1
anvil_rect = anvil.get_rect(topleft=(WIDTH // anvil_x, HEIGHT // anvil_y))
black_window_x, black_window_y = WIDTH + 1, 1.058
black_window_rect = anvil.get_rect(topleft=(WIDTH // black_window_x, HEIGHT // black_window_y))

tree = pygame.image.load('data/tree.png')
tree = pygame.transform.scale(tree, (30, 30))
tree = pygame.transform.scale(tree, (100, 130))
tree_rect = tree.get_rect(topleft=(WIDTH // 2.5, HEIGHT // 3.5))

hay_img = pygame.image.load('data/hay.png')
hay_img = pygame.transform.scale(hay_img, (30, 30))
hay_img = pygame.transform.scale(hay_img, (100, 115))
hay_rect = hay_img.get_rect(topleft=(WIDTH // 1.3, HEIGHT // 1.2))

# Ресурсы
millet = 0
hay = 0
main_res = 0
tree_res = 0
hay_res = 0

walk_right = [goat, goat1, goat2, goat2]
boss3_animation = [boss3, boss3_2, boss3_2, boss3]
walk_left = [pygame.transform.flip(img, True, False) for img in walk_right]
win_blit = 'start_bg'

right = False
left = False
allow_animation = False
allow_boss3_animation = False
walk_count = 0
walk_boss3_count = 0
left_attack, right_attack = False, False
allow_walk = True
allow_boss_fight1 = False
allow_boss_fight2 = False
allow_boss_fight3 = False
allow_make_res = False

move_boss_event = None
move_boss_event_check = 'small'
move_boss2_event = None
move_boss2_event_check = 'small'

cost_speed_attack = 0
cost_strength = 0
cost_speed = 0

no_res_event = pygame.USEREVENT + 1

# Звуки
sound1_playing = False
sound1 = pygame.mixer.Sound('data/cartoon-running-sound-effect.mp3')
sound1.set_volume(0.2)

sound2_playing = False
sound2 = pygame.mixer.Sound('data/206638.mp3')
sound2.set_volume(0.2)

sound3 = pygame.mixer.Sound('data/click.mp3')
sound3.set_volume(0.5)

sound4_playing = False
sound4 = pygame.mixer.Sound('data/peritune-noway3.mp3')
sound4.set_volume(0.2)


# Загрузка данных txt
def txt_BD_loading():
    global player_speed, lines, player_super_speed, player_max_health, millet, goat_attack_speed, player_strength
    global cost_speed, cost_strength, cost_speed_attack, hay, main_res, tree_res, hay_res
    with open('characteristics.txt', encoding='utf-8') as file:
        lines = file.readlines()
        player_speed = int(lines[0])
        player_super_speed = player_speed * 2
        player_max_health = int(lines[1])
        millet = int(lines[2])
        goat_attack_speed = int(lines[3])
        player_strength = int(lines[4])
        cost_speed = int(lines[5])
        cost_speed_attack = int(lines[6])
        cost_strength = int(lines[7])
        hay = int(lines[8])
        main_res = int(lines[9])
        tree_res = int(lines[10])
        hay_res = int(lines[11])


# Запись в txt
def txt_BD_input(num, str):
    global lines
    lines[num] = f'{str}\n'
    with open('characteristics.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
        file.close()


txt_BD_loading()


class Draw:

    def __init__(self, draw_x=0, draw_y=0):
        self.x, self.y = draw_x, draw_y

    def draw_mill(self):
        win.blit(mill, (self.x, self.y))

    def draw_barn(self):
        win.blit(barn, (self.x, self.y))

    def draw_anvil(self):
        win.blit(anvil, (self.x, self.y))

    def draw_black_window(self):
        win.blit(black_window, (self.x, self.y))

    def draw_tree(self):
        win.blit(tree, (self.x, self.y))

    def draw_hay(self):
        win.blit(hay_img, (self.x, self.y))

    def draw_characteristic_btn(self):
        win.blit(characteristic_btn, (self.x, self.y))

    def draw_charact_menu(self):
        txt_BD_loading()

        win.blit(charact_menu, (self.x, self.y))
        win.blit(charact_esc_btn, (charact_esc_btn_rect.x, charact_esc_btn_rect.y))
        win.blit(speed_btn, (speed_btn_rect.x, speed_btn_rect.y))
        win.blit(attack_speed_btn, (attack_speed_btn_rect.x, attack_speed_btn_rect.y))
        win.blit(strength_btn, (strength_btn_rect.x, strength_btn_rect.y))
        # Ресурсы игрока
        get_text(25, "Пшено", 2.5, 3, (0, 0, 0), millet)
        get_text(25, "Сено", 2.5, 2.8, (0, 0, 0), hay)
        get_text(25, "Комки активации", 2.5, 2.6, (0, 0, 0), main_res)
        get_text(25, "Древесина", 1.9, 3, (0, 0, 0), tree_res)
        get_text(25, "Камень", 1.9, 2.8, (0, 0, 0), hay_res)
        # Характеристика игрока
        get_text(25, "Скорость", 2.6, 1.4, (0, 0, 0), player_speed)
        get_text(25, "Макс.Здоровье", 1.81, 1.4, (0, 0, 0), player_max_health)
        get_text(25, "Сила", 2.6, 1.34, (0, 0, 0), player_strength)
        get_text(25, "Скорость атаки", 1.81, 1.34, (0, 0, 0), goat_attack_speed)
        get_text(25, "Ускорение", 2.8, 1.8, (0, 0, 0))
        get_text(25, "Ускорение атаки", 2.08, 1.8, (0, 0, 0))
        get_text(25, "Увеличить силу", 1.63, 1.8, (0, 0, 0))
        get_text(25, "Комки", 2.8, 2.3, (0, 0, 0), cost_speed)
        get_text(25, "Комки", 2.08, 2.3, (0, 0, 0), cost_speed_attack)
        get_text(25, "Комки", 1.63, 2.3, (0, 0, 0), cost_strength)

    # Отрисовка персонажа и его интерфейса
    def draw_player(self):
        global walk_count, allow_animation, win_blit

        # Хп игрока
        get_text(50, "Здоровье", 8, 16, (255, 255, 0), player_health)
        if win_blit == 'main1_bg':
            get_text(50, "Комки активации", 2.3, 16, (255, 255, 0), main_res)

        if win_blit != 'start_bg':

            if walk_count + 1 >= 12:
                walk_count = 0
            if allow_animation:
                if left:
                    win.blit(walk_left[walk_count // 3], (self.x, self.y))
                    walk_count += 1
                elif right:
                    win.blit(walk_right[walk_count // 3], (self.x, self.y))
                    walk_count += 1
                else:
                    win.blit(walk_right[walk_count // 3], (self.x, self.y))
                    walk_count += 1
            else:
                if left:
                    win.blit(walk_left[0], (self.x, self.y))
                elif right:
                    win.blit(walk_right[0], (self.x, self.y))
                else:
                    win.blit(walk_right[0], (self.x, self.y))

    # Отрисовка Главного Босса и его интерфейса

    def draw_boss3(self):
        global walk_boss3_count, allow_boss3_animation, win_blit

        # Хп Главного Босса
        get_text(50, "Главный Босс", 7, 8, (255, 0, 0), boss3_health)

        if win_blit == 'boss_fight3':

            if walk_boss3_count + 1 >= 12:
                walk_boss3_count = 0
            if allow_boss3_animation:
                win.blit(boss3_animation[walk_boss3_count // 3], (self.x, self.y))
                walk_boss3_count += 1


def get_text(size, str, x_coord, y_coord, color, count=None):
    if count or count == 0:
        font1 = pygame.font.Font(None, size)
        text1 = font1.render(f"{str}: {count}", True, color)
        text_rect1 = text1.get_rect(center=(WIDTH // x_coord, HEIGHT // y_coord))
        win.blit(text1, text_rect1)
    else:
        font1 = pygame.font.Font(None, size)
        text1 = font1.render(f"{str}", True, color)
        text_rect1 = text1.get_rect(center=(WIDTH // x_coord, HEIGHT // y_coord))
        win.blit(text1, text_rect1)


def intro_maker():
    global win_blit, background, player_health, goat_attack, left_attack, right_attack, goat_attack_rect

    win_blit = 'start_bg'
    image = pygame.image.load('data/goat_bg.jpg')
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    win.blit(image, (0, 0))
    win.blit(play_btn, play_btn_rect)
    win.blit(new_game_btn, new_game_btn_rect)

    goat_rect.center = (WIDTH // 2, HEIGHT / 1.5)
    player_health = player_max_health
    goat_attack = None
    goat_attack_rect.center = (-100, -100)
    left_attack, right_attack = False, False

    background = pygame.image.load('data/bg.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))


intro_maker()


def boss_fight1():
    global win_blit, background, move_boss_event, move_boss_event_check, boss1, boss1_health, boss1_rect
    boss1_health = 100
    move_boss_event = pygame.USEREVENT + 1
    pygame.time.set_timer(move_boss_event, 5000)
    boss1 = pygame.image.load('data/boss1.png')
    boss1 = pygame.transform.scale(boss1, (200, 200))
    boss1_rect = boss1.get_rect()
    boss1_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    move_boss_event_check = 'small'
    win_blit = 'boss_fight1'
    background = pygame.image.load('data/bg_boss_fight1.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    win.blit(background, (0, 0))


def boss_fight2():
    global win_blit, background, move_boss2_event, move_boss2_event_check, boss2, boss2_health, boss2_rect
    boss2_health = 150
    move_boss2_event = pygame.USEREVENT + 1
    pygame.time.set_timer(move_boss2_event, 5000)
    boss2 = pygame.image.load('data/boss2.png')
    boss2 = pygame.transform.scale(boss2, (200, 250))
    boss2_rect = boss2.get_rect()
    boss2_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    move_boss2_event_check = 'small'
    win_blit = 'boss_fight2'
    background = pygame.image.load('data/bg_boss_fight1.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    win.blit(background, (0, 0))


def boss_fight3():
    global win_blit, background, allow_boss3_animation
    allow_boss3_animation = True
    win_blit = 'boss_fight3'
    background = pygame.image.load('data/black.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    win.blit(background, (0, 0))


def check_interaction():
    global mill, mill_rect, barn, barn_rect, allow_boss_fight1, allow_boss_fight2, anvil, anvil_rect, allow_make_res
    global black_window, black_window_rect, allow_boss_fight3
    # Область взаимодействия с мельницей
    mill = pygame.transform.scale(mill, (250, 350))
    mill_rect = mill.get_rect(topleft=(WIDTH // 12, HEIGHT // 10))
    if goat_rect.colliderect(mill_rect):
        allow_boss_fight1 = True
    else:
        allow_boss_fight1 = False
    mill = pygame.transform.scale(mill, (200, 300))
    mill_rect = mill.get_rect(topleft=(WIDTH // 10, HEIGHT // 10))
    # Область взаимодействия с амбаром
    barn = pygame.transform.scale(barn, (350, 350))
    barn_rect = barn.get_rect(topleft=(WIDTH / 2.1, HEIGHT // 10))
    if goat_rect.colliderect(barn_rect):
        allow_boss_fight2 = True
    else:
        allow_boss_fight2 = False
    barn = pygame.transform.scale(barn, (300, 300))
    barn_rect = barn.get_rect(topleft=(WIDTH // 2, HEIGHT // 10))
    # Область взаимодействия с наковальней
    anvil = pygame.transform.scale(anvil, (200, 200))
    anvil_rect = anvil.get_rect(topleft=(WIDTH // anvil_x, HEIGHT // (anvil_y + 0.2)))
    if goat_rect.colliderect(anvil_rect):
        allow_make_res = True
    else:
        allow_make_res = False
    anvil = pygame.transform.scale(anvil, (100, 100))
    anvil_rect = anvil.get_rect(topleft=(WIDTH // anvil_x, HEIGHT // anvil_y))
    # Область взаимодействия с наковальней
    black_window = pygame.transform.scale(black_window, (100, 100))
    black_window_rect = black_window.get_rect(
        topleft=(WIDTH // black_window_x, HEIGHT // (black_window_y + 0.1)))
    if goat_rect.colliderect(black_window_rect):
        allow_boss_fight3 = True
    else:
        allow_boss_fight3 = False
    black_window = pygame.transform.scale(black_window, (50, 50))
    black_window_rect = black_window.get_rect(topleft=(WIDTH // black_window_x, HEIGHT // black_window_y))


def check_collision(obj):
    # Проверка на столкновение с препятствием
    if goat_rect.colliderect(obj):
        # Если столкновение произошло, возвращаем персонажа на предыдущую позицию
        if keys[pygame.K_a]:
            goat_rect.move_ip(goat_speed, 0)
        if keys[pygame.K_d]:
            goat_rect.move_ip(-goat_speed, 0)
        if keys[pygame.K_w]:
            goat_rect.move_ip(0, goat_speed)
        if keys[pygame.K_s]:
            goat_rect.move_ip(0, -goat_speed)


def no_resours():
    global no_res_event
    get_text(50, 'НЕ ХВАТАЕТ СРЕДСТВ', 5, 10, (255, 0, 0))
    no_res_event = pygame.USEREVENT + 1
    pygame.time.set_timer(no_res_event, 1500)


def push():
    if keys[pygame.K_a]:
        goat_rect.move_ip(30, 0)
    if keys[pygame.K_d]:
        goat_rect.move_ip(-30, 0)
    if keys[pygame.K_w]:
        goat_rect.move_ip(0, 30)
    if keys[pygame.K_s]:
        goat_rect.move_ip(0, -30)


running = True
clock = pygame.time.Clock()
# Основной игровой цикл
while running:
    txt_BD_loading()
    # Проверка локации
    if win_blit == 'main1_bg':
        sound4.stop()
        if not sound2_playing or not channel2.get_busy():
            channel2 = sound2.play()
            sound2_playing = True
        win.blit(background, (0, 0))
    elif win_blit == 'boss_fight1':
        sound2.stop()
        if not sound4_playing or not channel4.get_busy():
            channel4 = sound4.play()
            sound4_playing = True
        win.blit(background, (0, 0))
        get_text(50, "Босс", 8, 8, (255, 0, 0), boss1_health)
    elif win_blit == 'boss_fight2':
        sound2.stop()
        if not sound4_playing or not channel4.get_busy():
            channel4 = sound4.play()
            sound4_playing = True
        win.blit(background, (0, 0))
        get_text(50, "Босс", 8, 8, (255, 0, 0), boss2_health)
    elif win_blit == 'boss_fight3':
        sound2.stop()
        if not sound4_playing or not channel4.get_busy():
            channel4 = sound4.play()
            sound4_playing = True
        win.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Нажатие по кнопкам
            if play_btn_rect.collidepoint(event.pos) and win_blit == 'start_bg':
                win.blit(background, (0, 0))
                player_x, player_y = WIDTH // 2, HEIGHT // 2
                win_blit = 'main1_bg'
                sound3.play()
            if characteristic_btn_rect.collidepoint(event.pos) and win_blit == 'main1_bg':
                win_blit = 'characteristic_bg'
                sound3.play()
            if charact_esc_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                win_blit = 'main1_bg'
                sound3.play()
            if speed_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                sound3.play()
                if main_res >= cost_speed:
                    main_res -= cost_speed
                    cost_speed = int(str(round(cost_speed * 1.5, 0))[:-2])
                    player_speed += 1
                    txt_BD_input(2, millet)
                    txt_BD_input(9, main_res)
                    txt_BD_input(0, player_speed)
                    txt_BD_input(5, cost_speed)
                    txt_BD_loading()
                else:
                    no_resours()
            if attack_speed_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                sound3.play()
                if main_res >= cost_speed_attack:
                    main_res -= cost_speed_attack
                    cost_speed_attack = int(str(round(cost_speed_attack * 1.5, 0))[:-2])
                    goat_attack_speed += 1
                    txt_BD_input(2, millet)
                    txt_BD_input(9, main_res)
                    txt_BD_input(3, goat_attack_speed)
                    txt_BD_input(6, cost_speed_attack)
                    txt_BD_loading()
                else:
                    no_resours()
            if strength_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                sound3.play()
                if main_res >= cost_strength:
                    main_res -= cost_strength
                    cost_strength = int(str(round(cost_strength * 2.5, 0))[:-2])
                    player_strength += 1
                    txt_BD_input(2, millet)
                    txt_BD_input(9, main_res)
                    txt_BD_input(4, player_strength)
                    txt_BD_input(7, cost_strength)
                    txt_BD_loading()
                else:
                    no_resours()
            if new_game_btn_rect.collidepoint(event.pos) and win_blit == 'start_bg':
                sound3.play()
                txt_BD_input(0, 3)  # скорость
                txt_BD_input(1, 100)  # здоровье
                txt_BD_input(2, 0)  # пшено
                txt_BD_input(3, 10)  # скорость атаки
                txt_BD_input(4, 1)  # сила
                txt_BD_input(5, 3)  # ст.скорости
                txt_BD_input(6, 3)  # ст.ск.атаки
                txt_BD_input(7, 16)  # ст.силы
                txt_BD_input(8, 0)  # сено
                txt_BD_input(9, 0)  # комки активации
                win_blit = 'main1_bg'

        if event.type == pygame.KEYUP:
            allow_animation = False

        if event.type == move_boss_event:
            if move_boss_event_check == 'big':
                move_boss_event_check = 'small'
                boss1_speed = 1
            else:
                move_boss_event_check = 'big'
                boss1_speed = 2

        if event.type == move_boss2_event:
            if move_boss2_event_check == 'big':
                boss2 = pygame.transform.flip(boss2, True, False)
                move_boss2_event_check = 'small'
                boss2_speed = 1
            else:
                boss2 = pygame.transform.flip(boss2, True, False)
                move_boss2_event_check = 'big'
                boss2_speed = 2

        if event.type == no_res_event:
            if win_blit == 'characteristic_bg':
                win.blit(background, (0, 0))
                draw = Draw(charact_menu_rect.x, charact_menu_rect.y)
                draw.draw_charact_menu()
                pygame.time.set_timer(no_res_event, 0)

    keys = pygame.key.get_pressed()
    # Движение персонажа
    if win_blit != 'start_bg' and win_blit != 'characteristic_bg':
        if keys[pygame.K_LSHIFT]:
            goat_speed = player_super_speed
            if not sound1_playing or not channel1.get_busy():
                channel1 = sound1.play()
                sound1_playing = True
        else:
            goat_speed = player_speed
            sound1.stop()
            sound1_playing = False
        if keys[pygame.K_a]:
            goat_rect.move_ip(-goat_speed, 0)
            left = True
            right = False
            allow_animation = True
        if keys[pygame.K_d]:
            goat_rect.move_ip(goat_speed, 0)
            right = True
            left = False
            allow_animation = True
        if keys[pygame.K_w]:
            goat_rect.move_ip(0, -goat_speed)
            allow_animation = True
        if keys[pygame.K_s]:
            goat_rect.move_ip(0, goat_speed)
            allow_animation = True

        if keys[pygame.K_f] and win_blit == 'main1_bg':
            if allow_boss_fight1 is True:
                boss_fight1()
            elif allow_boss_fight2 is True:
                boss_fight2()
            elif allow_boss_fight3 is True:
                boss_fight3()
            elif allow_make_res is True:
                if millet >= 3 and hay >= 2 and hay_res >= 150 and tree_res >= 350:
                    millet -= 3
                    hay -= 2
                    hay_res -= 150
                    tree_res -= 350
                    main_res += 1
                    txt_BD_input(2, millet)
                    txt_BD_input(8, hay)
                    txt_BD_input(9, main_res)
                    txt_BD_input(10, tree_res)
                    txt_BD_input(11, hay_res)
                    txt_BD_loading()

        if keys[pygame.K_c] and win_blit != 'start_bg':
            if left_attack is False and right_attack is False:
                goat_attack = pygame.image.load('data/horn.png')
                goat_attack = pygame.transform.scale(goat_attack, (20, 20))
                goat_attack = pygame.transform.scale(goat_attack, (50, 50))
                goat_attack_rect = goat_attack.get_rect()
                goat_attack_rect.center = (goat_rect.x, goat_rect.y)
                left_attack = False
                right_attack = False

    check_interaction()

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
        check_collision(mill_rect)
        check_collision(barn_rect)
        check_collision(anvil_rect)
        check_collision(black_window_rect)
        # добыча ресов
        if goat_rect.colliderect(tree_rect) and goat_speed == player_super_speed:
            check_collision(tree_rect)
            push()
            # Шанс на выпадение древесины
            fortune = random.randint(0, 2)
            if fortune == 1:
                tree_res += 1
            txt_BD_input(10, tree_res)
        elif goat_rect.colliderect(tree_rect) and goat_speed != player_super_speed:
            check_collision(tree_rect)
        if goat_rect.colliderect(hay_rect) and goat_speed == player_super_speed:
            check_collision(hay_rect)
            push()
            # Шанс на выпадение камня
            fortune = random.randint(0, 4)
            if fortune == 1:
                hay_res += 1
            txt_BD_input(11, hay_res)
        elif goat_rect.colliderect(hay_rect) and goat_speed != player_super_speed:
            check_collision(hay_rect)

    # Движение босса №1 за персонажем
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

        # Нанесение боссу №1 урона аттакой
        if goat_attack_rect.colliderect(boss1_rect):
            boss1_health -= player_strength

        if boss1_health <= 0:
            win.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render("ПОБЕДА +3 Пшена", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            win.blit(text, text_rect)
            millet += 3
            txt_BD_input(2, millet)
            pygame.display.update()
            # Задержка
            pygame.time.wait(2000)
            intro_maker()

    # Движение босса №2 за персонажем
    if win_blit == 'boss_fight2':
        if boss2_rect.x < goat_rect.x:
            boss2_rect.move_ip(boss2_speed, 0)
        elif boss2_rect.x > goat_rect.x:
            boss2_rect.move_ip(-boss2_speed, 0)
        if boss2_rect.y < goat_rect.y:
            boss2_rect.move_ip(0, boss2_speed)
        elif boss2_rect.y > goat_rect.y:
            boss2_rect.move_ip(0, -boss2_speed)

        # В случае столкновения, возвращаем персонажа на предыдущую позицию
        if goat_rect.colliderect(boss2_rect):
            goat_rect.move_ip(-player_speed, 0)
            player_health -= 1

        # Нанесение боссу №2 урона аттакой
        if goat_attack_rect.colliderect(boss2_rect):
            boss2_health -= player_strength

        if boss2_health <= 0:
            win.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render("ПОБЕДА +2 Сена", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            win.blit(text, text_rect)
            hay += 2
            txt_BD_input(8, hay)
            pygame.display.update()
            # Задержка
            pygame.time.wait(2000)
            intro_maker()

    if win_blit == 'boss_fight3':
        # В случае столкновения, возвращаем персонажа на предыдущую позицию
        if goat_rect.colliderect(boss3_rect):
            goat_rect.move_ip(-player_speed, 0)
            player_health -= 1

    # Случай гибели персонажа
    if player_health <= 0:
        win.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("ОТБРОСИЛ КОПЫТА", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)
        pygame.display.update()
        # Задержка
        pygame.time.wait(2000)
        intro_maker()

    # Отрисовка игровых объектов
    if win_blit != 'start_bg' and win_blit != 'characteristic_bg':
        draw = Draw(goat_rect[0], goat_rect[1])
        draw.draw_player()
    if win_blit == 'boss_fight1':
        win.blit(boss1, boss1_rect)
    if win_blit == 'boss_fight2':
        win.blit(boss2, boss2_rect)
    if win_blit == 'boss_fight3':
        draw = Draw(boss3_rect.x, boss3_rect.y)
        draw.draw_boss3()
    if win_blit == 'main1_bg':
        draw = Draw(mill_rect.x, mill_rect.y)
        draw.draw_mill()
        draw = Draw(barn_rect.x, barn_rect.y)
        draw.draw_barn()
        draw = Draw(characteristic_btn_rect.x, characteristic_btn_rect.y)
        draw.draw_characteristic_btn()
        draw = Draw(anvil_rect.x, anvil_rect.y)
        draw.draw_anvil()
        draw = Draw(tree_rect.x, tree_rect.y)
        draw.draw_tree()
        draw = Draw(hay_rect.x, hay_rect.y)
        draw.draw_hay()
        draw = Draw(black_window_rect.x, black_window_rect.y)
        draw.draw_black_window()
    if win_blit == 'characteristic_bg':
        draw = Draw(charact_menu_rect.x, charact_menu_rect.y)
        draw.draw_charact_menu()

    # Отрисовка текста взаимодействия с предметом
    if ((allow_boss_fight1 is True) or (allow_boss_fight2 is True)) and (win_blit == 'main1_bg'):
        get_text(36, f"Взаимодействовать - F", 1.2, 1.1, (255, 255, 255))
    if (allow_make_res is True) and (win_blit == 'main1_bg'):
        if millet >= 3 and hay >= 2 and tree_res >= 350 and hay_res >= 150:
            get_text(36, f"Создать комок активации - F", 1.2, 1.1, (255, 255, 255))
        else:
            get_text(36, "Не хватает средств", 1.3, 1.1, (255, 255, 255))
            get_text(30, "Требуется: 3 Пшена, 2 Сена, 150 Камня и 350 Древесины", 1.3, 1.05, (255, 255, 255))
    if (allow_boss_fight3 is True) and (win_blit == 'main1_bg'):
        get_text(36, f"Главный Босс - F", 1.2, 1.1, (255, 255, 255))

    # Обновление экрана
    pygame.display.update()
    # Ограничение скорости игры
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()
