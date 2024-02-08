define com = Character('Radio du Pilote', color="#5574da")
define M = Character('Marc', color="#ad0d0d")
define B = Character('Sélène Garde de la cage', color="#473439")
define C = Character('Julian le Joyeux', color="#473439")
define A = Character('Homme masqué', color="#312d69")
define A2 = Character('Sergent Tristan', color="#ad0d0d")
define A3 = Character('Inconnu', color="#4d2614")
define secte = Character('Personnes masquées', color="#a5a5a5")
define com_shout = Character('Radio du Pilote', color="#5574da", what_size = 40)
define M_shout = Character('Marc', color="#ad0d0d", what_size = 40)
define B_shout = Character('Sélène Garde de la cage', color="#473439", what_size = 40)
define C_shout = Character('Julian le Joyeux', color="#473439", what_size = 40)
define A_shout = Character('Homme masqué', color="#312d69", what_size = 40)
define A2_shout = Character('Sergent Tristan', color="#ad0d0d", what_size = 40)
define A3_shout = Character('Inconnu', color="#4d2614", what_size = 40)
define secte_shout = Character('Personnes masquées', color="#a5a5a5", what_size = 40)
define com_whisper = Character('Radio du Pilote', color="#5574da", what_size = 25)
define M_whisper = Character('Marc', color="#ad0d0d", what_size = 25)
define B_whisper = Character('Sélène Garde de la cage', color="#473439", what_size = 25)
define C_whisper = Character('Julian le Joyeux', color="#473439", what_size = 25)
define A_whisper = Character('Homme masqué', color="#312d69", what_size = 25)
define A2_whisper = Character('Sergent Tristan', color="#ad0d0d", what_size = 25)
define A3_whisper = Character('Inconnu', color="#4d2614", what_size = 25)
define secte_whisper = Character('Personnes masquées', color="#a5a5a5", what_size = 25)
define P = Character('Policier', color="#1100f8", what_size = 25)




transform pos_perso:
    xpos .0 ypos .2
transform pos_perso1:
    xpos 0.40 ypos .2
transform pos_perso2:
    xpos 0.75 ypos .2 
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

transform background:
    xzoom 1.25 yzoom 1.3
transform backgroundvillage:
    xzoom .75 yzoom .75
init:
    $ cle_trouve = False
    $ open = False
    $ nbr_forcage = 0
    $ nbr_morceaux_mince = 0
    $ policier_mort = False
    $ noeud_clique = 0
    $ time = 5
    $ end = False
    $ puzzle = {1:1,2:0,3:3,
        4:4,5:5,6:6,
        7:7,8:8,9:9}

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
    scene avion at background 
    with Dissolve(.5)
    show marccc at pos_perso
    show screen sac
    "On approche du site."
    com_shout "Bon, Marc! Tu es prêt, on arrive bientôt sur site, tu vas pouvoir sauter"
    show marccc at pos_perso
    M_shout "OK! Souhaite-moi bonne chance!"
    com_shout "Bonne chance! Atterris pas dans un arbre! Ah ah!"
    show marccc at pos_perso
    M_whisper "C'est ça! Prend-moi pour un débutant tant que tu y es!"
    scene parachute at background
    with Dissolve(.5)
    $ renpy.pause(5.0, hard=True)
    scene branche at background
    with Dissolve(.5)
    show marccc at pos_perso
    M "Et merde! J'aurai du plus écouter le pilote quand il m'a dit que c'était dangereux de planer par ici."
    "Remarque qu'il y a des gens autours d'un feu de camp en contrebas."
    show marccc at pos_perso
    M_whisper "Tiens. On ne m'avait pas dit que la forêt était inhabité?"
    scene sacrifice at background
    with Dissolve(.5)
    M "Mais... Mais qu'est ce qu'il se passe là-bas?! Mais qu'est ce que... Il y a quelqu'un dans le feu ?!"
    M "Bordel! Je crois que je n'aurais jamais dû être ici. Il faut que j'appelle le pilote pour le prévenir de ce qu'il se passe ici."
    "Essaie de fouiller ses poches."
    M "Et merde! J'ai oublié mon téléphone dans l'avion. Fais chier! Je vais devoir attendre qu'ils partent pour descendre."
    M_whisper "Je vais tenter de défaire mes liens en attendant."
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
    scene branche at background
    with Dissolve(.5)
    "Marc n'a pas réussi à se défaire de son parachute."
    "Marc s'est pendu à une branche."
    jump start
    

