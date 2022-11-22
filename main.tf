# Create resource group
resource "azurerm_resource_group" "prod" {
  name     = "${var.prefix}iot-prod-rg"
  location = var.location
}

# Create Azure storage account
resource "azurerm_storage_account" "prod" {
  name                     = "${var.prefix}iotprodsa"
  resource_group_name      = azurerm_resource_group.prod.name
  location                 = azurerm_resource_group.prod.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Create Azure storage account container
resource "azurerm_storage_container" "prod" {
  name                  = "iotprodml"
  storage_account_name  = azurerm_storage_account.prod.name
  container_access_type = "private"
}

# Create Application insights
resource "azurerm_application_insights" "prod" {
  name                = "${var.prefix}iot-prod-ai"
  location            = azurerm_resource_group.prod.location
  resource_group_name = azurerm_resource_group.prod.name
  application_type    = "web"
}

data "azurerm_client_config" "current" {}


# Create Azure key vault
resource "azurerm_key_vault" "prod" {
  name                     = "${var.prefix}iot-prod-kv"
  location                 = azurerm_resource_group.prod.location
  resource_group_name      = azurerm_resource_group.prod.name
  tenant_id                = data.azurerm_client_config.current.tenant_id
  sku_name                 = "premium"
  purge_protection_enabled = false
}

# # Create Azure container registry
# resource "azurerm_container_registry" "prod" {
#   name                = "${var.prefix}iotprodcr"
#   location            = azurerm_resource_group.prod.location
#   resource_group_name = azurerm_resource_group.prod.name
#   sku                 = "Premium"
#   admin_enabled       = true
# }

# # Create Azure machine learning workspace
# resource "azurerm_machine_learning_workspace" "prod" {
#   name                    = "${var.prefix}-iot-prod-workspace"
#   location                = azurerm_resource_group.prod.location
#   resource_group_name     = azurerm_resource_group.prod.name
#   application_insights_id = azurerm_application_insights.prod.id
#   key_vault_id            = azurerm_key_vault.prod.id
#   storage_account_id      = azurerm_storage_account.prod.id
#   container_registry_id   = azurerm_container_registry.prod.id

#   identity {
#     type = "SystemAssigned"
#   }
# }

# Create Azure iot hub (https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/iothub)
resource "azurerm_iothub" "prod" {
  name                = "${var.prefix}iot-prod-iothub"
  resource_group_name = azurerm_resource_group.prod.name
  location            = azurerm_resource_group.prod.location

  sku {
    name     = "S1"
    capacity = "1"
  }

  endpoint {
    type                       = "AzureIotHub.StorageContainer"
    connection_string          = azurerm_storage_account.prod.primary_blob_connection_string
    name                       = "export"
    batch_frequency_in_seconds = 60
    max_chunk_size_in_bytes    = 10485760
    container_name             = azurerm_storage_container.prod.name
    encoding                   = "Avro"
    file_name_format           = "{iothub}/{partition}_{YYYY}_{MM}_{DD}_{HH}_{mm}"
  }

  route {
    name           = "export"
    source         = "DeviceMessages"
    condition      = "true"
    endpoint_names = ["export"]
    enabled        = true
  }

  enrichment {
    key            = "tenant"
    value          = "$twin.tags.Tenant"
    endpoint_names = ["export"]
  }

  cloud_to_device {
    max_delivery_count = 30
    default_ttl        = "PT1H"
    feedback {
      time_to_live       = "PT1H10M"
      max_delivery_count = 15
      lock_duration      = "PT30S"
    }
  }

  tags = {
    purpose = "testing"
  }
}

# Create Azure service plan as compute resource on which the Azure function will run
resource "azurerm_app_service_plan" "prod" {
  name                = "${var.prefix}iot-prod-asp"
  location            = azurerm_resource_group.prod.location
  resource_group_name = azurerm_resource_group.prod.name
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

# Create Azure functions (https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/function_app)
resource "azurerm_function_app" "prod" {
  name                       = "${var.prefix}iot-prod-fa"
  location                   = azurerm_resource_group.prod.location
  resource_group_name        = azurerm_resource_group.prod.name
  app_service_plan_id        = azurerm_app_service_plan.prod.id
  storage_account_name       = azurerm_storage_account.prod.name
  storage_account_access_key = azurerm_storage_account.prod.primary_access_key
  os_type                    = "linux"
  version                    = "~4"
  app_settings = {
    "AzureWebJobsDashboard"          = "UseDevelopmentStorage=true",
    "APPINSIGHTS_INSTRUMENTATIONKEY" = azurerm_application_insights.prod.instrumentation_key,
    "FUNCTIONS_WORKER_RUNTIME"       = "python"
  }

  site_config {
    linux_fx_version = "python|3.9"
  }
}
