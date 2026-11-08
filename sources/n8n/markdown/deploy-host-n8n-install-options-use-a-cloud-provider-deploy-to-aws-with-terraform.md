For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform.md)
.

[terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n)
 is a Terraform module that deploys a production-grade, multi-main n8n instance to AWS. It provisions an Amazon EKS cluster running n8n's Helm chart, with managed PostgreSQL (RDS), Redis (ElastiCache), and S3 for shared file storage.

This differs from the manual [Kubernetes setup](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws)
 n8n documents elsewhere: that guide walks you through hand-written manifests for a single n8n instance. This module automates a highly available, auto-scaling deployment, and it's maintained independently by the n8n Solutions team.

**Pre-release module**

`terraform-aws-n8n` is in pre-release. Expect breaking changes before the module reaches its first stable (1.0) release.

**Feature availability**

The default multi-main topology this module deploys is available on:

*   **Self-hosted:** Enterprise
    

Setting `n8n_main_hpa_min_replicas = 1` runs a single main pod instead, which only requires a Business plan license. In that mode, the main pod's autoscaling maximum is forced to one, and upgrades use a `Recreate` strategy. Expect downtime for the editor, REST API, and scheduled triggers during upgrades and maintenance.

Architecture[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#architecture)

-----------------------------------------------------------------------------------------------------------------------------------

Users and inbound webhooks reach an Application Load Balancer that fronts the EKS cluster. Inside the cluster, the n8n Helm chart runs three separate deployments:

*   **Main pods:** handle leader election, the editor UI, and the REST API.
    
*   **Webhook processor pods:** handle inbound triggers.
    
*   **Worker pods:** run workflow executions, and scale on Redis queue depth using [KEDA](https://keda.sh/)
    .
    

State lives in managed services outside the cluster: RDS PostgreSQL for workflow data, ElastiCache Redis for leader election and the worker queue, and S3 for binary data. AWS Certificate Manager (ACM) issues the TLS certificate for the load balancer.

AWS grants pods permissions (for the Load Balancer Controller, Cluster Autoscaler, EBS CSI driver, and n8n's own S3 access) through EKS Pod Identity.

Prerequisites[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#prerequisites)

-------------------------------------------------------------------------------------------------------------------------------------

*   An **n8n license key**: an Enterprise license for the default multi-main topology, or a Business license if you set `n8n_main_hpa_min_replicas = 1`.
    
*   A **pre-existing VPC** with public and private subnets tagged for EKS and ALB use. The module doesn't create a VPC. See [Customize the AWS infrastructure](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/customize-the-infrastructure)
    .
    
*   **Terraform CLI 1.11 or later**, with the `aws`, `kubernetes`, and `helm` providers configured.
    
*   A DNS option: either a Route 53 hosted zone (`route53_zone_id`), which lets the module issue the ACM certificate and manage the DNS record itself, or a pre-validated certificate from another provider (`certificate_arn`).
    

Usage[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#usage)

---------------------------------------------------------------------------------------------------------------------

For a step-by-step walkthrough that takes you from an empty folder to a running instance, see [Deploy your first n8n instance on AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/deploy-your-first-instance)
. The configuration below is the minimum set of inputs:

Copy

    module "n8n" {
      source  = "n8n-io/n8n/aws"
      version = "~> 0.5.0"
    
      aws_region      = "us-east-1"
      cluster_name    = "n8n-cluster"
      n8n_domain      = "n8n.example.com"
      n8n_license_key = var.n8n_license_key
    
      # Bring your own VPC.
      vpc_id          = module.vpc.vpc_id
      private_subnets = module.vpc.private_subnets
      public_subnets  = module.vpc.public_subnets
      vpc_cidr_block  = module.vpc.vpc_cidr_block
    
      # EKS node group autoscaling bounds. You pay for node_min nodes at all times.
      node_min = 3
      node_max = 6
    
      # Set exactly one of these for DNS and TLS.
      route53_zone_id = "Z0123456789ABCDEFGHIJ"
      # certificate_arn = aws_acm_certificate_validation.n8n.certificate_arn
    }

Pass sensitive values such as `n8n_license_key` from a secrets manager, and store Terraform state in an encrypted, access-controlled backend because the module writes the key into the Helm release. Never hardcode the key in a `.tfvars` file you commit to version control.

Choose a starting size[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#choose-a-starting-size)

-------------------------------------------------------------------------------------------------------------------------------------------------------

The module ships three sizing examples. Use one as your starting point, then tune node type, count, and database size from there.

[small](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/small)
 (default)

[medium](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/medium)

[large](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/large)

Target scale

Development or small team

~5-15M executions/day

~50-60M+ executions/day

Node type

t3.xlarge

m6i.2xlarge

m7i.4xlarge

Nodes (min/max)

3/6

5/15

10/50

Database

RDS db.t3.small

RDS db.m6g.2xlarge

Aurora PostgreSQL I/O-Optimized

Redis

cache.t3.medium

cache.r6g.large

cache.r6g.large

Estimated cost/month (on-demand)

~$440

~$2,000

~$21,000+

Two topology variants are also available as examples: [split-ingress](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/split-ingress)
 (see [Customize the AWS infrastructure](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/customize-the-infrastructure#customer-managed-ingress)
) and [worker-pools](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/worker-pools)
, an alpha n8n feature that runs separate labelled worker pools.

Support[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#support)

-------------------------------------------------------------------------------------------------------------------------

This module is open source, maintained by the n8n Solutions team independently of n8n's Enterprise support offering. Report bugs or request features on [GitHub issues](https://github.com/n8n-io/terraform-aws-n8n/issues)
; the maintainers triage on a best-effort basis, with no SLA. For general n8n questions unrelated to the module, use the [n8n community forum](https://community.n8n.io/)
.

In this section[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#in-this-section)

-----------------------------------------------------------------------------------------------------------------------------------------

*   [Deploy your first n8n instance on AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/deploy-your-first-instance)
    : a step-by-step walkthrough, from an empty folder to a running instance.
    
*   [Scale and run at high availability on AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/scale-and-run-at-high-availability)
    : configure multi-main, worker autoscaling, and Redis high availability.
    
*   [Configure Enterprise features on AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/use-enterprise-features-on-aws)
    : wire up S3 execution data, Prometheus metrics, OpenTelemetry tracing, log streaming, and external secrets.
    
*   [Customize the AWS infrastructure](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/customize-the-infrastructure)
    : bring your own VPC, database, cache, or cluster, split ingress, or use a custom n8n image.
    
*   [Maintain and tear down the AWS deployment](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/maintain-and-tear-down)
    : manage encryption keys, verify database TLS, and configure deletion protection.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

*   [Use a cloud provider](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider)
    
*   [Deploy to AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws)
    
*   [DigitalOcean](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean)
    
*   [Heroku](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku)
    
*   [Hetzner Cloud](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner)
    
*   [Azure](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure)
    
*   [Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)
    
*   [Google Kubernetes Engine](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes)
    
*   [OpenShift Local (CRC)](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc)
    
*   [Use Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose)
    
*   [Enable queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
    

[PreviousDeploy to AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws)
[NextDeploy your first n8n instance on AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws-with-terraform/deploy-your-first-instance)

Last updated 5 days ago

Was this helpful?