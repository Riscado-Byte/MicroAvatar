import os
import random
import string
from dotenv import load_dotenv

load_dotenv()
WorkingDirectory =os.getenv("WorkingDirectory")

dir_fd = os.open(WorkingDirectory, os.O_RDONLY)


def random_hex():
    return '#{:02x}{:02x}{:02x}'.format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def background():
    choice = random.randint(0, 1)
    backgroundColor = random_hex()
    backgroundOptions = [
        f'<circle cx="100" cy="100" r="100" fill="{backgroundColor}"/>',
        f'<rect x="0" y="0" height="200" width="200" fill="{backgroundColor}"/>'
    ]

    print(choice)
    return '    ' + backgroundOptions[choice]

def ears():
    choice = random.randint(0, 2)
    earsColor = random_hex()
    earsOptions = [
        f'<circle cx="30" cy="100" r="20" fill="{earsColor}"/>\n    <circle cx="170" cy="100" r="20" fill="{earsColor}"/>',
        f'<rect x="10" y="80" ry="10" rx="10" height="40" width="40" fill="{earsColor}"/>\n    <rect x="150" y="80" ry="10" rx="10" height="40" width="40" fill="{earsColor}"/>',
        f'<circle cx="60" cy="30" r="20" fill="{earsColor}"/>\n    <circle cx="140" cy="30" r="20" fill="{earsColor}"/>'
    ]

    print(choice)
    return '    ' + earsOptions[choice]

def head():
    choice = random.randint(0, 1)
    headColor = random_hex()
    headOptions = [
        f'<circle cx="100" cy="100" r="80" fill="{headColor}"/>',
        f'<rect x="20" y="20" ry="60" height="160" width="160" fill="{headColor}"/>'
    ]

    print(choice)
    return '    ' + headOptions[choice]

def eyes():
    choice = random.randint(0, 3)
    eyesColor = random_hex()
    eyesOptions = [
        f'<circle cx="70" cy="70" r="25" fill="white"/>\n    <circle cx="130" cy="70" r="25" fill="white"/>\n    <rect x="60" y="70" ry="10" rx="10" height="20" width="20" fill="{eyesColor}"/>\n    <rect x="120" y="70" ry="10" rx="10" height="20" width="20" fill="{eyesColor}"/>',
        f'<rect x="60" y="50" ry="10" rx="10" height="40" width="20" fill="{eyesColor}"/>\n    <rect x="120" y="50" ry="10" rx="10" height="40" width="20" fill="{eyesColor}"/>', 
        f'<rect x="53" y="67" ry="5" rx="5" height="5" width="35" fill="{eyesColor}"/>\n    <rect x="112" y="67" ry="5" rx="5" height="5" width="35" fill="{eyesColor}"/>',
        f'<path d="m 63.008341,45 c -2.556191,0 -5.111627,0.978814 -7.070312,2.937499 -3.917372,3.917372 -3.917372,10.225207 0,14.142579 l 7.070312,7.070312 -7.070312,7.072266 c -3.917372,3.917374 -3.917372,10.225204 0,14.142574 3.917371,3.91738 10.223253,3.91738 14.140625,0 L 84.221232,76.222656 c 0.258792,-0.258792 0.50001,-0.528365 0.724609,-0.806641 3.175189,-3.934017 2.933971,-9.677358 -0.724609,-13.335937 L 70.078654,47.937499 C 68.119968,45.978814 65.564532,45 63.008341,45 Z" fill="{eyesColor}"/>\n    <path d="m 126.00834,45 c -2.55619,0 -5.11162,0.978814 -7.07031,2.937499 -3.91737,3.917372 -3.91737,10.225207 0,14.142579 l 7.07031,7.070312 -7.07031,7.072266 c -3.91737,3.917374 -3.91737,10.225204 0,14.142574 3.91737,3.91738 10.22326,3.91738 14.14063,0 l 14.14258,-14.142574 c 0.25879,-0.258792 0.50001,-0.528365 0.7246,-0.806641 3.17519,-3.934017 2.93398,-9.677358 -0.7246,-13.335937 L 133.07866,47.937499 C 131.11997,45.978814 128.56454,45 126.00834,45 Z" fill="{eyesColor}"/>',
    ]

    print(choice)
    return '    ' + eyesOptions[choice]

def accessory():
    choice = random.randint(0, 1)
    accessoryColor = random_hex()
    accessoryOptions = [
        f'<circle cx="70" cy="70" r="30" fill="none" stroke="{accessoryColor}" stroke-width="2"/>',
        f'<circle cx="70" cy="70" r="30" fill="none" stroke="{accessoryColor}" stroke-width="2"/>\n    <circle cx="130" cy="70" r="30" fill="none" stroke="{accessoryColor}" stroke-width="2"/>'
    ]

    print(choice)
    return '    ' + accessoryOptions[choice]

def mouth():
    choice = 0 #random.randint(0, 1)
    mouthColor = random_hex()
    mouthOptions = [
        f'<rect x="70" y="100" ry="10" rx="10" height="50" width="60" fill="{mouthColor}"/>\n    <rect x="90" y="98" ry="5" rx="5" height="10" width="20" fill="black"/>'
    ]

    print(choice)
    return '    ' + mouthOptions[choice]

def create(count=1, bg=False):
    amount = count

    def opener(path, flags):
        return os.open(path, flags, dir_fd=dir_fd)

    for i in range(amount):
        name = random_string(5)
        print(name)
    
        with open(f'{name}.txt', 'w', opener=opener) as f:

            print('<svg width="200" height="200">', file=f)

            if bg:
                print(background(), file=f)
            
            print(ears(), file=f)
            print(head(), file=f)
            print(eyes(), file=f)
            print(accessory(), file=f)
            print(mouth(), file=f)
            print('</svg>', file=f)


        if os.path.exists('avatar.svg'):
            os.rename(f'{name}.txt', f'avatar {name}.svg')
        else:
            os.rename(f'{name}.txt','avatar.svg')
    
    os.close(dir_fd)
