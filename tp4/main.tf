terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "765266c6-9a23-4638-af32-dd1e32613047"
}

variable "region"{
  default       = "france central"
  description   = "Location of the resource group."
}

data "azurerm_virtual_network" "tp4" {
  name                  = "network-tp4"
  resource_group_name   = data.azurerm_resource_group.tp4.name
}

data "azurerm_resource_group" "tp4" { 
   name   =   "ADDA84-CTP" 
} 

data "azurerm_subnet" "tp4" {
  name                 = "internal"
  virtual_network_name = data.azurerm_virtual_network.tp4.name
  resource_group_name  = data.azurerm_resource_group.tp4.name
}

resource "azurerm_network_interface" "myterraformnic" {
  name                = "NI-20221535"
  location            = data.azurerm_virtual_network.tp4.location
  resource_group_name =  data.azurerm_resource_group.tp4.name

  ip_configuration {
    name                          = "NIConfiguration-20221535"
    subnet_id                     = data.azurerm_subnet.tp4.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.myterraformpublicip.id
  }
}

resource "azurerm_public_ip" "myterraformpublicip" {
  name                = "PublicIP-20221535"
  location            = data.azurerm_virtual_network.tp4.location
  resource_group_name = data.azurerm_resource_group.tp4.name
  allocation_method   = "Dynamic"
}

resource "azurerm_linux_virtual_machine" "myterraformvm" {
  name                  = "devops-20221535"
  location              = data.azurerm_virtual_network.tp4.location
  resource_group_name   = data.azurerm_resource_group.tp4.name
  network_interface_ids = [azurerm_network_interface.myterraformnic.id]
  size                  = "Standard_D2s_v3"

  os_disk {
    name                 = "Os-20221535"
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  computer_name                   = "devops-20221535"
  admin_username                  = "devops"
  disable_password_authentication = true

  admin_ssh_key {
    username   = "devops"
    public_key = tls_private_key.my_ssh.public_key_openssh
  }
}

resource "tls_private_key" "my_ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

output "tls_private_key" {
  value     = tls_private_key.my_ssh.private_key_pem
  sensitive = true
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.myterraformvm.public_ip_address
}
