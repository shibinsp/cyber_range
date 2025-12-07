terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC Module
module "vpc" {
  source = "./modules/networking"

  vpc_cidr = var.vpc_cidr
  environment = var.environment
}

# EKS Cluster
module "eks" {
  source = "./modules/k8s"

  cluster_name = "retrorange-${var.environment}"
  vpc_id = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
}
