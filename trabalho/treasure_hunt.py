import random

def init_grid(m,n):
    grid = [[ 1/(m*n) for _ in range(n)] for _ in range(m)] #inicialização da grelha com as probabilidades
    treasure_row = random.randint(0, m-1) 
    treasure_col = random.randint(0, n-1) # inicialização random da posição do tesouro
    return grid, (treasure_row, treasure_col)
#init_grid(4,4)

def manhattan_distance(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

#print(manhattan_distance([1,3], [2,4]))

grid = [[1/16 ,1/16 ,1/16, 1/16 ],[1/16 ,1/16 ,1/16,1/16 ],[1/16 ,1/16 , 1/16, 1/16],[1/16 ,1/16 , 1/16, 1/16]]
signal_table={0: {"++++": 0.8, "+++":0.1, "++":0.07, "+":0.03 },
                1: {"++++": 0.08, "+++":0.8, "++":0.08, "+":0.04 },
                2:{"++++": 0.04, "+++":0.08, "++":0.8, "+":0.08 },
                3:{"++++": 0.03, "+++":0.07, "++":0.1, "+":0.8 }} #tabela dos sinais do enunciado
def generate_signal(distance): # gerador de sinais baseado nas probabilidades da tabela e nos sinais e pesos
    probs = signal_table[min(distance,3)]
    sinais, pesos = zip(*probs.items())
    #print(sinais)
    #print(pesos)
    return random.choices(sinais, weights= pesos, k=1)[0]

generate_signal(0)

def update_grid_probabilities(signal, cell, grid, signal_table): #atualiza as probabilidades na grelha para o detect mode
    prob_total = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            distance = manhattan_distance([row,col], cell)
            likelihood = signal_table[min(distance,3)][signal]
            prior = grid[row][col]
            grid[row][col] = likelihood * prior
            prob_total += grid[row][col]
    
    for row in range(rows):
        for col in range(cols):
            grid[row][col] /= prob_total
            grid[row][col] = round(grid[row][col],4)
    
    return grid

#updated_grid= update_grid_probabilities("+++",(1,1),grid, signal_table)
#print(updated_grid)
#total_probability = sum(sum(row) for row in updated_grid)
#total_probability
#for row in updated_grid:
#    print([round(prob,4) for prob in row])

def display_grid(grid): # devolve a grelha em forma de tabela
    for row in grid:
        print(" | ".join(f"{cell:.4f}" for cell in row))

def main():
    print("Bem vindos à Caça ao Tesouro")
    print("Introduza o nº de quadrados das linhas da grelha")
    m = int(input())
    grid, treasure_loc = init_grid(m, m)
    score = 100
    found = False
    #print(grid)
    #print(treasure_loc[0])
    while score >0 and not found:
        print(grid)
        print("Score: ",score)
        signal_table={0: {"++++": 0.8, "+++":0.1, "++":0.07, "+":0.03 },
                1: {"++++": 0.08, "+++":0.8, "++":0.08, "+":0.04 },
                2:{"++++": 0.04, "+++":0.08, "++":0.8, "+":0.08 },
                3:{"++++": 0.03, "+++":0.07, "++":0.1, "+":0.8 }}
        print("Introduza o modo de jogo: ")
        print("1. detect ")
        print("2. dig")
        mode = input()
        if mode == "1":
            display_grid(grid)
            print("Introduza as coordenadas: ")
            i = int(input())
            j = int(input())
            if i < len(grid) and j < len(grid[i]) and i>=0 and j >=0:
                distance = manhattan_distance([i,j], [treasure_loc[0], treasure_loc[1]])
                signal = generate_signal(distance)
                grid = update_grid_probabilities(signal, [i,j], grid, signal_table)
                score -= 100 /(m*m)
            else:
                print("célula inválida")
        elif mode == "2":
            print("Introduza as coordenadas")
            i = int(input())
            j = int(input())
            if i == treasure_loc[0] and j == treasure_loc[1]:
                print("Encontraste o tesouro!")
                found = True
            else:
                print("Célula errada. Game over fracote!")
                break
        else:
            print("Célula inválida")
    if not found:
        print("O tesouro estava em :", treasure_loc)
    print("Score final", score)
                
main()