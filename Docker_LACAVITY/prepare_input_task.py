#!/usr/bin/env python3
#
import os
import os.path as osp
import shutil

'''
Renaming the input images for LACAVITY

'''

import SimpleITK as sitk
import glob

if __name__ == '__main__':

    count = 0
    nnunet_folder = os.getenv("nnUNet_raw_data_base")
    input_folder = os.getenv("INPUTDIR")
    imagesTs_folder_LA_Cavity = nnunet_folder + '/nnUNet_raw_data/' +'Task400_LA_Cavity/' + "imagesTs/"


    if not osp.exists(imagesTs_folder_LA_Cavity):
        os.makedirs(imagesTs_folder_LA_Cavity)

    print("start renaming...")

    for case in os.listdir(input_folder):
        inputcase = os.path.join(input_folder, case)

        inputcase_nnunet = os.path.join(imagesTs_folder_LA_Cavity, case.replace(".nii.gz", "_0000.nii.gz") )
        shutil.copy(inputcase, inputcase_nnunet)
        

        count += 1

        print("{} files processed".format(count))
        print("Done")
