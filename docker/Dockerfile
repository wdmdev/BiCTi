FROM continuumio/miniconda3:4.10.3

#Install Python libraries
COPY environment.yml .
RUN conda env create -f environment.yml

RUN python -m nltk.downloader popular

# Activate conda for local development with orgenv kernel conda environment 
SHELL ["conda", "run", "-n", "bicti", "/bin/bash", "-c"]