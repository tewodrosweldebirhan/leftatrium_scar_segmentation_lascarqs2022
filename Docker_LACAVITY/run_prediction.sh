#!/bin/bash

echo '==============================='
echo 'Prepare Input'
echo '==============================='
python /nnUNet/Docker_LACAVITY/prepare_input_task.py

echo '==============================='
echo 'Run nnUnet Prediction'
echo '==============================='

#export CUDA_VISIBLE_DEVICES=0

# LACAVITY segmentation

python /nnUNet/nnunet/inference/predict_simple.py -i $nnUNet_raw_data_base/nnUNet_raw_data/Task400_LA_Cavity/imagesTs/ -o $nnUNet_raw_data_base/nnUNet_raw_data/Task400_LA_Cavity/testset_predictions/3d_1000_Loss_DicePolyCE_bestmodel_all/3d_1000_Loss_DicePolyCE_bestmodel/ -tr nnUNetTrainerV2_Loss_DicePolyCE -m 3d_fullres -p nnUNetPlansv2.1 -t Task400_LA_Cavity


python /nnUNet/Docker_LACAVITY/prepare_output.py
echo '==============================='
echo 'End of Prediction'
echo '==============================='
