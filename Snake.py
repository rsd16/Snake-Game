import pygame
import random
import time


def game_over(game_window, width, height, window_color, font_color):
    font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = font.render('YOU DIED...', True, color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    game_window.fill(window_color)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

def show_score(game_window, width, score, color):
    score_font = pygame.font.SysFont('consolas', 20)
    score_surface = score_font.render(f'Score: {str(score)}', True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width / 10, 15)
    game_window.blit(score_surface, score_rect)

def main():
    '''
    Difficulty settings:
        Easy: fps == 10
        Medium: fps == 25
        Hard: fps == 40
        Harder: fps == 60
        Impossible: fps == 120
    '''

    fps = 25
    fps_controller = pygame.time.Clock()

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    width = 720
    height = 480

    snake_position = [100, 50]
    snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

    food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    direction = 'right'
    move_to = direction

    score = 0

    pygame.init()

    pygame.display.set_caption('Snake Eater')
    game_window = pygame.display.set_mode((width, height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    move_to = 'up'

                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    move_to = 'down'

                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    move_to = 'left'

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    move_to = 'right'

                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if move_to == 'up' and direction != 'down':
            direction = 'up'

        if move_to == 'down' and direction != 'up':
            direction = 'down'

        if move_to == 'left' and direction != 'right':
            direction = 'left'

        if move_to == 'right' and direction != 'left':
            direction = 'right'

        if direction == 'up':
            snake_position[1] -= 10

        if direction == 'down':
            snake_position[1] += 10

        if direction == 'left':
            snake_position[0] -= 10

        if direction == 'right':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))

        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]

        food_spawn = True

        game_window.fill(black)

        for position in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(position[0], position[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > width-10:
            game_over(game_window, width, height, black, red)

        if snake_position[1] < 0 or snake_position[1] > height-10:
            game_over(game_window, width, height, black, red)

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window, width, height, black, red)

        show_score(game_window, width, score, white)

        pygame.display.update()

        fps_controller.tick(fps)

if __name__ == '__main__':
    main()
