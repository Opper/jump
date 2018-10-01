### Jump

Utility that builds a 2-level menu based on applications and their available environments.

### Installation

To install the jumpgate script, run the following command:

`$ wget https://github.com/opper/jump/blob/master/install.sh | bash`

This will install the jumpgate in the following directory: `/opt/jump`. After the installation is done, create and
populate an `.env` file in the root directory of the script with the following values:

- AUTH_KEY: If you use any kind of authentication when retrieving the items. If not, leave it empty.
- AUTH_HEADER: If you use authentication (via a header) set this to the value of your header.
- ENDPOINT: API endpoint from where to fetch the list of applications.

After this is done, you can start using the jumpgate.

#### Todo:

 - add documentation and examples
 - add install script
