import yaml
import os
from typing import List

class Alignment:
    def __init__(self, name, directions):
        self.name = name
        self.directions:List[str] = directions

class Package:
    def __init__(self, name):
        self.name = name
        self.alignments:List[Alignment] = []

class Packages:
    def __init__(self):
        self.data = None
        self.packages:List[Package] = []
        self.read_yaml()
        self.parser_data()
    
    def read_yaml(self):
        yaml_path = os.path.join(os.path.dirname(__file__), 'package.yaml') # Optional
        with open(yaml_path) as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def parser_data(self):
        for package in self.data['package']:
            name = package['name']
            pack = Package(name)
            for alignment in package['alignment']:
                ali = alignment['name']
                directions = alignment['direction']
                align = Alignment(ali, directions)
                pack.alignments.append(align)
            self.packages.append(pack)

def get_packages():
    packages = Packages()
    return packages.packages   