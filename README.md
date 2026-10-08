# MicroAvatar

## A simple avatar generator in python

![demo](/Assets/icon)

## Usage

```　py
import MicroAvatar

MicroAvatar.create()
```

## Options

| Option | Input      | Default               | Description                     |
|--------|------------|-----------------------|---------------------------------|
| count  | ``Int``    | 1                     | Specifies the amount of avatars |
| bg     | ``Bool``   | False                 | Adds background                 |
| path   | ``String`` | Directory of the file | Defines a custom export path    |

## Example
``` py
import MicroAvatar

MicroAvatar.create(5, True, '/home/user/') # Outputs 5 avatars with background to the Home directory

```

## Roadmap

- [x] Add a way to add the background
- [x] Add a way to config the file path
- [ ] Add an option to raster the svgs