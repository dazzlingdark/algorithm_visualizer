from src.utils import *

def bubbleSort():
    n=len(array)
    total_step=n*(n-1)/2
    count=0
    curr_pass=1
    step=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_RETURN or event.key== pygame.K_SPACE:
                    if(array[step]>array[step+1]):
                        swap_blocks(curr_pass,step,step+1)
                    step+=1
                    count+=1
                    if(step>n-1-curr_pass):
                        step=0
                        array_pass.append(array.copy())
                        curr_pass+=1
                              
        draw_blocks_bubble(curr_pass,step,step+1)
        if(count==total_step):
            break
    #displaying final sorted array
    sorted_array_display_bubble()
    
    #randomizing array again        
    arrRandomize()       
           
def draw_blocks_bubble(curr_pass,highlight1,highlight2):
    n=len(array)
    screen.fill(BACKGROUND_COLOR)
    # instruction to press enter
    instruction=font_small.render("Press Enter or Space key for next step",True,TEXT_COLOR)
    instruction_rect=instruction.get_rect(center=(SCREEN_WIDTH//2,50))
    screen.blit(instruction,instruction_rect)
    # title
    title=font_title.render("Bubble Sort",True,VIOLET)
    title_rect=title.get_rect(center=(SCREEN_WIDTH//2,100))
    screen.blit(title,title_rect)

    # Pass number display
    text=font.render("Pass: %d"%(curr_pass),True,TEXT_COLOR)
    text_rect=text.get_rect(center=(SCREEN_WIDTH//2,150))
    screen.blit(text,text_rect)

    #Symbols meaning
    pygame.draw.rect(screen,CRIMSON,(100,SCREEN_HEIGHT-100,BLOCK_SIZE,BLOCK_SIZE))
    compared=font.render("Compare",True,TEXT_COLOR)
    compared_rect=compared.get_rect(center=(100+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(compared,compared_rect)

    pygame.draw.rect(screen,BLOCK_COLOR,(SCREEN_WIDTH//2-BLOCK_SIZE//2,SCREEN_HEIGHT-100,BLOCK_SIZE,BLOCK_SIZE))
    unsorted_part=font.render("Unsorted",True,TEXT_COLOR)
    unsorted_part_rect=compared.get_rect(center=(600,SCREEN_HEIGHT-150))
    screen.blit(unsorted_part,unsorted_part_rect)

    pygame.draw.rect(screen,GOLD,(SCREEN_WIDTH-100-BLOCK_SIZE,SCREEN_HEIGHT-100,BLOCK_SIZE,BLOCK_SIZE))
    sorted_part=font.render("Sorted",True,TEXT_COLOR)
    sorted_part_rect=compared.get_rect(center=(SCREEN_WIDTH-120,SCREEN_HEIGHT-150))
    screen.blit(sorted_part,sorted_part_rect)
    
    # Calculate the position for each block
    for index, number in enumerate(array):
        x = start_x + index * (BLOCK_SIZE + SPACING)
        y = start_y
        
        # Draw the block
        if(index==highlight1 or index==highlight2):
            pygame.draw.rect(screen, CRIMSON, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        elif index>n-curr_pass:
            pygame.draw.rect(screen, GOLD, (x, y, BLOCK_SIZE, BLOCK_SIZE))

        else:
            pygame.draw.rect(screen, BLOCK_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))

        # Render the number
        text = font.render(str(number), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(x + BLOCK_SIZE // 2, y + BLOCK_SIZE // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

def sorted_array_display_bubble():
    condition=True
    while condition:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_RETURN or event.key==pygame.K_SPACE:
                    condition=False

        screen.fill(BACKGROUND_COLOR)
        #Displaying array after every pass
        y=30
        for i in range(len(array_pass)):
            array_curr=array_pass[i] 
            curr_pass="Pass %d"%(i)
            if(i==0):
                curr_pass="Initial Array"
            # Displaying pass
            text=font_small.render(curr_pass,True,TEXT_COLOR)
            text_rect=text.get_rect(center=(start_x_small-100,y+SMALL_BLOCK_SIZE//2))
            screen.blit(text,text_rect)

            for index, number in enumerate(array_curr):
                # Draw the block
                x = start_x_small + index * (SMALL_BLOCK_SIZE + SPACING)
                color=BLOCK_COLOR
                if(index>=len(array_curr)-i):
                    color=GOLD
                pygame.draw.rect(screen, color, (x, y, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
                # Render the number
                text = font_small.render(str(number), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + SMALL_BLOCK_SIZE // 2, y + SMALL_BLOCK_SIZE // 2))
                screen.blit(text, text_rect)
            y+=70

        pygame.display.flip()            

