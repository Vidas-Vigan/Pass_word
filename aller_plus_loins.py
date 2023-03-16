import hashlib
import string
import json

# Comparer les mots de passe afin de ne pas avoir 2 fois le même mot de passe
# enregistré dans le fichier.
with open("data.json", "r") as f:
    mot_de_passe = f.readlines()
    nouveau_mot_de_passe = input("Nouveau mot de passe : ")
if nouveau_mot_de_passe + "\n" in mot_de_passe:
        print("Ce mot de passe est déjà enregistré.")
else:
    with open("data.json", "a") as f:
        f.write(nouveau_mot_de_passe + "\n")
    print("ce mot de passe est déja utiliser.")

#  Function haslib
def encode(m2p):
   mdp_encode = m2p.encode()
   mdp_haslib =  hashlib.sha256(mdp_encode).hexdigest()
   print(mdp_haslib)
   return mdp_haslib

#  Fonction pour ajouter dans un fichier haslib
def ajouter(mdp, mdp_encode):
    f = open('data.json', "r+")
    data = json.load(f)
    data[mdp] = mdp_encode
    f.seek(0)
    json.dump(data, f, indent=4)
    f.close()

#   Function creation du mot de passe*
def mot_de_passe():
    minuscul = list(string.ascii_lowercase)
    majuscul =  list(string.ascii_uppercase)
    numero = list(string.digits)
    caractere_speciaux = list(string.punctuation)
    nbr_min = 0
    nbr_maj = 0
    nbr_num = 0
    nbr_car = 0
    while True:
        mdp = input("entrer un mot de passe de 8 caractères exemple(Voltig5@):")
        for i in mdp:
            if i in minuscul:
                nbr_min += 1
            if i in majuscul:
                nbr_maj += 1
            if i in numero:
                nbr_num += 1
            if i in caractere_speciaux:
                nbr_car += 1
        if len(mdp) < 8 or nbr_min == 0 or nbr_maj == 0 or nbr_num == 0 or nbr_car == 0:
            print('mot de passe refusé')
        else:
            print('mot de passe accepté')
            mdp_encode = encode(mdp)
            ajouter(mdp, mdp_encode)
            break
mot_de_passe()


