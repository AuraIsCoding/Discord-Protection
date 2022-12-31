import requests
import colorama
import os
import sys
import time
import random
from pystyle import *
from colorama import Fore
from time import sleep

sys.stdout.write("\x1b]2;Aura V1 | Protect Your Token\x07")
os.system(f'mode con: cols=103 lines=25')

class bot:

    def __init__ (self):

        def menu(self):

            try:

                ui = '''

          _____                                   
         /  _  \  __ ______________               
        /  /_\  \|  |  \_  __ \__  \              
       /    |    \  |  /|  | \// __ \_            
       \____|__  /____/ |__|  (____  /            
               \/                  \/             
__________                __                 __   
\______   \_______  _____/  |_  ____   _____/  |_ 
 |     ___/\_  __ \/  _ \   __\/ __ \_/ ___\   __|
 |    |     |  | \(  <_> )  | \  ___/\  \___|  |  
 |____|     |__|   \____/|__|  \___  >\___  >__|  
                                   \/     \/      

                    '''
                
                print(
                    Colorate.Vertical(
                        Colors.DynamicMIX((Col.blue, Col.purple)), Center.XCenter(ui)
                    )
                )

                self.token = input(f'              Whats Your Token? ')
                self.password = input(f'              Whats Your Password? ')
                self.time = input(f'              Time Between Each Pass Switching: ')

                os.system('cls')

            except:
                print('How did you get this error.')

        
        def getpasswords(self):
            try:
                    self.passwords = open('passwords.txt', 'r').read().splitlines()
                    self.newpassword = random.choice(self.passwords)
            except:
                 print(f'Failed To Get Passwords')


        def changepass(self):

            try:
                getpasswords(self)

                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': self.token,
                    'content-type': 'application/json',
                    'origin': 'https://discord.com',
                    'referer': 'https://discord.com/channels/@me',
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.54',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDguMC4xNDYyLjU0IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA4LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNjU0ODUsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                }

                json_data = {
                    'password': self.password,
                    'new_password': self.newpassword,
                }

                response = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json_data)

                print(f'{Fore.RESET}[{Fore.BLUE}+{Fore.RESET}] Switched Your Token')
                print(f'{Fore.RESET}[{Fore.BLUE}+{Fore.RESET}] New Pass: {self.newpassword}')
                print(f'{Fore.RESET}[{Fore.BLUE}+{Fore.RESET}] New Token: ' + response.json()['token'])

                self.token = response.json()['token']
                self.password = self.newpassword
                print(f'{Fore.RESET}[{Fore.GREEN}*{Fore.RESET}] Waiting: ' + self.time)

                print('')
                
                time.sleep(int(self.time))

                changepass(self)
            
            except:
                print(f'{Fore.RESET}[{Fore.RED}-{Fore.RESET}] Failed To Switch Your Token !')
                exit()

        menu(self)
        changepass(self)

bot()
