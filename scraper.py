import pandas as pd
import requests as http

ETHERSCAN_URL = "https://etherscan.io/blocks"


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


def getBlockTable():
    response = http.get(ETHERSCAN_URL, headers=header)

    if response.status_code != 200:
        raise Exception

    df = pd.read_html(response.content)[0]
    df.rename(columns={"Unnamed: 1": "Block Age"})
    return df.head().iloc[0, 0]
