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
