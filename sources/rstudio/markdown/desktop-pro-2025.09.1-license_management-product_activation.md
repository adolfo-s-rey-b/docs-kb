**Documentation Version**

You are viewing version **2025.09.1**. [View the latest version](https://docs.posit.co/ide/desktop-pro/)
.

Product Activation[](https://docs.posit.co/ide/desktop-pro/2025.09.1/license_management/product_activation.html#product-activation)

------------------------------------------------------------------------------------------------------------------------------------

An RStudio Desktop Pro license is delivered as a License File (.lic).

### Activation Basics[](https://docs.posit.co/ide/desktop-pro/2025.09.1/license_management/product_activation.html#activation-basics)

As the evaluation period or a previously installed license nears expiration, a warning bar will appear at the bottom of RStudio.

![](https://docs.posit.co/ide/desktop-pro/2025.09.1/images/license-will-expire-bar.png)

License Expiring Soon Warning Bar

When a license expires, the warning bar will indicate that the license has expired. If the license expires entirely while RStudio is being used, an error is displayed. At this point, you can select a new license or quit the application.

![](https://docs.posit.co/ide/desktop-pro/2025.09.1/images/no-license.png)

License Expired Dialog

**Do not let users continue using the product right up to the end of this grace period, as it could result in lost work.**

Purchase a license to continue using the product. The license is delivered as a license file (.lic). We recommend activating RStudio Desktop Pro using the license file to take full advantage of your [purchased RStudio Desktop license terms](https://posit.co/about/software-license-descriptions/)
.

It is not necessary to wait until the evaluation period has expired to install a license.

![](https://docs.posit.co/ide/desktop-pro/2025.09.1/images/expired-license.png)

Manage License Dialog Showing Select License File

### License File Activation[](https://docs.posit.co/ide/desktop-pro/2025.09.1/license_management/product_activation.html#license-file-activation)

Once you receive a license file (.lic) from RStudio, click _Select license file…_ in the **Manage RStudio License** dialog, and browse to the file.

Once the file is imported and validated, RStudio Desktop Pro will be ready for use. The **Manage RStudio License** dialog will now show details on the installed license, and buttons for updating or removing the license.

_Select new license file…_ will replace the existing license with that from a new license file.

_Remove license…_ will delete the current license, and a new license will need to be installed to continue using the product (if the evaluation period has also expired).

![](https://docs.posit.co/ide/desktop-pro/2025.09.1/images/valid-license-file.png)

Manage License Dialog Showing License File Details

### Preconfiguring License File Location[](https://docs.posit.co/ide/desktop-pro/2025.09.1/license_management/product_activation.html#preconfiguring-license-file-location)

Instead of requiring users to manually select a license file, an administrator can set the environment variable `RSTUDIO_LICENSE_FILE` to the full path to the license file and RStudio Desktop Pro will use that license file automatically. For example: `RSTUDIO_LICENSE_FILE=C:\Users\Fred\rstudio-license.lic`.

The environment variable must remain set, and the license file available in the specified location, whenever RStudio is used.

Back to top