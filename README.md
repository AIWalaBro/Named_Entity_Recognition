# Named_Entity_Recognition

# steps to create a named_entity_recognition_project

# Flow Chart
- **Data Ingestion**
<p align="center">
  <img src="https://github.com/AIWalaBro/Named_Entity_Recognition/blob/main/flow_charts/data_ingestion.svg" width=100% height=50%>
</p>

- **Data Transformation**
<p align="center">
  <img src="https://github.com/AIWalaBro/Named_Entity_Recognition/blob/main/flow_charts/data_transformation.svg" width=100% height=50%>
</p>


- **Model Training**
<p align="center">
  <img src="https://github.com/AIWalaBro/Named_Entity_Recognition/blob/main/flow_charts/mode_training.svg" width=100% height=50%>
</p>


## Workflows
- constants
- config_entity
- artifact_entity
- components
- pipeline
- app.py


## Git commands
```bash
git add .

git commit -m "Updated"

git push origin main

AWS GCP Configuration
```

```bash
# Gcloud cli download link: https://cloud.google.com/sdk/docs/install#windows
- gcloud init

- gcloud projects create ner_testing
or change to another project using

- gcloud config set project <PROJECT ID>
```

## How to run?
```bash
conda create -p venv_ner python=3.10 -y
conda activate  venv_ner
pip install -r requirements.txt
python app.py
```