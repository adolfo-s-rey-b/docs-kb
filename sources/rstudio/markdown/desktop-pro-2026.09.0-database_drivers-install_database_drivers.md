**Documentation Version**

You are viewing version **2026.09.0**. [Verify that this is the latest version](https://docs.posit.co/supported-versions/rstudio.html)
.

Copy for LLM View as Markdown

RStudio Professional Database Drivers
=====================================

The RStudio Pro Database Drivers are installed on-demand by the RStudio IDE. Doing so requires internet connectivity.

To test this, start RStudio and invoke the **New Connection** dialog from the Connections pane.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/connections-pane.png)

New Connection Button on Connections Pane Toolbar

The **New Connection** dialog shows the available database drivers.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/new-connection.png)

New Connections Dialog Showing Database Drivers

Select one, such as MySQL. RStudio first offers to install or update the necessary packages for database connectivity (unless previously installed). These packages apply to all database drivers, so this step will only happen once.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/update-drivers.png)

Dialog Asking Permission to Install Database Connectivity Packages

Proceed, and the packages will download and install.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/package-install.png)

Installing Database Packages Progress Dialog

Once packages are installed, the prompt for installation of the database driver itself will appear.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/my-sql.png)

Dialog Asking Permission to Install a Database Driver

On Windows, each driver needs to make changes to the registry, and will require administrator access.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/uac.png)

Windows User Account Control Dialog

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/registry.png)

Registry Editor Asking Permission to Modify Registry

Finally, the database connection can be configured by the user. On subsequent attempts to create a connection with this driver, RStudio will go straight to this screen.

![](https://docs.posit.co/ide/desktop-pro/2026.09.0/images/create-sql-connection.png)

Dialog for Creating a Connection with a Database Driver

Back to top