label QTE_reussi:
    scene sacrifice at background
    with Dissolve(.5)
    "Le rituel se finit et les personnes masquées partent sans avoir remarqués Marc."
    scene branche at background
    with Dissolve(.5)
    show marccc at pos_perso
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
    scene sacrifice at background
    with Dissolve(.5)
    "Crack!"
    "Les personnes autours du feu remarquent Marc et commencent à courir vers lui."
    show marccc at pos_perso
    M_shout "Merde! Je n'arrive pas à me défaire de ce parachute, il faut que je parte de là en vitesse."
    "Les personnes masquées se jettent sur Marc."
    M_shout "Non! Arrêtez! Mais cassez-vous! Qu'est-ce que vous me voulez!"
    "Marc s'évanouit."
    jump dans_la_cage

label blesse:
    scene foret_claireee at background
    with Dissolve(.5)
    show marccc at pos_perso
    M "Aïe! Je me suis tordu la cheville. C'est vraiment le pire moment pour ça!"
    M "Bon, maintenant je dois trouver un endroit pour me cacher et soigner ma cheville."
    $ blesse = True
    jump balade_foret

label pas_blesse:
    scene foret_claireee
    with Dissolve(.5)
    show marccc at pos_perso
    M "Ouf! C'était juste. Il faut que je trouve un endroit pour me reposer "
    $ blesse = False
    jump balade_foret

label balade_foret:
    scene baladeforettt at background
    with Dissolve(.5)
    show marccc at pos_perso 
    M "Bon, je prend quel chemin maintenant."
    menu:
        "Que faites-vous ?"
        "Aller vers la cabane":        
            jump cabane
        "Aller vers le village":
            jump voir_village

label voir_village:
    scene entreevillageee at backgroundvillage
    with Dissolve(.5)
    show marccc at pos_perso
    M "Oh! Un village! Est-ce qu'ils savent ce qui se passe dans leur forêt?"
    M "Est-ce que j'y vais?"
    menu:
        "Que faites-vous ?"
        "Entrer dans le village":        
            jump entrer_village
        "Faire demi-tour":
            jump balade_foret

label entrer_village:
    scene entreevillageee at backgroundvillage
    with Dissolve(.5)
    show marccc at pos_perso
    M "C'est un très beau village. Bon j'y vais."
    "Marc se rapproche et une alarme se déclenche directement."
    M_shout "Mince! Une alarme! Il me faut fuire!"
    if blesse == True :
        jump capture_entree_village
    if blesse == False :
        jump fuite_cabane
    

label fuite_cabane:
    scene lit 
    with Dissolve(.5)
    "Marc aperçoit une cabane dans la forêt."
    show marccc at pos_perso
    M "Vite! Une cabane! Il faut que j'aille me réfugier là-bas."
    "Il rentre dans la cabane."
    show marccc at pos_perso
    M_whisper "Je vais me cacher sous le lit."
    scene lit 
    show tristanmask at pos_perso1
    show selenemask at pos_perso2
    secte_shout "Bon! Il ne doit pas être ici. Continuez de fouiller la forêt!"
    "Marc est soulagé et s'évanouit."
    jump reveil_cabane

