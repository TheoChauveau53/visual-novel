# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

transform pos_sac:
    xzoom .2 yzoom .2
    xpos .0 ypos .1



init python:
    class Item:
        def __init__(self, name, image):
            self.name = name
            self.image = image

$ inventaire = []
$ sac = Item("sac", "sac.jpg")

# Le jeu commence ici
label start:
    scene avion
    
    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"
    
    return