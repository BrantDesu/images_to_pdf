from PIL import Image
import glob
import os
input_path = os.getcwd() + r'\input'
images_paths_list = glob.glob(input_path + r'\*.*')

all_images = []
for path in images_paths_list:
    path_split = path.split('.')
    extension = path_split[-1]
    ### PNG images filter ###
    if extension == 'png':
        im = Image.open(path)
        rgb_im = im.convert('RGB')
        all_images.append(rgb_im)
    else: all_images.append(Image.open(path))

pdf_path = os.getcwd() + r'\output\merged_images.pdf' 
all_images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=all_images[1:]
)