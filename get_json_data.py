import pandas as pd
import json
import os
from flask import Flask, request, session
from github import Github

g = Github("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")

#######################################    Consumer   ###################################################

def get_dropdown_intent_consumer():   
    b=[]
    with open(r'data\intent.json','r') as f:
        data = json.load(f)
        for x in data['data']:          
            #print(x['responses'])
            b.append(x['responses'])
        return b
def show_dropdownIntent_Keywords_ConSubFunctionalArea():     
    if request.method=='POST':
        response=request.form['Intent_consumer']
    with open(r'data\intent.json','r') as f:                        
            data = json.load(f)
            for x in data['data']:
                a=x['patterns']
                b=x['responses']
                for words in b:
                    if response==words:
                        return a 
def del_keywords_ConSubFunctionalArea():
    if request.method=='POST':
        response=request.form['del_word']
        response1=request.form['Intent_consumer']
        org=response.replace("|","'")
        print(org)
        print(response1)
    with open(r'data\intent.json') as f:
        data=json.load(f)
        for  x in data['data']:
            z=x['responses']
            y=x['patterns']
            for words in z:
                if words==response1:
                    y.remove(org)
                    #try:
                    for repo in g.get_user().get_repos():
                        if repo.name == 'Workout':                            
                            repo.edit(has_wiki=False)
                            #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                            file = repo.get_contents("intent.json")
                            print(repo.name)
                            repo.update_file("intent.json", "FileUpdated", str(data), file.sha)
                    
                            f = open(r"data\intent.json", "w")
                            json.dump(data, f,indent=4)
                    # except Exception as e:
                    #     print(str(e))
                    #     pass

def Show_Keywords_ConAutoSuggestion():   
    with open(r'data\All_Consumer_Keywords.json') as f:
        data2=json.load(f)
        return data2['keywords']

def get_new_Keywords_ConAutoSuggestion():
    if request.method=='POST':
        response=request.form['Keyword']
    with open(r'data\All_Consumer_Keywords.json') as f:
        data=json.load(f)
        x=data['keywords']
        x.append(response)
        for repo in g.get_user().get_repos():
            if repo.name == 'Workout':                            
                repo.edit(has_wiki=False)
                #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                file = repo.get_contents("intent.json")
                print(repo.name)
                repo.update_file("intent.json", "FileUpdated", str(data), file.sha)
                f = open("C:\\Users\ELCOT\python_env\c2c\edit_entities\MasoriPOC-main\data\All_Consumer_Keywords.json", "w")
                json.dump(data, f,indent=4)

def delete_Keywords_ConAutoSuggestion():
    if request.method=='POST':
        response=request.form['KeywordDelete']
        res=response.replace("|","'")
    with open(r'data\All_Consumer_Keywords.json') as f:
        data=json.load(f)
        x=data['keywords']
        x.remove(res)
        for repo in g.get_user().get_repos():
            if repo.name == 'Workout':                            
                repo.edit(has_wiki=False)
                #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                file = repo.get_contents("All_Consumer_Keywords.json")
                print(repo.name)
                repo.update_file("All_Consumer_Keywords.json", "FileUpdated", str(data), file.sha)
        f = open("C:\\Users\ELCOT\python_env\c2c\edit_entities\MasoriPOC-main\data\All_Consumer_Keywords.json", "w")
        json.dump(data, f,indent=4)

def Add_Keyword_ConSubFunctionalArea():
    if request.method=='POST':
        response=request.form['Add_Keyword']
        response1=request.form['Intent_consumer']
        print(response)
        with open(r'data\intent.json') as f:
            data=json.load(f)
            for  x in data['data']:
                z=x['responses']
                y=x['patterns']
                for words in z:
                    if words==response1:
                        y.append(response)

                        for repo in g.get_user().get_repos():
                            if repo.name == 'Workout':                            
                                repo.edit(has_wiki=False)
                                #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                                file = repo.get_contents("intent.json")
                                print(repo.name)
                                repo.update_file("intent.json", "FileUpdated", str(data), file.sha)    

                                f = open(r"data\intent.json", "w")
                                json.dump(data, f,indent=4)
        
   
