import requests
from bs4 import BeautifulSoup
import pprint
resp= requests.get("https://www.goal.com/en-us/results/2020-01-05")
raw_text= BeautifulSoup(resp.content, 'html.parser')
status=raw_text.select('.match-row__data')
comp_name= raw_text.select('.competition-matches')
link_name= raw_text.select('.match-row__link')
#pprint.pprint(comp_name)
#pprint.pprint(link_name)

def goal(status,link_name):
    num=0
    lst=[]
    lst2=[]
    for i,j in enumerate (status):
        title= status[i].getText()
        
        link= link_name[(i+3) +num ].get('href', None)
        num=num+3
        print(title)
        complete_link= "https://www.goal.com" + link
        print(complete_link)
        print("\n")
        lst.append({'Match-Info':title, 'Link': link})
    return lst
        
        

#pprint.pprint(goal(status,link_name))
def teams(data):
    #print(data)
    lst=[ "AFC Bournemouth", "Arsenal", "Aston Villa", "Brighton & Hove Albion", "Burnley","Chelsea" ,"Crystal Palace" ,"Everton" ,"Leicester City" , "Manchester City",
          "Liverpool" ,"Manchester United" , "Newcastle United" , "Norwich City" , "Sheffield United" ,"Tottenham Hotspur"  , "Watford" ,"West Ham United","Wolverhampton Wanderers"]
    for i in range(len(lst)):
        x=data.find(lst[i])>0
        #print(x)
        if x==True:
            return "Premiere League"
    lst2=["Alavés", "Athletic Bilbao","Atlético Madrid","Barcelona","Celta Vigo","Eibar","Espanyol","Getafe","Granada","Leganés","Levante","Mallorca","Osasuna","Real Betis","Real Madrid", 	
"Real Sociedad","Sevilla","Valencia","Valladolid","Villarreal"]
    for i in range(len(lst2)):
        x=data.find(lst2[i])>0
        #print(x)
        if x==True:
            return "La Liga Santandir"

    
    return "Other League"



def goalwebscraper(comp):
    for i,j in enumerate (comp):
        name= comp[i].select('.competition-title')     #get competition name inside the achor tags
        new_name= str(name[i].getText())      # get competition name from achor tags
        #print(name)
        #print(new_name)
        num=0
        lst=[]
        lst2=[]
        for i,j in enumerate (status):
            title= status[i].getText()
            
            link= link_name[(i+3) +num ].get('href', None)
            num=num+3
            new_title = str(title).replace(" ","")
            print(title)
            #print(new_title)
            competition_name=teams(new_title)
            complete_link= "https://www.goal.com" + link
            print(complete_link)
            print("\n")
            lst.append({'Match-Info':title, 'Link': complete_link, "Competition Name": competition_name  })
        return lst
pprint.pprint(goalwebscraper(comp_name))




