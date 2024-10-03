from .initialize import *
import random
import time

# Array of numbers, for now creating a random array of size 10
array = []
for i in range(10):
    array.append(random.randint(0,150))
# Array of array for storing resultant array after all passes
array_pass=[array.copy()]


# centering array on x and y axis and finding their starting coordinate
start_x = (SCREEN_WIDTH - (BLOCK_SIZE*len(array) + SPACING*(len(array)-1))) // 2
start_y = (SCREEN_HEIGHT - BLOCK_SIZE) // 2
start_x_small=(SCREEN_WIDTH - (SMALL_BLOCK_SIZE*len(array) + SPACING*(len(array)-1))) // 2

#array randomizer
def arrRandomize():
    for i in range(10):
        array[i]=random.randint(0,150)


def swap_blocks(curr_pass,a, b):
    # No need to swap
    if a==b:
        return 

    # Constants needed for swapping
    loopsNeeded=((b-a)*(SPACING+BLOCK_SIZE) + 200)  # 100 up and 100 down
    ay=start_y
    by=start_y
    ax=start_x + a*(BLOCK_SIZE+ SPACING)
    bx=start_x + b*(BLOCK_SIZE+ SPACING)
    time.sleep(WAIT)

    for i in range(loopsNeeded):
        screen.fill(BACKGROUND_COLOR)
        text=font.render("Pass: %d"%(curr_pass),True,TEXT_COLOR)
        text_rect=text.get_rect(center=(SCREEN_WIDTH//2,100))
        screen.blit(text,text_rect)

        # Calculate the position for each block
        for index, number in enumerate(array):
            x = start_x + index * (BLOCK_SIZE + SPACING)
            y = start_y
            if(index!=a and index!=b):
                # Draw the block
                pygame.draw.rect(screen, BLOCK_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        
                # Render the number
                text = font.render(str(number), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + BLOCK_SIZE // 2, y + BLOCK_SIZE // 2))
                screen.blit(text, text_rect)
            elif(index==a):
                if(i<100):
                    ay+=1
                elif(loopsNeeded-i<100):
                    ay-=1
                else:
                    ax+=1
                pygame.draw.rect(screen, GREEN, (ax, ay, BLOCK_SIZE, BLOCK_SIZE))
        
                # Render the number
                text = font.render(str(number), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(ax + BLOCK_SIZE // 2, ay + BLOCK_SIZE // 2))
                screen.blit(text, text_rect)
            else:
                if(i<100):
                    by-=1
                elif(loopsNeeded-i<100):
                    by+=1
                else:
                    bx-=1
                pygame.draw.rect(screen, GREEN, (bx, by, BLOCK_SIZE, BLOCK_SIZE))
        
                # Render the number
                text = font.render(str(number), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(bx + BLOCK_SIZE // 2, by + BLOCK_SIZE // 2))
                screen.blit(text, text_rect)

        pygame.display.flip()
    # swapping a and b
    array[a],array[b]=array[b],array[a]
        