from PIL import Image
from glob import glob

ROOT_DIR = 'static/'

# Glob all images recursively in the directory (jpg, jpeg, png, JPG, etc.)
images = glob(ROOT_DIR + '**/*', recursive=True)
images = [image for image in images if image.lower().endswith(('.jpg', '.jpeg', '.png'))]

def clean_exif(imageUrl):
    """
    Save as same image without exif data
    """
    print(f'Cleaning EXIF data from {imageUrl}')
    image = Image.open(imageUrl)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(imageUrl)
    image_without_exif.close()

i = 0
for image in images:
    clean_exif(image)
    print(f'Cleaned EXIF data from {image}')
    i += 1

print(f'Cleaned EXIF data from {i} images')