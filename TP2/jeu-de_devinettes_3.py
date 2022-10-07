"""
Projet fait par Sebastian Hasbun Poveda le 30-09-2022
Groupe 403
Code joue un jeu de devinette evec l'usager ou il doit deviner un nombre choisi par le code entre 0 et 100
"""

from random import randint
score = 0
continue_playing = True


def check_answer(answer):
    print(f"Votre essai est plus {answer} que le numero\n")


def correct_answer():
    global continue_playing, answer_found, score
    print(f"\nVous avez choisi le bon numero\nVotre score est: {score}")
    continue_playing_answer = input("Voulez vous continuer? y/n")
    answer_found = True
    if continue_playing_answer == "n":
        continue_playing = False


while continue_playing:
    answer_found = False
    minimum, maximum = input("entrer les bornes (min et max): ").split(' et ')  # '5 et 6' -> ['5', '6'] -> [5, 6]
    maximum = int(maximum)
    minimum = int(minimum)
    computer_generated_number = randint(minimum, maximum)
    print(f"\n")

    while not answer_found:
        player_guess = int(input("\nDevinez:"))
        score += 1

        if player_guess < computer_generated_number:
            check_answer("petit")

        elif player_guess > computer_generated_number:
            check_answer("grand")

        elif player_guess == computer_generated_number:
            correct_answer()
