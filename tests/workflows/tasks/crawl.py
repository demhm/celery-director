from director import task
import requests
import re
import time

@task(name="CRAWL", bind=True)
def extract(self, *args, **kwargs):
    print("START")
    payload = kwargs["payload"]
    resp = requests.get(payload.get('url'))
    total = 100
    for i in range(total):
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'current': i, 'total': total})
    
    return resp.content.decode('latin-1', 'utf-8')


@task(name="FIND_URL")
def transform(*args, **kwargs):
    print("Transforming data")
    #Find all links
    result = re.findall('<a href="(.*?)">(.*?)</a>', str(args[0]))
    return ''.join(''.join(tup) for tup in result)


@task(name="SAVE_FILE")
def load(*args, **kwargs):
    print("WRITE TO FILE")
    with open('html.txt', 'w') as f:
        f.write(args[0])