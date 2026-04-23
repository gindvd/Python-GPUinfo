from GPUinfo.GPUinfo import *

connected_gpu_manufacturers = manufacturers()

for idx, name in enumerate(connected_gpu_manufacturers):
  print(f"Connected GPU {idx + 1} manufacturered by {name}")

connected_gpu_names = fullnames()

for idx, name in enumerate(connected_gpu_names):
  print(f"GPU {idx + 1}: {name}")