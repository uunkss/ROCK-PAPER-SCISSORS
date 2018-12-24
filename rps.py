import pygame
import random
import time

# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


# --- Game ----
class Game(object):
 
    def __init__(self):
        #score
        self.score_win = 0
        self.score_lose = 0

        #select
        self.player_select = 0
        self.com_select = 0

        #result
        self.player_result = 0
        
        # scene
        self.game_select = True
        self.game_judged = False
        self.game_over = False
 

 
    def process_events(self):
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_select:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    if ((200<x)&(x<300))&((100<y)&(y<200)):
                        self.player_select = 0
                        self.run_logic()
                    elif ((300<x)&(x<400))&((100<y)&(y<200)):
                        self.player_select = 1
                        self.run_logic()
                    elif ((400<x)&(x<500))&((100<y)&(y<200)):
                        self.player_select = 2
                        self.run_logic()
                        
                elif self.game_judged:
                    # add score
                    if self.player_result == 1:
                        self.score_win += 1
                    if self.player_result == 2:
                        self.score_lose += 1
                    #change scene
                    self.game_select = False
                    self.game_judged = False
                    self.game_over = True

                elif self.game_over:
                    #change scene
                    self.game_select = True
                    self.game_judged = False
                    self.game_over = False
                    
                
 
        return False
 
    def run_logic(self):
        
        if self.game_select:
            # random select
            self.com_select = random.randint(0, 2)
            print("------------------------")
            print("player "+str(self.player_select))
            print("com "+str(self.com_select))
            # check result
            if self.com_select == self.player_select:
                self.player_result = 0
            elif self.player_select == 0:
                if self.com_select == 1:
                    self.player_result = 2
                else:
                    self.player_result = 1
            elif self.player_select == 1:
                if self.com_select == 2:
                    self.player_result = 2
                else:
                    self.player_result = 1
            else:
                if self.com_select == 0:
                    self.player_result = 2
                else:
                    self.player_result = 1
            # change scene
            self.game_select = False
            self.game_judged = True
            self.game_over = False
            
            
            
            

            
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(WHITE)
 
        if self.game_select:
            # title
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Choose one !!!!", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            # choice
            rock_image = pygame.image.load("RockImg.jpg").convert()
            paper_image = pygame.image.load("PaperImg.jpg").convert()
            scissor_image = pygame.image.load("ScissorImg.jpg").convert()
            x=200
            y=100
            screen.blit(rock_image, [x,y])
            screen.blit(paper_image, [x+100,y])
            screen.blit(scissor_image, [x+200,y])
            # score
            text = font.render("Your score :", True, BLACK)
            center_x = 200
            center_y = 400
            screen.blit(text, [center_x, center_y])
            # win
            text = font.render("W "+str(self.score_win), True, BLACK)
            center_x = 350
            center_y = 400
            screen.blit(text, [center_x, center_y])
            # lose
            text = font.render("L "+str(self.score_lose), True, BLACK)
            center_x = 450
            center_y = 400
            screen.blit(text, [center_x, center_y])

        if self.game_judged:
            # title
            font = pygame.font.SysFont("serif", 25)
            text = font.render("PLAYER", True, BLACK)
            center_x = 200
            center_y = 100
            screen.blit(text, [center_x, center_y])

            
            text = font.render("COM", True, BLACK)
            center_x = 400
            center_y = 100
            screen.blit(text, [center_x, center_y])
            
            # select
            if self.player_select == 0:
                PlayerSelect_image = pygame.image.load("RockImg.jpg").convert()
            elif self.player_select == 1:
                PlayerSelect_image = pygame.image.load("PaperImg.jpg").convert()
            else:
                PlayerSelect_image = pygame.image.load("ScissorImg.jpg").convert()

            if self.com_select == 0:
                ComSelect_image = pygame.image.load("RockImg.jpg").convert()
            elif self.com_select == 1:
                ComSelect_image = pygame.image.load("PaperImg.jpg").convert()
            else:
                ComSelect_image = pygame.image.load("ScissorImg.jpg").convert()
                
            VS_image = pygame.image.load("VS.jpg").convert()
            x=200
            y=200
            screen.blit(PlayerSelect_image, [x,y])
            screen.blit(VS_image, [x+100,y])
            screen.blit(ComSelect_image, [x+200,y])

            
            # Result
            if self.player_result == 0:
                text = font.render("--- DRAW ---", True, BLACK)
                
            elif self.player_result == 1:
                text = font.render("--- WIN ---", True, BLACK)
                
            else:
                text = font.render("--- LOSE ---", True, BLACK)
                
            #sound.play()
            center_x = 300
            center_y = 400
            screen.blit(text, [center_x, center_y])

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Do you to want play again??, click to next round!!!", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        pygame.display.flip()
        
# --- Main fuction ----
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Rock Paper Scissor")

 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        #game.run_logic()
        
        # Draw the current frame
        game.display_frame(screen)

        pygame.display.flip()
        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()

 # Call the main function, start up the game
if __name__ == "__main__":
    main()

