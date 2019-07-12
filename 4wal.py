import sys
import json
import requests
import urllib
import os
from random import randint, choice

sys.stdout.write("\033[H\033[J") # clear screen at program start

logo = """
  ▒▒▒▒▒▒            ▒▒▒▒▒▒
▒▒██████▒▒        ▒▒██████▒▒      \033[91m__        __    __              __\033[0m
  ▒▒██████▒▒    ▒▒██████▒▒       \033[91m/ /_ __ __/ /   / /_ __ ____ _  / /\033[0m
▒▒████████▒▒    ▒▒████████▒▒    \033[91m/ /\ V  V / /   / /\ V  V / _` |/ /\033[0m
  ▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒     \033[91m/_/  \_/\_/_/   /_/  \_/\_/\__, /_/\033[0m
                                                          \033[91m|___/\033[0m

      ▒▒▒▒        ▒▒▒▒            \033[91m4wal - 4chan based wallpaper\033[0m
    ▒▒████▒▒    ▒▒████▒▒               \033[91mscraper and changer\033[0m
  ▒▒██████▒▒    ▒▒██████▒▒
  ▒▒██████▒▒    ▒▒██████▒▒      \033[91mr <board>  -  set random wallpaper\033[0m
  ▒▒██▒▒██▒▒    ▒▒██▒▒██▒▒      \033[91mo  -  adjust program options\033[0m
    ▒▒  ▒▒        ▒▒  ▒▒
"""

logo = logo.replace("█", "\033[92m█\033[0m")
logo = logo.replace("▒", "\033[92m▒\033[0m")
print(logo)

def main():
    try:
        command = input("> ")
        command = command.lower().strip().replace("/", "")
        if command == "r":
            try:
                print("Enter board (/w/, /wg/):")
                board = input("> ")
                board = board.lower().strip().replace("/", "")
                if board in ["w", "wg"]:
                    print()
                    get_random_thread(board)
                else:
                    print(f"Board '{board}' invalid.")
                    main()
            except KeyboardInterrupt:
                print(logo)
                main()
        elif command.startswith("r "):
            if command[2:] in ["w", "wg"]:
                get_random_thread(command[2:])
            else:
                print(f"Board '{command[2:]}' invalid.")
                main()
        elif command == "clear":
            sys.stdout.write("\033[H\033[J")
            main()
        elif command in ["q", "quit", "exit"]:
            sys.stdout.write("\033[H\033[J")
            sys.exit()
        else:
            sys.stdout.write("\x1b[1A")  # clear line if
            sys.stdout.write("\x1b[2K")  # invalid command
            main()
    except KeyboardInterrupt:
        sys.stdout.write("\033[H\033[J")
        sys.exit()
    except Exception as err:
        print("\033[1mError:\033[0m", err)
        main()


def get_random_thread(board):
    sys.stdout.write("\r" + "[+] finding random thread...".ljust(32, " "))
    page_num = randint(1, 10)
    url = f"https://a.4cdn.org/{board}/{page_num}.json"
    response = requests.get(url)
    page = response.json()
    for i in range(15):  # num of threads per page
        try:
            thread_list = [thread for thread in page.values()]
            thread = choice(thread_list)
            get_random_post(thread, board)
        except:
            main()


def get_random_post(thread, board):
    sys.stdout.write("\r" + "[+] finding random post...".ljust(32, " "))
    posts = [post for post in thread[randint(0, 14)].values()]
    url = f"https://a.4cdn.org/{board}/thread/{posts[0][0]['no']}.json"
    response = requests.get(url)
    page = response.json()
    posts = [post for post in page.values()]
    get_random_pape(posts, board)


def get_random_pape(thread, board):
    posts = choice(thread)
    post = choice(posts)
    try:
        if post["ext"] == ".webm":
            get_random_thread(board)
        filename = str(post["tim"]) + post["ext"]
    except KeyError:
        sys.stdout.write("\r" + "[-] post cointains no image file".ljust(32, " "))
        get_random_thread(board)
    try:
        title = posts[0]["sub"]
    except KeyError:
        title = ""
    if board == "wg":
        folder = "general"
    elif board == "w":
        folder = "anime"
    else:
        folder = board
    url = f"https://i.4cdn.org/{board}/{filename}"
    path = f"4wal_papers/{folder}/"
    os.makedirs(path, exist_ok=True)
    if os.path.exists(path + filename):
        sys.stdout.write("\r" + "[-] image file already exists".ljust(32, " "))
        get_random_thread(board)
    else:
        sys.stdout.write("\r" + "[+] downloading image file...".ljust(32, " "))
        urllib.request.urlretrieve(url, path + filename)
    sys.stdout.write("\r" + "[+] finished".ljust(32, " "))
    print()
    if title:
        print("\033[92mThread title:\033[91m", title, "\033[0m")
    print("\033[92mServer filename:\033[91m", str(post["tim"]) 
            + post["ext"], "\033[0m")
    print("\033[92mFilename:\033[91m", post["filename"] + post["ext"], "\033[0m")
    print("\033[92mResolution:\033[91m", post["w"], "x", post["h"], "\033[0m")
    print("\033[92mURL:\033[91m", url, "\033[0m")
    print()
    call_wal(path + filename)


def call_wal(img):
    os.system(f"wal -i {img} -q")
    main()


if __name__ == "__main__":
    main()
