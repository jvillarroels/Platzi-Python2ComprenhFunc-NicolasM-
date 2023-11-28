print("")
print("Programa 0_main.py")
print("Juego de Piedra, Papel o Tijera")
print("=====================")
print("")

import random


def choose_options():
    options = ('piedra', 'papel', 'tijera') 
    user_option = input('Piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('*** ---> Esa opción no es válida')
        # continue
        return None, None

    computer_option = random.choice(options)

    print('Puntos del usuario => ', user_option)
    print('Puntos de la computadora => ', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins, rounds) :
    """Check Rules

    Args:
        user_option (_type_): _description_
        computer_option (_type_): _description_
        user_wins (_type_): _description_
        computer_wins (_type_): _description_
        rounds (_type_): _description_

    Returns:
        _type_: _description_
    """

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('\npiedra gana a tijera')
            print('    user ganó EL ROUND ' + str(rounds))
            user_wins += 1
        else:
            print('\nPapel gana a piedra')
            print('    computer ganó EL ROUND ' + str(rounds))
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('\npapel gana a piedra')
            print('    user ganó EL ROUND ' + str(rounds))
            user_wins += 1
        else:
            print('\ntijera gana a papel')
            print('    computer gano EL ROUND ' + str(rounds))
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('\ntijera gana a papel')
            print('    user gano EL ROUND ' + str(rounds))
            user_wins += 1
        else:
            print('\npiedra gana a tijera')
            print('    computer ganó EL ROUND ' + str(rounds))
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    """ RUN GAME
    Rutina principal del juego
    """
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:

        print('\n'+('*' * 10))
        print('ROUND', rounds)
        print('*' * 10)

        print('    computer_wins', computer_wins)
        print('    user_wins', user_wins)
        print(' ')
        rounds += 1    

        user_option, computer_option =  choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins, rounds)


        if computer_wins == 2:
            print('\nEl ganador del JUEGO es LA COMPUTADORA')
            break

        if user_wins == 2:
            print('\nEl ganador del JUEGO es EL USUARIO')
            break

run_game()
    
    


