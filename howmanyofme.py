try:
    import requests
    from bs4 import BeautifulSoup
except:
    raise ModuleNotFoundError("Please install requests and BeautifulSoup4 before using this Aceruos module!")



def howmanyofme(name:str):
    name = name.split(" ")
    fname = name[0]
    lname = " ".join(name[1:]) # Gets first and last names
    if name.__len__() <= 1:
        return {'success':False} # if no last name
    try:
        data=requests.post("http://howmanyofme.com/search/", data={'given':fname,'sur':lname,'ofage':'yes'}) # Same thing the site does
    except:
        return {'success':False} # if site down/bad request

    soup = BeautifulSoup(data.text, 'html.parser')

    li = soup.find_all('li')
    f_li = int([el for el in li if "people in the U.S. with the first name" in el.text][0].find('span',{'class':'popnum'}).text.replace(",","")) # first name count
    l_li = int([el for el in li if "people in the U.S. with the last name" in el.text][0].find('span',{'class':'popnum'}).text.replace(",","")) # last name count
    li = [el for el in li if "in the U.S. named" in el.text] # gets name count

    li = li[0]

    tex = li.find('span', {'class':'popnum'}).text # final name count

    tex=int(tex) # convert count to int

    howmany = {'success':True,'firstname':fname.lower().capitalize(),'lastname':lname.lower().capitalize(),'count':tex,'first_count':f_li,'last_count':l_li,'or_fewer':False}



    if "or fewer" in li.text:
        howmany['or_fewer'] = True # if uncertain results

    return howmany