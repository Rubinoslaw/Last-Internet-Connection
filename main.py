import pygame, asyncio, random, webbrowser, sys, platform

# pygbag: width=1080, height=1080, fit=contain

async def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=2048)
    pygame.init()

    await asyncio.sleep(0.1)

    FPS = 22
    SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 1080
    game_finished = False
    score = 0

# Colors
    RED = (205, 20, 20)
    GREEN = (50, 157, 50)
    YELLOW = (218, 165, 32)
    GOLD = (130, 150, 32)
    BLACK = (22, 15, 12)
    WHITE = (250, 250, 250)
    BLUE = (100, 149, 237)
    CYAN = (3, 255, 255)
    LIME = (0, 255, 0)
    ORANGE = (255, 165, 0)
    DARK_TAN = (210, 180, 140)
    MEDIUM_BLUE = (0, 0, 205)
    PINK = (255, 120, 180)
    OLIVE = (128, 128, 0)
    GREY = (128, 128, 128)
    INDIGO = (128, 0, 130)
    MAROON = (128, 0, 0)
    VIOLET = (238, 120, 238)
    DARK_GREY = (0, 128, 128)
    ROYAL_BLUE = (65, 105, 225)
    REBECCA_PURPLE = (128, 51, 153)
    PURPLE = (128, 0, 128)
    TAN = (255, 250, 140)
    CORAL = (255, 127, 80)
    CHOCOLATE = (210, 127, 30)
    DARK_CYAN = (3, 150, 150)

    pygame.display.set_caption("Last Internet Connection")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

# Password generation
    password = random.randint(10000000, 99999999)
    password = str(password)
    user_input = ""
    limit = 8

# Timer things
    timer_number = 11
    timer_ms = 1180
    abb = pygame.time.get_ticks()

# Random things
    elon = [5, 7, 10]
    heh = random.choice(elon)
    son = [1, 2, 4, 6]
    sonion = random.choice(son)

# Texts
    czcionka = pygame.font.SysFont("Comic Sans MS", 70)
    czcionka_2 = pygame.font.SysFont("Comic Sans MS", 120)
    czcionka_3 = pygame.font.SysFont("Comic Sans MS", 57)
    czcionka_4 = pygame.font.SysFont("Comic Sans MS", 40)
    text_0 = czcionka_2.render("0", False, (255, 170, 170))
    text_1 = czcionka_2.render("1", False, BLACK)
    text_2 = czcionka_2.render("2", False, (255, 170, 170))
    text_3 = czcionka_2.render("3", False, (255, 170, 170))
    text_4 = czcionka_2.render("4", False, BLACK)
    text_5 = czcionka_2.render("5", False, (255, 170, 170))
    text_6 = czcionka_2.render("6", False, (255, 170, 170))
    text_7 = czcionka_2.render("7", False, (255, 170, 170))
    text_8 = czcionka_2.render("8", False, BLACK)
    text_9 = czcionka_2.render("9", False, BLACK)
    text_eraser = czcionka_2.render("*", False, BLACK)
    text_death = czcionka_4.render("DEATH", False, WHITE)
    ii_2 = czcionka_3.render("Can you or your homies do it better?!", False, BLACK)

