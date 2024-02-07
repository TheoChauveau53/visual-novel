define com = Character('Pilote', color="#5574da")
define M = Character('Marc', color="#ad0d0d")
define B = Character('Sélène Garde de la cage', color="#473439")
define C = Character('Julian le Joyeux', color="#473439")
define A = Character('Homme masqué', color="#312d69")
define A2 = Character('Sergent Tristan', color="#ad0d0d")
define secte = Character('Personnes masquées', color="#a5a5a5")




transform pos_perso:
    xpos .0 ypos .2
transform pos_inv1:
    xpos 0.155 ypos .2
transform pos_inv2:
    xpos 0.27 ypos .2
transform pos_inv3:
    xpos 0.385 ypos .2
transform pos_inv4:
    xpos 0.5 ypos .2
transform pos_inv5:
    xpos 0.615 ypos .2
transform pos_inv6:
    xpos 0.73 ypos .2
transform pos_inv7:
    xpos 0.155 ypos .4
transform pos_inv8:
    xpos 0.27 ypos .4
transform pos_inv9:
    xpos 0.385 ypos .4
transform pos_inv10:
    xpos 0.5 ypos .4
transform pos_inv11:
    xpos 0.615 ypos .4
transform pos_inv12:
    xpos 0.73 ypos .4
transform pos_inv13:
    xpos 0.155 ypos .6
transform pos_inv14:
    xpos 0.27 ypos .6
transform pos_inv15:
    xpos 0.385 ypos .6
transform pos_inv16:
    xpos 0.5 ypos .6
transform pos_inv17:
    xpos 0.615 ypos .6
transform pos_inv18:
    xpos 0.73 ypos .6

transform zoom_corde:
    xzoom .5 yzoom.5
transform pos_sac:
    xzoom .3 yzoom .3
    xpos .0 ypos .1
init:
    $ open = False
    $ nbr_forcage = 0
    $ nbr_morceaux_mince = 0
    $ policier_mort = False
    $ noeud_clique = 1
    $ time = 5
    $ end = False

init python:
    class Item:
        def __init__(self, name, image):
            self.name = name
            self.image = image
        def getPNG(self):
            return self.image
    kit_soin = Item("Kit de soin", "medkit.png")
    inventaire = [kit_soin]


# Le jeu commence ici
label start:
    scene avion with Dissolve(.5)
    show marccc at pos_perso
    show screen sac
    "On approche du site."
    com "Bon, Marc! Tu es prêt, on arrive bientôt sur site, tu vas pouvoir sauter"
    show marccc at pos_perso
    M "OK! Souhaite-moi bonne chance!"
    com "Bonne chance! Atterris pas dans un arbre! Ah ah!"
    show marccc at pos_perso
    M "C'est ça! Prend-moi pour un débutant tant que tu y es!"
    scene parachute with Dissolve(.5)
    $ renpy.pause(5.0, hard=True)
    scene #branche with Dissolve(.5)
    show marccc at pos_perso
    M "Et merde! J'aurai du plus écouter le pilote quand il m'a dit que c'était dangereux de planer par ici."
    "Remarque qu'il y a des gens autours d'un feu de camp en contrebas."
    show marccc at pos_perso
    M "Tiens. On ne m'avait pas dit que la forêt étais inhabité?"
    scene sacrifice with Dissolve(.5)
    M "Mais... Mais qu'est ce qu'il se passe là-bas?! Mais qu'est ce que... Il y a quelqu'un dans le feu ?!"
    M "Bordel! Je crois que je n'aurais jamais du être ici. Il faut que j'appelle le pilote pour le prévenir de ce qu'il se passe ici."
    "Essaie de fouiller ses poches."
    M "Et merde! J'ai oublié mon téléphone dans l'avion. Fais chier! Je vais devoir attendre qu'ils partent pour descendre."
    M "Je vais tenter de défaire mes liens en attendant."
    show screen noeud1
    show screen noeud2
    show screen noeud3
    show screen noeud4
    show screen noeud5
    show screen noeud6
    show screen noeud7
    show screen noeud8
    show screen noeud9
    show screen noeud10

    show screen countdown 
    $ renpy.pause(5.0, hard=True)
    
    
    if noeud_clique<1:
        jump pendaison
    if 0<noeud_clique<6:
        jump QTE_echoue
    if 5<noeud_clique:
        jump QTE_reussi

