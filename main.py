import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700

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
tree_res = 0
hay_res = 0

# Шаблон козла
goat = pygame.image.load('data/goat.png')
goat = pygame.transform.scale(goat, (player_width, player_height))
goat1 = pygame.image.load('data/goat1.png')
goat1 = pygame.transform.scale(goat1, (player_width, player_height))
goat2 = pygame.image.load('data/goat2.png')
goat2 = pygame.transform.scale(goat2, (player_width, player_height))
goat_rect = goat.get_rect()
goat_rect.center = (WIDTH // 2, HEIGHT / 1.5)
# Атака
goat_attack = pygame.image.load('data/cursor.png')
goat_attack = pygame.transform.scale(goat_attack, (player_width, player_height))
goat_attack_rect = goat_attack.get_rect()
goat_attack_rect.center = (-100, -100)
goat_attack_speed = 10

background = pygame.image.load('data/bg.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

charact_menu = pygame.image.load('data/charact_menu.png')
charact_menu = pygame.transform.scale(charact_menu, (600, 600))
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
boss1 = pygame.transform.scale(boss1, (100, 100))
boss1_rect = boss1.get_rect()
boss1_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
boss1_speed = 1
boss1_health = 100
# Босс №2
boss2 = pygame.image.load('data/boss2.png')
boss2 = pygame.transform.scale(boss2, (100, 100))
boss2_rect = boss2.get_rect()
boss2_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
boss2_speed = 1
boss2_health = 150

# Объекты
mill = pygame.image.load('data/mill.png')
mill = pygame.transform.scale(mill, (200, 300))
mill_rect = mill.get_rect(topleft=(WIDTH // 10, HEIGHT // 10))

barn = pygame.image.load('data/barn.png')
barn = pygame.transform.scale(barn, (300, 300))
barn_rect = barn.get_rect(topleft=(WIDTH // 2, HEIGHT // 10))

tree = pygame.image.load('data/tree.png')
tree = pygame.transform.scale(tree, (100, 100))
tree_rect = tree.get_rect(topleft=(700, 500))

hay = pygame.image.load('data/hay.png')
hay = pygame.transform.scale(hay, (100, 100))
hay_rect = hay.get_rect(topleft=(0, 400))


# Ресурсы
res1 = 0
res2 = 0

walk_right = [goat, goat1, goat2, goat2]
walk_left = [pygame.transform.flip(img, True, False) for img in walk_right]
win_blit = 'start_bg'

right = False
left = False
allow_animation = False
walk_count = 0
left_attack, right_attack = False, False
allow_walk = True
allow_boss_fight1 = False
allow_boss_fight2 = False

move_boss_event = None
move_boss_event_check = 'small'
move_boss2_event = None
move_boss2_event_check = 'small'

cost_speed_attack = 0
cost_strength = 0
cost_speed = 0


# Загрузка данных txt
def txt_BD_loading():
    global player_speed, lines, player_super_speed, player_max_health, res1, goat_attack_speed, player_strength
    global cost_speed, cost_strength, cost_speed_attack
    with open('characteristics.txt', encoding='utf-8') as file:
        lines = file.readlines()
        player_speed = int(lines[0])
        player_super_speed = player_speed * 2
        player_max_health = int(lines[1])
        res1 = int(lines[2])
        goat_attack_speed = int(lines[3])
        player_strength = int(lines[4])
        cost_speed = int(lines[5])
        cost_speed_attack = int(lines[6])
        cost_strength = int(lines[7])


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

    def draw_characteristic_btn(self):
        win.blit(characteristic_btn, (self.x, self.y))

    def draw_tree(self):
        win.blit(tree, (self.x, self.y))

    def draw_hay(self):
        win.blit(hay, (self.x, self.y))
    def draw_charact_menu(self):
        txt_BD_loading()

        win.blit(charact_menu, (self.x, self.y))
        win.blit(charact_esc_btn, (charact_esc_btn_rect.x, charact_esc_btn_rect.y))
        win.blit(speed_btn, (speed_btn_rect.x, speed_btn_rect.y))
        win.blit(attack_speed_btn, (attack_speed_btn_rect.x, attack_speed_btn_rect.y))
        win.blit(strength_btn, (strength_btn_rect.x, strength_btn_rect.y))
        # Ресурсы игрока
        get_text(25, "Пшено", 2.5, 3, (0, 0, 0), res1)
        # Характеристика игрока
        get_text(25, "Скорость", 2.6, 1.4, (0, 0, 0), player_speed)
        get_text(25, "Макс.Здоровье", 1.81, 1.4, (0, 0, 0), player_max_health)
        get_text(25, "Мощь", 2.6, 1.34, (0, 0, 0), player_strength)
        get_text(25, "Скорость атаки", 1.81, 1.34, (0, 0, 0), goat_attack_speed)
        get_text(25, "Ускорение", 2.75, 1.8, (0, 0, 0))
        get_text(25, "Ускорение атаки", 2.08, 1.8, (0, 0, 0))
        get_text(25, "Подкачка", 1.63, 1.8, (0, 0, 0))
        get_text(25, "Пшено", 2.8, 2.3, (0, 0, 0), cost_speed)
        get_text(25, "Пшено", 2.08, 2.3, (0, 0, 0), cost_speed_attack)
        get_text(25, "Пшено", 1.63, 2.3, (0, 0, 0), cost_strength)

    # Отрисовка персонажа и его интерфейса
    def draw_player(self):
        global walk_count, allow_animation, win_blit

        # Хп игрока
        get_text(50, "Здоровье", 8, 16, (255, 255, 0), player_health)
        get_text(25, "Древесина", 16, 8, (255, 255, 0), tree_res)
        get_text(25, "Сено", 16, 10, (255, 255, 0), hay_res)

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
    boss1 = pygame.transform.scale(boss1, (100, 100))
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
    boss2 = pygame.transform.scale(boss2, (100, 100))
    boss2_rect = boss2.get_rect()
    boss2_rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    move_boss2_event_check = 'small'
    win_blit = 'boss_fight2'
    background = pygame.image.load('data/bg_boss_fight1.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    win.blit(background, (0, 0))


def check_interaction():
    global mill, mill_rect, barn, barn_rect, allow_boss_fight1, allow_boss_fight2
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
        win.blit(background, (0, 0))
    elif win_blit == 'boss_fight1':
        win.blit(background, (0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(f"Босс: {boss1_health}", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 8, HEIGHT // 8))
        win.blit(text, text_rect)
    elif win_blit == 'boss_fight2':
        win.blit(background, (0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(f"Босс: {boss2_health}", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 8, HEIGHT // 8))
        win.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Нажатие по кнопкам
            if play_btn_rect.collidepoint(event.pos) and win_blit == 'start_bg':
                win.blit(background, (0, 0))
                player_x, player_y = WIDTH // 2, HEIGHT // 2
                win_blit = 'main1_bg'
            if characteristic_btn_rect.collidepoint(event.pos) and win_blit == 'main1_bg':
                win_blit = 'characteristic_bg'
            if charact_esc_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                win_blit = 'main1_bg'
            if speed_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                if res1 >= cost_speed:
                    res1 -= cost_speed
                    cost_speed = int(str(round(cost_speed * 1.5, 0))[:-2])
                    player_speed += 1
                    txt_BD_input(2, res1)
                    txt_BD_input(0, player_speed)
                    txt_BD_input(5, cost_speed)
                    txt_BD_loading()
            if attack_speed_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                if res1 >= cost_speed_attack:
                    res1 -= cost_speed_attack
                    cost_speed_attack = int(str(round(cost_speed_attack * 1.5, 0))[:-2])
                    goat_attack_speed += 1
                    txt_BD_input(2, res1)
                    txt_BD_input(3, goat_attack_speed)
                    txt_BD_input(6, cost_speed_attack)
                    txt_BD_loading()
            if strength_btn_rect.collidepoint(event.pos) and win_blit == 'characteristic_bg':
                if res1 >= cost_strength:
                    res1 -= cost_strength
                    cost_strength = int(str(round(cost_strength * 2.5, 0))[:-2])
                    player_strength += 1
                    txt_BD_input(2, res1)
                    txt_BD_input(4, player_strength)
                    txt_BD_input(7, cost_strength)
                    txt_BD_loading()
            if new_game_btn_rect.collidepoint(event.pos) and win_blit == 'start_bg':
                txt_BD_input(0, 3)
                txt_BD_input(1, 100)
                txt_BD_input(2, 0)
                txt_BD_input(3, 10)
                txt_BD_input(4, 1)
                txt_BD_input(5, 3)
                txt_BD_input(6, 3)
                txt_BD_input(7, 64)
                win_blit = 'main1_bg'

        if event.type == pygame.KEYUP:
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

        if event.type == move_boss2_event:
            if move_boss2_event_check == 'big':
                x, y, = boss2_rect.x, boss2_rect.y
                boss2 = pygame.transform.scale(boss2, (100, 100))
                boss2_rect = boss1.get_rect()
                boss2_rect.move_ip(x, y)
                move_boss2_event_check = 'small'
            else:
                x, y, = boss2_rect.x, boss2_rect.y
                boss2 = pygame.transform.scale(boss2, (200, 200))
                boss2_rect = boss2.get_rect()
                boss2_rect.move_ip(x, y)
                move_boss2_event_check = 'big'
                boss2_speed = 2

    keys = pygame.key.get_pressed()
    # Движение персонажа
    if win_blit != 'start_bg' and win_blit != 'characteristic_bg':
        if keys[pygame.K_LSHIFT]:
            goat_speed = player_super_speed
        else:
            goat_speed = player_speed
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

        if keys[pygame.K_c] and win_blit != 'start_bg':
            if left_attack is False and right_attack is False:
                goat_attack = pygame.image.load('data/cursor.png')
                goat_attack = pygame.transform.scale(goat_attack, (player_width, player_height))
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

    # проверка на столкновения с др предметами
    if win_blit == 'main1_bg':
        check_collision(mill_rect)
        check_collision(barn_rect)
        # добыча ресов
        if goat_rect.colliderect(tree_rect) and goat_speed == player_super_speed:
            check_collision(tree_rect)
            push()
            tree_res += 5
        elif goat_rect.colliderect(tree_rect) and goat_speed != player_super_speed:
            check_collision(tree_rect)
        if goat_rect.colliderect(hay_rect) and goat_speed == player_super_speed:
            check_collision(hay_rect)
            push()
            hay_res += 2
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
            res1 += 3
            txt_BD_input(2, res1)
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
            text = font.render("ПОБЕДА", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            win.blit(text, text_rect)
            pygame.display.update()
            # Задержка
            pygame.time.wait(2000)
            intro_maker()

    # Случай гибели персонажа
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

    # Отрисовка игровых объектов
    if win_blit != 'start_bg' and win_blit != 'characteristic_bg':
        draw = Draw(goat_rect[0], goat_rect[1])
        draw.draw_player()
    if win_blit == 'boss_fight1':
        win.blit(boss1, boss1_rect)
    if win_blit == 'boss_fight2':
        win.blit(boss2, boss2_rect)
    if win_blit == 'main1_bg':
        draw = Draw(mill_rect.x, mill_rect.y)
        draw.draw_mill()
        draw = Draw(barn_rect.x, barn_rect.y)
        draw.draw_barn()
        draw = Draw(characteristic_btn_rect.x, characteristic_btn_rect.y)
        draw.draw_characteristic_btn()
        draw = Draw(tree_rect.x, tree_rect.y)
        draw.draw_tree()
        draw = Draw(hay_rect.x, hay_rect.y)
        draw.draw_hay()
    if win_blit == 'characteristic_bg':
        draw = Draw(charact_menu_rect.x, charact_menu_rect.y)
        draw.draw_charact_menu()

    # Отрисовка текста взаимодействия с предметом
    if ((allow_boss_fight1 is True) or (allow_boss_fight2 is True)) and (win_blit == 'main1_bg'):
        font = pygame.font.Font(None, 36)
        text = font.render("Взаимодействовать - F", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH / 1.2, HEIGHT / 1.1))
        win.blit(text, text_rect)

    # Обновление экрана
    pygame.display.update()
    # Ограничение скорости игры
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()
