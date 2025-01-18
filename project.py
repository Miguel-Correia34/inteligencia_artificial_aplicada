#Game modes - Detect mode and Dig mode
import random
score  = 100
detection = True
numcells = 0
signal_strength = ["", "+", "++", "+++"]
d = 0

def init_grid(m, n):
    grid = [[None for _ in range(n)] for _ in range(m)]
    tres_row = random.randint(0, m-1)
    tres_col = random.randint(0, n-1)
    grid[tres_row][tres_col] = 'T'
    return grid, (tres_row, tres_col)

def init_prob(m,n):
    total_cells = m*n
    return [[1/total_cells for _ in range(n)] for _ in range(m)]


def detect_cell(grid, probabilities, tres_pos, row, col):
    distance = abs(tres_pos[0] -row) + abs(tres_pos[1]- col)
    signal_strength, updated_probabilities = calculate_signal_strength(distance, probabilities)
    update_probabilities(probabilities, signal_strength,row,col)
    return updated_probabilities, signal_strength

def calculate_signal_strength(distance, probabilities):
    if distance == 0:
        return["++++",0.80]

def update_probabilities(probabilities, signal_strength, row, col):
    # Depending on signal_strength, adjust the probability for the current cell and its neighbors
    # This should involve adjusting the probability values based on how close the cell is to the treasure
    pass



if detection == True:
    score -= numcells
else:
    score = numcells



print(score)