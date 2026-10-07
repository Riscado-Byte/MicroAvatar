# MicroAvatar

## A simple avatar generator in python

![demo](/Assets/icon)

## Usage

```　py
import MicroAvatar

MicroAvatar.create()
```

## Options

| Option | Input    | Default | Description |
|--------|----------|---------|-------------|
| count  | ``Int``  | 1       | Specifies the amount of avatars |
| bg     | ``Bool`` | False   | Adds background |

## Example
``` py
import MicroAvatar

MicroAvatar.create(5, True) # Outputs 5 avatars with background
```

## Roadmap

- [x] Add a way to add the background
- [ ] Add a way to config the file path
- [ ] Add an option to raster the svgs