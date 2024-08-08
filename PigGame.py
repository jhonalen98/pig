from random import randint


def check_die(score, die_value):
    if die_value == 1:
        return 0
    else:
        return score + die_value


def display_scoreboard(player_score, computer_score):
    print()
    print("#" * 20)
    print(f"Puntuación del jugador: {player_score}")
    print(f"Puntuación de la computadora: {computer_score}")
    print("#" * 20)
    print()


player_score = 0
computer_score = 0

welcome_message = """
          ¡Bienvenido a 'Pig', un juego de dados!
    
    En este juego, un usuario y un oponente de la computadora 
    Tira un dado de 6 caras en cada ronda. Si el valor de
    El dado es un 1, el jugador que sacó el 1 pierde.
    todos sus puntos. De lo contrario, el jugador obtiene el
    valor del dado sumado a sus puntos. El primer
    jugador que alcance los 30 puntos gana!
"""

print(welcome_message)

username = input("¿Cómo te llamas? ")

while True:
    input(f"¡Presiona 'Entrar' para tirar el dado {username}!\n")

    player_die_value = randint(1, 6)
    print(f"{username} lanza un {player_die_value}")

    computer_die_value = randint(1, 6)
    print(f"Computadora lanza un {computer_die_value}")

    player_score = check_die(player_score, player_die_value)
    computer_score = check_die(computer_score, computer_die_value)

    display_scoreboard(player_score, computer_score)

    if player_score >= 30:
        print(f"{username} gana!")
        break
    elif computer_score >= 30:
        print("Computadora gana!")
        break
