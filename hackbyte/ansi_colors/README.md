# ansi\_colors

Internal module for terminal text styling using ANSI escape codes.

## Features

* 8 standard foreground and background colors
* Bright color variants
* Text styles: **bold**, *underline*, reset
* Truecolor support with HEX (`#rrggbb`)

## Usage Example

```python
from ansi import Fore, Back, Style, rgb_fore, rgb_back

print(Fore.RED + "Red Text" + Style.RESET)
print(Back.YELLOW + "Yellow Background" + Style.RESET)
print(Style.BOLD + "Bold Text" + Style.RESET)

print(rgb_fore("#ff8800") + "Orange Text via RGB" + Style.RESET)
print(rgb_back("#1e1e1e") + rgb_fore("#ffffff") + "White on Dark" + Style.RESET)
```

## API Reference

* `Fore.RED`, `Fore.BRIGHT_GREEN`, `Fore.CYAN`, etc.
* `Back.BLUE`, `Back.BRIGHT_MAGENTA`, etc.
* `Style.BOLD`, `Style.UNDERLINE`, `Style.RESET`
* `rgb_fore("#rrggbb")`, `rgb_back("#rrggbb")`

## Demo

Run this to preview all styles:

```bash
python ansi_colors/demo.py
```