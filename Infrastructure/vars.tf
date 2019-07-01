##
## var.tf
## Variable values for FaceDetection Cloud Infrastructure
####


variable "AWS_REGION" {
  default = "us-west-2"
}

variable "AMIS" {
  type = "map"
  default = {
    us-east-1 = "ami-13be557e"
    us-west-2 = "ami-06b94666"
    eu-west-1 = "ami-0d729a60"
  }
}

variable "keypair_name" {
        description = "The name of your pre-made key-pair in Amazon (e.g. david-IAM-keypair )"
}
variable "fellow_name" {
  description = "The name that will be tagged on your resources."
}

/*

Not using AWS credential variables since they're automatically detected
from the environment variables

However, you could remove this and use a **properly** secured variable file
If you prefer to use a variable file, then you should NOT commit that file
and should use a proper security measures (e.g. use .gitignore, restrict access)

It is also worth noting that Terraform stores state in plaintext, so should
be used in production with a remote backend that is encrypted (e.g. S3, Consul)

variable "aws_access_key" {
        description = "AWS access key (e.g. ABCDE1F2G3HIJKLMNOP )"
}

variable "aws_secret_key" {
        description = "AWS secret key (e.g. 1abc2d34e/f5ghJKlmnopqSr678stUV/WXYZa12 )"
}

 */


variable "server_port" {
  description = "The port the server will use for HTTP requests"
  default     = 8080
}

variable "i2c_ami" {
  description = "OS image with flask AI engine for image caption"
  #default     = "ami-0949b16e4a69464f4"
  #default     = "ami-02d5cc2265b0fe8a4"
  default     = "ami-01c7e29efc5719ba4"
}

