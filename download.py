import requests

def download(url):
    try:
        req=requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Invalid URL "{}"'.format(url))
        return
    if req.status_code==403
        print('You do not have the authority to access this page.')
        return
    filename=url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
