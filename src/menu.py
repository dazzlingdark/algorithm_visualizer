from .initialize import *

# defining start menu arrow start position
arrow_x=200
arrow_y=200

def algorith_selector(arrow_y):
    screen.fill(BACKGROUND_COLOR)
    # Adding  Heading
    header=font.render("Which algorithm do you want to visualize?",True,TEXT_COLOR)
    header_rect=header.get_rect(center=(SCREEN_WIDTH//2,100))
    screen.blit(header,header_rect)
    
    # Adding Algorith selection logic
    screen.blit(arrow_right,(arrow_x,arrow_y))

    # calculationg vlalue of x0 so that blocks are in middle horizontally
    algo_block_len=500
    algo_block_height=80
    x0=(SCREEN_WIDTH -algo_block_len)//2

    # Bubble sort
    pygame.draw.rect(screen,BLOCK_COLOR,(x0,200,algo_block_len,algo_block_height))
    algo1=font.render("Bubble Sort",True,TEXT_COLOR)
    algo1_rect=algo1.get_rect(center=(x0+algo_block_len//2,200+algo_block_height//2))
    screen.blit(algo1,algo1_rect)

    # Insertion Sort
    pygame.draw.rect(screen,BLOCK_COLOR,(x0,300,algo_block_len,algo_block_height))
    algo2=font.render("Insertion Sort",True,TEXT_COLOR)
    algo2_rect=algo2.get_rect(center=(x0+algo_block_len//2,300+algo_block_height//2))
    screen.blit(algo2,algo2_rect)

    # Selection Sort
    pygame.draw.rect(screen,BLOCK_COLOR,(x0,400,algo_block_len,algo_block_height))
    algo3=font.render("Selection Sort",True,TEXT_COLOR)
    algo3_rect=algo3.get_rect(center=(x0+algo_block_len//2,400+algo_block_height//2))
    screen.blit(algo3,algo3_rect)  

    text2=font.render("Use arrow keys to choose option",True,TEXT_COLOR)
    text2_rect=text2.get_rect(center=(SCREEN_WIDTH//2,650))
    screen.blit(text2,text2_rect)               


    pygame.display.flip()