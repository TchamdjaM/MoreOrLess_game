import random

def jeu_plus_ou_moins():
    # Définir la plage pour le nombre aléatoire
    limite_inférieure = 1
    limite_supérieure = 100
    nombre_secret = random.randint(limite_inférieure, limite_supérieure)

    # Initialiser les variables
    tentatives = 0
    nombre_deviné = None

    print(f"Bienvenue dans le jeu Plus ou Moins ! Devinez le nombre entre {limite_inférieure} et {limite_supérieure}.")

    while nombre_deviné != nombre_secret:
        try:
            nombre_deviné = int(input("Entrez votre estimation : "))
            tentatives += 1

            if nombre_deviné == nombre_secret:
                print(f"Félicitations ! Vous avez deviné le nombre correct {nombre_secret} en {tentatives} tentatives.")
            elif nombre_deviné < nombre_secret:
                print("Plus ! Essayez un nombre plus élevé.")
            else:
                print("Moins ! Essayez un nombre plus bas.")

        except ValueError:
            print("Entrée non valide. Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    jeu_plus_ou_moins()
