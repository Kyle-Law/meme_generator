import os
import random
from PIL import Image, ImageFont, ImageDraw

class MemeEngine:
  """ A class to create meme. """
  def __init__(self,output_folder):
    """ Create meme to the output folder"""
    self.out_folder = output_folder
    self.num = 1
    if not os.path.exists(output_folder):
      os.makedirs(output_folder)

  def make_meme(self,img_path,text,author,width=500):
    """ Create meme from image, text, and author"""
    img = Image.open(img_path)
    outfile = os.path.join(self.output_folder,f"img-{self.num}.jpg")
    self.num += 1
    ori_width,ori_height = img.size
    ratio = width / ori_width
    height = int(ori_height * ratio)
    img.thumbnail((width,height))

    font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', size=20)
    font_position = random.choice(range(width-40,height-40))
    fill='white'
    stroke_fill = 'black'

    draw = ImageDraw.draw(img)
    draw.text((50,font_position),text,fill,font,stroke_width=1,stroke_fill = stroke_fill)
    draw.text((50,font_position),f" - {author}",fill,font,stroke_width=1,stroke_fill = stroke_fill)

    img.save(outfile,'jpg')
    return outfile
