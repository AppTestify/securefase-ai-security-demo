provider "aws" {
  region = "us-east-1"
}

# DEMO: public S3 bucket
resource "aws_s3_bucket" "reports" {
  bucket = "acme-ai-demo-reports"
  acl    = "public-read"
}

# DEMO: SSH open to the world
resource "aws_security_group" "web" {
  name = "ai-demo-web"

  ingress {
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
    cidr_blocks = [
      "10.0.0.0/8",
      "0.0.0.0/0",
    ]
  }
}

# DEMO: wildcard IAM
resource "aws_iam_policy" "admin" {
  name = "ai-demo-everything"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}

# DEMO: public unencrypted RDS
resource "aws_db_instance" "orders" {
  identifier          = "ai-demo-orders"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  publicly_accessible = true
  storage_encrypted   = false
}

# DEMO: unencrypted EBS
resource "aws_ebs_volume" "data" {
  availability_zone = "us-east-1a"
  size              = 20
  encrypted         = false
}

# DEMO: IMDSv1 allowed
resource "aws_instance" "app" {
  ami           = "ami-0123456789abcdef0"
  instance_type = "t3.micro"

  metadata_options {
    http_tokens = "optional"
  }
}

# DEMO: KMS rotation off
resource "aws_kms_key" "app" {
  description         = "ai-demo key"
  enable_key_rotation = false
}

# DEMO: plaintext secret in Lambda env
resource "aws_lambda_function" "worker" {
  function_name = "ai-demo-worker"
  role          = "arn:aws:iam::482193110274:role/worker"
  handler       = "index.handler"
  runtime       = "nodejs18.x"

  environment {
    variables = {
      DB_PASSWORD = "lambda-plaintext-password"
    }
  }
}
