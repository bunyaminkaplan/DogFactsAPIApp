import requests
import json
from tkinter import *

window = Tk()
window.minsize(height= 200 , width= 200)
window.title("Dog Facts")
target_url = "https://dog-api.kinduff.com/api/facts"

def make_request(url):
    response = requests.get(url)
    print(response.status_code)
    return response

def jprint(obj): #print full json in json format

    text = json.dumps(obj , sort_keys= True , indent=4)
    print(text)




def show_a_fact():
    try:
        fact_label_row2.config(text="")
        facts = make_request(target_url)
        if facts.status_code != 404:
            if facts.json()['success'] == True:
                print("success")
                for fact in facts.json()['facts']:
                    fact_str : str = fact
                    if len(fact_str) > 100:
                        print(fact_str[0:100])
                        print("\n", fact_str[100:200])
                        fact_label.config(text=fact_str[0:100])
                        fact_label_row2.config(text=fact_str[100:200])
                    else:
                        fact_label.config(text=fact)



    except requests.exceptions.ConnectionError:
        print("check your internet connection")


new_fact_button = Button(text= "new fact" , command= show_a_fact)
new_fact_button.pack()

fact_label = Label(width=75)
fact_label.pack()
fact_label_row2 = Label()
fact_label_row2.pack()
window.mainloop()