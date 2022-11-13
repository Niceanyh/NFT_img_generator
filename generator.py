import os
import random
from layer import Layer
from PIL import Image


class Generator:
    
    def __init__(self,image_path:str,size:int = 100):
        self.layers = self.load_image_layers(image_path)
        self.output_path : str = "./output"
        self.size = (size,size)
        os.makedirs(self.output_path,exist_ok=True)
        
    
    def load_image_layers(self, image_path):
        layers = [] 
        sub_paths = [name for name in sorted(os.listdir(image_path)) if os.path.isdir(os.path.join(image_path, name))]
        #print(sub_paths)
        for sub_path in sub_paths:
            layers.append(os.path.join(image_path, sub_path))
        return layers
        
    
    def gen_image_path(self):
        image_all_elements = []
        for layer_path in self.layers:
            layer = Layer(layer_path)
            e = layer.get_random_element_from_layer()
            image_all_elements.append(os.path.join(layer_path,e))
        return image_all_elements
    
    def render_image(self,image_all_elements):
        bg = Image.new("RGBA", self.size, (random.randint(0,250),150,180))
        for element in image_all_elements:
            layer_img = Image.open(element)
            bg = Image.alpha_composite(bg, layer_img)
        return bg
    
    def save_image(self,image,index):
        image.save(os.path.join(self.output_path, f"{index}.png"))
    
    def genearte_avatar(self,output_number:int = 1):
        for i in range(output_number):
            image_path = self.gen_image_path()
            print(image_path)
            image = self.render_image(image_path)
            self.save_image(image,i)
        
        
    
        