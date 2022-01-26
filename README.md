# currency-rates-polybar
Two modules that display rates of fiat currencies and cryptocurrencies



![screen](https://github.com/Speskov2000/files/blob/master/currency-rates-polybar/crypto.png)

![screen](https://github.com/Speskov2000/files/blob/master/currency-rates-polybar/fiat.png)



# Setup
1. Clone the repository somewhere
2. Move (or create symlink from dotfiles) the scripts `fiat.py` and `crypto.py` to `~/.config/polybar/scripts `
3. Make them executable:
```
sudo chmod u+x ~/.config/polybar/scripts/crypto.py
sudo chmod u+x ~/.config/polybar/scripts/fiat.py
```

Then in `~/.config/polybar/config.ini` create and use the modules:

```
[bar/monLeft]
...
modules-right = crypto
...

[bar/monRight]
...
modules-right = fiat
...



[module/crypto]
type = custom/script
exec = ~/.config/polybar/scripts/crypto.py
interval = 300
label-foreground = #FAFAD2

[module/fiat]
type = custom/script
exec = ~/.config/polybar/scripts/fiat.py
interval = 300
label-foreground = #9DE5DD 
```

You can see an example of the configuration [here](https://github.com/Speskov2000/dotfiles/tree/job/polybar/.config/polybar).

## Dependencies
In the screenshots [this font](https://github.com/allienworks/cryptocoins) was used for cryptocurrencies. For fiat currencies was used Material Design Icons.

If you don't know how to use custom icons in polybar - [this video](https://www.youtube.com/watch?v=nVSUiRUgspQ) will help you)

Installing these fonts in the Archlinux:
```
yay -S ttf-material-design-icons-git cryptocoins-git
```

If using the **cryptocoins icon font** or **Material Disign Icons**, ensure that the following lines is present in your `~/.config/polybar/config.ini`:

```
[bar/base]
...
font-0 = cryptocoins:size=11;2 
...
font-2 = Material Design Icons:size=12;2 
```
(Don't forget that fonts can overlap each other, so it is important to place cryptocoins above)

## Fullscreen examples:
![screen](https://github.com/Speskov2000/files/blob/master/currency-rates-polybar/crypto-fs.png)
![screen](https://github.com/Speskov2000/files/blob/master/currency-rates-polybar/fiat-fs.png)
