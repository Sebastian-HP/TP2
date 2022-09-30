"""
Projet fait par Sebastian Hasbun Poveda le 26-09-2022
Groupe 403
Code joue un jeu de devinette evec l'usager ou il doit deviner un nombre choisi par le code entre 0 et 100
"""


from random import randint
score = 0
continue_playing = True


def check_answer(answer):
    global score
    print(f"Votre essai est plus {answer} que le numero\n")
    score += 1


def correct_answer():
    """

    :return: None
    """
    global continue_playing, answer_found, score
    print(f"Vous avez choisi le bon numero\nVotre score est: {score}")
    continue_playing_answer = input("Voulez vous continuer? y/n")

    if continue_playing_answer == "n":
        continue_playing = False
        answer_found = True


while continue_playing:
    answer_found = False
    computer_generated_number = randint(0, 10)
    print("\nL'ordinateur a choisi un numero aleatoire entre 0 et 100, c'est a vous de le trouver!")
    while not answer_found:
        player_guess = int(input("\nDevinez:"))

        if player_guess < computer_generated_number:
            check_answer("petit")

        elif player_guess > computer_generated_number:
            check_answer("grand")

        elif player_guess == computer_generated_number:
            correct_answer()

        else:
            print("error")
