#!/usr/bin/env python
from lxml import etree
from lxml.builder import ElementMaker
import numpy as np

SVGNS = 'http://www.w3.org/2000/svg'
INKSCAPENS = 'http://www.inkscape.org/namespaces/inkscape'
SVG = ElementMaker(namespace=SVGNS, nsmap={None: SVGNS, 'inkscape': INKSCAPENS})


def stroke_text_to_path_d(stroke_text):
    points = np.array(stroke_text.strip().split()).reshape((-1, 2))
    return ' '.join([' '.join([('M' if i == 0 else 'L')] + list(pt)) for i, pt in enumerate(points)])


def stroke_to_path(stroke):
    width = stroke.attrib.get('width', '1')
    color = stroke.attrib.get('color', 'black')
    style = "fill:none;stroke:{color};stroke-width:{width};stroke-miterlimit:4;stroke-dasharray:none;stroke-linejoin:round;stroke-linecap:round".format(
        color=color, width=width)
    return SVG.path(d=stroke_text_to_path_d(stroke.text), style=style)

def xoj_page_to_svg_layer(page, id):
    paths = [
        stroke_to_path(stroke)
        for layer in page.iterfind('layer')
        for stroke in layer.iterfind('stroke')]
    return SVG.g(*paths, id=id)


def convert_xoj(xoj_root):
    layers = [
        xoj_page_to_svg_layer(page, id='layer{}'.format(i+1))
        for i, page in enumerate(xoj_root.iterfind('page'))
    ]
    return etree.ElementTree(SVG.svg(*layers, version='1.1'))


def convert_xoj_file(in_name, out_name):
    convert_xoj(etree.parse(in_name)).write(out_name)

if __name__ == '__main__':
    import sys
    convert_xoj_file(sys.argv[1], sys.argv[2])
