# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import requests
import Hazard

from colorama import Fore
from util.plugins.common import setTitle, print_slow, getheaders, proxy

def MassDM(token, channels, Message):
    # with open("yes.js", "w", encoding='utf-8') as f:
    #     f.write(str(channels))
    for channel in channels:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
            try:
                setTitle(f"Messaging "+user)
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                    proxies={"http": f'{proxy()}'},
                    headers={'Authorization': token},
                    data={"content": f"{Message}"})
                print(f"{Fore.RED}Messaged: {Fore.WHITE}"+user+Fore.RESET)
            except Exception as e:
                print(f"The following error has been encountered and is being ignored: {e}")