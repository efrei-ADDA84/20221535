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
