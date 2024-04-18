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
En suivant les contraintes, voici un début permettant une initialisation :
```
resource "azurerm_resource_group" "tp4" {
  name     = "ADDA84-CTP"
  location = "france central"
}

resource "azurerm_virtual_network" "tp4" {
  name                = "devops-20221535"
  location            = data.azurerm_resource_group.tp4.location
  resource_group_name = data.azurerm_resource_group.tp4.name
  address_space       = ["10.3.0.0/16"]

  subnet {
    name                 = "internal"
    address_prefixes     = ["10.3.1.0/24"]
  }
}

```
à compléter