#######################################    HCP   ###################################################
def get_dropdown_intent_HCP():  
    w=[] 
    with open(r'data\HCP_intent.json','r') as f:
        data = json.load(f)
        for x in data['data']:          
            #print(x['responses'])
            w.append(x['responses'])
        return w
def show_dropdownIntent_Keywords_HCPSubFunctionalArea():     
    if request.method=='POST':
        response=request.form['Intent_hcp']
    with open(r'data\HCP_intent.json','r') as f:                        
            data = json.load(f)
            for x in data['data']:
                a=x['patterns']
                b=x['responses']
                for words in b:
                    if response==words:
                        return a 

def Show_Keywords_HCPAutoSuggestion():   
    with open(r'data\All_HCP_Keywords.json') as f:
        data2=json.load(f)
        return data2['keywords']

def get_new_Keywords_HCPAutoSuggestion():
    if request.method=='POST':
        response=request.form['Keyword']
    with open(r'data\All_HCP_Keywords.json') as f:
        data=json.load(f)
        x=data['keywords']
        x.append(response)
        for repo in g.get_user().get_repos():
            if repo.name == 'Workout':                            
                repo.edit(has_wiki=False)
                #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                file = repo.get_contents("All_HCP_Keywords.json")
                print(repo.name)
                repo.update_file("All_HCP_Keywords.json", "FileUpdated", str(data), file.sha)
                f = open(r"data\All_HCP_Keywords.json", "w")
                json.dump(data, f,indent=4)

def del_keywords_HCPSubFunctionalArea():
    if request.method=='POST':
        response=request.form['del_word']
        response1=request.form['Intent_hcp']
        org=response.replace("|","'")
        print(org)
        print(response1)
    with open(r'data\HCP_intent.json') as f:
        data=json.load(f)
        for  x in data['data']:
            z=x['responses']
            y=x['patterns']
            for words in z:
                if words==response1:
                    y.remove(org)
                    for repo in g.get_user().get_repos():
                        if repo.name == 'Workout':                            
                            repo.edit(has_wiki=False)
                            #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                            file = repo.get_contents("HCP_intent.json")
                            print(repo.name)
                            repo.update_file("HCP_intent.json", "FileUpdated", str(data), file.sha)
                            f = open(r"data\HCP_intent.json", "w")
                            json.dump(data, f,indent=4)

def Add_Keyword_HCPSubFunctionalArea():
    if request.method=='POST':
        response=request.form['Add_Keyword']
        response1=request.form['Intent_hcp']
        print(response)
        with open(r'data\HCP_intent.json') as f:
            data=json.load(f)
            for  x in data['data']:
                z=x['responses']
                y=x['patterns']
                for words in z:
                    if words==response1:
                        y.append(response)
                        for repo in g.get_user().get_repos():
                            if repo.name == 'Workout':                            
                                repo.edit(has_wiki=False)
                                #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                                file = repo.get_contents("HCP_intent.json")
                                print(repo.name)
                                repo.update_file("HCP_intent.json", "FileUpdated", str(data), file.sha)
                        f = open(r"data\HCP_intent.json", "w")
                        json.dump(data, f,indent=4)

def delete_Keywords_HCPAutoSuggestion():
    if request.method=='POST':
        response=request.form['KeywordDel']
        org1=response.replace("|","'")
    with open(r'data\All_HCP_Keywords.json') as f:
        data=json.load(f)
        x=data['keywords']
        x.remove(org1)
        for repo in g.get_user().get_repos():
            if repo.name == 'Workout':                            
                repo.edit(has_wiki=False)
                #repo.create_file("Test.txt", "Initial Changes", "Wonderful")
                file = repo.get_contents("All_HCP_Keywords.json")
                print(repo.name)
                repo.update_file("All_HCP_Keywords.json", "FileUpdated", str(data), file.sha)
        f = open("data\All_HCP_Keywords.json", "w")
        json.dump(data, f,indent=4)


#######################################    Login   ###################################################

def check_user(username, password):
    if username.lower() == 'admin' and password == 'mt1@nz1$':
        return True
    if username.lower() == 'masori' and password == 'v1@mst1$':
        return True
        