label reveil_cabane:
    scene bureau 
    with Dissolve(.5)
    "Marc se réveille attaché à une chaise."
    show marccc at pos_perso
    show tristanmask at pos_perso2
    M_shout "Qu'est-ce... Qu'est-ce qu'il se passe! Pourquoi je suis attaché ?!"
    A "Qu'est-ce que vous faites chez moi?"
    jump cabane_rencontre_A

label cabane_rencontre_A:
    show tristan at pos_perso2
    show marccc at pos_perso
    A "Voici mon repère jeune homme, comment vous vous sentez ?"
    M "Disons que ça pourrait aller mieux, qu'est-ce qu'il se passe ici ?"
    A "Je vais vous en parler. Mais, tout d'abord, place aux présentations."
    A2 "Je m'appelle Tristan, je suis sergent de police et j'enquête sur la secte depuis 6 mois. Et vous, comment vous vous êtes retrouvé ici ?"
    M "Je m'appelle Marc. J'ai fait du saut en parachute, et me suis retrouvé coincé ici après que mon parachute se soit coincé dans un arbre."
    A2 "Très bien marc, je vais vous poser une simple question. J'ai assez d'éléments pour faire stopper les activités de la secte." 
    A2 "Mais il me manque les pièces de ma radio et je ne peux pas aller moi-même les chercher." 
    A2 "Accepteriez-vous de m'aider dans ma tâche ou souhaitez-vous que je vous aide à sortir de la forêt?"
    jump revelation_policier 

label cabane:
    scene lit 
    with Dissolve(.5)
    "Il aperçoit une cabane isolée"
    show marccc at pos_perso
    M "Tiens! Une cabane. Elle n'a pas l'air d'être habitée."
    M "Je vais essayer de me reposer un peu. Je vais me mettre sous le lit au cas où."
    jump reveil_cabane

label capture_entree_village:
    scene entreevillageee at backgroundvillage
    with Dissolve(.5)
    "Marc se déplace lentement à cause de sa blessure"
    show marccc at pos_perso
    M_shout "Merde! Ils sont en train de me rattraper!"
    "Il se fait attraper et s'évanouit"
    jump dans_la_cage

label dans_la_cage:
    scene cage at background
    with Dissolve(1)
    A3 "Bonjour Marc, comment allez-vous?"
    "Marc se réveille."
    show marccc at pos_perso
    show juliannn at pos_perso2
    M "Qui...Qui êtes-vous ?! Qu'est-ce que vous me voulez ?!"
    A3 "Oh, je suis bête. Je ne me suis pas présenté. Où sont mes bonnes manières!"
    C "Je m'appelle Julian. Je suis le Joyeux de cette magnifique communauté."
    M "Le gourou de cette secte plutôt!"
    C "Attention à votre langage jeune homme. Tant que je reste aimable"
    M_shout "\"Aimable\"! Ne me faite pas rire! Vous m'avez kidnappé et enfermé, bande de dégénérés!"
    C "Malheureusement, vous avez vu des choses que vous n'auriez jamais dû voir."
    C "Nous ne pouvons pas vous laisser partir. Ne vous en faites pas, votre sort ne sera pas différent de ce que vous avez vu."
    C_shout "Garde!"
    show selenemask at pos_perso1
    A "Vous m'avez appelé?"
    C "Sélène, surveillez notre invité, ne le laissez pas s'échapper."
    B "Entendu."

    jump cadavre_cage

label cadavre_cage:
    scene cage at background
    with Dissolve(.5)
    "Marc examine la cage dans laquelle il a été enfermé."
    "Il remarque un cadavre à ses pieds."
    show marccc at pos_perso
    M_shout "Ah! Mais! Qu'est ce qu'il fait là!"
    menu:
        "Que faites-vous ?"
        "Forcer la cage":        
            jump forcer_cage
        "Fouiller la cage":
            jump fouiller_cage
    
    

