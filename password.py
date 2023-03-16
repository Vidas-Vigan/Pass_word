import hashlib
import string



#  Créactio

#  Function haslib
def encode(mdp):
   mdp_encode = mdp.encode()
   mdp_haslib =  hashlib.sha256(mdp_encode).hexdigest()
   print(mdp_haslib)

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
        mdp = input("entrer un mot de passe de 8 caractères :")
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
            encode(mdp)
            break
mot_de_passe()

