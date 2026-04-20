"""
GPUinfo
Callable functions to get GPU names, manufacturers, and compatible codecs
David Gingerich
Version 1.0.0
"""

from utils import *
  
def manufacturers() -> list[str]:
  gpus = get_list_of_gpu_names()

  
      
  return connected_manufacturer