# Images
    background = pygame.image.load("assets/7.png").convert()
    victory_screen = pygame.image.load("assets/victory_s.png").convert_alpha()
    go_screen = pygame.image.load("assets/game_over_s.png").convert_alpha()
    youtube_img = pygame.image.load("assets/Jutuba_bandycka.png").convert_alpha()
    youtube_img = pygame.transform.scale(youtube_img, (120, 120))
    github_img = pygame.image.load("assets/GitHubert.png").convert_alpha()
    github_img = pygame.transform.scale(github_img, (120, 120))
    tweet_img = pygame.image.load("assets/tweet_img.png").convert_alpha()
    tweet_img = pygame.transform.scale(tweet_img, (420, 243))
    replay_button_img = pygame.image.load("assets/replay_button_png.png").convert_alpha()
    replay_button_img = pygame.transform.scale(replay_button_img, (200, 200))
    obamahavedih = pygame.image.load("assets/obamahavedih.png")
    obamahavedih = pygame.transform.scale(obamahavedih, (283, 283))
    trollface_img = pygame.image.load("assets/trollface.png")
    trollface_img = pygame.transform.scale(trollface_img, (283, 283))
    panik_img = pygame.image.load("assets/panik.png")
    panik_img = pygame.transform.scale(panik_img, (283, 283))
    jumpscare_img = pygame.image.load("assets/jumpscare.png")
    jumpscare_img = pygame.transform.scale(jumpscare_img, (1080, 1080))
    img_1 = pygame.image.load("assets/1_img.png").convert_alpha()
    img_1 = pygame.transform.scale(img_1, (206, 243))
    img_2 = pygame.image.load("assets/2_img.png").convert_alpha()
    img_2 = pygame.transform.scale(img_2, (111, 181))
    img_3 = pygame.image.load("assets/3_img.png").convert_alpha()
    img_3 = pygame.transform.scale(img_3, (103, 196))
    img_4 = pygame.image.load("assets/4_img.png").convert_alpha()
    img_4 = pygame.transform.scale(img_4, (160, 261))
    img_5 = pygame.image.load("assets/5_img.png").convert_alpha()
    img_5 = pygame.transform.scale(img_5, (103, 177))
    img_6 = pygame.image.load("assets/6_img.png").convert_alpha()
    img_6 = pygame.transform.scale(img_6, (131, 188))
    img_7 = pygame.image.load("assets/7_img.png").convert_alpha()
    img_7 = pygame.transform.scale(img_7, (131, 186))
    img_8 = pygame.image.load("assets/8_img.png").convert_alpha()
    img_8 = pygame.transform.scale(img_8, (240, 244))
    img_9 = pygame.image.load("assets/9_img.png").convert_alpha()
    img_9 = pygame.transform.scale(img_9, (205, 205))
    img_10 = pygame.image.load("assets/10_img.png").convert_alpha()
    img_10 = pygame.transform.scale(img_10, (240, 280))
    img_11 = pygame.image.load("assets/11_img.png").convert_alpha()
    img_11 = pygame.transform.scale(img_11, (240, 280))

    listahh = [obamahavedih, trollface_img, panik_img]
    imageahh = random.choice(listahh)

# Sounds
    pygame.mixer.init()
    goofy_piano = pygame.mixer.Sound("assets/goofy_piano.ogg")
    goofy_piano.set_volume(0.3)
    keypad_sound = pygame.mixer.Sound("assets/keypad.ogg")
    keypad_sound.set_volume(0.7)
    good_sound = pygame.mixer.Sound("assets/good.ogg")
    good_sound.set_volume(0.7)
    explosion_sound = pygame.mixer.Sound("assets/explosion.ogg")
    explosion_sound.set_volume(0.2)

# Key buttons
    o_1 = (110, 425, 100, 100)
    o_2 = (260, 425, 100, 100)
    o_3 = (410, 425, 100, 100)
    o_4 = (110, 550, 100, 100)
    o_5 = (260, 550, 100, 100)
    o_6 = (410, 550, 100, 100)
    o_7 = (110, 675, 100, 100)
    o_8 = (260, 675, 100, 100)
    o_9 = (410, 675, 100, 100)
    o_10 = (110, 800, 100, 100)
    o_11 = (260, 800, 100, 100)
    o_12 = (410, 800, 100, 100)

    os = [o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8, o_9, o_10, o_11, o_12]

    r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12 = random.sample(os, 12)

    key_0 = pygame.Rect(r_1)
    key_0_value = False

    key_1 = pygame.Rect(r_2)
    key_1_value = False

    key_2 = pygame.Rect(r_3)
    key_2_value = False

    key_3 = pygame.Rect(r_4)
    key_3_value = False

    key_4 = pygame.Rect(r_5)
    key_4_value = False

    key_5 = pygame.Rect(r_6)
    key_5_value = False

    key_6 = pygame.Rect(r_7)
    key_6_value = False

    key_7 = pygame.Rect(r_8)
    key_7_value = False

    key_8 = pygame.Rect(r_9)
    key_8_value = False

    key_9 = pygame.Rect(r_10)
    key_9_value = False

    key_eraser = pygame.Rect(r_11)
    key_eraser_value = False

    dead_key = pygame.Rect(r_12)
    dead_key_value = False

