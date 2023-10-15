rowTilesNum = 3
columnTilesNum = 3
player1Name = ''
player2Name = ''

tilesArray = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]

def printGameField():
    for i in range(rowTilesNum):
        for j in range(columnTilesNum):
            print(f'{tilesArray[i][j]} ', end='')
        print('\n')

def fillTheTile(char, tile_num1, tile_num2):
    if(tilesArray[tile_num1][tile_num2] != '[ ]'):
        return False
    else:
        tilesArray[tile_num1][tile_num2] = f'[{char}]'
        return True
    
def gameEnder():
    endCombinations = [[[1,1], [2,2], [3,3]], [[1,3], [2,2], [3,1]], [[1,1], [1,2], [1,3]], [[2,1], [2,2], [2,3]], [[3,1], [3,2], [3,3]],
                       [[1,1], [2,1], [3,1]], [[1,2], [2,2], [3,2]], [[1,3], [2,3], [3,3]]]
    chars = ['[x]', '[o]']
    ender = 0
    for char in chars:
        for combination in endCombinations:
            ender = 0
            for i in range(3):
                num1 = combination[i][0]
                num2 = combination[i][1]
                if(tilesArray[num1 - 1][num2 - 1] == char):
                    ender += 1
            if(ender == 3):
                return char
            else:
                pass


def createGame():
    playersTurn = 0
    print('Правила:\n1. Перший гравець грає за хрестик "x", другий гравець за нолик "o"\n2. Мета гри - зібрати три символи свого типу в рядку, стовпці або діагоналі\n3. Якщо все поле зайнято символами, а переможця немає - гра завершується нічиєю\n')
    
    player1Name = input("Введіть ім'я для першого гравця: ")
    player2Name = input("Введіть ім'я для другого гравця: ")

    print(f'\nВітаємо вас {player1Name} та {player2Name}!\n')

    while True:
        char = ''
        if(playersTurn == 0):
            print(f'Зараз ходить гравець {player1Name} з символом хрестика "x"!\n')
            char = 'x'
        else:
            print(f'Зараз ходить гравець {player2Name} з символом нолика "o"!\n')
            char = 'o'

        printGameField()

        print('Введіть клітинку яку ви хочете заповнити. ')
        filledSuccess = None
        while filledSuccess != True:
            num1 = input('Введіть рядок: ')
            while num1 not in ['1', '2', '3']:
                num1 = input('Введіть рядок: ')

            num2 = input('Введіть стовпчик: ')
            while num2 not in ['1', '2', '3']:
                num2 = input('Введіть стовпчик: ')

            filledSuccess = fillTheTile(char, (int(num1) - 1), (int(num2) - 1))
        
            if filledSuccess:
                break
            elif(filledSuccess == False):
                print('\nЦя клітинка занята! Виберіть іншу!\n')

        gameEnd = gameEnder()

        if(gameEnd == '[x]'):
            print(f'\nГравець {player1Name} виграв!\n')
            printGameField()
            break
        elif(gameEnd == '[o]'):
            print(f'\nГравець {player2Name} виграв!\n')
            printGameField()
            break

        if(playersTurn == 0):
            print(f'Хід гравця {player1Name} завершено!\n')
            playersTurn = 1
        else:
            print(f'Хід гравця {player2Name} завершено!\n')
            playersTurn = 0

createGame()

while True:
    print("Щоб зіграти заново натисніть будь-яку клавішу:\nЗавершити гру: 'q' ")
    
    if input() == 'q':
        break
    else:
        createGame()