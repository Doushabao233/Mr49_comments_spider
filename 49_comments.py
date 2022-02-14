import json
import time
import requests
import random

def get_like(tlp: tuple):
    return tlp[2]

aid: int = 766246209
i = 0
all_comments = []
like_sort_mode = True
print(f'aid: {aid}')

while 1:
    i += 1
    data = requests.get(f'http://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={i}&type=1&oid={aid}').json()
    print('len: ', len(data['data']['replies']))
    if len(data['data']['replies']) < 1:
        break
    else:
        all_comments.extend(data['data']['replies'])
    time.sleep(random.uniform(0.8, 1.2))

print('oh i finished step 1')
filter_data = []

for i in range(len(all_comments)):
    msg = all_comments[i]['content']['message']
    if len(msg) >= 20 or '建议' in msg or '觉得' in msg or '看法' in msg:
        filter_data.append((all_comments[i]['member']['uname'], all_comments[i]['content']['message'], all_comments[i]['like']))

if like_sort_mode:
    filter_data = sorted(filter_data, key=get_like, reverse=True)
print('step 2')

with open(f'49_comments_output_av{aid}.txt', 'w', encoding='u8') as f:
    for i in filter_data:
        # json.dumps(filter_data, ensure_ascii=False)
        f.write(f'{i[0]}:\n{i[1]}\n')
        f.write(f'[👍 点赞数] {i[2]}')
        f.write('\n==========================================\n')