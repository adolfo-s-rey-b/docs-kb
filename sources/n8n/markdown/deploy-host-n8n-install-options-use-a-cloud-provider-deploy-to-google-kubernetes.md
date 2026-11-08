For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes.md)
.

Google Cloud offers several options suitable for hosting n8n, including Cloud Run (optimized for running containers), Compute Engine (VMs), and Kubernetes Engine (containers running with Kubernetes).

This guide uses the Google Kubernetes Engine (GKE) as the hosting option. If you want to use Cloud Run, refer to [these instructions](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)
.

Most of the steps in this guide use the Google Cloud UI, but you can also use the [gcloud command line tool](https://cloud.google.com/sdk/gcloud/)
 instead to undertake all the steps.

Prerequisites[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#prerequisites)

------------------------------------------------------------------------------------------------------------------------------------

*   The [gcloud command line tool](https://cloud.google.com/sdk/gcloud/)
    
*   The [gke-gcloud-auth-plugin](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke)
     (install the gcloud CLI first)
    

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

Create project[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#create-project)

--------------------------------------------------------------------------------------------------------------------------------------

GCP encourages you to create projects to logically organize resources and configuration. Create a new project for your n8n deployment from your Google Cloud Console: select the project dropdown menu and then the **NEW PROJECT** button. Then select the newly created project. As you follow the other steps in this guide, make sure you have the correct project selected.

Enable the Kubernetes Engine API[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#enable-the-kubernetes-engine-api)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GKE isn't enabled by default. Search for "Kubernetes" in the top search bar and select "Kubernetes Engine" from the results.

Select **ENABLE** to enable the Kubernetes Engine API for this project.

Create a cluster[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#create-a-cluster)

------------------------------------------------------------------------------------------------------------------------------------------

From the [GKE service page](https://console.cloud.google.com/kubernetes/list/overview)
, select **Clusters** > **CREATE**. Make sure you select the "Standard" cluster option, n8n doesn't work with an "Autopilot" cluster. You can leave the cluster configuration on defaults unless there's anything specifically you need to change, such as location.

Set Kubectl context[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#set-kubectl-context)

------------------------------------------------------------------------------------------------------------------------------------------------

The rest of the steps in this guide require you to set the GCP instance as the Kubectl context. You can find the connection details for a cluster instance by opening its details page and selecting **CONNECT**. The displayed code snippet shows a connection string for the gcloud CLI tool. Paste and run the code snippet in the gcloud CLI to change your local Kubernetes settings to use the new gcloud cluster.

Clone configuration repository[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#clone-configuration-repository)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kubernetes and n8n require a series of configuration files. You can clone these from [this repository](https://github.com/n8n-io/n8n-hosting)
 locally. The following steps explain the file configuration and how to add your information.

Clone the repository with the following command:

Copy

    git clone https://github.com/n8n-io/n8n-hosting.git

And change directory:

Copy

    cd n8n-hosting/kubernetes

Configure Postgres[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#configure-postgres)

----------------------------------------------------------------------------------------------------------------------------------------------

For larger scale n8n deployments, Postgres provides a more robust database backend than SQLite.

### Create a volume for persistent storage[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#create-a-volume-for-persistent-storage)

To maintain data between pod restarts, the Postgres deployment needs a persistent volume. Running Postgres on GCP requires a specific Kubernetes Storage Class. You can read [this guide](https://cloud.google.com/architecture/deploying-highly-available-postgresql-with-gke)
 for specifics, but the `storage.yaml` manifest creates it for you. You may want to change the regions to create the storage in under the `allowedTopologies` > `matchedLabelExpressions` > `values` key. By default, they're set to `us-central`.

Copy

    …
    allowedTopologies:
      - matchLabelExpressions:
          - key: failure-domain.beta.kubernetes.io/zone
            values:
              - us-central1-b
              - us-central1-c

### Postgres environment variables[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#postgres-environment-variables)

Postgres needs some environment variables set to pass to the application running in the containers.

The example `postgres-secret.yaml` file contains placeholders you need to replace with your own values. Postgres will use these details when creating the database..

The `postgres-deployment.yaml` manifest then uses the values from this manifest file to send to the application pods.

Configure n8n[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#configure-n8n)

------------------------------------------------------------------------------------------------------------------------------------

### Create a volume for file storage[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#create-a-volume-for-file-storage)

While not essential for running n8n, using persistent volumes is required for:

*   Using nodes that interact with files, such as the binary data node.
    
*   If you want to persist [manual n8n encryption keys](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)
     between restarts. This saves a file containing the key into file storage during startup.
    

The `n8n-claim0-persistentvolumeclaim.yaml` manifest creates this, and the n8n Deployment mounts that claim in the `volumes` section of the `n8n-deployment.yaml` manifest.

Copy

    …
    volumes:
      - name: n8n-claim0
        persistentVolumeClaim:
          claimName: n8n-claim0
    …

### Pod resources[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#pod-resources)

[Kubernetes lets you](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
 optionally specify the minimum resources application containers need and the limits they can run to. The example YAML files cloned above contain the following in the `resources` section of the `n8n-deployment.yaml` and `postgres-deployment.yaml` files:

Copy

    …
    resources:
      requests:
        memory: "250Mi"
      limits:
        memory: "500Mi"
    …    

This defines a minimum of 250mb per container, a maximum of 500mb, and lets Kubernetes handle CPU. You can change these values to match your own needs. As a guide, here are the resources values for the n8n cloud offerings:

Tier

RAM

CPU

Starter

320mb

10 millicore burstable

Pro (10k executions)

640mb

20 millicore burstable

Pro (50k executions)

1280mb

80 millicore burstable

### Optional: Environment variables[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#optional-environment-variables)

You can configure n8n settings and behaviors using environment variables.

Create an `n8n-secret.yaml` file. Refer to [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
 for n8n environment variables details.

Deployments[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#deployments)

--------------------------------------------------------------------------------------------------------------------------------

The two deployment manifests (`n8n-deployment.yaml` and `postgres-deployment.yaml`) define the n8n and Postgres applications to Kubernetes.

The manifests run PostgreSQL 18. Setting up for the first time needs nothing extra.

If you already have a database running an older PostgreSQL major version, don't apply this to it. PostgreSQL 18 can't open a data directory written by an older major version, and moving the folder doesn't help. The pod stays in `CrashLoopBackOff` with `database files are incompatible with server`. PostgreSQL leaves your data alone, and you can pin the image back to the version you were on.

To move an existing database across, follow the official [PostgreSQL upgrade guide](https://www.postgresql.org/docs/18/upgrading.html)
 first.

The manifests define the following:

*   Send the environment variables defined to each application pod
    
*   Define the container image to use
    
*   Set resource consumption limits with the `resources` object
    
*   The `volumes` defined earlier and `volumeMounts` to define the path in the container to mount volumes.
    
*   Scaling and restart policies. The example manifests define one instance of each pod. You should change this to meet your needs.
    

Services[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#services)

--------------------------------------------------------------------------------------------------------------------------

The two service manifests (`postgres-service.yaml` and `n8n-service.yaml`) expose the services to the outside world using the Kubernetes load balancer using ports 5432 and 5678 respectively.

Send to Kubernetes cluster[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#send-to-kubernetes-cluster)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

Send all the manifests to the cluster with the following command:

Copy

    kubectl apply -f .

**Namespace error**

You may see an error message about not finding an "n8n" namespace as that resources isn't ready yet. You can run the same command again, or apply the namespace manifest first with the following command:

Copy

    kubectl apply -f namespace.yaml

Set up DNS[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#set-up-dns)

------------------------------------------------------------------------------------------------------------------------------

n8n typically operates on a subdomain. Create a DNS record with your provider for the subdomain and point it to the IP address of the n8n service. Find the IP address of the n8n service from the **Services & Ingress** menu item of the cluster you want to use under the **Endpoints** column.

**GKE and IP addresses**

[Read this GKE tutorial](https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip#configuring_your_domain_name_records)
 for more details on how reserved IP addresses work with GKE and Kubernetes resources.

Delete resources[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#delete-resources)

------------------------------------------------------------------------------------------------------------------------------------------

Remove the resources created by the manifests with the following command:

Copy

    kubectl delete -f .

Next steps[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#next-steps)

------------------------------------------------------------------------------------------------------------------------------

*   Learn more about [configuring](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
     and [scaling](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling)
     n8n.
    
*   Or explore using n8n: try the [Quickstarts](https://docs.n8n.io/build-your-first-workflow)
    .
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------

*   [Use a cloud provider](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider)
    
*   [DigitalOcean](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean)
    
*   [Heroku](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku)
    
*   [Hetzner Cloud](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner)
    
*   [AWS](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws)
    
*   [Azure](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure)
    
*   [Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)
    
*   [OpenShift Local (CRC)](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc)
    
*   [Use Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose)
    

[PreviousDeploy to Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)
[NextDeploy to OpenShift Local (CRC)](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc)

Last updated 10 days ago

Was this helpful?