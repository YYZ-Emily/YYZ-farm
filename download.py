import requests
import os
def download(url):
    filename=url.split('/')[-1]
    if os.path.exists(filename):
        print('The file is already exist.')
        return
    try:
        req=requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    if req.status_code==403:
        print('You do not have the authority to access this page.')
        return
    filename=url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))

if __name__=='__main__':
    url=input('Enterd a URL:')
    download(url)