# Info screens
    class V_Screen:
        def __init__(self, x, y):
            self.image = victory_screen
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.show = False
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    v_screen = V_Screen(0, 0)

    class GOS:
        def __init__(self, x, y):
            self.image = go_screen
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.show = False
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    gos = GOS(0, 0)

# Buttons
    class YouTube:
        def __init__(self, x, y):
            self.image = youtube_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    YT = YouTube(712, 850)

    class GitHub:
        def __init__(self, x, y):
            self.image = github_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    GitHub = GitHub(857, 850)

    class Twitter:
        def __init__(self, x, y):
            self.image = tweet_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.show = False
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    Twitter = Twitter(200, 850)

    class Replay:
        def __init__(self, x, y):
            self.image = replay_button_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.show = False
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    Replay = Replay(670, 865)

# Goofy
    class Goofy:
        def __init__(self, x, y):
            self.image = imageahh
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.show = False
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    Goofy = Goofy(705, 477)

    class Jumpscare:
        def __init__(self, x, y):
            self.image = jumpscare_img
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.show = False
            self.clicked = False

        def draw(self):
            screen.blit(self.image, (self.rect.x, self.rect.y))

    Jumpscare = Jumpscare(0, 0)

# Game loop
    running = True
    while running:
        current = pygame.time.get_ticks()

        screen.blit(background, (0, 0))

        YT.draw()
        GitHub.draw()

        if sys.platform == "emscripten":
            platform.window.canvas.style.imageRendering = "pixelated"

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if not game_finished or not gos.show:
                if timer_number > 0 and (current - abb >= timer_ms):
                    timer_number -= 1
                    abb = current

                    o_1 = (110, 425, 100, 100)
                    o_2 = (260, 425, 100, 100)
                    o_3 = (410, 425, 100, 100)
                    o_4 = (110, 550, 100, 100)
                    o_5 = (260, 550, 100, 100)
                    o_6 = (410, 550, 100, 100)
                    o_7 = (110, 675, 100, 100)
                    o_8 = (260, 675, 100, 100)
                    o_9 = (410, 675, 100, 100)
                    o_10 = (110, 800, 100, 100)
                    o_11 = (260, 800, 100, 100)
                    o_12 = (410, 800, 100, 100)

                    os = [o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8, o_9, o_10, o_11, o_12]

                    r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12 = random.sample(os, 12)

                    key_0 = pygame.Rect(r_1)
                    key_0_value = False

                    key_1 = pygame.Rect(r_2)
                    key_1_value = False

                    key_2 = pygame.Rect(r_3)
                    key_2_value = False

                    key_3 = pygame.Rect(r_4)
                    key_3_value = False

                    key_4 = pygame.Rect(r_5)
                    key_4_value = False

                    key_5 = pygame.Rect(r_6)
                    key_5_value = False

                    key_6 = pygame.Rect(r_7)
                    key_6_value = False

                    key_7 = pygame.Rect(r_8)
                    key_7_value = False

                    key_8 = pygame.Rect(r_9)
                    key_8_value = False

                    key_9 = pygame.Rect(r_10)
                    key_9_value = False

                    key_eraser = pygame.Rect(r_11)
                    key_eraser_value = False

                    dead_key = pygame.Rect(r_12)
                    dead_key_value = False

            if len(user_input) > limit:
                user_input = user_input[:-1]

