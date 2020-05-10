import pygame
import pygame.locals
# === CONSTANTS === (UPPER_CASE names)

WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (220, 20, 60)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

def main():
    
    # --- play init ---
    
    pygame.init()
    
    # --- play init board ---

    board = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Ping Pong")
    board_width, board_height = pygame.display.get_surface().get_size()
    
    # --  play init sounds
    
    sound_clash = pygame.mixer.Sound("sonidos/sfx_zap.ogg")
    
    # --- play init ball ---
    
    ball = pygame.image.load("imagenes/ball.png")
    ball_xy = ball.get_rect()
    ball_xy.move_ip(400-16, 300-16)
    ball_velocity = [1, 1]
    
    # --- play init points ---

    points_player_one = 0
    points_player_two = 0
    
    # --- play init players ---

    font_size = 30
    font_type = pygame.font.Font("fuentes/mifuente.ttf", font_size)
   
    # -------- play configure player One ---
    
    player_one = pygame.image.load("imagenes/bate.png")
    player_one_xy = player_one.get_rect()
    player_one_xy.move_ip(50, board_height/2)
    text_player_one = font_type.render("Player One: "+str(points_player_one), 0, BLUE)
    
    # -------- play configure player Two ---
    
    player_two = pygame.image.load("imagenes/palazul.png")
    player_two_xy = player_two.get_rect()
    player_two_xy.move_ip(board_width-50, board_height/2)
    text_player_two = font_type.render("Player Two: "+str(points_player_two), 0, BLUE)

    # --- play run ---
    
    run = True
    while run:
        
        # --- finish? ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        # --- winner?
        if points_player_one == 5 or points_player_two == 5:
            
            # --- stop game ---
            ball_xy.move_ip(0, 0)
            
            print("Play again? 0=No, 1=Yes")
            play_again = input()
            if int(play_again) == 1:
                main()
            else:
                pygame.quit()
           
        # --- ball move ---
        
        ball_xy = ball_xy.move(ball_velocity)
        
        if ball_xy.left < 0 or ball_xy.right > board_width:
            
            # --- score increases ---
            
            if ball_xy.left < 0:
                points_player_two += 1
            if ball_xy.right > board_width:
                points_player_one += 1
                
            # --- ball bounces ---
            
            ball_velocity[0] =- ball_velocity[0]
                
            # --- score show increases ---

            text_player_one = font_type.render("Player One: "+str(points_player_one), 0, BLUE)
            text_player_two = font_type.render("Player Two: "+str(points_player_two), 0, BLUE)
        
        # --- ball bounces on margins ---
        
        if ball_xy.top < 0 or ball_xy.bottom > board_height:
            ball_velocity[1] =- ball_velocity[1]
            
        # --- player one can scroll top ---
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if player_one_xy[1] < 0:
                player_one_xy = player_one_xy.move(0 , 5)
            else:
                player_one_xy = player_one_xy.move(0 , -5)
                
        # --- player one can scroll down ---
        
        if keys[pygame.K_s]:
            if player_one_xy[1] > board_height - 96:
                player_one_xy = player_one_xy.move(0 , -5)
            else:
                player_one_xy = player_one_xy.move(0 , 5)
                
        # --- player two can scroll top ---
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if player_two_xy[1] < 0:
                player_two_xy = player_two_xy.move(0 , 5)
            else:
                player_two_xy = player_two_xy.move(0 , -5)
        
        # --- player two can scroll top ---
        
        if keys[pygame.K_DOWN]:
            if player_two_xy[1] > board_height - 96:
                player_two_xy = player_two_xy.move(0 , -5)
            else:
                player_two_xy = player_two_xy.move(0 , 5)
                
        # --- ball bounces on players ---
        
        if player_one_xy.colliderect(ball_xy):
            sound_clash.play()
            ball_velocity[0] = - ball_velocity[0]
        
        if player_two_xy.colliderect(ball_xy):
            sound_clash.play()
            ball_velocity[0] = - ball_velocity[0]
            
        # --- show winner ---
        if points_player_one > 4:
            text_player_one = font_type.render("Player One: Winner!", 0, RED)
        
        if points_player_two > 4:
            text_player_two = font_type.render("Player Two: Winner!", 0, RED)
        
        # --- update game ---
        
        board.fill(WHITE)
        
        # --- score ---
        board.blit(text_player_one, (20,20))
        board.blit(text_player_two, ((board_width/2)-40,20))
        
        # --- ball ---
        board.blit(ball, (ball_xy))
        
        # --- players ---
        board.blit(player_one, (player_one_xy))
        board.blit(player_two, (player_two_xy))
        
        # --- refresh ---
        pygame.display.update()
        
        # --- show ---
        pygame.display.flip()
        
#----------------------------------------------------------------------

if __name__ == '__main__':

    main()

