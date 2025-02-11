## Steps to setup vertexai locally inour machine

## install GCP CLI


## Create the virtual environment
````bash
conda create --name vertexai python=3.10 -y
conda activate vertexai
````


## Install the required packages
````bash
python -m pip install -r requirements.txt
````
##  Initialize the GCP project
````bash
gcloud init
````


## Run the main.py file
````bash
streamlit run main.py
````