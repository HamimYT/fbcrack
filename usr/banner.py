import time
g="\33[0;32m"
lg="\33[32;1m"
b="\33[0;36m"
lb="\33[36;1m"
r="\33[31;1m"
w="\33[37;1m"
b="\33[30;1m"
y ="\33[33;1m"
C = "\033[94;m"
G = "\033[92;m"
r = "\033[0;m"
P = "\033[93;m"


def bersih():
    os.system('clear')
    bersih()


def banner():
    print("""
    ____________________________
   |  HACKER CROTTT DI DALAM    |
   |  AUTHOR : Hanief Aktivisme |
   |  Youtube : Hanief Aktivis  |
|About : Dunia Teknologi Dan Hacking|
 ____________________________________
            """.format(C,r,G))


def menu():
    print(f"{C}[1]{lg} Hack From FriendList")
    time.sleep(1)
    print(f"{C}[2]{lg} Hack From Likes On Post")
    time.sleep(1)
    print(f"{C}[3]{lg} Hack By Search Name")
    time.sleep(1)
    print(f"{C}[4]{lg} Hack From Group (Hanya 100 User)")
    time.sleep(1)
    print(f"{C}[5]{lg} Hack From Friend FriendList")
    time.sleep(1)
    print(f"{C}[6]{lg} Hack From Hashtag ")
    time.sleep(1)
    print(f"{C}[7]{lg} Hack Ulang Dari result")
    time.sleep(1)

