import os
import requests
for i in range(1,562):
    url = 'https://image.slidesharecdn.com/clinical-20manual-20for-20oral-140206021148-phpapp02/95/clinical-manual-for-oralmedicine-and-radiology-'+str(i)+'-638.jpg'
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'page{}{}'.format(i,f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)