#!/bin/bash

echo '==============================='
echo 'Prepare Input'
echo '==============================='
python /nnUNet/Docker_LASCAR/prepare_input_task.py

echo '==============================='
echo 'Run nnUnet Prediction'
echo '==============================='

#export CUDA_VISIBLE_DEVICES=0

# LASCAR segmentation

python /nnUNet/nnunet/inference/predict_simple.py -i $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/imagesTs/ -o $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/testset_predictions/3d_1000_Loss_DiceFocal_Uncertainty_bestmodel_all/3d_1000_Loss_DiceFocal_Uncertainty_bestmodel/ -tr nnUNetTrainerV2_Loss_DiceFocal_Uncertainty -m 3d_fullres -p nnUNetPlansv2.1 -t Task402_LA_Scar_Cavity


#python /nnUNet/nnunet/inference/predict_simple.py -i $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/imagesTs/ -o $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/testset_predictions/3d_1000_Loss_DicePolyCE_bestmodel_all/3d_1000_Loss_DicePolyCE_bestmodel/ -tr nnUNetTrainerV2_Loss_DicePolyCE -m 3d_fullres -p nnUNetPlansv2.1 -t Task402_LA_Scar_Cavity --save_npz
#python /nnUNet/nnunet/inference/ensemble_predictions.py -f $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/testset_predictions/3d_1000_Loss_DiceFocal_bestmodel_all/3d_1000_Loss_DiceFocal_bestmodel/ $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/testset_predictions/3d_1000_Loss_DicePolyCE_bestmodel_all/3d_1000_Loss_DicePolyCE_bestmodel/ -o $nnUNet_raw_data_base/nnUNet_raw_data/Task402_LA_Scar_Cavity/testset_predictions/3d_1000_Loss_DiceFocal_DicePolyCE_bestmodel_ensemble_all/3d_1000_Loss_DiceFocal_DicePolyCE_bestmodel_ensemble/ -pp $RESULTS_FOLDER/nnUNet/3d_fullres/Task402_LA_Scar_Cavity/nnUNetTrainerV2_Loss_DiceFocal__nnUNetPlansv2.1/postprocessing.json

python /nnUNet/Docker_LASCAR/prepare_output.py
echo '==============================='
echo 'End of Prediction'
echo '==============================='
