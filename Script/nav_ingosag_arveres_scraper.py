#!/usr/bin/env python3

import os
import re
import time
import datetime
import unicodedata
from pathlib import Path

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


OUTDIR = Path("/home/xunguist/NAV_arveresek/NAV-ingosag-arveres-scraper")


URL = "https://arveres.nav.gov.hu/index-meghirdetesek-ingosag"\
".html?.actionId=action.auction.FilterAction&fi=kategoriaFilter&fk"\
"=auctionFilterData_1&v=-1&FRAME_SKIP_DEJAVU=1"
res = requests.get(URL)
res.raise_for_status()
content = res.text
soup = BeautifulSoup(content, 'html.parser')
rows = soup.find_all("tr",{'class': "Bg2"})
all_items_df = pd.DataFrame()

for row in rows:
    item_type = row.find_all("a")[0].get_text()
    
    item_name = row.find_all("td")[2].get_text()
    
    auction_url = row.find_all("a",href=True)
    auction_id_re = re.search('(?<=auctionId=)(.*)', 
                              str(auction_url))
    auction_id = auction_id_re.group(0).split("&")[0]
    item_url = f"https://arveres.nav.gov.hu/index-meghirdetesek-ingosag."\
    "html?.actionId=action.auction.AuctionSummaryAction&auctionId="\
    f"{auction_id}&FRAME_SKIP_DEJAVU=1"
    auction_id_long = row.find_all("td")[1].get_text()
    
    raw_price = row.find_all("td")[3].get_text()
    price = int(unicodedata.normalize('NFKC', raw_price).replace(" ",""))
    
    posted_on_raw = row.find_all("td")[4].get_text()
    posted_on = datetime.datetime.strptime(posted_on_raw, 
                                           '%Y.%m.%d. %H:%M')
    begins_at_raw = row.find_all("td")[5].get_text()
    begins_at = datetime.datetime.strptime(begins_at_raw, 
                                           '%Y.%m.%d. %H:%M')
    ends_at_raw = row.find_all("td")[6].get_text()
    ends_at = datetime.datetime.strptime(ends_at_raw, 
                                           '%Y.%m.%d. %H:%M')
    contact_tel = row.find_all("td")[7].get_text()
    
    row_dict = {}
    row_dict["item_type"] = [item_type]
    row_dict["item_name"] = [item_name]
    row_dict["price"] = [price]
    row_dict["posted_on"] = [posted_on]
    row_dict["begins_at"] = [begins_at]
    row_dict["ends_at"] = [ends_at]
    row_dict["contact_tel"] = [contact_tel]
    row_dict["auction_id"] = [auction_id]
    row_dict["auction_id_long"] = [auction_id_long]
    row_dict["item_url"] = [item_url]

    row_df = pd.DataFrame.from_dict(row_dict,orient="columns")
    all_items_df = all_items_df.append(row_df)
    
all_items_df.dropna(subset=["auction_id"],inplace=True)
all_items_df["auction_id"] = all_items_df["auction_id"].astype("int")
all_items_df.set_index("auction_id",inplace=True)

ts =  datetime.datetime.now().strftime("%Y_%m_%d")
all_items_df.to_csv(OUTDIR/f"nav_arveresek_{ts}.csv")

print(OUTDIR)
print(f"nav_arveresek_{ts}.csv")
