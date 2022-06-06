
# OS [ https://docs.python.org/3/library/os.html ]
# Pygame [ https://www.pygame.org/docs/ ]

from os.path import join, dirname
from pygame.mixer import Sound, init
from pygame.display import set_caption, set_icon, set_mode
from pygame.time import Clock
from pygame.image import load
from pygame.transform import scale

# ---------- Directory creation

game_folder = dirname(__file__)
images_folder = join(game_folder, 'Pixel_Art')
sounds_folder = join(game_folder, 'Sounds')
f_menu = join(images_folder, 'Menu')
f_backgrounds = join(images_folder, 'Backgrounds')
f_music = join(sounds_folder, 'Music')
f_sfx = join(sounds_folder, 'SFX')
f_pause = join(f_menu, 'Pause')
f_gameOver = join(f_menu, 'Game_Over')
f_load = join(f_menu, 'Load_Game')
f_howToPlay = join(f_menu, 'How_To_Play')
f_credits = join(f_menu, 'Credits')

# ---------- Base screen creation

CLOCK = Clock()
FPS = 60
Width, Height = 600, 600
SCREEN = set_mode((Width, Height))
set_caption('MazeWar [0.3]')
set_icon(load(join(images_folder, 'icon.png')).convert_alpha())

# ---------- Assets creation - images

imgCursor = scale(load(join(f_menu, 'Cursor.png')).convert_alpha(), (50, 47))

bgMenu = load(join(f_backgrounds, 'BG_Menu.png')).convert_alpha()
bgGameOver = load(join(f_backgrounds, 'BG_Results.png')).convert_alpha()
bgCredits = load(join(f_backgrounds, 'BG_Credits.png')).convert_alpha()
bgPause = load(join(f_backgrounds, 'BG_Pause.png')).convert_alpha()

imgCredits = load(join(f_credits, 'Credits_Image.png')).convert_alpha()
imgHowToPlay = load(join(f_howToPlay, 'How_To_Play.png')).convert_alpha()

# ---------- Assets creation - sounds

init()
sfxButtonClick = Sound(join(f_sfx, 'Button_Click.ogg'))
