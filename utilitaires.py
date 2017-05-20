from urllib.request import urlretrieve


def download_zip(url, path):
    # create a zipfile to receive the datas
    output = open(path, "w")
    output.close()
    urlretrieve(url, path)
    return


def main():
    download_zip("http://data.assemblee-nationale.fr/static/openData/repository/VP/reunions/Agenda_XIV.json.zip","./test.zip")

if __name__ == '__main__':
    main()