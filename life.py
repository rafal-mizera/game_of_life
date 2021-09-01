import pygame
import sys
from pygame.locals import * # udostepnienie nazw metod z locals

pygame.init()

# ustalenie szerokości i wysokości okna gry
window_w = 800
window_h = 400

#inicjacja okna gry
game_window = pygame.display.set_mode((window_w,window_h),0,32)
#tytuł oraz ikona okna gry
pygame.display.set_caption("Game of life")
icon = pygame.image.load("game_tetris_game_blocks_casual_icon_133760.png")
pygame.display.set_icon(icon)
#rozmiar komórki oraz ilość w pionie i poziomie
cell_size = 10
cells_w = int(window_w/cell_size)
cells_h = int(window_h/cell_size)
# ustalenie wartości żywych i martwych komórek
dead = 0
alive = 1
game_field = [dead] * cells_w
for i in range(cells_w):
    game_field[i] = [dead] * cells_h


def prepare_population(gamefield):
    #przygotowanie nastepnej populacji komorek, analogicznie jak wyzej
    next_gen = [dead] * cells_w
    for i in range(cells_w):
        next_gen[i] = [dead] * cells_h

    #nastepnie iteracja po kazdej z komorek
    for i in range(cells_h):
        for j in range(cells_w):
            #zliczenie zywych sasiadow
            neighbours_alive = 0
            try:
                if gamefield[j-1][i-1] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j][i-1] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j+1][i-1] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j-1][i] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j+1][i] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j-1][i+1] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j][i+1] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass
            try:
                if gamefield[j+1][i+1] == alive:
                    neighbours_alive += 1
            except IndexError:
                pass


            #niedoludnienie/przeludnienie bedzie skutkowac smiercia komorki
            if gamefield[j][i] == alive and (neighbours_alive < 2 or neighbours_alive > 3):
                next_gen[j][i] = dead
            if gamefield[j][i] == alive and (neighbours_alive == 2 or neighbours_alive == 3):
                next_gen[j][i] = alive
            elif gamefield[j][i] == dead and neighbours_alive == 3:
                next_gen[j][i] = alive



    #zwraca pole gry nastepnej generacji komorek
    return next_gen

def draw_population():
    #rysowanie zywych komorek na planszy
    for x in range(cells_w):
        for y in range(cells_h):
            if game_field[x][y] == alive:
                pygame.draw.rect(game_window, (255, 0, 255), Rect((x * cell_size, y * cell_size), (cell_size, cell_size)), 1)



#zmienne sterujące wykorzystane w pętli głównej
life_goes = False
down_button = False

#główna pętla
while True:
    for event in pygame.event.get():
        #przechwycenie zamknięcia okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RETURN:
            life_goes = True

        if life_goes is False:
            if event.type == MOUSEBUTTONDOWN:
                down_button = True
                button_type = event.button
            if event.type == MOUSEBUTTONUP:
                down_button = False
            if down_button:
                mouse_j, mouse_i = pygame.mouse.get_pos()
                mouse_j = int(mouse_j / cell_size)
                mouse_i = int(mouse_i / cell_size)
            #lewy przycisk ożywia komórkę
                if button_type == 1:
                    game_field[mouse_j][mouse_i] = alive
            #prawy uśmierca
                if button_type == 3:
                    game_field[mouse_j][mouse_i] = dead

    if life_goes is True:
        game_field = prepare_population(game_field)


    game_window.fill((0,0,0)) # kolor pola gry
    draw_population()
    pygame.display.update()
    pygame.time.delay(100)







