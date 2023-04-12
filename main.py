import os

chemin_dossier = "C:/Users/amich/OneDrive/Images/img" # Chemin du dossier à parcourir
liste_dossiers = [nom for nom in os.listdir(chemin_dossier) if os.path.isdir(os.path.join(chemin_dossier, nom))] # Initialisation de la liste des dossiers

for nom in os.listdir(chemin_dossier): # Parcours du dossier et ajout des noms des dossiers dans la liste
    if os.path.isdir(os.path.join(chemin_dossier, nom)):
        liste_dossiers.append(nom)

print(liste_dossiers)

def rename(liste):
    for i in range(len(liste)):
        chemin_dossier2 = "C:/Users/amich/OneDrive/Images/img/" + str(liste[i]) # Chemin du dossier contenant les images à renommer
        print(chemin_dossier2)
        num = 1
        for fichier in sorted(os.listdir(chemin_dossier2)): # Parcours tous les fichiers du dossier
            if not fichier.endswith((".jpg", ".jpeg", ".png", ".gif")): # Ignore les fichiers non-images 
                continue
            nouveau_nom = os.path.basename(chemin_dossier2) + "!" + str(num).zfill(4) + os.path.splitext(fichier)[1] # Génère un nouveau nom pour le fichier
            os.rename(os.path.join(chemin_dossier2, fichier), os.path.join(chemin_dossier2, nouveau_nom)) # Renomme le fichier avec le nouveau nom
            num += 1

    return "Renommage terminé !"

print(rename(liste_dossiers))
