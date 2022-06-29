# MazeWar Project - File 2
# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]

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
f_characters = join(images_folder, 'Characters')
f_music = join(sounds_folder, 'Music')
f_sfx = join(sounds_folder, 'SFX')
f_pause = join(f_menu, 'Pause')
f_howToPlay = join(f_menu, 'How_To_Play')
f_credits = join(f_menu, 'Credits')

# ---------- Base screen creation

CLOCK = Clock()
FPS = 60
DEFAULT_SCREEN = set_mode((600, 600))
set_caption('MazeWar [0.5] - Developer Version')
set_icon(load(join(images_folder, 'icon.png')).convert_alpha())

# ---------- Maze Defaults / Grid and Cell's Default Settings ( 20 )

cell_size = 20
cell_wall_size = cell_size//4
rows = DEFAULT_SCREEN.get_width()//cell_size
cols = DEFAULT_SCREEN.get_height()//cell_size

# ---------- Assets creation - images

imgCursor = scale(load(join(f_menu, 'Cursor.png')).convert_alpha(), (50, 47))

bgMainMenu = load(join(f_backgrounds, 'BG_MainMenu.png')).convert_alpha()
bgGameOver = load(join(f_backgrounds, 'BG_GameOver.png')).convert_alpha()
bgCredits = load(join(f_backgrounds, 'BG_Credits.png')).convert_alpha()
bgHowToPlay = load(join(f_backgrounds, 'BG_HowToPlay.png')).convert_alpha()
bgSettings = load(join(f_backgrounds, 'BG_Settings.png')).convert_alpha()
bgAlgorithms = load(join(f_backgrounds, 'BG_PlayAlgorithms.png')).convert_alpha()
bgCellSize = load(join(f_backgrounds, 'BG_PlayCellSize.png')).convert_alpha()
bgVisualMode = load(join(f_backgrounds, 'BG_VisualMode.png')).convert_alpha()
bgDifficulty = load(join(f_backgrounds, 'BG_Difficulty.png')).convert_alpha()

ftPause = load(join(f_pause, 'Image_pause.png')).convert_alpha()
ftCredits = load(join(f_backgrounds, 'FT_Credits.png')).convert_alpha()

imgCredits = load(join(f_credits, 'Credits_Image.png')).convert_alpha()
imgHowToPlay = load(join(f_howToPlay, 'How_To_Play.png')).convert_alpha()
imgLoadingScreen = load(join(f_backgrounds, 'IMG_LoadingScreen.png')).convert_alpha()
imgMazeReady = load(join(f_backgrounds, 'IMG_MazeReady.png')).convert_alpha()

spPlayer = load(join(f_characters, 'sp_Player.png')).convert_alpha()
spEnemy1 = load(join(f_characters, 'sp_Enemy1.png')).convert_alpha()
spEnemy2 = load(join(f_characters, 'sp_Enemy2.png')).convert_alpha()
spEnemy3 = load(join(f_characters, 'sp_Enemy3.png')).convert_alpha()

# ---------- Assets creation - sounds

init()
sfxButtonClick = Sound(join(f_sfx, 'Button_Click.ogg'))
