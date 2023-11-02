import pygame
import random

def run_snake_game():
    pygame.init()


    # Constants
    screen_width, screen_height = 640, 480
    cell_size = 20
    black = (50, 50, 50)
    green = (0, 255, 0)
    red = (255, 0, 0)

    # Initialize Pygame
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    # Snake and food initial positions
    snake_pos = [(screen_width // 2, screen_height // 2)]
    snake_dir = (cell_size, 0)
    food_pos = (random.randrange(1, screen_width // cell_size) * cell_size,
                random.randrange(1, screen_height // cell_size) * cell_size)

    snake_moving = False  # Variable to control snake movement
    score = 0  # Score counter

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and snake_dir != (cell_size, 0):
                snake_dir = (-cell_size, 0)
                snake_moving = True
            if keys[pygame.K_RIGHT] and snake_dir != (-cell_size, 0):
                snake_dir = (cell_size, 0)
                snake_moving = True
            if keys[pygame.K_UP] and snake_dir != (0, cell_size):
                snake_dir = (0, -cell_size)
                snake_moving = True
            if keys[pygame.K_DOWN] and snake_dir != (0, -cell_size):
                snake_dir = (0, cell_size)
                snake_moving = True

        if snake_moving:
            # Move the snake only if snake_moving is True
            snake_head = (snake_pos[0][0] + snake_dir[0], snake_pos[0][1] + snake_dir[1])
            snake_pos.insert(0, snake_head)

            # Check if snake collides with food and update food position and score
            if snake_head == food_pos:
                food_pos = (random.randrange(1, screen_width // cell_size) * cell_size,
                            random.randrange(1, screen_height // cell_size) * cell_size)
                score += 1  # Increase the score when the snake eats food
            else:
                snake_pos.pop()

            # Check if snake collides with itself or walls
            if (snake_head[0] < 0 or snake_head[0] >= screen_width or
                    snake_head[1] < 0 or snake_head[1] >= screen_height or
                    snake_head in snake_pos[1:]):
                pygame.quit()
                quit()

        # Draw everything, including the score
        screen.fill(black)
        for pos in snake_pos:
            pygame.draw.rect(screen, green, (pos[0], pos[1], cell_size, cell_size))
        pygame.draw.rect(screen, red, (food_pos[0], food_pos[1], cell_size, cell_size))

        # Display the score on the screen
        font = pygame.font.SysFont(None, 36)
        score_text = font.render("Score: " + str(score), True, green)
        screen.blit(score_text, (10, 10))

        if score >= 5:
            pygame.quit()
            print("""Congratulations you have defeated the snake game
    you collect your 40 gold from defeating the puzzle and are now free to continue to the next room""")
            from rooms import bear_room
            bear_room()
            return True

        pygame.display.update()
        clock.tick(10)  # Snake speed (frames per second)

    else:
        print("""you suck""")

### Naughts and Crosses game

def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    # Check if the board is full (no empty cells)
    return all([cell != " " for row in board for cell in row])

def naughts_and_crosses_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0
    
    print("You have selected a game of naughts and crosses!")
    print_board(board)
    
    while True:
        player = players[current_player_index]
        print(f"Player {player}, it's your turn.")
        row, col = map(int, input("Enter row (0, 1, or 2) and column (0, 1, or 2) separated by space: ").split())
        
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That cell is already occupied. Try again.")
            continue
        
        print_board(board)
        
        if check_winner(board, player):
            print(f"Congratulations! Player {player} wins!")
            break
        
        if is_board_full(board):
            print("It's a draw! The board is full.")
            break
        
        current_player_index = 1 - current_player_index  # Switch players

