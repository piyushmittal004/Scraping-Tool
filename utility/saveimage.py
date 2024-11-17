import os
import requests

def save_image(url:str, img_path:str) -> str:
    try:
        os.makedirs(img_path, exist_ok=True)
        img_name = url.split('/')[-1]
        img_dir = os.path.join(img_path,img_name)
        response = requests.get(url, stream=True)
        with open(img_dir, "wb") as fd:
            for chunk in response.iter_content(1024):
                fd.write(chunk)
        return img_dir
    except Exception as e:
        print(f"An error occured: {e}")