










































































import threading
from colorama import Fore
from time import *
from util.common import *
import webbrowser

clear() # Clear console to stop colorama buggin

threads = [] # Set threads to 0


webbrowser.open('https://github.com/yeahitsnexus/neXus-BTC-Stealer')

print(Fore.RED + "                                      neXus Wallet Miner 2022")
thread_ammount = int(input(f"{Fore.BLUE}                                       Thread Ammount >> {Fore.RESET}")) # Enter thread ammount into console
input(f"\n{Fore.CYAN}                                       Press enter to get rich!{Fore.RESET}")
clear()


def run_stealer():
    for i in range(9999999999999999999999999): # Use for loop since its ALOT faster than a while loop
        address = random_string_generator() # Get random address
        if random.random() < percentage_chance:
            # Get random balance and convert to NOK
            bal = random_balance_generator()
            worth = BTC_check(bal)
            # Display address info
            print(f"\n\n{Fore.LIGHTCYAN_EX}CRACKED ADDRESS!!!{Fore.RESET}")
            print(f"{Fore.GREEN}{address} = {bal} BTC | {worth}{Fore.RESET}")
            write_address_info(address, bal, worth) # Write address info to txt file
            print(f"{Fore.LIGHTYELLOW_EX}Info for address saved to addressInfo.txt{Fore.RESET}")
            input(f"{Fore.CYAN}Press enter to exit miner. . .{Fore.RESET}")
            os._exit() # Exits code
        else:
            print(f"{Fore.CYAN}                                           {address} = SIKE NIGGER{Fore.RESET}")




setTitle(f'Cookies BTC Stealer') # Change title

# Set threads
for i in range(thread_ammount):
    t = threading.Thread(target=run_stealer)
    t.daemon = True
    threads.append(t)

# Start threads
for i in range(thread_ammount):
    threads[i].start()

# Join threads
for i in range(thread_ammount):
    threads[i].join()


