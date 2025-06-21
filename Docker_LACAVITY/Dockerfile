FROM cmartinis/mm2
#FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-devel

COPY nnUNet /nnUNet

RUN cd /nnUNet && pip install nnunet && pip install -e .

ENV nnUNet_raw_data_base "/nnUNet/all_data/nnUNet_raw"
ENV nnUNet_preprocessed "/nnUNet/all_data/nnUNet_preprocessed"
ENV RESULTS_FOLDER "/nnUNet/all_data/nnUNet_trained_models"

ENV INPUTDIR "/input_data"
ENV OUTPUTDIR "/output_data"

WORKDIR "/"

ENTRYPOINT ["bash", "/nnUNet/Docker_LACAVITY/run_prediction.sh" ]

