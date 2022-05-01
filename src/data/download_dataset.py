from google.cloud import storage 
import os 
import  sys 
import json 

def download_dataset():
    """Downloads the dataset from my google cloud bucket and saves it under data/raw folder
    """
    path = os.path.join(os.getcwd(), "recommendationmlops-deb1e6a11df0.json")
    print(f"using {path} for credentials")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= path 

    storage_client = storage.Client(path)
    bucket = storage_client.get_bucket("movie-dataset-mlops")
    filename = [filename.name for filename in list(bucket.list_blobs(prefix=''))]

    for file in filename: 
        print(f"Downloading {file} into data/raw ")
        blop = bucket.blob(blob_name = file).download_as_string()
        with open(os.path.join('data/raw', file), 'wb') as f: 
            f.write(blop)
    # we can read the file immediately to  pandas using pd.read_csv(io.BytesIo(blop), encoding='UTF-8', sep=',')
if __name__ == "__main__":
    download_dataset()