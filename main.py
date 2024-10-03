from src.initialize import *
from src.menu import algorith_selector,arrow_y
from algorithms.bubble_sort import bubbleSort
from algorithms.selection_sort import selectionSort

def main():
    global arrow_y
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # writing logic for moving arrow up/down
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_UP and arrow_y>200:
                    arrow_y-=100
                if event.key == pygame.K_DOWN and arrow_y<400:
                    arrow_y+=100

                # logic for selecting a particular algorithm    
                if event.key == pygame.K_RETURN:
                    if(arrow_y==200):
                        bubbleSort()  
                    if(arrow_y==400):
                        selectionSort()      
                            

        algorith_selector(arrow_y)

if __name__ == "__main__":
    main()
