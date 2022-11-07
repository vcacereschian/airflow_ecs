variable "aws_region" {
   default = "us-east-1"
}

variable "availability_zones" {
   type    = list(string)
   default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

variable "project_name" {
   default = "project_name"
}

variable "s3_bucket" {
   default="bucket_name"
}

variable "fernet_key"{
   default= "fernet_key"
}

variable "profile" {
   default = "local_profile"
}

variable "stage" {
   default = "stage"
}

variable "base_cidr_block" {
   default = "10.0.0.0"
}

variable "log_group_name" {
   default = "ecs/project_name"
}

variable "image_version" {
   default = "latest"
}

variable "metadata_db_instance_type" {
   default = "db.t3.micro"
}

variable "celery_backend_instance_type" {
   default = "cache.t2.micro"
}