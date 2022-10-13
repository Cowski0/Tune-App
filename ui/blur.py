from PIL import Image, ImageFilter 
from PIL.ImageQt import ImageQt

original_image = Image.open("ed1baca98b88bc997b0fbd8a9410eeaf.png")
blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=10)) 

original_image.show() 
blurred_image.show()