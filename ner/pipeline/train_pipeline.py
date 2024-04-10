import sys
from ner.components.data_ingestion import DataIngestion
from ner.configuration.gcloud import GCloud
from ner.constants import *
from ner.entity.artifact_entity import DataIngestionArtifacts, DataTransformationArtifacts
from ner.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from ner.exception import NerException
from ner.logger import logging

from ner.components.data_transforamation import DataTransformation

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.gcloud = GCloud()
        
    # starting second method data ingestion
    
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of train pipeline class")
        try:
            logging.info("getting the data from google cloud storage")
            
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config, gcloud=self.gcloud
            )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Got the file from Google cloud storage. File name - {os.path.basename(self.data_ingestion_config.gcp_data_file_path)}")
            logging.info(
                'Exited the start_data_ingestion method of TrainPipeline class'
            )
            return data_ingestion_artifact
        except Exception as e:
            raise NerException(e, sys) from e
        
        
    
     # This method is used to start the data validation
    def start_data_transformation(
        self, data_ingestion_artifact: DataIngestionArtifacts
    ) -> DataTransformationArtifacts:
        logging.info(
            "Entered the start_data_transformation method of TrainPipeline class"
        )
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.data_transformation_config,
                data_ingestion_artifacts=data_ingestion_artifact,
            )

            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )

            logging.info("Performed the data validation operation")
            logging.info(
                "Exited the start_data_transformation method of TrainPipeline class"
            )
            return data_transformation_artifact

        except Exception as e:
            raise NerException(e, sys) from e
        
        
        
    # this method is use to start the training pipeline
    
    def run_pipeline(self) -> None:
        try:
            logging.info('started model training >>>>>>>>>>>>>>>>>>')
            data_ingestion_artifact = self.start_data_ingestion()
            data_transformation_artifact = self.start_data_transformation(
                data_ingestion_artifact = data_ingestion_artifact
            )
            
        except Exception as e:
            raise NerException(e, sys) from e
    