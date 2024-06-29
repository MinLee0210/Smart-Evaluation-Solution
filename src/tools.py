from PIL import Image

def get_image(image): 
    image = Image.open(image).convert("RGB")
    return image