from PIL import Image

pil_im = Image.open(r"C:\Users\B1ACB1RD\Pictures\Screenshot 2026-01-23 180136.png").convert('L')

print(pil_im)
pil_im.thumbnail((128, 128))
box = (100, 100, 400, 400)
region = pil_im.crop(box)
