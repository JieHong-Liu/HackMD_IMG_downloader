import requests
import json



def download_image(url, save_path, token,cookies_dict):

    headers = {
            'Authorization': f'Bearer {token}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    }  

    response = requests.get(url, headers=headers, cookies=cookies_dict)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f'img {url} download success')
    else:
        print(f'can not download {url}', '(resp code : ', response.status_code, ')')



with open('cookies.json') as f:
    myCookies = json.load(f)

    # transfer cookie list to dict
    cookies_dict = {}
    for cookie in myCookies:
        cookies_dict[cookie['name']] = cookie['value']

# read url list
file_path = './hackmd_image_urls.txt'
with open(file_path, 'r') as file:
    image_urls = file.readlines()


token = # put your token here

# download all imgs
for url in image_urls:
    url = url.strip()  # remove space and newline
    save_location = f'./downloaded_images/{url.split("/")[-1].strip()}'
    download_image(url, save_location, token, cookies_dict)
