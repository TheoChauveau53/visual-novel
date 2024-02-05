# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define com = Character('Commandant de Bord', color="#5574da")
define player = Character('Marc', color="#ad0d0d")
define B = Character('Tristan Garde de la cage', color="#473439")
define A = Character('Homme masqué', color="#312d69")
define A2 = Character('Sergent Sélène', color="#ad0d0d")
define secte = Character('Personnes masquées', color="#a5a5a5")






transform pos_sac:
    xzoom .2 yzoom .2
    xpos .0 ypos .1



#init python:
#    class Item:
#        def __init__(self, name, image):
#            self.name = name
#            self.image = image

#init:
    #$ inventaire = []
    #$ sac = Item("sac", "sac.jpg")


# Le jeu commence ici
label start:
    scene avion
    
    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"
    
    return