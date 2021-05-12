# From : https://github.com/Hamza442004/DXF2img
import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
# import wx
import glob
import re
import sys
import os
class DXF2IMG(object):

    default_img_format = '.png'
    default_img_res = 300
    default_img_output = 'output.png'
    def subname(self, path):
      return os.path.splitext(path)[-1].replace('.','') 
    def convert_dxf2img(self, names, img_output=default_img_output,img_format=default_img_format, img_res=default_img_res):
        for name in names:
            doc = ezdxf.readfile(name)
            msp = doc.modelspace()
            # Recommended: audit & repair DXF document before rendering
            auditor = doc.audit()
            # The auditor.errors attribute stores severe errors,
            # which *may* raise exceptions when rendering.
            if len(auditor.errors) != 0:
                raise exception("The DXF document is damaged and can't be converted!")
            else :
                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                ctx = RenderContext(doc)
                ctx.set_current_layout(msp)
                ctx.current_layout.set_colors(bg='#FFFFFF')
                out = MatplotlibBackend(ax)
                Frontend(ctx, out).draw_layout(msp, finalize=True)

                img_name = re.findall("(\S+)\.",name)  # select the image name that is the same as the dxf file name
                #first_param = ''.join(img_name) + img_format  #concatenate list and string
                #fig.savefig(first_param, dpi=img_res)
                fig.savefig(img_output, dpi=img_res)


if __name__ == '__main__':
    first =  DXF2IMG()
    #first.convert_dxf2img(['95164029.dxf'],img_format='.png')
    message = '''
Dxf to png

Author: 
  Feather Mountain (https://3wa.tw)
      
Usage :
  dxf2img.exe [Source.dxf] [Target.png]
'''
    if len(sys.argv) !=3:
      print(message);
      sys.exit(1) 
    if os.path.isfile(sys.argv[1]) == False:
      print("\n Source dxf not found ... %s" % (sys.argv[1]))
      sys.exit(1)
    if first.subname(sys.argv[1]).lower() != "dxf":
      print("\n Source file not dxf not found ... %s" % (sys.argv[1]))
      sys.exit(1)
    if first.subname(sys.argv[2]).lower() != "png":
      print("\n Target file not png not found ... %s" % (sys.argv[2]))
      sys.exit(1)
    
    first.convert_dxf2img([sys.argv[1]],img_output=sys.argv[2],img_format='.png')