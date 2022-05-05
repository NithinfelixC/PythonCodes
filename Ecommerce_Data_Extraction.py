import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import re
#from datetime import datetime
import ipaddress
import time
start_time = datetime.now()

data = pd.read_excel(r'input.xlsx')   
len(data)

# Import data from file excel
columns_list = ["url","product_title","delivery_time","size","price"]
result = pd.DataFrame(columns = columns_list)


# Function using regex to extract the size from string based on size pattern
def get_size_func(get_size):
    for item in str(get_size).split("\n"):
        if "selected" in item:
            if re.search('value="(.+?)">', item):
                m = re.search('(\d+)\s*x\s*(\d+)', item)
                if m:
                    size = m.group(0).replace(" ","")
                    return size

# Function to extract different informations of the product
def do_task(iteration,data):
    url = data.iloc[iteration,0]
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    product_title = ""
    size = ""
    delivery_time =""
    #available =""
    price = ""

    try:
        product_title = soup.find("div", class_  = "Overview-TitleLeft").get_text().strip()
    except:
        pass
    try:
        price = soup.find("div", class_  = "uptfEnHZrwaxsa5cxQ0L").get_text().strip()
    except:
        pass
    try:
        size = soup.find("span", class_  = "ProductVariantGroup-Title-GroupValue").get_text().strip()
    except:
        pass
    try:
        delivery_time = soup.find("div", class_  = "OGN5NAwA_yDY4OdM0D1T").get_text().strip()
    except:
        pass
    try:
        delivery_time = soup.find("div", class_  = "OGN5NAwA_yDY4OdM0D1T").get_text().strip()
    except:
        pass
    
    
    try:
#              
        
#         Get the size from title 
        if size is None:
            m = re.search('(\d+)\s*x\s*(\d+)', product_title)
            if m:
                size = m.group(0).replace(" ","")
                
#        
        if size is None:
            size = ""
            
    except:
        pass
    output = [url,product_title,delivery_time,size,price]
    return output

ip = 1
# Running the loop to crawl links in file import
for iteration in range(len(data)):
    print(f"We are working on the {iteration + 1} link")

    if iteration % 10 == 0:
        ipaddress.IPv4Address(f"192.168.1.{ip}")
        ip = ip + 1
    if iteration != 0 and iteration % 50 == 0:
        time.sleep(30)
        
        
    output = do_task(iteration,data)    
    result.loc[len(result)] = output
    
    if result['product_title'].isnull().values.any():
        break

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

timestr = time.strftime("%Y%m%d-%H%M%S")
name = "Check24_PC_"+timestr
result.to_excel(r'{}.xlsx'.format(name), index=False)   
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

