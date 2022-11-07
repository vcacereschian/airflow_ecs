<pre>
export AWS_ACCOUNT=your_account_id
export AWS_DEFAULT_REGION=your_region
export AWS_PROFILE=your_profule
</pre>

### Deploy Infrastructure using Terraform

<pre>
cd infrastructure
terraform init
terraform plan
terraform apply
</pre>


Push to ECR
<pre>
bash scripts/push_to_ecr.sh project_name-stage
</pre>


## TODO
* Private Subnets
* Move ECS to Private Subnets
* Gateway Endpoints
* Authentification
* DAG Syncronization