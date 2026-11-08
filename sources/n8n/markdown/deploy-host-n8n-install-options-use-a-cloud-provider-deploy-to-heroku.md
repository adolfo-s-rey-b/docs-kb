For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku.md)
.

This hosting guide shows you how to self-host n8n on Heroku. It uses:

*   [Docker Compose](https://docs.docker.com/compose/)
     to create and define the application components and how they work together.
    
*   [Heroku's PostgreSQL service](https://devcenter.heroku.com/categories/heroku-postgres)
     to host n8n's data storage.
    
*   A **Deploy to Heroku** button offering a one click, with minor configuration, deployment.
    

**Self-hosting knowledge prerequisites**

Self-hosting n8n requires technical knowledge, including:

*   Setting up and configuring servers and containers
    
*   Managing application resources and scaling
    
*   Securing servers and applications
    
*   Configuring n8n
    

n8n recommends self-hosting for expert users. Mistakes can lead to data loss, security issues, and downtime. If you aren't experienced at managing servers, n8n recommends [n8n Cloud](https://n8n.io/cloud/)
.

**Stable and Beta versions**

n8n releases a new minor version most weeks. The `stable` version is for production use. `beta` is the most recent release. The `beta` version may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12)
.

Current `stable`: 2.46.6 Current `beta`: 2.47.2

Use the deployment template to create a Heroku project[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#use-the-deployment-template-to-create-a-heroku-project)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The quickest way to get started with deploying n8n to Heroku is using the **Deploy to Heroku** button:

[![Deploy](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2Fwww.herokucdn.com%2Fdeploy%2Fbutton.svg&width=300&dpr=3&quality=100&sign=d67952b762f84565199f18e1b3b3e8b5&sv=3)](https://dashboard.heroku.com/new?template=https://github.com/n8n-io/n8n-heroku/tree/main)

This opens the **Create New App** page on Heroku. Set a name for the project, and choose the region to deploy the project to.

### Configure environment variables[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#configure-environment-variables)

Heroku pre-fills the configuration options defined in the `env` section of the `app.json` file, which also sets default values for the environment variables n8n uses.

You can change any of these values to suit your needs. You must change the following values:

*   **N8N\_ENCRYPTION\_KEY**, which n8n uses to [encrypt user account details](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
     before saving to the database.
    
*   **WEBHOOK\_URL** should match the application name you create to ensure that webhooks have the correct URL.
    

### Deploy n8n[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#deploy-n8n)

Select **Deploy app**.

After Heroku builds and deploys the app it provides links to **Manage App** or **View** the application.

**Heroku and DNS**

Refer to the [Heroku documentation](https://devcenter.heroku.com/categories/networking-dns)
 to find out how to connect your domain to a Heroku application.

Changing the deployment template[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#changing-the-deployment-template)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

You can make changes to the deployment template by forking the [repository](https://github.com/n8n-io/n8n-heroku)
 and deploying from you fork.

### The Dockerfile[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#the-dockerfile)

By default the Dockerfile pulls the latest n8n image, if you want to use a different or fixed version, then update the image tag on the top line of the `Dockerfile`.

### Heroku and exposing ports[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#heroku-and-exposing-ports)

Heroku doesn't allow Docker-based applications to define an exposed port with the `EXPOSE` command. Instead, Heroku provides a `PORT` environment variable that it dynamically populates at application runtime. The `entrypoint.sh` file overrides the default Docker image command to instead set the port variable that Heroku provides. You can then access n8n on port 80 in a web browser.

**Docker limitations with Heroku**

[Read this guide](https://devcenter.heroku.com/articles/container-registry-and-runtime#unsupported-dockerfile-commands)
 for more details on the limitations of using Docker with Heroku.

### Configuring Heroku[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#configuring-heroku)

The `heroku.yml` file defines the application you want to create on Heroku. It consists of two sections:

*   `setup` > `addons` defines the Heroku addons to use. In this case, the PostgreSQL database addon.
    
*   The `build` section defines how Heroku builds the application. In this case it uses the Docker buildpack to build a `web` service based on the supplied `Dockerfile`.
    

Next steps[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#next-steps)

-------------------------------------------------------------------------------------------------------------------

*   Learn more about [configuring](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
     and [scaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
     n8n.
    
*   Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/build-your-first-workflow)
    .
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku#related-resources)

---------------------------------------------------------------------------------------------------------------------------------

*   [Use a cloud provider](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider)
    
*   [DigitalOcean](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean)
    
*   [Hetzner Cloud](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner)
    
*   [AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws)
    
*   [Azure](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure)
    
*   [Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)
    
*   [Google Kubernetes Engine](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes)
    
*   [OpenShift Local (CRC)](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc)
    
*   [Use Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose)
    

[PreviousDeploy to Digital Ocean](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean)
[NextDeploy to Hetzner](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner)

Last updated 10 days ago

Was this helpful?