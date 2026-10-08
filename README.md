# MicroAvatar

## A simple avatar generator in python

![demo](/Assets/icon)

## Denpendencies

```
cairovsvg # only needed if you want to raster the avatars
```

## Usage

```　py
import MicroAvatar

MicroAvatar.create()
```

## Options

| Option | Input      | Default               | Description                        |
|--------|------------|-----------------------|------------------------------------|
| count  | ``Int``    | 1                     | Specifies the amount of avatars    |
| bg     | ``Bool``   | False                 | Adds background                    |
| path   | ``String`` | Directory of the file | Defines a custom export path       |
| raster | ``Bool``   | False                 | Defines if the avatar gets rastered|

## Example
``` py
import MicroAvatar

MicroAvatar.create(5, True, '/home/user/', True) # Outputs 5 avatars with background and rastered to the Home directory

```

## Roadmap

- [x] Add a way to add the background
- [x] Add a way to config the file path
- [x] Add an option to raster the svgs