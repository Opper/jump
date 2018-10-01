## Jump

### Intro 

Utility that builds a 2-level menu based on applications and their available environments. The setup that we have is that
this utility resides on a 'jump' server and every time a user connects to that server (via SSH), the menu script is 
executed. 

In our current setup, there is 2 kinds of servers: one type which has serverpilot installed and another one which is 
a vanilla ubuntu installation. In the first case, there's a specific folder structure that needs to be taken in consideration

This script also handles some applications/servers not being in the jumpgate.

The menu is built based on a JSON response from a server. The response looks like this:

```json
{
    "items": [
        {
            "id": "b84b07c8-738e-4088-969f-0ee4c822fd3a",
            "in_jumpgate": false,
            "name": "test-app",
            "servers": [
                {
                    "display_name": "Staging",
                    "id": "939bf2ce-d0e0-42b8-8600-f7f7ef5db72b",
                    "ip": "1.2.3.4",
                    "is_serverpilot": true,
                    "name": "staging",
                    "port": 222,
                    "user": "serverpilot"
                },
                {
                    "display_name": "Production",
                    "id": "6a7f9169-5fe3-49d2-8eea-bfafcc53f4de",
                    "ip": "1.2.3.4",
                    "is_serverpilot": false,
                    "name": "prod",
                    "port": 222,
                    "user": "root"
                }
            ]
        }, {
            "id": "81a1afa3-f610-4b64-935f-7e93c025209b",
            "in_jumpgate": true,
            "last_backup": 1538352010,
            "name": "another-test-app",
            "servers": [
                {
                    "created_at": 1533644177,
                    "display_name": "Staging",
                    "id": "939bf2ce-d0e0-42b8-8600-f7f7ef5db72b",
                    "ip": "1.2.3.4",
                    "is_serverpilot": true,
                    "name": "staging",
                    "port": 222,
                    "updated_at": 1533808205,
                    "user": "serverpilot"
                }, {
                     "created_at": 1533644177,
                     "display_name": "Acceptance",
                     "id": "939bf2ce-d0e0-42b8-8600-f7f7ef5db72b",
                     "ip": "1.2.3.4",
                     "is_serverpilot": true,
                     "name": "acceptance",
                     "port": 222,
                     "updated_at": 1533808205,
                     "user": "serverpilot"
                 }
            ]
        }
    ]
}
```

This creates a menu like so:

![](docs/img/app-menu.png)

Note that only the 2nd item is shown because the first one has the property `in_jumpgate` set to False. When you select
an app, you get a list of its available servers (environments):

![](docs/img/env-menu.png)

After selecting an item the SSH connection will be forwarded to that server.


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
