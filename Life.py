import pygame
import time
import threading

#Created by Nut-Stack

'''
RULES
1. Each dead cell adjacent to exactly three live neighbors will become alive in the next generation.
2. Each live cell with one or fewer live neighbors will die in the next generation.
3. Each live cell with four or more live neighbors will die in the next generation.
4. If a cell has two or three live neighbors will remain alive in the next generation.

Advance the generation by pressing/holding the spacebar.
'''

pygame.init()
WINDOW_HEIGHT = 1024
WINDOW_WIDTH = 1024
gameDisplay = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption('Conways Game of Life')

crashed = False
x=0
y=0
height = 10
width = 10
BLOCKSIZE = 16
block_list = []
dead_list = []
live_list = []
generated_dead_list = []
xs = []
ys = []
drawn = False

def myround(x, base=BLOCKSIZE):
   return base * round(x/base)
LIVE_COLOR = (255,127,39)
DEAD_COLOR = (5,5,0)
gameDisplay.fill(DEAD_COLOR)



if drawn == False:
    for y1 in range (WINDOW_HEIGHT):
        for x1 in range (WINDOW_WIDTH):
            rect = pygame.Rect(x1*BLOCKSIZE,y1*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE)
            pygame.draw.rect(gameDisplay,LIVE_COLOR,rect,1)
