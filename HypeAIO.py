import requests
import time
from pyppeteer_stealth import stealth
from dhooks import Webhook, Embed
from os import system
import glob
import asyncio
import csv
import config
from kith import kithmodule
from sportsworldmodule import sportsworldmodule
def main():
    print("\u001b[36m██╗░░██╗░░███╗░░░██████╗░██╗░░██╗    ██╗░░██╗██╗░░░██╗██████╗░███████╗")
    print("\u001b[36m██║░░██║░████║░░██╔════╝░██║░░██║    ██║░░██║╚██╗░██╔╝██╔══██╗██╔════╝")
    print("\u001b[36m███████║██╔██║░░██║░░██╗░███████║    ███████║░╚████╔╝░██████╔╝█████╗░░")
    print("\u001b[36m██╔══██║╚═╝██║░░██║░░╚██╗██╔══██║    ██╔══██║░░╚██╔╝░░██╔═══╝░██╔══╝░░")
    print("\u001b[36m██║░░██║███████╗╚██████╔╝██║░░██║    ██║░░██║░░░██║░░░██║░░░░░███████╗")
    print("\u001b[36m╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝    ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚══════╝")
    print("\u001b[0m")
    a_file = open("scratch.txt", "r")
    list_of_lines = a_file.readlines()
    license_key =  list_of_lines[2]
    x= license_key.split()
    license_key=((x[1]).replace('"',"")).replace(',','')
    headers = {
        'Authorization': f'Bearer pk_bwvPcnhnraLbzQU7DqKP0hHpSPDrEN5p'
    }
    response = requests.get(f'https://api.hyper.co/v4/licenses/{license_key}', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user=user_data['user']['username']
        print('Welcome ' + user_data['user']['username'] + '! Your Key is Valid')
    else:
        print("Your Key is Invalid")
        new_key = input("Enter Your Key:")
        a_file = open("scratch.txt", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[2] = f'    "key": "{new_key}",\n'
        a_file = open("scratch.txt", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        print("Bot will now close, please reopen to authorize key")
        time.sleep(5)
        quit()
    config.user=user
    system("title " + f"{user}'s HypeAIO[1.01][Tasks: {config.tasks}][{config.captcha} Pending Captcha][{config.cart} Carted][{config.success} Succesfully Checkout][{config.failed} Failed]")
    while True:
        print("\nMenu : ")
        print("""
        1 : Start Tasks 
        2 : Webhook Settings
        3 : Check for Updates
        0 : Exit"""
              )
        choice = input("\nEnter your choice : ")

        if choice == '1':
            print('The following Groups are availible')
            filelist = glob.glob("Task Groups/*.csv")
            number = 0
            for x in filelist:
                number += 1
                print(f'        {number}:{x}')
            choice = int(input("\nEnter your choice : ")) - 1
            print(f'You chose {filelist[choice]}')
            task_list = []
            with open(filelist[choice]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        task_list.append(f'{row[1]}({row[0]},"{row[3]}","{row[2]}","{row[4]}","{row[5]}")')
                        line_count += 1
            length = len(task_list)
            async def test(arg1):
                print(arg1)

            async def main():
                statements = []
                for x in task_list:
                    statements.append(eval(x))
                results = await asyncio.gather(*statements)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        elif choice == '2' :
            newwebhook=input('      Enter Webhook:')
            def testwebhook(newer):
                hook = Webhook(newer)
                embed = Embed(
                    description="Test Webhook",
                    color=0xE74C3C,
                    timestamp='now'  # sets the timestamp to current time
                )
                image1 = 'https://media.discordapp.net/attachments/782329553107288095/831936574341644298/AIO.png?width=567&height=567'
                embed.set_author(name='Hype AIO', icon_url=image1)
                embed.set_footer(text='Ready', icon_url=image1)
                embed.add_field(name="Webhook is ready and Working!", value="Lets cook!")
                embed.set_thumbnail(image1)
                hook.send(embed=embed)
                print("Successfully Added Webhook!")
                a_file = open("scratch.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[4] = f'    "user_webhook": "{newer}",\n'
                a_file = open("scratch.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()
            testwebhook(newwebhook)
        elif choice == '3' :
            print("In-Bot Updates are not yet supported, please check discord for updates")
        elif choice == '0':
            exit()
if __name__ == "__main__":
    main()
