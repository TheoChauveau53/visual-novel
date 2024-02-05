# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define com = Character('Pilote', color="#5574da")
define M = Character('Marc', color="#ad0d0d")
define B = Character('Sélène Garde de la cage', color="#473439")
define C = Character('Julian le Joyeux', color="#473439")
define A = Character('Homme masqué', color="#312d69")
define A2 = Character('Sergent Tristan', color="#ad0d0d")
define secte = Character('Personnes masquées', color="#a5a5a5")






transform pos_sac:
    xzoom .3 yzoom .3
    xpos .0 ypos .1
init:
    $ open = False

init python:
    class Item:
        def __init__(self, name, image):
            self.name = name
            self.image = image
        def getPNG(self):
            return self.image
    kit_soin = Item("Kit de soin", "medkit.png")
    inventaire = []


# Le jeu commence ici
label start:
    scene avion
    show screen sac
    "On approche du site."
    com "Bon, Marc! Tu es prêt, on arrive bientôt sur site, tu vas pouvoir sauter"
    M "OK! Souhaite-moi bonne chance!"
    com "Bonne chance! Aterris pas dans un arbre! Ah ah!"
    M "C'est ça! Prend-moi pour un débutant tant que tu y es!"
    scene #atteris dans l'arbre
    M "Et merde! J'aurai du plus écouter le pilote quand il m'a dit que c'était dangereux de planer par ici."
    "Remarque qu'il y a des gens autours d'un feu de camp en contrebas."
    M "Tiens. On m'avait dit que le forêt étais inhabité."
    scene #sarifice
    M "Mais qu'est ce qu'il se passe là-bas?! Pourquoi il y a quelqu'un dans le feu ?!"
    M "Je crois que je n'aurais jamais du ici. Il faut que j'appele le pilote pour le prévenir de ce qu'il se passe ici."
    "Essaie de fouiller ses poches."
    M "Et merde! J'ai oublié mon tééphone dans l'avion. Je vais attendre q'ils partent pour descendre."
    #jump pendaison
    jump QTE_reussi
    jump QTE_echoue

label pendaison:
    

label QTE_reussi:
    "Le rituel se finit et les personnes partent sans avoir remarqué Marc."
    M "Il faut que je réussisse à descedre de l'arbre sans me blesser."
    M "Je vais devoir passer par une de ses deux branches. La plus fine me permettrait de descendre plus rapidement, mais la plus large me paraît plus solide."
    M "Laquelle vais-je choisir?"
    menu:
        "Que faites-vous ?"

        "se prendre une branche":        
            jump blesse

        "pas la prendre":
            jump pas_blesse

label QTE_echoue:
    "Crack!"
    "Les personnes autour du feu regarde Marc et commence a courir vers lui."
    M "Merde! J'ai fais trop de bruit, il faut que je parte de là en vitesse."
    "Les personnes masquées se jettent sur Marc."
    M "Non! Arrêtez! Cassez-vous qu'est-ce que vous me voulez!"
    "Marc s'évanouit."
    jump dans_la_cage

label blesse:
    M "Aïe! Je me suis tordu la cheville. J'ai jamais de chance dqns la vie, moi!"
    jump balade_foret

label pas_blesse:
    M "Ouf! C'était juste. Bon, maintenant je dois trouver un endroit pour me cacher et soigner ma cheville."
    jump balade_foret

label balade_foret:
    M "Bon, je prend quel chemin maintenant."
    jump voir_village
    jump cabane

label voir_village:
    M "Oh! Un village! Est-ce qu'ils savent ce qui se passe dans leurs forêt?"
    M "Est-ce que j'y vais?"
    jump entrer_village
    jump balade_foret

label entrer_village:
    M "C'est un très beau village. Bon, j'y vais."
    "Marc se rapproche et une alarme se déclenche directement."
    M "Mince! Une alarme! Il me faut fuire!"
    jump fuite_cabane
    jump capture_entree_village

label fuite_cabane:
    "Marc aperçoit une cabane dans la forêt."
    M "Vite! Une cabane! il faut que j'aille me réfugier là-bas."
    "Il rentre dans la cabane."
    M "je vais me cacher sous le lit."
    secte "Bon. Il ne doit pas être ici, continuez de fouiller la forêt!"
    "Marc est soulagé et il s'évanouit."
    jump reveil_cabane

label reveil_cabane:
    "Marc se réveil attaché a une chaise."
    M "Qu'est-ce qu'il se passe! Pourquoi je suis attaché ?!"
    A "Qu'est-ce que vous faites chez moi?"
    jump cabane_rencontre_A

label cabane_rencontre_A:
#    jump 

