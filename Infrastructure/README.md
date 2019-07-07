## Building Infrastructure as code consists of the following files:  



auto_scale_lb.tf : 	Create load balancer and Auto scaler with 3 app
main.tf	         : Set up  configuration for App instances
network.tf	     : Setup Sandbox VPC
output.tf	       : ip address of ELB
provider.tf	     : AWS
security.tf	     : Firewall configuration
terraform.tfvars : local variable setup for 
vars.tf          : 

## Usage:
terraflow init
terraflow apply
terraflow destroy
