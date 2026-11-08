For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n.md)
.

You can self-host n8n on your own infrastructure, on-premises, or in a private cloud, using Docker Compose, one-line setup, or other deployment methods. Not sure if self-hosting is right for you? See [Choose how to use n8n](https://docs.n8n.io/choose-how-to-use-n8n)
.

**Don't want to read the docs? Run this:**

Copy

    curl -fsSL https://get.n8n.io | sh

Requires Docker on Linux or macOS (or WSL on Windows). Sets up n8n locally in one step. See the [one-line setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup)
 for what it does, or keep reading to compare every installation method.

All self-hosted installations use the same core product. Without a license key, n8n runs as the free Community edition. Adding a Business or Enterprise license key enables those editions. See [Compare editions](https://docs.n8n.io/deploy/host-n8n/community-edition-features)
 for the differences between the self-hosted editions.

In this section[](https://docs.n8n.io/deploy/host-n8n#in-this-section)

-----------------------------------------------------------------------

*   [Install options](https://docs.n8n.io/deploy/host-n8n/install-options)
    : set up n8n with Docker, npm, Docker Compose, or a cloud provider.
    
*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    : manage databases, environment variables, users, licenses, and security settings.
    
*   [Keep n8n running](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running)
    : monitor, log, trace, and update your instance.
    
*   [Understand the architecture](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture)
    : learn how n8n works and how it structures its database.
    
*   [Deploy as an OEM integration](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration)
    : embed n8n's interface inside your own product's UI.
    
*   [Deploy with the AI starter kit](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit)
    : use n8n's curated self-hosted AI Starter Kit.
    
*   [Compare editions](https://docs.n8n.io/deploy/host-n8n/community-edition-features)
    : compare the self-hosted Community, Business, and Enterprise editions.
    

Choose your installation method[](https://docs.n8n.io/deploy/host-n8n#choose-your-installation-method)

-------------------------------------------------------------------------------------------------------

Select the installation method that best fits your technical requirements and infrastructure:

*   **One-line setup**
    
    **Best for:** Quick setup with minimal configuration.
    
    **Requirements:** Linux or macOS system with curl installed.
    
    Automated installation script that handles all dependencies and configuration for you.
    
    [One-line setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup)
    
*   **Docker Compose**
    
    **Best for:** Production deployments with databases and additional services.
    
    **Requirements:** Docker and Docker Compose installed on your system.
    
    Multi-container setup ideal for robust deployments with persistent data and scalability.
    
    [Docker Compose guide](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose)
    
*   **AWS**
    
    Deploy on Amazon Web Services using EC2, ECS, or other AWS services.
    
    [AWS setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws)
    
*   **Azure**
    
    Host n8n on Microsoft Azure with container instances or virtual machines.
    
    [Azure setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure)
    
*   **Google Cloud**
    
    Run n8n on Google Cloud using Cloud Run or Kubernetes Engine.
    
    [Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)
     | [Kubernetes Engine](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes)
    
*   **DigitalOcean**
    
    Simple droplet-based hosting ideal for small to medium deployments.
    
    [DigitalOcean setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean)
    
*   **Hetzner**
    
    Cost-effective European hosting option with excellent performance.
    
    [Hetzner setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner)
    
*   **Heroku**
    
    Platform-as-a-service option for quick deployment with minimal configuration.
    
    [Heroku setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku)
    
*   **OpenShift**
    
    Enterprise Kubernetes platform for containerized applications.
    
    [OpenShift setup guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc)
    
*   **npm**
    
    **Best for:** Local development or testing.
    
    **Requirements:** Node.js installed on your system.
    
    npm installation is deprecated from n8n 3.0. Consider using Docker Compose or one-line setup instead.
    
    Installs n8n directly using Node Package Manager. Quick to set up but requires managing Node.js versions and dependencies yourself.
    
    [npm installation guide](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm)
    

Related resources[](https://docs.n8n.io/deploy/host-n8n#related-resources)

---------------------------------------------------------------------------

*   [Deploy](https://docs.n8n.io/deploy)
    
*   [Use n8n Cloud](https://docs.n8n.io/deploy/use-n8n-cloud)
    

[PreviousDownload workflows](https://docs.n8n.io/deploy/use-n8n-cloud/download-workflows)
[NextInstall options](https://docs.n8n.io/deploy/host-n8n/install-options)

Last updated 10 days ago

Was this helpful?