![alt text](https://raw.githubusercontent.com/cyblily/4wal/master/img.png)

# 4wal
4chan based random wallpaper scraper and changer

uses 4chan's read only API to find a random post in a random thread on a random page number

by default it uses ![pywal](https://github.com/dylanaraps/pywal/), but you can set your own post-download command in the options menu

## commands
r <board>  -  set random wallpaper

s <board>  -  select thread 

o          -  show options menu
  
clear      -  clears the screen

## example usage
```
set random wallpaper from board wg:
> r wg

set random board with input prompt for board selection
> r 
Enter board (/w/, /wg/):
> wg

select thread to pull wallpaper from on board wg
> s wg

select thread to pull wallpaper from with input prompt for board selection
> s
Enter board (/w/, /wg/):
> wg
```

## options
* set image download path (default: cwd)

* set post-image download command (default: wal -i {img} -q)
 
* toggle all boards being available for scraping (default: only /w/ and /wg/)

* toggle the usage of server and user uploaded filenames (default: server)

* set minimum resolution (default: no minimum restrictions)

## TODO:
probably more stuff
