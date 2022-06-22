from PIL import Image
import glob

path_in = "output/result_*.png"
path_out = "result.gif"

imgs = (Image.open(f) for f in sorted(glob.glob(path_in)))
next(imgs).save(fp=path_out, format='GIF', append_images=imgs, save_all=True, duration=100, loop=0)