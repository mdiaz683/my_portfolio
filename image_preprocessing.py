import os
from PIL import Image, ExifTags

def fix_image_orientation(image_path):
    img = Image.open(image_path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = img._getexif()

        if exif is not None:
            orientation_value = exif.get(orientation)

            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except:
        pass

    return img

folder = "gallery"

for filename in os.listdir(folder):
    if filename.lower().endswith(("jpg", "jpeg", "png")):
        path = os.path.join(folder, filename)
        img = fix_image_orientation(path)
        img.save(path)