# Key buttons
            if not gos.show and not game_finished:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if YT.rect.collidepoint(event.pos):
                        YT.clicked = True
                        webbrowser.open("https://youtube.com/@REParadoxy?sub_confirmation=1")
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        YT.clicked = False

                    if GitHub.rect.collidepoint(event.pos):
                        GitHub.clicked = True
                        webbrowser.open("https://github.com/Rubinoslaw/Last-Internet-Connection")
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        GitHub.clicked = False

                    if key_0.collidepoint(event.pos):
                        key_0_value = True
                        user_input += "0"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_0_value = False

                    if key_1.collidepoint(event.pos):
                        key_1_value = True
                        user_input += "1"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_1_value = False

                    if key_2.collidepoint(event.pos):
                        key_2_value = True
                        user_input += "2"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_2_value = False

                    if key_3.collidepoint(event.pos):
                        key_3_value = True
                        user_input += "3"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_3_value = False

                    if key_4.collidepoint(event.pos):
                        key_4_value = True
                        user_input += "4"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_4_value = False

                    if key_5.collidepoint(event.pos):
                        key_5_value = True
                        user_input += "5"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_5_value = False

                    if key_6.collidepoint(event.pos):
                        key_6_value = True
                        user_input += "6"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_6_value = False

                    if key_7.collidepoint(event.pos):
                        key_7_value = True
                        user_input += "7"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_7_value = False

                    if key_8.collidepoint(event.pos):
                        key_8_value = True
                        user_input += "8"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_8_value = False

                    if key_9.collidepoint(event.pos):
                        key_9_value = True
                        user_input += "9"
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_9_value = False

                    if key_eraser.collidepoint(event.pos):
                        key_eraser_value = True
                        user_input = user_input[:-1]
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        key_eraser_value = False

                    if dead_key.collidepoint(event.pos):
                        dead_key_value = True
                        timer_number = 0
                        pygame.mixer.Sound.play(keypad_sound, 0)
                    else:
                        dead_key_value = False

            if gos.show:
                pygame.mixer.Sound.play(explosion_sound, 0)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Replay.rect.collidepoint(event.pos):
                        Replay.clicked = True
                        if Replay.clicked:
                            password = random.randint(10000000, 99999999)
                            password = str(password)
                            listahh = [obamahavedih, trollface_img, panik_img]
                            imageahh = random.choice(listahh)
                            elon = [5, 7, 10]
                            heh = random.choice(elon)
                            son = [1, 2, 4, 6]
                            sonion = random.choice(son)
                            user_input = ""
                            Replay.show = False
                            Jumpscare.clicked = False
                            Goofy.clicked = False
                            gos.show = False
                            timer_number = 11
                    else:
                        Replay.clicked = False
                        timer_number = 0

            if v_screen.show:
                game_finished = True
                pygame.mixer.Sound.play(good_sound, 0)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Replay.rect.collidepoint(event.pos):
                        Replay.clicked = True
                        if Replay.clicked:
                            password = random.randint(10000000, 99999999)
                            password = str(password)
                            listahh = [obamahavedih, trollface_img, panik_img]
                            imageahh = random.choice(listahh)
                            elon = [5, 7, 10]
                            heh = random.choice(elon)
                            son = [1, 2, 4, 6]
                            sonion = random.choice(son)
                            user_input = ""
                            Replay.show = False
                            v_screen.show = False
                            timer_number = 11
                            Jumpscare.clicked = False
                            Goofy.clicked = False
                            game_finished = False
                    else:
                        Replay.clicked = False

            if Twitter.show and v_screen.show:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Twitter.rect.collidepoint(event.pos):
                        Twitter.clicked = True
                        webbrowser.open(f"https://x.com/intent/post?text=I+saved+my+life+{score}+seconds+before+it+ended%21+%F0%9F%94%8B%F0%9F%94%8B%F0%9F%94%8B+%23LastInternetConnection+https%3A%2F%2Freparadoxy.itch.io%2Flast-internet-connection%20")
                    else:
                        Twitter.clicked = False

            if Twitter.show and gos.show:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Twitter.rect.collidepoint(event.pos):
                        Twitter.clicked = True
                        webbrowser.open("https://x.com/intent/post?text=Nope+%23LastInternetConnection+https%3A%2F%2Freparadoxy.itch.io%2Flast-internet-connection%20")
                    else:
                        Twitter.clicked = False

            if Goofy.show:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Goofy.rect.collidepoint(event.pos):
                        Goofy.clicked = True
                        Goofy.show = False
                    else:
                        Jumpscare.clicked = False

            if Jumpscare.show:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if Jumpscare.rect.collidepoint(event.pos):
                        Jumpscare.clicked = True
                        Jumpscare.show = False
                    else:
                        Jumpscare.clicked = False

        if not key_0_value:
            pygame.draw.rect(screen, RED, key_0)
        else:
            pygame.draw.rect(screen, MAROON, key_0)

        if not key_1_value:
            pygame.draw.rect(screen, YELLOW, key_1)
        else:
            pygame.draw.rect(screen, GOLD, key_1)

        if not key_2_value:
            pygame.draw.rect(screen, BLUE, key_2)
        else:
            pygame.draw.rect(screen, ROYAL_BLUE, key_2)

        if not key_3_value:
            pygame.draw.rect(screen, GOLD, key_3)
        else:
            pygame.draw.rect(screen, OLIVE, key_3)

        if not key_4_value:
            pygame.draw.rect(screen, VIOLET, key_4)
        else:
            pygame.draw.rect(screen, PINK, key_4)

        if not key_5_value:
            pygame.draw.rect(screen, GREY, key_5)
        else:
            pygame.draw.rect(screen, DARK_GREY, key_5)

        if not key_6_value:
            pygame.draw.rect(screen, MEDIUM_BLUE, key_6)
        else:
            pygame.draw.rect(screen, INDIGO, key_6)

        if not key_7_value:
            pygame.draw.rect(screen, REBECCA_PURPLE, key_7)
        else:
            pygame.draw.rect(screen, PURPLE, key_7)

        if not key_8_value:
            pygame.draw.rect(screen, TAN, key_8)
        else:
            pygame.draw.rect(screen, DARK_TAN, key_8)

        if not key_9_value:
            pygame.draw.rect(screen, CYAN, key_9)
        else:
            pygame.draw.rect(screen, DARK_CYAN, key_9)

        if not key_eraser_value:
            pygame.draw.rect(screen, CORAL, key_eraser)
        else:
            pygame.draw.rect(screen, CHOCOLATE, key_eraser)

        if not dead_key_value:
            pygame.draw.rect(screen, BLACK, dead_key)
        else:
            pygame.draw.rect(screen, WHITE, dead_key)

