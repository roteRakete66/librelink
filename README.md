[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes%20(Fork)-green.svg)](https://github.com/roteRakete66/librelink/commits/main)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Validate with Hassfest](https://github.com/gillesvs/librelink/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/gillesvs/librelink/actions/workflows/hassfest.yaml)
[![Validate with HACS](https://github.com/gillesvs/librelink/actions/workflows/validate.yaml/badge.svg)](https://github.com/gillesvs/librelink/actions/workflows/validate.yaml)

# LibrelinkUp Integration for Home Assistant (Maintained Fork)

> **ℹ️ About this Fork**  
> This is an actively used and enhanced fork of the original [gillesvs/librelink](https://github.com/gillesvs/librelink) integration (which is no longer maintained).  
> 
> **Key Improvements & New Features in this Fork:**
> - **Dynamic App Version Resolution:** Replaced static/hardcoded app versions with automatic version calculation to prevent API rejections after upstream app updates.
> - **App Version Diagnostic Sensor:** Added a dedicated `sensor` entity exposing the resolved app version directly in Home Assistant for easy debugging and verification.
> - **FreeStyle Libre Plus Support (`is_plus` Switch):** Added a `switch` entity to toggle whether a *Libre Plus* sensor is used, automatically adjusting the calculated sensor lifespan (+1 day).

[integration_librelink]: https://github.com/gillesvs/librelink.git
[buymecoffee]: https://www.buymeacoffee.com/gillesvs

**This integration will set up the following platforms for each patient linked to the librelinkUp account.**

| Platform | Description |
| :--- | :--- |
| `sensor` | **Show info from LibreLinkUp API & Integration:**<br>• **Active Sensor (in days):** All information about your sensor (state is days since activation, accounting for the *Plus* toggle).<br>• **Glucose Measurement (in mg/dL):** Measured value every minute.<br>• **Glucose Trend:** Plain text + icon.<br>• **Minutes since update (in min):** Time elapsed since last reading.<br>• **App Version *(New)*:** Displays the dynamically calculated LibreLinkUp app version for verification. |
| `binary_sensor` | **Measure high and low thresholds:**<br>• **Is High:** `True` or `False`<br>• **Is Low:** `True` or `False` |
| `switch` | **Configuration toggles *(New)*:**<br>• **Is Plus:** Enables *FreeStyle Libre Plus* mode, extending the expected sensor runtime by 1 day. |

## Illustration with a custom:mini-graph-card

![image](https://github.com/gillesvs/librelink/assets/51242147/bfed1b2b-dbf7-4666-a202-885ff3db67b8)

And the yaml if you like this card:
https://github.com/gillesvs/librelink/blob/main/custom_components/librelink/mini-graph-glucose.yml


## Installation

1. Add this repository URL as a custom repository in HACS
2. Restart Home Assistant
3. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Librelink"

## Configuration is done in the UI

You need a librelinkUp account to use this integration
User must have accepted Abbott user agreement in the librelinkUp app for the integration to work.

- Use username (mail) and password of the librelinkUp account.
- A token will be retreived for the duration of the HA session.


## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

<a href="https://www.buymeacoffee.com/roan7dxbbb" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