label forcer_cage:
    scene cage at background
    with Dissolve(.5)
    show marccc at pos_perso
    M "La cage ne m'a pas l'air bien solide. Je vais essayer de sortir en forçant la serrure."
    "Marc secoue la porte de sa cage avec toute sa force."
    show selenemask at pos_perso2
    B "Eh toi! Qu'es-ce que tu essaies de faire!"
    M "Mince, On m'a vu, je ne pourrais pas sortir."
    if nbr_forcage==2:
        jump mort_cage
    else:
        jump dans_la_cage

label mort_cage:
    B "Bon, ça suffit! Tu commences à m'énerver!"
    scene game_over at background
    with Dissolve(.5)
    "Le garde s'approche de la cage et décapite Marc."
    jump dans_la_cage

label fouiller_cage:
    show marccc at pos_perso
    M "La cage ne m'a pas l'air bien solide. Je vais essayer de trouver quelque chose pour sortir."
    "Marc fouille la cellule et trouve une lime."
    show marccc at pos_perso
    M "La lime est trop fine, je ne pourrais pas couper les barreaux avec."
    "Marc aperçoit un livre sous le cadavre."
    "Du sang couvre les pages du livre mais un morceau de texte reste lisible."
    "Ces gens sont complètement fous, ils nous obligent à manger des outils en pièces détachées, ça va finir par me tuer. J'ai déjà été obligé ..."
    show marccc at pos_perso
    M "Je n'arrive pas à lire la suite"
    M "Ils forcent les prisonniers à manger des outils! C'est horrible!"
    M "Si j'arrive à récupérer les autres morceaux de la pince, je devrais réussir à couper le cadenas"
    menu:
        "Que faites-vous?"
        #"Continuer de fouiller la cage":
        "Sortir de la cage": #a chaque tour tu proposes si il  veut fouiller la cage ou en sortir, il doit trouver 3 piece de pince, s'il a les 3 alors tu fais pop un mess qui dit qu'il a les 3 et qu'il peux sortir tu l'envoie dans pince reussi, s'il a pas les 3 et qu'il veux sortir tu l'envoies dans pinceechoué  
            if nbr_morceaux_mince ==3:
                jump pince_reussi
            else:
                jump pince_echoue
        


label pince_echoue:
    show slenemask at pos_perso2
    B "Eh! Qu'est-ce que tu fais avec une pince toi?!"
    show marccc at pos_perso
    M "Rien dutout! Je viens juste de la trouver par terre."
    B "Je vais t'aider à expier tes péchés!"
    "Le garde se fait assommer par derrière."
    show tristanmask at pos_perso1
    A "Bonjour jeune homme, si vous voulez vivre, suivez-moi."
    M_shout "Qui... Qui êtes-vous?!"
    A "Moins fort. Je ne peux rien te dire pour l'instant. Contente-toi de me suivre."
    jump mettre_masque

label pince_reussi:
    show marccc at pos_perso
    M "OK. Voyons voir si j'arrive à couper ce cadenas."
    "Marc réussit à couper le cadenas et il sort de la cage."
    M "Très bien. Comment je m'enfuie maintenant."
    "Marc se fait assommer."
    jump cabane_rencontre_A

label mettre_masque:
    "L'homme masqué tend un masque a Marc."
    show juliannn at pos_perso2
    A " Enfilez ça et ne vous éloignez pas."
    jump cabane_rencontre_A



label revelation_policier:
    scene bureau
    with Dissolve(.5)
    menu:
        "Que faites-vous?"
        "Aider le policier à démanteler la secte":
            jump demanteler_secte
        "Sortir de la foret":
            jump sortir_village

