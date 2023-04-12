import os

chemin_dossier = "C:/Users/amich/OneDrive/Images/img" # Chemin du dossier à parcourir
liste_dossiers = [] # Initialisation de la liste des dossiers

for nom in os.listdir(chemin_dossier): # Parcours du dossier et ajout des noms des dossiers dans la liste
    if os.path.isdir(os.path.join(chemin_dossier, nom)):
        liste_dossiers.append(nom)

print(liste_dossiers)

def rename(liste):
    for i in range(len(liste)): #changer ce parcours 
        chemin_dossier = "C:/Users/amich/OneDrive/Images/img" # Chemin du dossier contenant les images à renommer
        i = 1
        for fichier in sorted(os.listdir(chemin_dossier)): # Parcours tous les fichiers du dossier
            if not fichier.endswith((".jpg", ".jpeg", ".png", ".gif")): # Ignore les fichiers non-images 
                continue
            nouveau_nom = os.path.basename(chemin_dossier) + "!" + str(i).zfill(4) + os.path.splitext(fichier)[1] # Génère un nouveau nom pour le fichier
            os.rename(os.path.join(chemin_dossier, fichier), os.path.join(chemin_dossier, nouveau_nom)) # Renomme le fichier avec le nouveau nom
            i += 1

    return nouveau_nom
