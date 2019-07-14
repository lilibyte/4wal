![alt text](https://raw.githubusercontent.com/cyblily/4wal/master/img.png)

# 4wal [WIP]
4chan based random wallpaper scraper and changer

uses 4chan's read only API to find a random post in a random thread on a random page number

by default it uses ![pywal](https://github.com/dylanaraps/pywal/), but you can set your own post-download command in the options menu

## commands
r <board>  -  set random wallpaper

s <board>  -  select thread [WIP]

o          -  show options menu
  
clear      -  clears the screen
  
## TODO:
fix thread selection stuff:
  * retry selected thread until a pic is found rather than going to a random one
* currently sys.exit() is layered and doesn't properly work... needs clean up