label demanteler_secte:
    scene bureau 
    with Dissolve(.5)
    A2 "Tout ce que vous devez savoir, c'est que vous vous trouvez dans la secte Rexma." 
    A2 "Une secte cachée dans cette forêt qui sacrifie les personnes qui osent entrer dans leur forêt."
    M "Mais qui est Rexma ?"
    A2 "Pour eux, Rexma est l'élu divin, et son retour ne sera possible qu'après 2009 sacrifices."
    M " 2009 ! mais pourquoi autant de meurtres ?"
    A2 "Même moi je ne le sais pas. Il n'y a que le chef surnommé \"Le Joyeux\" qui sait pourquoi."
    # trouve le medkit
    jump voir_maire
    



label sortir_village:
    scene entreevillageee at backgroundvillage
    with Dissolve(.5)
    show marccc at pos_perso
    show tristan at pos_perso2
    M "Je veux m'en aller de cette forêt. Je n'en peux plus. Je veux retourner chez moi"
    A2 "Ne t'en fais pas, je comprends. Je vais t'accompagner jusqu'à la route la plus proche"
    A2 "Ils ont posé plusieurs pièges pour empêcher les victimes de s'enfuir."
    "Ils marchent pendant plusieurs heures et approchent de la sortie de la forêt."
    scene foret_sombre at background
    with Dissolve(.5)
    A2 "Nous nous séparons donc ici. Rentre bien chez toi, mon ami."
    M "Merci Tristan, je te dois la vie, je ne pourrais jamais assez te remercier. Je m'en veux de te laisser ici mais je n'en peux plus. Je te souhaite bonne chance."
    A2 "Il y a une ville de ce côté à environ une heure de marche."
    "Marc regarde Tristan retourner dans la forêt"
    scene foret_sombre at background
    with Dissolve(.5)
    show selenemask at pos_perso
    show tristan at pos_perso2
    A_shout "Qu'est-ce que tu fais là toi! Ne me dis pas que tu essayais de t'enfuir!"
    A2 "Non, c'est pas ça je cherchais le fugi..."
    "Pan!"
    "Marc voit Tristan se faire abattre froidement d'un simple coup de feu."
    scene foret_sombre at background
    with Dissolve(.5)
    show marccc at pos_perso1
    M "Noooon, Tristaaaaan!"
    menu:
        "Qu'est-ce que je vais faire?!"
        "Reprendre la mission du GOAT Tristan":
            jump reprendre_mission
        "Fuir":
            jump fuite

label fuite:
    scene foret_sombre at background
    with Dissolve(.5)
    show marccc at pos_perso
    M "Je suis désolé Tristan, je n'ai pas le courage d'y retourner pour te venger."
    "Marc a decidé de s'enfuir."
    "Il est resté en vie."
    "FIN"
    return

label reprendre_mission:
    scene foret_sombre at background
    with Dissolve(.5)
    M_shout "Non! Tristan est mort à cause de moi. Je dois le venger, je ne pourrais plus me regarder dans la glace sinon."
    scene baladeforet at background
    with Dissolve(.5)
    M "Je vais retourner à la cabane de Tristan, Je ne peux pas laisser mes émotions me contrôler."
    scene bureau
    with Dissolve(.5)
    secte_shout "Le fugitif est là-bas!"
    M "Il faut que je me dépêche de rentrer"
    jump minijeux_serrure
label minijeux_serrure:
    jump fouiller_cabane_fuite

label fouiller_cabane_fuite:
    M "Tristan a sûrement laissé des infos cachées ici."
    menu:
        "Il doit y avoir des infos ici"
        "Fouiller son bureau":
            if cle_trouve:
                M "C'est bon, ça s'ouvre!"
                jump tiroir_fouille
            else:
                M "Mince il me faut une clé pour ouvrir le tiroir."
                jump fouiller_cabane_fuite
        "Fouiller son lit":
            if cle_trouve:
                M "J'ai déjà fouiller là-bas"
            else:
                M "Je vais aller fouiller son lit"
                jump lit_fouille

label lit_fouille:
    scene lit 
    with Dissolve(.5)
    "Marc cherche sous le matelas."
    $ cle_trouve = True
    "Parfait, la clé. C'est sûrement celle du tiroir de son bureau."
    jump fouiller_cabane_fuite

