#!/usr/bin/env python
# coding: utf-8




#https://summerofcode.withgoogle.com/archive/2019/organizations/
from bs4 import BeautifulSoup
import requests
year=str(input("Enter the year "))
url="https://summerofcode.withgoogle.com/archive/{}/organizations/".format(year)
nametech=str(input("Enter Name of the technology that you want to see "))
r=requests.get(url)
#print(r.url)
soup=BeautifulSoup(r.content,"html.parser")
#r.content
orgs = soup.findAll('li', attrs = {"class": "organization-card__container"})
#print(orgs)
count=1
count2=0
for org in orgs:
    nm=org.find("h4",attrs={"class":"organization-card__name"})
    name=nm.text
    label=org.find("a",attrs={"class":"organization-card__link"})
    link=label["href"]
    
    link2=str("https://summerofcode.withgoogle.com"+link)
    
    count+=1
    r2=requests.get(link2)
    soup2=BeautifulSoup(r2.content,"html.parser")
    techs=soup2.find("ul",attrs={"class":"org__tag-container"})
    techused=techs.text
#     print(techused)
#     print(len(techused))
    list=[]
    list=techused.split()
#     #print(list)
    
    
    for j in list:
        if (j==nametech):
            
#             print("yes")
#             print("Organization No "+str(count))
#             print(name)
#             print(link2)
#             print(list)
            count2+=1
            with open("Gsoc_Tech_Used_{}_{}.txt".format(year,nametech),"a+") as file: # Write binary file mode
                file.write("Organization No "+str(count))
                file.write(" | No of Organizations using this tech "+ str(count2))
                file.write("\n")
                file.write(name)
                file.write("\n")
                file.write(link2)
                file.write("\n")
                for m in list:
                    file.write(m)
                    file.write("\n")
                file.write("\n")
        
        
    







