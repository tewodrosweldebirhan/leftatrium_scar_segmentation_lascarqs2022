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

LA_Scar_Cavity_method = "3d_1000_Loss_DiceFocal_Uncertainty_bestmodel" # 3d_1000_BN_splits_bestmodel

output_folder = os.getenv("OUTPUTDIR")

LA_Scar_Cavity_foldername = '/nnUNet/all_data/nnUNet_raw/nnUNet_raw_data/Task402_LA_Scar_Cavity/testset_predictions/'+LA_Scar_Cavity_method+ '_all/'+LA_Scar_Cavity_method+'/'

subjlist = os.listdir(LA_Scar_Cavity_foldername)

#filter only .nii.gz
subjlist = [sb for sb in subjlist if sb.endswith('.nii.gz')]

subjlist.sort()

submission_folder = os.path.join(output_folder, 'Submission_Task1')
if not os.path.isdir(submission_folder):
    os.makedirs(submission_folder)

for n, subj in enumerate(subjlist):

    if subj.endswith('.nii.gz'):


        imagename_SA = os.path.join(LA_Scar_Cavity_foldername, subj)

        #separate scar and LA cavity
        itk_mask, mask = load_itk(imagename_SA)
        mask_scar = np.zeros_like(mask)
        mask_cavity = np.zeros_like(mask)

        mask_scar[mask==2] = 1 # scar was labeled 2
        mask_cavity[mask == 1] = 1 # cavity was labeled 1

        itk_mask_scar = sitk.GetImageFromArray(mask_scar)
        itk_mask_scar.CopyInformation(itk_mask)

        itk_mask_cavity = sitk.GetImageFromArray(mask_cavity)
        itk_mask_cavity.CopyInformation(itk_mask)


        subjnew_scar = subj.replace("test", "predict_Scar_").replace("_enhanced","")
        subjnew_cavity = subj.replace("test", "predict_Cavity_").replace("_enhanced","")

        sitk.WriteImage(itk_mask_scar, os.path.join(submission_folder, subjnew_scar))
        sitk.WriteImage(itk_mask_cavity, os.path.join(submission_folder, subjnew_cavity))













