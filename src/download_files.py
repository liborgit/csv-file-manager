import requests
import os


def download_files(url_list, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for index, url in enumerate(url_list, start=1):

        safe_filename = f"datablist-{index}.csv"

        local_filename = os.path.join(download_folder, safe_filename)

        with requests.get(url) as r:
            with open(local_filename, 'wb') as f:
                f.write(r.content)
        print(f"Downloaded: {local_filename}")

    return download_folder


url_list = [
    "https://drive.google.com/uc?id=1phaHg9objxK2MwaZmSUZAKQ8kVqlgng4&export=download",
    "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download",
    "https://drive.google.com/uc?id=1VEi-dnEh4RbBKa97fyl_Eenkvu2NC6ki&export=download"
]

download_folder = "downloads"

download_files(url_list, download_folder)