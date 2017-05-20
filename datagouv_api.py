import requests
import json
from zipfile import ZipFile
from utilitaires import *


class GetData:

    def __init__(self, id):
        self.url = ''.join(['http://www.data.gouv.fr/api/1/datasets/', id, '/full/'])
        self.dataset_url = None
        self.dataset = None


    def get_community_dataset_url(self):
        response = requests.get(self.url).json()

        self.dataset_url = response['community_resources'][0]['url']
        print(self.dataset_url)

    def get_community_dataset(self):
        self.get_community_dataset_url()
        response = requests.get(self.dataset_url).json()

        self.dataset = response

    def save_community_dataset(self, outfile_name):
        self.get_community_dataset()
        outfile_directory = ''.join(['./datas/', outfile_name, '.json'])
        with open(outfile_directory, 'w') as outfile:
            json.dump(self.dataset, outfile)


    def get_zip_dataset_url(self):
        response = requests.get(self.url).json()

        self.dataset_url = response['resources'][1]['url']
        print(self.dataset_url)

    def get_dataset_from_zip(self, zipname):
        self.get_zip_dataset_url()
        zip_path = ''.join(['./datas/zipfile/', zipname, '.zip'])
        download_zip(self.dataset_url, zip_path)

        zipfile = ZipFile(zip_path)
        zipfile.extractall(path='./datas')
        file_list = zipfile.namelist()
        self.dataset = ZipFile(zip_path).read(file_list[0])

def main():
    GetData('58306906c751df14a8c0bb7e').get_zip_dataset_url()

if __name__ == '__main__':
    main()
