import requests
from pprint import pprint
from bs4 import BeautifulSoup
import 	json
import os 
import pathlib

url= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
url1=requests.get(url)

soup = BeautifulSoup(url1.text,"html.parser")
main_data=soup.find("div",class_="_1LZ3")
pikal_product=main_data.find("div",class_="_3RA-")
product=main_data.find("div",class_="_1EI9").span.get_text()
index=product.split()
index_data=index[1]
product_number = int(index_data)//32+1
print(index,index_data,product_number)

def pikel_data():
    number=1
    pikal_list=[] 
    # for j in range(1,product_number+1):
    #     url_data_store="picakle_data_files/"+"pikal"+str(j)+".json"
    #     filepath=pathlib.Path(url_data_store)
    #     if filepath.exists():
    #         with open(url_data_store,"r") as json_data:
    #             f=json_data.read()
    #             f1=json.loads(f)
            
    #         pikal_list.append(f1)
    # else:
    for j in range(1,product_number+1):
        pikal_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
        url_data=requests.get(pikal_url)
        soup1 = BeautifulSoup(url_data.text,"html.parser")
        main_data1=soup1.find("div",class_="_1LZ3")
        pikal_product1=soup1.find("div",class_="_3RA-")
        data1=pikal_product1.find_all("div",class_="_3WhJ")
        for i in data1:
            pikal_dic={}
            link=i.a["href"]
            link="https://paytmmall.com/"+link
            price=i.find("div",class_="_1kMS").span.get_text()
            name_div=i.find("div",class_="_2PhD").get_text()
            name = ""
            for i in name_div:
                if i.isalpha() == True or i == " ":
                    name = name + i
                else:
                    break
                    print(name)
            pikal_dic["pikal_name"]=name
            pikal_dic["pikal_url"]=link
            pikal_dic["pikal_price"]=price
            pikal_dic["pikal_position"]=number
            number=number+1
            pikal_list.append(pikal_dic)
            print(pikal_dic)
            print("**********")
            
                # url_data_store="picakle_data_files/"+"pikal"+str(number-1)+".json"
                # with open(url_data_store,"w") as data:
                #     data.write(json.dumps(pikal_dic))
    # return "pikallist",pikal_list
# pprint(pikel_data())