label pendaison:
    scene #branche with Dissolve(.5)
    "Marc n'a pas réussi à se défaire de son parachute."
    "Marc s'est pendu à une branche."
    jump start
    

label QTE_reussi:
    scene sacrifice with Dissolve(.5)
    "Le rituel se finit et les personnes masquées s'en aillent sans avoir remarqué Marc."
    M "Il faut que je réussisse à descendre de l'arbre sans me blesser."
    M "Je vais devoir passer par une de ses deux branches. La plus fine me permettrait de descendre plus rapidement, mais la plus large me paraît plus solide."
    M "Laquelle vais-je choisir?"
    menu:
        "Que faites-vous ?"

        "Choisir la branche large":        
            jump blesse

        "Choisir la branche fine":
            jump pas_blesse

label QTE_echoue:
    scene sacrifice with Dissolve(.5)
    "Crack!"
    "Les personnes autour du feu remarque Marc et commence a courir vers lui."
    M "Merde! J'arrive pas à me défaire de ce parachute, il faut que je parte de là en vitesse."
    "Les personnes masquées se jettent sur Marc."
    M "Non! Arrêtez! Mais cassez-vous! Qu'est-ce que vous me voulez!"
    "Marc s'évanouit."
    jump dans_la_cage

label blesse:
    scene foret_claire with Dissolve(.5)
    M "Aïe! Je me suis tordu la cheville. C'est vraiment le pire moment pour ça!"
    M "Bon, maintenant je dois trouver un endroit pour me cacher et soigner ma cheville."
    $ blesse = True
    jump balade_foret

label pas_blesse:
    scene foret_claire with Dissolve(.5)
    M "Ouf! C'était juste. Il faut que je trouve un endroit pour me reposer "
    $ blesse = False
    jump balade_foret

label balade_foret:
    scene foret_claire with Dissolve(.5)
    M "Bon, je prend quel chemin maintenant."
    menu:
        "Que faites-vous ?"
        "Aller vers la cabane":        
            jump cabane
        "Aller vers le village":
            jump voir_village

label voir_village:
    scene EntreeVillage with Dissolve(.5)
    M "Oh! Un village! Est-ce qu'ils savent ce qui se passe dans leur forêt?"
    M "Est-ce que j'y vais?"
    menu:
        "Que faites-vous ?"
        "Entrer dans le village":        
            jump entrer_village
        "Faire demi-tour":
            jump balade_foret

label entrer_village:
    scene EntreeVillage with Dissolve(.5)
    M "C'est un très beau village. Bon, j'y vais."
    "Marc se rapproche et une alarme se déclenche directement."
    M "Mince! Une alarme! Il me faut fuire!"
    if blesse == True :
        jump capture_entree_village
    if blesse == False :
        jump fuite_cabane
    

label fuite_cabane:
    scene lit with Dissolve(.5)
    "Marc aperçoit une cabane dans la forêt."
    M "Vite! Une cabane! Il faut que j'aille me réfugier là-bas."
    "Il rentre dans la cabane."
    M "Je vais me cacher sous le lit."
    secte "Bon. Il ne doit pas être ici, continuez de fouiller la forêt!"
    "Marc est soulagé et il s'évanouit."
    jump reveil_cabane

label reveil_cabane:
    scene bureau with Dissolve(.5)
    "Marc se réveille attaché à une chaise."
    M "Qu'est-ce... Qu'est-ce qu'il se passe! Pourquoi je suis attaché ?!"
    A "Qu'est-ce que vous faites chez moi?"
    jump cabane_rencontre_A

label cabane_rencontre_A:
    scene bureau with Dissolve(.5)
    jump revelation_policier 

label cabane:
    scene lit with Dissolve(.5)
    "Il aperçoit une cabane isolée"
    M "Tiens! Une cabane. Elle n'a pas l'air d'être habitée."
    M "Je vais essayer de me reposer un peu. Je vais me mettre sous le lit au cas où."
    jump reveil_cabane

