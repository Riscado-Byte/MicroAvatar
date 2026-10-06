import os
import random

from dotenv import load_dotenv

load_dotenv()
WorkingDirectory = os.getenv("WorkingDirectory")

dir_fd = os.open(WorkingDirectory, os.O_RDONLY)

def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)

def random_hex():
    return '#{:02x}{:02x}{:02x}'.format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

def background():
    choice = random.randint(0, 1)
    backgroundColor = random_hex()
    backgroundOptions = [
        f'<circle cx="100" cy="100" r="100" fill="{backgroundColor}"/>',
        f'<rect x="0" y="0" height="200" width="200" fill="{backgroundColor}"/>'
    ]
    print(choice)
    match choice:
        case 0:
            return backgroundOptions[0]
        case 1:
            return backgroundOptions[1]

def head():
    choice = random.randint(0, 1)
    headColor = random_hex()
    headOptions = [
        f'<circle cx="100" cy="100" r="80" fill="{headColor}"/>',
        f'<rect x="20" y="20" ry="60" height="160" width="160" fill="{headColor}"/>'
    ]
    print(choice)
    match choice:
        case 0:
            return headOptions[0]
        case 1:
            return headOptions[1]

def eyes():
    choice = random.randint(0, 1)
    eyesColor = random_hex()
    eyesOptions = [
        f'<circle cx="70" cy="70" r="25" fill="{eyesColor}"/>\n    <circle cx="130" cy="70" r="25" fill="{eyesColor}"/>',
        f'<rect x="60" y="50" ry="10" rx="10" height="40" width="20" fill="{eyesColor}"/>\n    <rect x="120" y="50" ry="10" rx="10" height="40" width="20" fill="{eyesColor}"/>',
    ]
    print(choice)
    match choice:
        case 0:
            return eyesOptions[0]
        case 1:
            return eyesOptions[1]

def accessory():
    choice = random.randint(0, 2)
    accessoryColor = random_hex()
    accessoryOptions = [
        f'<circle cx="70" cy="70" r="30" fill="none" stroke="{accessoryColor}" stroke-width="2"/>',
        f'<circle cx="70" cy="70" r="30" fill="none" stroke="{accessoryColor}" stroke-width="2"/>\n    <circle cx="130" cy="70" r="30" fill="none" stroke="{accessoryColor}" stroke-width="2"/>'
    ]
    print(choice)
    match choice:
        case 0:
            return accessoryOptions[0]
        case 1:
            return accessoryOptions[1]
        case 2:
            return ''

def mouth():
    choice = 0 #random.randint(0, 1)
    mouthColor = random_hex()
    mouthOptions = [
        f'<rect x="70" y="100" ry="10" rx="10" height="50" width="60" fill="{mouthColor}"/>\n    <rect x="90" y="98" ry="5" rx="5" height="10" width="20" fill="black"/>'
    ]
    print(choice)
    match choice:
        case 0:
            return mouthOptions[0]

with open('teste.txt', 'w', opener=opener) as f:

    print('<svg width="200" height="200">', file=f)
    print('    '+ background(), file=f)
    print('    '+ head(), file=f)
    print('    '+ eyes(), file=f)
    print('    '+ accessory(), file=f)
    print('    '+ mouth(), file=f)
    print('</svg>', file=f)


if os.path.exists('avatar.svg'):
    os.rename('teste.txt', f'avatar{random_hex()}.svg')
else:
    os.rename('teste.txt','avatar.svg')

os.close(dir_fd)