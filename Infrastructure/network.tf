# Note: 
# read dta from available zone
# create vpc
# create security group
# read the availability zones for the current region
data "aws_availability_zones" "all" {}


/*

Configuration to make a very simple sandbox VPC for a few instances

For more details and options on the AWS vpc module, visit:
https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/1.30.0

 */
module "sandbox_vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "1.30.0"

  name = "${var.fellow_name}-vpc"

  cidr             = "10.0.0.0/26"
  azs              = ["${data.aws_availability_zones.all.names}"]
  public_subnets   = ["10.0.0.0/28"]

  enable_dns_support   = true
  enable_dns_hostnames = true

  enable_s3_endpoint = true

  tags = {
    Owner       = "${var.fellow_name}"
    Environment = "dev"
    Terraform   = "true"
  }
}



