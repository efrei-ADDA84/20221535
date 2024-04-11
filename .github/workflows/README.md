# 20221535 - Devops - TP2
## Configurer un workflow Github Action
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
