from glob import glob
from PIL import Image
from os.path import basename

source_path = '../app_uis/'
dest_path = '../app_uis_resized/'

# loop over images and resize
for i, x in enumerate(glob(source_path + '*.jpg')):
    try:
        img = Image.open(x)
        size = img.size
        if size[0] < size[1]:
            img_resized = img.resize((270, 480), Image.ANTIALIAS)
        else:
            img_resized = img.resize((480, 270), Image.ANTIALIAS)
        img_resized.save(dest_path + basename(x))
    except OSError as e:
        pass
    if i % 1000 == 0:
        print(i)
