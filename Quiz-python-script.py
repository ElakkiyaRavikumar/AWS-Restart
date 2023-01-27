import json
from pathlib import Path 
import os

with open("Customer-details.json", 'r') as f:
    cust_det = json.load(f)
    print(f'The Customer details are: \n {cust_det}')
    print("\nThe Customer names are:")
    for row in cust_det:
        print(cust_det['Customer'][0]['Name'])
        print(cust_det['Customer'][1]['Name'])
 
    for item in cust_det['Customer']:
        item['City'] = item['City'].replace('Frankfurt', 'Hamburg')

    with open('Customer-details_update.json', 'w') as f1:
        json.dump(cust_det, f1)
    f1.close()
    f.close()