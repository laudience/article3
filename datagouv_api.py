import requests
import json
from zipfile import ZipFile
from utilitaires import *


class GetData:
    def __init__(self, id):
        self.url = 'https://www.data.gouv.fr/api/1/datasets/' + id
        self.dataset = []

    def get_dataset_info(self):
        print(self.url)
        dataset_info_json = requests.get(self.url).json()
        print('Number of datasets :', len(dataset_info_json['resources']))

        for dataset in dataset_info_json['resources']:  # Save the datasets URL .zip
            self.dataset.append({'title': dataset['title'], 'url': dataset['url']})
            print(dataset['title'], dataset['format'], dataset['url'])

    def download(self):
        self.get_dataset_info()

        for dataset in self.dataset:
            zip_path = './datas/zipfiles/' + dataset['title'] + '.zip'
            download_zip(dataset['url'], zip_path)

            zipfile = ZipFile(zip_path)
            zipfile.extractall(path='./datas')

def main():
    finances_publiques = GetData('58306906c751df14a8c0bb7e')
    finances_publiques.download()

if __name__ == '__main__':
    main()
