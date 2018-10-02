#!/usr/bin/env python3

import locale
import os
import subprocess
from typing import List, Dict

import dotenv
import requests
from dialog import Dialog

dotenv.load_dotenv()


class Jump:
    items = []
    formatted_menu_items = []

    def __init__(self) -> None:
        self.d: Dialog = Dialog()
        self.get_item_list()
        self.run()

    def get_item_list(self) -> None:
        secret_key: str = os.environ.get('AUTH_KEY')
        extra_headers: Dict = {}

        if secret_key is not None:
            extra_headers[os.environ.get('AUTH_HEADER')] = secret_key

        self.items: List = requests.get(os.environ.get('ENDPOINT'), headers=extra_headers).json()['items']

    def format_items(self, items: List, servers: bool = False) -> None:
        self.formatted_menu_items: List = []

        for item in items:
            if servers is False and item['in_jumpgate'] is False:
                pass
            else:
                self.formatted_menu_items.append((item['name'] if not servers else item['display_name'], ''))

    def create_menu(self, title: str, items: List, cancel_label: str = 'Back') -> tuple:
        return self.d.menu(
            title,
            choices=items,
            menu_height=15,
            cancel_label=cancel_label,
        )

    def get_server_info(self, app: str, server: str = None) -> List or Dict:  # TODO: split function
        for item in self.items:
            if item['name'] == app:
                if server is not None:
                    for s in item['servers']:
                        if s['display_name'] == server:
                            return s
                else:
                    return item

    def run(self):
        self.format_items(self.items)

        code, app = self.create_menu('Choose an application', self.formatted_menu_items, 'Exit')

        if code == self.d.OK:
            self.format_items(self.get_server_info(app)['servers'], True)

            code, server = self.create_menu('Choose a server', self.formatted_menu_items)

            if code == self.d.CANCEL:
                self.run()
            else:
                server_info = self.get_server_info(app, server)

                if server_info['is_serverpilot']:
                    command = 'ssh -p{} {}@{} -t "cd /srv/users/serverpilot/apps/{}; exec /bin/bash -l"'
                else:
                    command = 'ssh -p{} {}@{}'

                subprocess.call(
                    command.format(
                        server_info['port'],
                        server_info['user'],
                        server_info['ip'],
                        app
                    ),
                    shell=True,
                )

                self.run()


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')

    try:
        Jump()
    except KeyboardInterrupt:
        pass
