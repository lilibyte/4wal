## 4wal 2.0

Set a random wallpaper from 4chan!

Uses 4chan's read only API to find a random post in a random thread on a random page number

I completely rewrote the program in one sitting to be more simple because of how bad it was was before

## usage
```
--board        board to scrape for wallpaper (default: /wg/)

--command      command to set wallpaper 

--min-res      specify minimum resolution (e.g. 1920x1080) (default: 0x0)

--filename     save file with **user** or **server** filename (default: user)

--path         where to save wallpaper files (default: cwd)

--quiet        silence all output

--extension    filter by file extension (default: .jpg .jpeg .png)
```

## forks

Please have a look at [improvised-explosive-device's fork](https://github.com/improvised-explosive-device/4wal) of 4wal for more features.
