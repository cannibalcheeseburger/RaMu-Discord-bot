import datetime
import requests
import json
import re
clean = re.compile('<.*?>')


def recipeofday(token):
    today_date = datetime.date.today()
    reci = open('./src/reci.txt','r+')


    text = reci.read()

    if not str(today_date) == text.partition('\n')[0].strip():
        #truncate file
        reci.seek(0)
        reci.truncate(0)
        
        #get recipe and save in RECIPE
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

        querystring = {"number":"1","tags":"vegetarian%2Cdessert"}

        headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': "824bc0944dmsha1058bd1b0cc53ap1e9c21jsnb8d7f51fef9e"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data  = response.json()
        title = ""
        ingre = ""
        inst =""
        for item  in data['recipes']:
            title = item['title']
            count = 1
            for ing in item['extendedIngredients']:
                ingre = ingre + str(count)+'. '+ing['original']+'\n'
                count = count +1
            inst = re.sub(clean,'',item['instructions'])
     
        #add recipe to text
        text = str(today_date).strip() + """\nRECIPE OF THE DAY:\n""" + title+'\n\nINGREDIENTS:\n'+ingre+"\n\nINSTRUCTIONS:\n"+inst
        
        #replace text to file
        reci.writelines(text)

    reci.close()
    #return this
    return(text)


