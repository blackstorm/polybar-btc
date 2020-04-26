# polybar-btc
![image](http://github.com/blackstorm/blackstorm/polybar-btc/raw/master/preview.png)
show btc coin on your polybar

## how to use
1. clone project to polybar script dir

2. add btc module to bar right
```
modules-right = btc network-traffic alsa memory cpu wlan
```
3. add custom module
```
[module/btc]
type = custom/script
exec = $HOME/.config/polybar/scripts/polybar-btc/main.py
interval = 1
```