from PIL import Image
import sys
import os

with Image.open(sys.argv[1]) as image:
    width, height = image.size

    # android
    curSize = 4
    
    types = (
        {'size': 0.75,  'name': 'ldpi'}, 
        {'size': 1,     'name': 'mdpi'}, 
        {'size': 1.5,   'name': 'hdpi'}, 
        {'size': 2,     'name': 'xhdpi'}, 
        {'size': 3,     'name': 'xxhdpi'}, 
        {'size': 4,     'name': 'xxxhdpi'}
    )

    for t in types:
        if (not os.path.isdir('android')):
            os.mkdir('android');
        if (not os.path.isdir('android/drawable-'+t['name'])):
            os.mkdir('android/drawable-'+t['name']);
        new_width  = int(width*(t['size'] / curSize))
        new_height = int(new_width * height / width) 

        img = image.resize((new_width, new_height), Image.ANTIALIAS)
        img.save('android/drawable-'+t['name']+'/'+sys.argv[1], format='png')

    
    # ios
    curSize = 4
    
    types = (
        {'size': 1, 'name': '@1x'}, 
        {'size': 2, 'name': '@2x'}, 
        {'size': 3, 'name': '@3x'}
    )

    parts = sys.argv[1].split('.')
    for t in types:
        if (not os.path.isdir('ios')):
            os.mkdir('ios');
        new_width  = int(width*(t['size'] / curSize))
        new_height = int(new_width * height / width)

        img = image.resize((new_width, new_height), Image.ANTIALIAS)
        img.save('ios/'+parts[0]+t['name']+'.'+parts[1], format='png')