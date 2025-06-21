'''

Rename the files correctly
Arrange the files into a folder

Submission.zip
Submission_Task1
        predict_Cavity_index.nii.gz
        predict_Scar_index.nii.gz

    ...

'''

import shutil
import os
import SimpleITK as sitk
import numpy as np

def load_itk(filename):
    itk_img = sitk.ReadImage(filename)
    # Convert the image to a  numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    np_img = sitk.GetArrayFromImage(itk_img)
    return itk_img, np_img



#Parameters

LA_Cavity_method = "3d_1000_Loss_DicePolyCE_bestmodel" 

output_folder = os.getenv("OUTPUTDIR")

LA_Cavity_foldername = '/nnUNet/all_data/nnUNet_raw/nnUNet_raw_data/Task400_LA_Cavity/testset_predictions/'+LA_Cavity_method+ '_all/'+LA_Cavity_method+'/'

subjlist = os.listdir(LA_Cavity_foldername)

#filter only .nii.gz
subjlist = [sb for sb in subjlist if sb.endswith('.nii.gz')]

subjlist.sort()

submission_folder = os.path.join(output_folder, 'Submission_Task2')
if not os.path.isdir(submission_folder):
    os.makedirs(submission_folder)

for n, subj in enumerate(subjlist):

    if subj.endswith('.nii.gz'):


        imagename_SA = os.path.join(LA_Cavity_foldername, subj)
        
        subjnew = subj.replace("test", "predict_Cavity_").replace("_enhanced","")        

        shutil.copy(imagename_SA, os.path.join(submission_folder, subjnew ))











