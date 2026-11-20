
provider "aws" {
  region = "ap-south-1"
}

resource "aws_security_group" "demo_sg" {
  name        = "demo-security-group"
  description = "Allow SSH, HTTP and HTTPS traffic"
  vpc_id      = "vpc-0123456789abcdef0"

  # Inbound SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["MY_PUBLIC_IP/32"]
  }

  # Inbound HTTP
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Inbound HTTPS
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "demo-security-group"
  }
}
