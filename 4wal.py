from argparse import ArgumentParser, SUPPRESS
from pathlib import Path
from random import randint, choice
from requests import get
from shutil import which
from subprocess import Popen
from sys import exit
from urllib import request


def default_command():
    if which("wal") is not None:
        return "wal -q -i"
    elif which("feh") is not None:
        return "feh --bg-fill"
    elif which("xsetbg") is not None:
        return ("xsetbg")
    elif which("gsettings") is not None:
        return "gsettings set org.gnome.desktop.background picture-uri"
    else:
        return False


def get_random_thread():
    catalog = f"https://a.4cdn.org/{args.board.strip().replace('/', '')}/catalog.json"
    res = get(catalog).json()
    page = randint(0, len(res) - 1)
    return choice(res[page]["threads"])["no"]


def get_random_post(thread_post_num):
    thread = f"https://a.4cdn.org/{args.board}/thread/{thread_post_num}.json"
    res = get(thread).json()
    title = res["posts"][0].get("sub")

    post = choice(res["posts"])
    while not post.get("ext") or (post["w"] < int(args.min_res.split("x")[0]) or post["h"] < int(args.min_res.split("x")[1])):
        post = choice(res["posts"])

    filename = (post["filename"] if args.filename == "user" else str(post["tim"])) + post["ext"]

    request.urlretrieve(f"https://i.4cdn.org/{args.board}/{str(post['tim']) + post['ext']}", "".join((str(args.path).rstrip("/"), "/")) + filename)

    Popen(args.command + " " + f"'{''.join((str(args.path).rstrip('/'), '/')) + filename}'", shell=True).wait()

    if not args.quiet:
        if title: print("\33[1m" + title + "\33[0m")
        print(">> " + post["now"] + " No." + str(post["no"]))
        print("   " + filename + " " + str(post["w"]) + "x" + str(post["h"]))
        print("   saved to " + str(args.path))
        print("  \33[90m ██ \33[0m\33[91m ██ \33[0m\33[92m ██ \33[0m\33[93m ██ \33[0m"
              "\33[94m ██ \33[0m\33[95m ██ \33[0m\33[96m ██ \33[0m\33[97m ██  \33[0m")


if __name__ == "__main__":
    parser = ArgumentParser(description="Set a random wallpaper from 4chan!", add_help=False)
    parser.add_argument("-h", "--help", action="help", default=SUPPRESS, help="\b\b\b\bshow this help message and exit")
    parser.add_argument("-v", "--version", action="version", version="2.0", help="\b\b\b\bshow program version and exit")
    parser.add_argument("-b", "--board",  metavar="\b", default="wg", help="board to scrape for wallpaper (default: /wg/)")
    parser.add_argument("-c", "--command", metavar="\b", default=default_command(), help="command to set wallpaper")
    parser.add_argument("-m", "--min-res", metavar="\b", default="0x0", help="specify minimum resolution (e.g. 1920x1080)")
    parser.add_argument("-f", "--filename", metavar="\b", choices=["user", "server"], default="user", help="save file with \33[1muser\33[0m or \33[1mserver\33[0m filename")
    parser.add_argument("-p", "--path", metavar="\b", default=Path.cwd(), help=f"where to save wallpaper files (default: {Path.cwd()}/)")
    parser.add_argument("-q", "--quiet", default=False, action="store_true", help="\b\b\b\bsilence all output")
    args = parser.parse_args()

    if not args.command:
        print("No program for setting wallpapers found. Please specify one with '-c'.")
        exit(1)

    try:
        random_thread = get_random_thread()
        get_random_post(random_thread)
    except KeyboardInterrupt:
        if not args.quiet:
            print("\nProgram killed by user ;_;")
        exit(1)
