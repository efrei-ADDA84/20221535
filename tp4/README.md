# 20221535 - Devops - TP4
## Installation de Terraform
Installez la version qui vous correspond: https://developer.hashicorp.com/terraform/install
Une fois téléchargé, extrayez le fichier .zip et mettez le chemin vers l'exécutable dans le PATH.
Dans mon cas, sur Windows : 
- Cliquez sur le bouton Démarrer et cherchez les variables d'environnements ;
- Ajoutez une nouvelle variable (utilisateur ou système) et collez le chemin vers "terraform.exe" ;
- Vérifiez que Terraform est bien utilisation en exécutant dans un Terminal quelconque :
```
terraform --version
```
De plus, il ne faut pas oublier de télécharger l'extension Terraform sur VSCode (si on l'utilise !)

## Initialisation
On doit créer des fichiers de configuration avant d'initialiser le projet Terraform.

Ensuite j'ai exécuté les commandes suivantes:
```
az login
terraform init
terraform plan
terraform apply
```
puis : yes

![Capture d'écran 2024-04-20 182058](https://github.com/efrei-ADDA84/20221535/assets/120374187/c490b15f-ff91-4796-be39-c07ab39ab95c)

Erreur fatale qui m'empêche de continuer...

Après avoir tout supprimé, il est temps de recommencer les commandes :
```
az login
terraform init
terraform plan
terraform apply
```
puis

```
terraform output public_ip_address
"52.143.178.243"
```
```
[Output]
"52.143.178.243"
```
```
terraform output -raw tls_private_key > id_rsa
```
```
ssh -i id_rsa devops@52.143.178.243 cat /etc/os-release
```
```
[Output]
The authenticity of host '52.143.178.243 (52.143.178.243)' can't be established.
ED25519 key fingerprint is SHA256:nznmblZ6XoVoCqL+w8ZpY+TdXpCLBTiFR0cwJteiQCw.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '52.143.178.243' (ED25519) to the list of known hosts.
Load key "id_rsa": invalid format
devops@52.143.178.243: Permission denied (publickey).
```
Il faut ensuite modifier les droits mais je bloque...
sudo chmod ne fonctionne pas sur Windows et la commande icacls n'a pas fonctionné
