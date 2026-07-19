provider "aws" {
  region = var.region
}

resource "aws_instance" "ec2" {
  count = var.instance_count

  ami                    = var.ami_id
  instance_type          = var.instance_type
  associate_public_ip_address = true

  tags = {
    Name        = "${var.environment}-server-${count.index + 1}"
    Environment = var.environment
  }
}



variable "region" {
  description = "AWS Region"
  type        = string
  default     = "ap-south-1"
}

variable "ami_id" {
  description = "AMI ID"
  type        = string
}

variable "instance_type" {
  description = "EC2 Instance Type"
  type        = string
  default     = "t2.micro"
}

variable "instance_count" {
  description = "Number of EC2 instances"
  type        = number
  default     = 2
}

variable "environment" {
  description = "Environment Name"
  type        = string
  default     = "dev"
}




output "instance_ids" {
  value = aws_instance.ec2[*].id
}

output "public_ips" {
  value = aws_instance.ec2[*].public_ip
}