label tiroir_fouille:
    scene bureau 
    with Dissolve(.5)
    M "OK. Qu'est-ce qu'on a là dedans?"
    "Marc ouvre le tiroir."
    "Il trouve un journal et une pièce talkie-walkie."
    "Marc ouvre le journal"
    "Vous vous trouvez dans la secte Rexma, une secte cachée dans cette forêt qui sacrifie les personnes qui osent entrer dans leur forêt."
    "Je dois ... deuxième et troisième pièces de la radio. Elles... dans la maison du ... ou sinon ... église."
    "J'ai remarqué que le Joyeux sort de chez lui de 7h20 à 7h40 tous les matins pour aller à ... Je devrai aller fouiller."
    M "Je n'arrive pas à tout comprendre. Mais il faut que je retrouve les deux pièces manquantes"
    M "Si je comprends bien il devrait en avoir une à l'église et une dans une maison."
    M "\" la maison du \" ça doit faire référence à la maison du maire. Par chance, il est presque 7h20, je vais donc commencer par chercher là-bas."
    jump voir_maire

label voir_maire:
    scene maisonmaire at background
    with Dissolve(.5)
    M "OK. Il est 7h30, il ne me reste plus beaucoup de temps."
    M "Il faut que je me dépêche de retrouver la pièce du talkie-walkie."
    #chrono 
    #il faut fouiller la maison du maire *
    if piece_trouve:
        jump trouve_a_temps
    else:
        jump trouve_pas_a_temps

label trouve_a_temps:
    if policier_mort :
        jump se_cacher
    else:
        jump info_eglise

label trouve_pas_a_temps:
    scene maisonmaire at background
    with Dissolve(.5)
    C "Qu'est ce que vous faites chez moi Marc ?!"
    M "Mince, je n'ai pas réussi à trouver la pièce à temps"
    C "Venez tous ici! J'ai retrouvé le fugitif!"
    "Les personnes masquées se jettent sur Marc et le frappent à mort."
    jump voir_maire

label se_cacher:
    scene maisonmaire at background
    with Dissolve(.5)
    M "Je l'ai trouvé, il me reste plus qu'à aller chercher la dernière."
    "La porte de l'entrée s'ouvre brusquement."
    M_whisper "Mince, il est déjà là, il faut que je sorte sans faire de bruit. Il ne faut pas qu'il ne me remarque."
    if policier_mort :
        menu:
            "Où vais-je me cacher?"
            "Se cacher sous le lit":
                jump reussi_cacher
            "Sortir par la fenêtre":
                jump pas_reussi_cacher
    else:
        jump info_eglise

label reussi_cacher:
    scene maisonmaire at background
    with Dissolve(.5)
    secte_shout "Le fugitif s'est infiltré dans la maison du maire! Retrouvez-le avant qu'il en sorte!"
    "Après de longues minutes d'agitation, les personnes masquées sortent de la maison pour chercher aux alentours"
    M "J'ai le morceau que je cherchais."
    M "Il faut que j'aille chercher la dernière pièce"
    jump eglise

label pas_reussi_cacher:
    scene maisonmaire
    "Marc se dirige discrètement vers la fenêtre et essaie de l'ouvrir."
    M "Merde, elle ne s'ouvre pas. Qu'est-ce que je vais faire."
    secte_shout "Il est là! Tuez-le!"
    "Les personnes masquées se jettent sur Marc et le frappent à mort."
    jump se_cacher

