import neat
from chess_game import ChessGame

# Define the fitness function for the game
def evaluate_genome(genome, config):
    game = ChessGame()
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    
    while not game.is_game_over():
        # Get current game state as input to the function evaluation
        input_data = game.get_board_state()
        
        # Use the neural network to get the predicted move for the game
        output = net.activate(input_data)
        
        # Get the valid moves and select the move with the highest output value
        valid_moves = game.get_valid_moves()
        best_move = max(valid_moves, key=lambda move: output[move])
        
        # Make the move
        game.make_move(best_move)
    
    # Return the fitness based on the game outcome and the best move value for the game
    if game.is_checkmate():
        return 1.0
    elif game.is_stalemate() or game.is_draw():
        return 0.5
    else:
        return 0.0

# Load the NEAT configuration file
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    'neat-config.txt')

# Create the NEAT population and run the evolution
population = neat.Population(config)
stats = neat.StatisticsReporter()
population.add_reporter(stats)
winner = population.run(evaluate_genome, 100)

# Print the best genome and its fitness
print('Best genome:', winner)
print('Fitness:', evaluate_genome(winner, config))