label capture_entree_village:
    scene EntreeVillage with Dissolve(.5)
    "Marc se déplace lentement à cause de sa blessure"
    M "Merde! Ils sont en train de me rattraper!"
    "Il se fait attraper et s'évanouit"
    jump dans_la_cage

label dans_la_cage:
    A "Bonjour Monsieur Marc, comment allez-vous?"
    "Marc se réveille."
    M "Qui...Qui Êtes-vous ?! Qu'est-ce que vous me voulez ?!"
    A "Oh, je suis bête. Je ne me suis pas présenté. Où sont mes bonnes manières!"
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
    menu:
        "Que faites-vous ?"
        "Forcer la cage":        
            jump forcer_cage
        "Fouiller la cage":
            jump fouiller_cage
    
    

label forcer_cage:
    M "La cage ne m'a pas l'air bien solide. Je vais essayer de sortir en forçant la serrure."
    "Marc secoue la porte de sa cage avec toute sa force."
    B "Eh toi! Qu'es-ce que tu assaies de faire!"
    M "Mince, On m'a vu, je ne pourrais pas sortir."
    if nbr_forcage==2:
        jump mort_cage
    else:
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
    "Ces personnes sont complètement folles, ils nous oblige à manger des outils en pièce détaché, ça va finir par me tuer. J'ai déjà été obligé ..."
    M "Je n'arrive pas à lire la suite"
    M "Ils forcent les prisonniers à manger des outils! C'est horrible!"
    M "Si j'arrive à récupérer les autres morceaux de la pince, je devrais réussir à couper le cadenas"
    menu:
        "Que faites-vous?"
        #"Continuer de fouiller la cage":
        "Sortir de la cage":
            if nbr_morceaux_mince ==3:
                jump pince_reussi
            else:
                jump pince_echoue
        


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
    scene bureau with Dissolve(.5)
    menu:
        "Que faites-vous?"
        "Aider le policier à démanteler la secte":
            jump demanteler_secten
        "Sortir du village":
            jump sortir_village

label demanteler_secte:
    scene bureau with Dissolve(.5) 
    # trouve le medkit
    jump voir_maire
    



label sortir_village:
    scene EntreeVillage with Dissolve(.5)
    jump fuite

label fuite:
    scene foret_sombre with Dissolve(.5)
    "Marc a decidé de s'enfuir."
    "Il est resté en vie."
    return

label reprendre_mission:
    scene bureau with Dissolve(.5)
    scene lit with Dissolve(.5)
    scene bureau with Dissolve(.5)
    jump voir_maire

label voir_maire:
    jump trouve_a_temps
    jump trouve_pas_a_temps

label trouve_a_temps:
    if policier_mort :
        jump se_cacher
    else:
        jump info_eglise

label trouve_pas_a_temps:
    jump voir_maire

label se_cacher:
    jump reussi_cacher
    jump pas_reussi_cacher

label reussi_cacher:
    jump eglise

label pas_reussi_cacher:
    jump se_cacher

label puzzle:
    jump donjon_rexma

label donjon_rexma:
    if policier_mort:
        jump fin_3_mal
    else:
        jump fin_2_bien
    
label fin_2_bien:
    return

label fin_3_mal:
    return

label info_eglise:
    jump puzzle



#image button
screen sac:
    imagebutton:
        idle "sac.png"
        at pos_sac
        if open==False:
            action [Show("inventory"), SetVariable("open", True)]
        else:
            action [Hide("inventory"), SetVariable("open", False)]

screen noeud1:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud1"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv1
        
screen noeud2:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud2"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv2
screen noeud3:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud3"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv3
screen noeud4:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud4"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv4
screen noeud5:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud5"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv5
screen noeud6:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud6"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv6
screen noeud7:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud7"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv7
screen noeud8:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud8"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv8
screen noeud9:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud9"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv9
screen noeud10:
    imagebutton:
        idle "noeud.png"
        action [Hide("noeud10"),SetVariable("noeud_clique", noeud_clique+1)]
        at pos_inv10

screen inventory:
    image "inventory.png" at truecenter
    if len(inventaire)!=0 : 
        image inventaire[0].getPNG() at pos_inv1

screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Hide("noeud1"),SetVariable("end",True)])
    if time <= 3:
        text str(time) color "#FF0000" 
    else:
        text str(time)