drawn = True
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = (pygame.mouse.get_pos())
                if pos[0] % BLOCKSIZE and pos[1] % BLOCKSIZE:
                    block_to_fill_x = myround(pos[0] - (BLOCKSIZE) * .5) + 1
                    block_to_fill_y = myround(pos[1] - (BLOCKSIZE) * .5) + 1

                    if not [block_to_fill_x,block_to_fill_y] in block_list:
                        pygame.draw.rect(gameDisplay,LIVE_COLOR,(block_to_fill_x,block_to_fill_y,BLOCKSIZE-2,BLOCKSIZE-2))
                        block_list.append([block_to_fill_x,block_to_fill_y])
                    else:
                        pygame.draw.rect(gameDisplay,DEAD_COLOR,(block_to_fill_x,block_to_fill_y,BLOCKSIZE-2,BLOCKSIZE-2))
                        block_list.remove([block_to_fill_x,block_to_fill_y])
                block_list.sort()
                print(block_list)

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE]:

            class Generate_Dead:
                def Generate_X():
                    for i in range(0,WINDOW_WIDTH-BLOCKSIZE-1,BLOCKSIZE):
                        xs.append(i+1)
                def Generate_Y():
                    for i in range(0,WINDOW_WIDTH-BLOCKSIZE-1,BLOCKSIZE):
                        ys.append(i+1)
                def Make_Dead_List():
                    for x in xs:
                        for y in ys:
                            if ([x,y]) not in block_list:
                                generated_dead_list.append([x,y])

            def Kill_Em():
                for block in block_list:

                    Kblock_right = [block[0] + BLOCKSIZE,block[1]]
                    Kblock_left = [block[0] - BLOCKSIZE,block[1]]
                    Kblock_up = [block[0],block[1] - BLOCKSIZE]
                    Kblock_down = [block[0],block[1] + BLOCKSIZE]

                    Kblock_right_up = [block[0] + BLOCKSIZE,block[1] + BLOCKSIZE]
                    Kblock_right_down = [block[0] + BLOCKSIZE,block[1] - BLOCKSIZE]
                    Kblock_left_up = [block[0] - BLOCKSIZE,block[1] - BLOCKSIZE]
                    Kblock_left_down = [block[0] - BLOCKSIZE,block[1] + BLOCKSIZE]


                    Kbool_right = 0
                    Kbool_left = 0
                    Kbool_up = 0
                    Kbool_down = 0
                    Kbool_right_up = 0
                    Kbool_right_down = 0
                    Kbool_left_up = 0
                    Kbool_left_down = 0

                    if Kblock_right in block_list:
                        Kbool_right = 1

                    if Kblock_left in block_list:
                        Kbool_left = 1

                    if Kblock_up in block_list:
                        Kbool_up = 1

                    if Kblock_down in block_list:
                        Kbool_down = 1

                    if Kblock_right_up in block_list:
                        Kbool_right_up = 1

                    if Kblock_right_down in block_list:
                        Kbool_right_down = 1

                    if Kblock_left_up in block_list:
                        Kbool_left_up = 1

                    if Kblock_left_down in block_list:
                        Kbool_left_down = 1

                    bool_KILL_list = [Kbool_right , Kbool_left , Kbool_up , Kbool_down , Kbool_right_up , Kbool_right_down , Kbool_left_up , Kbool_left_down]

                    if (sum(bool_KILL_list)) <= 1:
                        pygame.draw.rect(gameDisplay,DEAD_COLOR,(block[0],block[1],BLOCKSIZE-2,BLOCKSIZE-2))
                        dead_list.append([block[0],block[1]])

                    if (sum(bool_KILL_list)) >= 4:
                        pygame.draw.rect(gameDisplay,DEAD_COLOR,(block[0],block[1],BLOCKSIZE-2,BLOCKSIZE-2))
                        dead_list.append([block[0],block[1]])

            def Give_Life():
                for block in generated_dead_list:
                    Lblock_right = [block[0] + BLOCKSIZE,block[1]]
                    Lblock_left = [block[0] - BLOCKSIZE,block[1]]
                    Lblock_up = [block[0],block[1] - BLOCKSIZE]
                    Lblock_down = [block[0],block[1] + BLOCKSIZE]

                    Lblock_right_up = [block[0] + BLOCKSIZE,block[1] + BLOCKSIZE]
                    Lblock_right_down = [block[0] + BLOCKSIZE,block[1] - BLOCKSIZE]
                    Lblock_left_up = [block[0] - BLOCKSIZE,block[1] - BLOCKSIZE]
                    Lblock_left_down = [block[0] - BLOCKSIZE,block[1] + BLOCKSIZE]

                    Lbool_right = 0
                    Lbool_left = 0
                    Lbool_up = 0
                    Lbool_down = 0
                    Lbool_right_up = 0
                    Lbool_right_down = 0
                    Lbool_left_up = 0
                    Lbool_left_down = 0

                    if Lblock_right in block_list:
                        Lbool_right = 1

                    if Lblock_left in block_list:
                        Lbool_left = 1

                    if Lblock_up in block_list:
                        Lbool_up = 1

                    if Lblock_down in block_list:
                        Lbool_down = 1

                    if Lblock_right_up in block_list:
                        Lbool_right_up = 1

                    if Lblock_right_down in block_list:
                        Lbool_right_down = 1

                    if Lblock_left_up in block_list:
                        Lbool_left_up = 1

                    if Lblock_left_down in block_list:
                        Lbool_left_down = 1

                    bool_CREATE_list = [Lbool_right , Lbool_left , Lbool_up , Lbool_down , Lbool_right_up , Lbool_right_down , Lbool_left_up , Lbool_left_down]

                    if sum(bool_CREATE_list) == 3:
                        pygame.draw.rect(gameDisplay,LIVE_COLOR,(block[0],block[1],BLOCKSIZE-2,BLOCKSIZE-2))
                        live_list.append([block[0],block[1]])

            class Cleanup:
                def Dead_List_Remover():
                    for block in dead_list:
                        block_list.remove(block)
                def Live_List_Appender():
                    for block in live_list:
                        block_list.append(block)
                def List_Demolisher():
                    dead_list.clear()
                    live_list.clear()
                    generated_dead_list.clear()
                    xs.clear()
                    ys.clear()


            t1 = threading.Thread(target = Generate_Dead.Generate_X)
            t2 = threading.Thread(target = Generate_Dead.Generate_Y)
            t3 = threading.Thread(target = Generate_Dead.Make_Dead_List)

            t4 = threading.Thread(target = Kill_Em)
            t5 = threading.Thread(target = Give_Life)

            t6 = threading.Thread(target = Cleanup.Dead_List_Remover)
            t7 = threading.Thread(target = Cleanup.Live_List_Appender)
            t8 = threading.Thread(target = Cleanup.List_Demolisher)

            t1.start()
            t2.start()
            t3.start()

            t4.start()
            t5.start()
            t5.join()

            t6.start()
            t7.start()
            t8.start()
            t8.join()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True

    pygame.display.update()

pygame.quit()
quit()


