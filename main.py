import requests
import colorama
import ctypes
import random
from colorama import Fore , Back , Style
import threading
colorama.init(autoreset = True)


ctypes.windll.kernel32.SetConsoleTitleW(f"[\nR\n\n\ne\nc\n\n\n.\nN\n\n\ne\n\n\nt\n \n\nU\n\ns\n\ne\nr\nn\na\n\nm\n\ne \nC\nh\n\ne\n\n\n\n\n\nc\n\nke\n\n\nr]\n\n b\n\n\ny i\n\nr\n\nt\n\nc\n\n\no \n\n|  \ni\n\n\nr\nt\n\nc\n\no\n#\n0\n7\n0\n\n2 | http\n\n\n\n\ns:/\n\n/d\n\ni\ns\n\ncor\nd.\n\ng\ng/yt\nrT8\n\n3\ngh\n\nMp")
print(f"""{Fore.MAGENTA}
 _____________________________________________________________________________
/                                                                             \\
|                      {Fore.LIGHTBLUE_EX}Rec.Net Username Checker by irtco{Fore.MAGENTA}                      |
\_____________________________________________________________________________/
/                                                                             \\
|                              {Fore.LIGHTBLUE_EX}Discord:irtco#702{Fore.MAGENTA}                              |
\_____________________________________________________________________________/
/                                                                             \\
|                        {Fore.LIGHTBLUE_EX}https://discord.gg/ytrT83ghMp{Fore.MAGENTA}                        |
\_____________________________________________________________________________/
""")

num = input(f"length?")
ABC = 'abcdefghigklmnopqrstuvwxyz123456789_-.'
i=1
Vaild = 0
def main():
  while i<5:
            listnames = str("".join(random.choice(ABC)for x in range(int(num))))
            ck= requests.get(f"https://accounts.rec.net/account?username={listnames}")
            if ck.status_code ==404:
             print(f"{Fore.GREEN} {listnames} Vaild")                                                                                                                                                                                                                                                                                                                                                    # by irtco
             with open("vaild.txt","a+") as file:
              file.write(listnames)
              file.write("\n")
              
              
            else:
             print(f"{Fore.RED} {listnames} invaild")
             

for _ in range(7):
   [].append(threading.Thread(target=main).start())
for _2 in []:
   _2.join()
main()