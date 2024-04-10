import requests
import pandas as pd
import csv
import utils

url_nominatim = "https://nominatim.openstreetmap.org/search"

def get_gps_data(city):

    params = {
        "q": city,
        "format": "json",
    }
    response = requests.get(url_nominatim, params=params)

    # Vérification du statut de la requête
    if response.status_code == 200:
        data = response.json()
        # Extraction des données GPS
        if data: 
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
        else:
            latitude = ""  # Remplacer None par une chaîne vide
            longitude = ""          
        return latitude, longitude  
    else:
        print(f"Erreur : {response.status_code}")
        return None, None

csv_filename = "gps_data.csv"
with open(csv_filename, "w", newline="") as csvfile:
    # Créer un objet writer
    writer = csv.writer(csvfile)
    # Écrire l'en-tête du fichier CSV
    writer.writerow(["Ville", "Latitude", "Longitude"])
    #ajouter la liste des gps
    # Itérer sur les villes
    for ville in utils.villes:
        # Extraire les données GPS
        latitude, longitude = get_gps_data(ville)
            
        # Préparer les données pour le fichier CSV
        csv_data = [ville, latitude, longitude]

        # Écrire la ligne de données
        writer.writerow(csv_data)
        
print("Les résultats ont été enregistrés dans 'gps_data.csv'")


def get_gps_list():
    gps_lst = []
    # Récupérer coordonnées gps des villes
    for ville in utils.villes:
        latitude, longitude = get_gps_data(ville)
        gps_lst.append((ville, latitude, longitude))
    return gps_lst
