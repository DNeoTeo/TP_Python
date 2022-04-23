READ ME

Le fichier client.py contient l'application graphique permettant à l'utilisateur 
d'indiquer les deux facteurs de la multiplication egyptienne. Lorsque le client
entre deux nombres valide dans les emplacements indiqués, le client envoie une requete
au serveur et ainsi il lui répond la valeur de la multiplication et le nombre d'itération
faite pour obtenir le résultat.

En étant dans l'environnement python ayant les modules installés:
    1. on lance le webserver avec la commande "uvicorn webserv:app --reload"
    2. on exécute le fichier python client.py avec la commande "py <possition du fichier client.py dans votre ordinateur>" 
    3. on remplit les deux champs puis on clique sur calcul et le réulstat s'affiche si aucun problème n'est rencontré