# Texts
        screen.blit(text_0, r_1)
        screen.blit(text_1, r_2)
        screen.blit(text_2, r_3)
        screen.blit(text_3, r_4)
        screen.blit(text_4, r_5)
        screen.blit(text_5, r_6)
        screen.blit(text_6, r_7)
        screen.blit(text_7, r_8)
        screen.blit(text_8, r_9)
        screen.blit(text_9, r_10)
        screen.blit(text_eraser, r_11)
        screen.blit(text_death, r_12)
        password_text = czcionka.render(str(password), False, GREEN)
        screen.blit(password_text, (725, 570))
        show = czcionka_2.render(user_input, False, GREEN)
        screen.blit(show, (77, 250))

        a_a = random.randint(80, 490)
        a_b = random.randint(239, 330)

        b_a = random.randint(80, 490)
        b_b = random.randint(239, 330)

        c_a = random.randint(80, 490)
        c_b = random.randint(239, 330)

        d_a = random.randint(80, 490)
        d_b = random.randint(239, 330)

        e_a = random.randint(80, 490)
        e_b = random.randint(239, 330)

        f_a = random.randint(80, 490)
        f_b = random.randint(239, 330)

        g_a = random.randint(80, 490)
        g_b = random.randint(239, 330)

        h_a = random.randint(80, 490)
        h_b = random.randint(239, 330)

        i_a = random.randint(80, 490)
        i_b = random.randint(239, 330)

        j_a = random.randint(80, 490)
        j_b = random.randint(239, 330)

        k_a = random.randint(80, 490)
        k_b = random.randint(239, 330)

        l_a = random.randint(80, 490)
        l_b = random.randint(239, 330)

        m_a = random.randint(80, 490)
        m_b = random.randint(239, 330)

        n_a = random.randint(80, 490)
        n_b = random.randint(239, 330)

        o_a = random.randint(80, 490)
        o_b = random.randint(239, 330)

        p_a = random.randint(80, 490)
        p_b = random.randint(239, 330)

        r_a = random.randint(80, 490)
        r_b = random.randint(239, 330)

        a_noise = pygame.Rect(a_a, a_b, 23, 23)
        b_noise = pygame.Rect(b_a, b_b, 23, 23)
        c_noise = pygame.Rect(c_a, c_b, 23, 23)
        d_noise = pygame.Rect(d_a, d_b, 23, 23)
        e_noise = pygame.Rect(e_a, e_b, 23, 23)
        f_noise = pygame.Rect(f_a, f_b, 23, 23)
        g_noise = pygame.Rect(g_a, g_b, 23, 23)
        h_noise = pygame.Rect(h_a, h_b, 23, 23)
        i_noise = pygame.Rect(i_a, i_b, 23, 23)
        j_noise = pygame.Rect(j_a, j_b, 23, 23)
        k_noise = pygame.Rect(k_a, k_b, 23, 23)
        l_noise = pygame.Rect(l_a, l_b, 23, 23)
        m_noise = pygame.Rect(m_a, m_b, 23, 23)
        n_noise = pygame.Rect(n_a, n_b, 23, 23)
        o_noise = pygame.Rect(o_a, o_b, 23, 23)
        p_noise = pygame.Rect(p_a, p_b, 23, 23)
        r_noise = pygame.Rect(r_a, r_b, 23, 23)

        pygame.draw.rect(screen, RED, a_noise)
        pygame.draw.rect(screen, GREEN, b_noise)
        pygame.draw.rect(screen, YELLOW, c_noise)
        pygame.draw.rect(screen, GOLD, d_noise)
        pygame.draw.rect(screen, BLUE, e_noise)
        pygame.draw.rect(screen, CORAL, f_noise)
        pygame.draw.rect(screen, LIME, g_noise)
        pygame.draw.rect(screen, MEDIUM_BLUE, h_noise)
        pygame.draw.rect(screen, ORANGE, i_noise)
        pygame.draw.rect(screen, GREY, j_noise)
        pygame.draw.rect(screen, RED, k_noise)
        pygame.draw.rect(screen, GREEN, l_noise)
        pygame.draw.rect(screen, YELLOW, m_noise)
        pygame.draw.rect(screen, CHOCOLATE, n_noise)
        pygame.draw.rect(screen, BLUE, o_noise)
        pygame.draw.rect(screen, CYAN, p_noise)
        pygame.draw.rect(screen, DARK_CYAN, r_noise)

        if timer_number == 0 and user_input != password:
            gos.show = True

        if user_input == password:
            v_screen.show = True

        if not game_finished and timer_number == 11:
            screen.blit(img_11, (637, 165))
            score = 11

        if not game_finished and timer_number == 10:
            screen.blit(img_10, (635, 170))
            score = 10

        if not game_finished and timer_number == 9:
            screen.blit(img_9, (655, 200))
            score = 9

        if not game_finished and timer_number == 8:
            screen.blit(img_8, (640, 205))
            score = 8

        if not game_finished and timer_number == 7:
            screen.blit(img_7, (690, 205))
            score = 7

        if not game_finished and timer_number == 6:
            screen.blit(img_6, (690, 210))
            score = 6

        if not game_finished and timer_number == 5:
            screen.blit(img_5, (705, 212))
            score = 5

        if not game_finished and timer_number == 4:
            screen.blit(img_4, (690, 207))
            score = 4

        if not game_finished and timer_number == 3:
            screen.blit(img_3, (705, 207))
            score = 3

        if not game_finished and timer_number == 2:
            screen.blit(img_2, (700, 212))
            score = 2

        if not game_finished and timer_number == 1:
            screen.blit(img_1, (655, 210))
            score = 1

        if not game_finished and timer_number == 0:
            score = 0

        if Goofy.show:
            Goofy.draw()

        if Jumpscare.show:
            Jumpscare.draw()

        if timer_number == heh and not Goofy.clicked:
            Goofy.show = True
            if Goofy.show:
                pygame.mixer.Sound.play(goofy_piano, 0)
        else:
            Goofy.show = False

        if timer_number == sonion and not Jumpscare.clicked:
            Jumpscare.show = True
            pygame.mixer.Sound.play(goofy_piano, 0)
        else:
            Jumpscare.show = False

        if v_screen.show:
            v_screen.draw()

        if game_finished:
            Goofy.show = False
            ii_1 = czcionka_3.render(f"Score: {score} seconds before the death!", False, BLACK)
            screen.blit(ii_1, (200, 780))
            screen.blit(ii_2, (200, 830))
            Twitter.show = True
            Twitter.draw()
            Replay.show = True
            Replay.draw()

        if gos.show:
            Goofy.show = False
            gos.draw()
            screen.blit(ii_2, (200, 780))
            Twitter.show = True
            Twitter.draw()
            Replay.show = True
            Replay.draw()

        clock.tick(FPS)

        pygame.display.flip()

        await asyncio.sleep(0)

asyncio.run(main())