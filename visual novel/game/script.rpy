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
    
    jump QTE_reussi
    jump QTE_echoue

label QTE_reussi:
    jump blesse
    jump pas_blesse

label QTE_echoue:
    jump dans_la_cage

label pas_blesse:
    jump balade_foret

label blesse:
    jump balade_foret

label balade_foret:
    jump voir_village
    jump cabane

label voir_village:
    jump entrer_village

label entrer_village:
    jump fuite_cabane
    jump capture_entree_village

label fuite_cabane:
    jump reveil_cabane

label cabane_rencontre_A:
    jump 

label cabane:
    jump reveil_cabane

label capture_entree_village:
    jump dans_la_cage

label dans_la_cage:
    jump cadavre_cage

label cadavre_cage:
    jump forcer_cage
    jump fouiller_cage

label forcer_cage:
    jump mort_cage
    jump dans_la_cage

label mort_cage:
    jump dans_la_cage

label fouiller_cage:
    jump pince_echoue
    jump pince_reussi

label pince_echoue:
    jump mettre_masque

label pince_reussi:
    jump cabane_rencontre_A

label mettre_masque:
    jump cabane_rencontre_A

label reveil_cabane:
    jump cabane_rencontre_A

label revelation_policier:
    jump

label choix_demanteler_secte:
    jump

label fouiller_cabane:
    jump

label sortir_village:
    jump

label choix_fuite:
    jump

label reprendre_mission:
    jump