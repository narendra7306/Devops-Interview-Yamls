provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "dev" {
  ami           = "ami-11aa22bb33cc44dd"
  instance_type = "t2.micro"

  tags = {
    Name        = "demo-server"
    Environment = "Dev"
  }
}

