import cv2
import os
import numpy as np
import subprocess
from tqdm import tqdm

path = 'E:/Cable_Detection/liot/30.3.23_(bw)-res/rgb_segms_panaroma'
# for folder in tqdm(os.listdir(path)):
#     input_path = os.path.join(path,folder)
#     save_path = os.path.join('res',folder)
#     cmd = "python .\infer_building.py --config .\pp_liteseg_infer_model\pp_liteseg_infer_model\deploy.yaml \
#         --image_path \"{}\" --save_dir \"{}\" --batch_size 1 --device gpu".format(input_path,save_path)
#     s = subprocess.check_call(cmd)

save_path = 'ext_houses' 
if not os.path.exists(save_path):
    os.makedirs(save_path)
for folder in tqdm(os.listdir('res')):
    save_folder = os.path.join(save_path,folder)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    for file in os.listdir(os.path.join('res',folder)):
        print(file)
        img_path = os.path.join('res',folder,file)
        img = cv2.imread(img_path)
        mask = np.zeros(img.shape)
        mask[np.all(img == [0,128,128], axis=-1)] = 255
        cv2.imwrite((os.path.join(save_folder,file)),mask)