from src.utils import *

# Selection sort
def selectionSort():
    n=len(array)
    curr_pass=1
    count=0
    index=1
    total_step=n*(n-1)/2
    curr_min_index=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_RETURN or event.key== pygame.K_SPACE:
                    if(array[index]<array[curr_min_index]):
                        curr_min_index=index
                    index+=1
                    count+=1
                    if(index>n-1):
                        
                        swap_blocks(curr_pass,curr_pass-1,curr_min_index)
                        array_pass.append(array.copy())
                        curr_pass+=1
                        index=curr_pass
                        curr_min_index=curr_pass-1

        if(count==total_step or index>n-1):
            break    
        draw_blocks_selection(curr_pass,curr_min_index,index)
       
    #displaying final sorted array
    sorted_array_display_selection()
    
    #randomizing array again        
    arrRandomize() 


def draw_blocks_selection(curr_pass,highlight1,highlight2):
    screen.fill(BACKGROUND_COLOR)
    # instruction to press enter
    instruction=font_small.render("Press Enter or Space key for next step",True,TEXT_COLOR)
    instruction_rect=instruction.get_rect(center=(SCREEN_WIDTH//2,50))
    screen.blit(instruction,instruction_rect)
    # title
    title=font_title.render("Selection Sort",True,VIOLET)
    title_rect=title.get_rect(center=(SCREEN_WIDTH//2,100))
    screen.blit(title,title_rect)

    # Pass number display
    text=font.render("Pass: %d"%(curr_pass),True,TEXT_COLOR)
    text_rect=text.get_rect(center=(SCREEN_WIDTH//2,150))
    screen.blit(text,text_rect) 

    #Symbols meaning
    pygame.draw.rect(screen,CRIMSON,(80,SCREEN_HEIGHT-100,BLOCK_SIZE,BLOCK_SIZE))
    compared=font.render("Compare",True,TEXT_COLOR)
    compared_rect=compared.get_rect(center=(80+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(compared,compared_rect)

    pygame.draw.rect(screen,BLOCK_COLOR,(280,SCREEN_HEIGHT-100,BLOCK_SIZE,BLOCK_SIZE))
    unsorted_part=font.render("Unsorted",True,TEXT_COLOR)
    unsorted_part_rect=unsorted_part.get_rect(center=(280+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(unsorted_part,unsorted_part_rect)

    pygame.draw.rect(screen,GOLD,(480,SCREEN_HEIGHT-100,BLOCK_SIZE,BLOCK_SIZE))
    sorted_part=font.render("Sorted",True,TEXT_COLOR)
    sorted_part_rect=sorted_part.get_rect(center=(480+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(sorted_part,sorted_part_rect)

    screen.blit(down_arrow_black,(650,SCREEN_HEIGHT-100))
    iterator=font.render("Iterator",True,TEXT_COLOR)
    iterator_rect=iterator.get_rect(center=(650+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(iterator,iterator_rect)

    screen.blit(down_arrow_red,(850,SCREEN_HEIGHT-100))
    minimum=font.render("Minimum",True,TEXT_COLOR)
    minimum_rect=minimum.get_rect(center=(850+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(minimum,minimum_rect)

    screen.blit(up_arrow,(1050,SCREEN_HEIGHT-100))
    current=font.render("Current",True,TEXT_COLOR)
    current_rect=current.get_rect(center=(1050+BLOCK_SIZE//2,SCREEN_HEIGHT-150))
    screen.blit(current,current_rect)
    
    # Calculate the position for each block
    for index, number in enumerate(array):
        x = start_x + index * (BLOCK_SIZE + SPACING)
        y = start_y
        
        # Draw the block
        if(index==curr_pass-1):
            screen.blit(up_arrow,(x,y+100))
        if(index==highlight1):
            pygame.draw.rect(screen, CRIMSON, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            screen.blit(down_arrow_red,(x,y-100))
        elif(index==highlight2):
            pygame.draw.rect(screen, CRIMSON, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            screen.blit(down_arrow_black,(x,y-100))

        elif(index<=curr_pass-2):
            pygame.draw.rect(screen, GOLD, (x, y, BLOCK_SIZE, BLOCK_SIZE))
        else:    
            pygame.draw.rect(screen, BLOCK_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE))

        # Render the number
        text = font.render(str(number), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(x + BLOCK_SIZE // 2, y + BLOCK_SIZE // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

def sorted_array_display_selection():
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
            text_rect=text.get_rect(center=(start_x_small-100,y+ BLOCK_SIZE//2))
            screen.blit(text,text_rect)

            for index, number in enumerate(array_curr):
                # Draw the block
                x = start_x_small + index * (SMALL_BLOCK_SIZE + SPACING)
                color=BLOCK_COLOR
                if(index<i):
                    color=GOLD
                pygame.draw.rect(screen, color, (x, y, SMALL_BLOCK_SIZE, SMALL_BLOCK_SIZE))
                # Render the number
                text = font_small.render(str(number), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + SMALL_BLOCK_SIZE // 2, y + SMALL_BLOCK_SIZE // 2))
                screen.blit(text, text_rect)
            y+=70

        pygame.display.flip()            