label cabane:
    "Il aperçoit une cabane isolée"
    M "Tiens! Une cabane. Elle n'a pas l'air d'être habitée."
    M "Je vais essayer de me reposer un peu. Je vais me mettre sous le lit au cas où."
    jump reveil_cabane

label capture_entree_village:
    "Marc se déplace lentement à cause de sa blessure"
    M "Merde! Il gagne du terrain sur moi!"
    "Il se fait attraper et s'évanouit"
    jump dans_la_cage

label dans_la_cage:
    A "Bonjour Monsieur Marc, comment allez-vous?"
    "Marc se réveille."
    M "Qui...Qui Êtes-vous ?! Qu'est-ce que vous me voulez ?!"
    A "Oh, je suis bête. Je ne me suis pas présenté. Où sont mes bonnes manières..."
    C "Je m'appele Julian. Je suis le Joyeux de cette magnifique communauté."
    M "Le gourou de cette secte plutôt!"
    C "Attention à votre langage jeune homme. Tant que je rest aimable"
    M "\"Aimable\"! Ne me faite pas rire! Vous m'avez kidnappé et enfermé bande de dégénérés!"
    C "Malheureusement, vous avez vu des choses que vous n'auriez jamais du voir."
    C "Nous ne puvons pas vous laisser partir. Ne vous en faites pas, votre sort ne sera pas dfférent de ce que vous avez vu."
    C "Garde!"
    A "Vous m'avez appelé?"
    C "Sélène, surveillez notre invité, ne le laissez pas s'échapper."
    B "Entendu."

    jump cadavre_cage

label cadavre_cage:
    "Marc examine la cage dans laquelle il a été enfermé."
    "Il remarque un cadavre à ses pieds."
    M "Ah! Mais! Qu'est ce qu'il fait là!"

    jump forcer_cage
    jump fouiller_cage

label forcer_cage:
    M "La cage ne m'a pas l'air bien solide. Je vais essayer de sortir en forçant la serrure."
    "Marc secoue la porte de sa cage avec toute sa force."
    B "Eh toi! Qu'es-ce que tu assaies de faire!"
    M "Mince, On m'a vu, je ne pourrais pas sortir."
    jump mort_cage
    jump dans_la_cage

label mort_cage:
    B "Bon, ça suffit! Tu commences à m'énerver!"
    "Le garde s'approche de la cage et décapite Marc."
    jump dans_la_cage

label fouiller_cage:
    M "La cage ne m'a pas l'air bien solide. Je vais essayer de trouver quelque chose pour sortir."
    "Marc fouille la cellule et trouve une lime."
    M "La lime est trop fine, je ne pourrais pas couper les barreaux avec."
    "Marc aperçoit un livre sous le cadavre."
    "Du sang couvre les pages du livre mais un morceau de texte reste lisible."
    "Ces personnes sont complètement folles, ils nous oblige à manger des outils en pièce détaché, ça va finir par me tuer. J'ai déjà été obliger ..."
    M "Je n'arrive pas à lire la suite"
    M "Ils forcent les prisonniers à manger des outils! C'est horrible!"
    M "Si j'arrive à récupérer les autres morceaux de la pince, je devrais réussir à couper le cadenas"
    jump pince_echoue
    jump pince_reussi

label pince_echoue:
    B "Eh! Qu'est ce que tu fais avec une pince toi?!"
    M "Rien dutout! Je viens juste de la trouver par terre."
    B "Je vais t'aider à expier tes péchés!"
    "Le garde se fait assomer par derrière."
    A "Bonjour jeune homme, si vous voulez vivre, suivez-moi."
    M "Qui ête-vous?!"
    A "Je ne peux rien te dire pour l'instant. Contente-toi de me suivre."
    jump mettre_masque

label pince_reussi:
    M "OK. Voyons voir si j'arrive à couper ce cadenas."
    "Marc réussit à couper le cadenas et il sort de la cage."
    M "Très bien. Comment je m'enfuit maintenant."
    "Marc se fait assomer."
    jump cabane_rencontre_A

label mettre_masque:
    "L'homme masqué tend un masque a Marc."
    A " Enfilez ça et ne vous éloignez pas."
    jump cabane_rencontre_A



label revelation_policier:
    jump choix_demanteler_secten
    jump sortir_village

label choix_demanteler_secte:
    jump fouiller_cabane

label fouiller_cabane:
#    jump

label sortir_village:
    jump choix_fuite

label choix_fuite:
    #jump 

label reprendre_mission:
    #jump 




#image button
screen sac:
    imagebutton:
        idle "sac.jpg"
        at pos_sac
        if open==False:
            action [Show("inventory"), SetVariable("open", True)]
        else:
            action [Hide("inventory"), SetVariable("open", False)]

screen inventory:
    image "inventory.png" at truecenter
    if len(inventaire)!=0 : 
        image inventaire[0].getPNG()
