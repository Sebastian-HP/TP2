'''
Projet fait par Sebastian Hasbun Poveda le 26-09-2022
Groupe 403
Code joue un jeu de devinette evec l'usager ou il doiit deviner un nombre choisi par le code entre 0 et 100
'''


from random import randint

player_guess = int(input("Numero"))
computer_generated_number = randint(0,100)
score = 0
continue_playing = True

def answer_is_bigger_than():
    global score
    print("Votre essai est plus grand que le numero\n\n")
    score += 1


def answer_is_smaller_than():
    global score
    print("Votre essai est plus petit que le numero\n\n")
    score += 1


def correct_answer():
    global score
    global continue_playing
    print("Vous avez choisi le bon numero\nVotre score est: " + score)
    continue_


while continue_playing == True :
    if player_guess < computer_generated_number:
        answer_is_smaller_than()

    elif player_guess > computer_generated_number:
        answer_is_bigger_than()

    elif player_guess == computer_generated_number:
        correct_answer()

    else:
        print("error")