"""
Projet fait par Sebastian Hasbun Poveda le 30-09-2022
Groupe 403
Code joue un jeu de devinette evec l'usager ou il doit deviner un nombre choisi par le code entre 0 et 100
"""
from random import randint

continue_playing = True


def check_answer(answer):
    """
    Indique si la reponse est plus petite ou plus grande que la reponse de l'ordi
    :param answer: nombre du joueur

    :return: None
    """
    print(f"Votre essai est plus {answer} que le numero\n")


def correct_answer():
    """
    Indique le score et demande si le joueur veut rejouer
    :return:
    """
    global continue_playing, answer_found, score
    print(f"\nVous avez choisi le bon numero\nVotre score est: {score}")
    continue_playing_answer = input("Voulez vous continuer? y/n")
    answer_found = True
    if continue_playing_answer == "n":
        continue_playing = False


while continue_playing:
    score = 0
    answer_found = False
    minimum, maximum = int(input("Borne Minimale:")), int(input("Borne Maximale:"))
    computer_generated_number = randint(minimum, maximum)

    while not answer_found:
        player_guess = int(input("\nDevinez:"))
        score += 1

        if player_guess < computer_generated_number:
            check_answer("petit")

        elif player_guess > computer_generated_number:
            check_answer("grand")

        elif player_guess == computer_generated_number:
            correct_answer()