label eglise:
    scene entreevillage at backgroundvillage
    with Dissolve(.5)
    "Marc arrive dans l'Église."
    scene eglisee at background
    with Dissolve(.5)
    M "Il faut que je trouve le dernier morceau du talkie-walkie et je pourrai contacter la police."
    "Il aperçoit le dernier morceau à droite de l'hôtel."
    M "Ah! le voilà."
    "Marc allume la radio et contacte la police."
    P "Oui, Allo commissariat de Pouletdeborgue, que pouvons-nous faire pour vous?"
    M "Oui, je vous appelle car je suis dans un village de meurtrier. Il y a énormément de cadavres ici, ils en ont après moi. Ils viennent de tuer un policier! Dépêchez-vous! Je ne vais pas pouvoir attendre longtemps."
    P "Du calme monsieur, je comprends votre situation mais essayez de vous calmer. Vous me dites que des personnes assassinent des gens là où vous vous trouvez?"
    M "Oui et ils vont finir par m'avoir aussi! On est dans la forêt à côté de votre ville! Dépêchez-vous je vous en supplie!"
    P "Très bien, je vous envoie tous nos policiers dans les environs et des renforts arriveront plus tard. Ne tentez rien jusqu'à ce qu'ils arrivent."
    P "Ils seront là dans moins de 10 minutes. Gardez courage."
    M_whisper "Il y a une porte de ce côté, je vais me cacher par là."
    jump puzzle

label puzzle:
    "Il me faut résoudre ce puzzle pour passer. Je ne dois pas traîner, ils ne tarderont pas à arriver ici"
    if policier_mort:
        jump donjon_rexma_mal
    else:
        jump donjon_rexma_bien

label donjon_rexma_mal:
    scene donjonnn at background
    with Dissolve(.5)
    M "Qu'est-ce que c'est que cette pièce! On dirait une salle de rituels!"
    C_shout "Marc! Mais quelle surprise que je te retrouve ici."
    C_shout "Tu t'es bien caché, mais maintenant c'est fini! Tu ne peux plus t'échapper! Tu ne peux plus te cacher!"
    M_shout "AH, AH, tu te trompes vieux dégénéré! J'ai prévenu la police, ils seront là d'une minute à l'autre! TU ne pourras plus te cacher. Vous êtes tous foutu!"
    C "Je le sais bien, mais... mais que vont-ils trouver ici? Dis-moi. J'ai brûlé tous les secrets que gardait le village, les membres du culte se sont déjà tous enfuie!"
    C "Il ne restera rien à l'arrivée des policiers!"
    M "Mais... Impossible... je..."
    M_shout "Tu resteras avec moi pour les attendre! Je te laisserais pas t'enfuir aussi! Tu seras jugé pour tous tes meurtres!"
    C "Et comment comptes-tu t'y prendre?"
    M_shout "TU NE T'ENFUIRAS PAS!"
    jump fin_3_mal
    
label donjon_rexma_bien:
    scene donjonnn at background
    with Dissolve(.5)
    M "Qu'est-ce que c'est que cette pièce! On dirait une salle de rituel!"
    A2 "Exactement! C'est ici qu'ils font leurs rituels."
    C_shout "Marc! Tristan Mais quelle surprise que de vous retrouver ici."
    C_shout "Vous vous êtes bien caché mais maintenant c'est fini! Vous ne pouvez plus vous échapper! Vous ne peux plus vous cacher!"
    M_shout "AH, AH, tu te trompes vieux dégénéré! Nous avons prévenu la police, ils seront là d'une minute à l'autre! TU ne pourras plus te cacher. Vous êtes tous foutu!"
    C "Je le sais bien, mais... Mais que vont-ils trouver ici?! Dis-moi. J'ai brûlé tout les secrets que gardait le village, les membres du culte se sont déjà tous enfuie!"
    C "Il ne restera rien à l'arrivée des policiers!"
    M "Mais... Impossible... je..."
    M_shout "Tu resteras avec nous pour les attendre! Je te laisserais pas t'enfuire aussi! Tu seras jugé pour tout tes meurtres!"
    C "Et comment comptes-tu t'y prendre?"
    "Julian le Joyaux sort un long couteau de son dos."
    M_shout "TU NE T'ENFUIRAS PAS!"
    jump fin_2_bien
    
