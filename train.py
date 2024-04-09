# from ner.configuration.gcloud import GCloud
# obj = GCloud()

# obj.sync_folder_from_gcloud(gcp_bucket_url="ner-using-bert-95",filename="archive.zip",destination="test")



# we are calling end point here for intializing

import os
import sys
from ner.exception import NerException
from ner.pipeline.train_pipeline import TrainPipeline

from ner.constants import *

def training():
    try:
        train_pipeline = TrainPipeline()
   
       
        train_pipeline.run_pipeline()
    except NerException as e:
        raise NerException(e, sys) from e
            
if __name__ == "__main__":
    training()