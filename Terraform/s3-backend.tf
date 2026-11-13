terraform {
  backend "s3" {
    bucket       = "my-terraform-state-bucket"
    key          = "dev/my-app/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }
}

resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = "my-terraform-state-bucket"

  versioning_configuration {
    status = "Enabled"
  }
}
