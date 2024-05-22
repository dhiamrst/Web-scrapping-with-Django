# '''
#  This script is used to extract data from the excel file.
#  🚨🚨🚨🚨🚨🚨🚨🚨  IMPORTANT --------->  
 
#  note that this script should be run in a django environment
#  USE: python manage.py shell
#  THEN: exec(open('projetPython\extract.py').read())
# '''

from Jumia.models import Smartphone
import pandas as pd

df = pd.read_csv('C:\\Users\\dhiam\\Desktop\\ProjetRSI\\projetPython\\scrap\\data.csv',names=['brand', 'price'])


for index, row in df.iterrows():
    try:
        price = ''.join(c for c in row['price'] if c.isdigit() or c == '.')
        price = float(price)
        smartphone, created = Smartphone.objects.create(
            brand=row['brand'],
            price=price
        )
    except Exception as e:
        print(f"Error at index {index}: {str(e)}")