terraform {
  #required_version = ">= 0.8, < 0.9"
  required_version = ">= 0.8"
}

#provider "aws" {
  #`region = "us-east-1"
  #region = "us-west-2"
#}

resource "aws_instance" "example" {
  #ami           = "ami-40d28157"
  ami           = "ami-005bdb005fb00e791"
  instance_type = "t2.micro"
  key_name        = "${var.keypair_name}"
  vpc_security_group_ids      = ["${module.open_all_sg.this_security_group_id}"]
  #vpc_security_group_ids= ["${aws_security_group.ingress-all-test.id}"]
  associate_public_ip_address = true
  subnet_id                   = "${module.sandbox_vpc.public_subnets[0]}"
  tags {
    Name = "my-masterServer"
  }


}

resource "aws_instance" "FD_app" {
  #ami                    = "ami-40d28157"
  ami           = "${var.i2c_ami}"
  instance_type          = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.FD_security_group.id}"]


  key_name        = "${var.keypair_name}"
  associate_public_ip_address = true

  tags {
    Name = "FaceDetectionWebApp"
  }
}


