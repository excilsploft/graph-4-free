terraform {

  required_version = "~> 1.16.0"

  required_providers {
   local = {
      source  = "hashicorp/local"
      version = "~> 2.8.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
}
