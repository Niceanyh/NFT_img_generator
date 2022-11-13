import random
import os
class Layer:
    
    def __init__(self,layer_path):
        self.layer_path = layer_path
        
        
    def get_random_element_from_layer(self):
        element_path = random.choice([name for name in os.listdir(self.layer_path) if not name.startswith('.')])
        return element_path