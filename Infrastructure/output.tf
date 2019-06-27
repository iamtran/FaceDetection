##
## output.tf
##
## We need to have access to ip address of load balancer to receive service
##
output "public_ip" {
  value = "${aws_instance.example.public_ip}"
}
output "webserver-public_ip" {
  value = "${aws_instance.FD_app.public_ip}"
}
output "elb_dns_name" {
  value = "${aws_elb.fd_load_balancer.dns_name}"
}


