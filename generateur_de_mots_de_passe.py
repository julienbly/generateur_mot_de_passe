from tkinter import *
import pyperclip
from random import randint, choice
import string

f_principal = Tk()
mot_de_passe = 0

# création de la fonction pour générer le mot de passe
def générer_mot_de_passe():
    global mot_de_passe
    mot_de_passe_min = 6
    mot_de_passe_max = 24
    lette_autorisé = string.ascii_letters + string.punctuation + string.digits
    mot_de_passe = "".join(choice(lette_autorisé) for x in range(randint(mot_de_passe_min, mot_de_passe_max)))
    entrée_texte_mdp.delete(0, END)
    entrée_texte_mdp.insert(0, mot_de_passe)
    return mot_de_passe

# création de la fonction pour copier le mot de passe
def copier_mdp():
    pyperclip.copy(mot_de_passe)

# création de la fenêtre
f_principal.title("Générateur de mots de passe")
f_principal.geometry("740x480")
f_principal.minsize(740, 480)
f_principal.config(background='#4065A4')

# création de la boite principal
frame_principal = Frame(f_principal, bg='#4065A4')

# création du canva pour l'image
Vn_largeur = 300
Vn_hauteur = 300
image = PhotoImage(file="mdp.png").zoom(17).subsample(14)
canvas = Canvas(frame_principal, width=Vn_largeur, height=Vn_hauteur, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(Vn_largeur/2, Vn_hauteur/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# création d'une sous boite pour la géneration du mdp
sous_frame_generer = Frame(frame_principal, bg='#4065A4')

texte_principal = Label(sous_frame_generer, text="Mot de passe", font=("helvetica", 20), bg='#4065A4', fg='white')
texte_principal.pack()

#création d'un champs de saisie/input/champs
entrée_texte_mdp= Entry(sous_frame_generer, font=("helvetica", 20), bg='#4065A4', fg='white', bd=1, highlightthickness=0)
entrée_texte_mdp.pack()

#création d'un bouton pour générer le mdp
bouton_génération_mot_de_passe =  Button(sous_frame_generer, text='générer le mot de passe', font=("helvetica", 20), bg='#4065A4', fg='black', command=générer_mot_de_passe)
bouton_génération_mot_de_passe.pack(pady=10, fill=X)

#création d'un bouton pour copier le mdp
bouton_lancement = Button(sous_frame_generer, text='copier le mot de passe', font=("helvetica", 20), bg='#4065A4', fg='black', command=copier_mdp)
bouton_lancement.pack(pady=10, fill=X)

sous_frame_generer.grid(row=0, column=2, sticky=W)
frame_principal.pack(expand=YES)

#création d'une barre de menu
barre_menu = Menu(f_principal)

recherche_menu = Menu(barre_menu, tearoff=0)
recherche_menu.add_command(label='Nouveau', command=générer_mot_de_passe)
recherche_menu.add_command(label='Quitter', command=f_principal.quit)
recherche_menu.add_command(label='Copier', command=copier_mdp)
barre_menu.add_cascade(label='Fichier', menu=recherche_menu)


f_principal.config(menu=barre_menu)
f_principal.mainloop()