label fin_2_bien:
    scene donjonnn at background
    with Dissolve(.5)
    "Julian se rapprocha de Marc et lui assena un coup de couteau rapide."
    "Tristan dégaina un pistolet et tira deux fois sur Julian." 
    "Pan! Pan!"
    "Julian, abattu, s'écroula sur le sol"
    "Les sirènes des voitures de police se firent entendre."
    "Quand la police arriva sur les lieux, tous les bâtiments avaient brûlé."
    "Les policiers ont ammené Marc à l'hôpital et il fût soigner."
    "Il ne restait que des cendres. Mais grâce aux efforts de Marc et Tritan, tous les membres du culte furent retrouvés et condamnés."
    
    return

label fin_3_mal:
    scene donjonnn at background
    with Dissolve(.5)
    "Marc se jetta sur le Joyeux"
    "Julian évita Marc d'un simple mouvement fluide et précis"
    "Sélène, cachée dans l'ombre de la porte apparaît et décapita Marc avec une Hache à deux mains."
    C "Au final, tu as été le plus fou de nous deux a croire que tu pouvais nous combattre."
    "Les sirènes des voitures de police se firent entendrent."
    C "J'ai encore le temps de m'en aller. Tu n'auras donc servi à rien. Tu n'as causé que destruction et violence, jeune pêcheur."
    "Quand la police arriva sur les lieux, tous les bâtiments avaient brûlé."
    "Il ne restait que des cendres. Et faute de preuve l'affaire de la forêt fût classée sans suite."
    return

label info_eglise:
    scene entreevillage at backgroundvillage
    with Dissolve(.5)
    A2 "Marc, viens."
    M "Oui?"
    A2 "Il ne nous reste qu'à trouver le dernier morceau du talkie-walkie."
    A2 "Il devrait être dans l'église. Une fois que nous l'auront trouvé, nous appelerons la police directement."
    M "Et s'ils nous trouvent avant qu'on les appelle ?"
    A2 "J'ai fait diversion pour nous laisser le temps de le trouver."
    "Marc et Tristan arrivent dans l'Église."
    scene eglisee at background 
    with Dissolve(.5)
    M "Il faut qu'on trouve le dernier morceau du talkie-walkie et nous pourrons contacter la police."
    "Il aperçoit le dernier morceau à droite de l'hôtel."
    M "Ah! Le voilà."
    "Marc répare la radio et laisse Tristan contacter la police."
    P "Oui, Allo commissariat de Pouletdeborgue, qu'est ce que nous pouvons faire pour vous."
    A2 "Oui, Je vous appelle car je suis dans un village de meurtriers. Il y a énormément de cadavres ici, ils en ont après moi et tous les gens qui rentrent dans le village. Dépêchez-vous! Nous ne pouvons pas attendre longtemps."
    P "Du calme monsieur, je comprends votre situation mais essayez de vous calmer. Vous me dîtes que des personnes assassinent des gens là où vous vous trouvez?"
    M "Oui et ils vont finir par nous avoir aussi! On est dans la forêt à côté de votre ville! Dépêchez-vous je vous en supplie!"
    P "Très bien, je vous envoie tous nos policiers dans les environs et des renforts arriveront plus tard. Ne tentez rien jusqu'à ce qu'ils arrivent."
    P "Ils seront là dans moins de 10 minutes. Gardez courage."
    M_whisper "Il y a une porte de ce côté, nous devrions nous cacher par là."
    A2 "Oui, allons-y"
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
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Hide("noeud1"), Hide("noeud2"),Hide("noeud3"),Hide("noeud4"),Hide("noeud5"),Hide("noeud6"),Hide("noeud7"),Hide("noeud8"),Hide("noeud9"),Hide("noeud10"),SetVariable("end",True)])
    if time <= 3:
        text str(time) color "#FF0000" 
    else:
        text str(time)