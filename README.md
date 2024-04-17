# 20221535 - Devops - TP1
## Exécutez dans un terminal
$env:LONGITUDE="2.3522"                      
$env:LATITUDE="48.8566" 
### Code
Initialisation des valeurs :
```
$env:LATITUDE="5.902785" 
$env:LONGITUDE="102.754175"                      
python tp1.py
```
On obtient ainsi les informations météorologiques en fonction de nos valeurs.

### Docker
#### Création:
```
# Création de l'image
docker build -t tp1 .

# Test du code
docker run --env LATITUDE="5.902785" --env LONGITUDE="102.754175" --env API_KEY="442ed94cfe6ecc84c50d15ba360be7ce" tp1
```

Push sur Dockerhub :
```
docker tag tp1 artranart/20221535
```
Puis on clique sur "Push to hub"

#### Récupération:
```
docker pull artranart/20221535
docker run --env LAT=5.902785 --env LONG=102.754175 --env API_KEY="your_key" tp1
```


# 20221535 - Devops - TP2
## Configurer un workflow Github Actions
Afin de configurer un workflow, il faut se rendre dans la section "Actions" de notre répositoire.
On clique sur "New workflow" et on copie-colle sans vergogne le code suivant (pour tester) : [https://github.com/vDMG/efrei-tp2](https://github.com/vDMG/efrei-tp2/blob/master/.github/workflows/main.yaml)

Il suffit de commit puis d'aller dans la section "Actions" et appuyer sur le dernier workflow run que l'on a exécuté. 
## Transformer un wrapper en API
Après avoir tester plusieurs actions du lien suivant : https://github.com/marketplace?type=actions,
voici notre workflow:
```
name: "Transform Wrapper into API"
on: [push]
jobs:
  transform_wrapper:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Docker Login
        uses: docker/login-action@v3.1.0
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build Docker image
        run: docker build -t tp2 .
      - name: Tag Docker image
        run: docker tag tp2 artranart/20221535
      - name: Push Docker image to Docker Hub
        run: docker push artranart/20221535
```
Il se déclenche à chaque fois qu'un nouveau commit est poussé sur le dépôt. Voici le détail étape par étape :
1. **Checkout Repository** : Récupère le contenu du dépôt.
2. **Set up QEMU** : Configure QEMU, un émulateur de processeur.
3. **Set up Docker Buildx** : Configure Docker Buildx, un outil pour construire des images Docker multiplateformes.
4. **Docker Login** : Se connecte au registre DockerHub en utilisant des secrets pour le nom d'utilisateur et le token. Dans settings>Security>Secrets and variables, créez les repository secrets "DOCKERHUB_USERNAME" et "DOCKERHUB_TOKEN" en entrant votre username Docker et un Token généré dans DockerHub (click sur le profil, My account>Security>New access token et copiez-collez le lien dans la variables secrètes de Github).
5. **Build Docker image** : Construit une image Docker nommée "tp2" en utilisant le Dockerfile présent dans le dépôt.
6. **Tag Docker image** : Ajoute une étiquette à l'image Docker construite, la nommant "artranart/20221535".
7. **Push Docker image to Docker Hub** : Pousse l'image Docker construite sur Docker Hub dans le référentiel "artranart/20221535".





# 20221535 - Devops - TP3
## Etapes de déploiement
Comme pour le TP2, on configure un workflow Github Actions.
Voici les étapes du workflow du TP3:
**Check out repository code** : On récupère le code source depuis le référentiel GitHub.
**Update application configuration** : On met à jour des configurations de l'application.
**hadolint/hadolint-action** : On utilise Hadolint pour analyser le Dockerfile.
**Login via Azure CLI** : On se connecte à Azure à l'aide de l'interface de ligne de commande Azure.
**Azure Container Registry Login** : On s'authentifie auprès du registre Azure Container.
**Build Docker image** : On construit l'image Docker à partir du code source.
**Push Docker image** : On publie l'image Docker sur le registre Azure Container.
**Deploy to Azure Container Instances** : On déploie l'application sur Azure Container Instances.
## Problèmes rencontrés
La commande suivant ne fonctionne pas :
```
curl "http://devops-20221535.francecentral.azurecontainer.io/?lat=5.902785&lon=102.754175"
```
En effet, "Connection reset by peer". Que ce soit dans un terminal en local, sur Github Actions ou encore un bash d'Azure, rien ne fonctionne.
J'ai alors cherché à identifier le problème.
![image](https://github.com/efrei-ADDA84/20221535/assets/120374187/bb4d2556-f7b8-48c5-abcd-7d2a0b32fac5)
Le ping fonctionne bien, donc il y a une connecxion avec le serveur.
