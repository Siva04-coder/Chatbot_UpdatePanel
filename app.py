from flask import Flask, render_template, request, session
from flask.templating import render_template_string
from flask.wrappers import Response
import  db_proxy,json

app = Flask(__name__)
app.secret_key = 'POC1'
login_users = []
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/logon', methods=['GET', 'POST'])
def logon():
    print(request.method)
    res = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        res = db_proxy.check_user(username, password)

        if res == True:
            login_users.append(username)
            session["username"] = username

    return json.dumps(res)


@app.route('/home')
def home():
    try:
        if session["username"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
    session["page_name"] = ""
    return render_template('land.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    status = ""

    try:
        session["username"] = ''
        status = "updated"
    except:
        pass

    return status

############################################# consumer ##################################################

@app.route('/ConSubFunctionalArea')
def deletekeywords():
    try:
        if session["username"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')

    session["page_name"] = "Consumer Sub Functional Area"
    return render_template('ConSubFunctionalArea.html')

@app.route('/ConAutoSuggestion')
def addkeywords():
    try:
        if session["username"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')

    session["page_name"] = "Consumer Auto Suggestion"
    return render_template('ConAutoSuggestion.html')

@app.route('/Show_Keywords_ConAutoSuggestion', methods=['GET', 'POST'])
def Show_Keywords_ConAutoSuggestion():
    key = db_proxy.Show_Keywords_ConAutoSuggestion()
    #print(json.dumps(int))
    return json.dumps(key)

@app.route('/get_dropdown_intent_consumer', methods=['GET', 'POST'])
def get_dropdown_intent_consumer():
    intg = db_proxy.get_dropdown_intent_consumer()
    #print(json.dumps(int))
    return json.dumps(intg)

@app.route('/show_dropdownIntent_Keywords_ConSubFunctionalArea', methods=['GET', 'POST'])
def show_dropdownIntent_Keywords_ConSubFunctionalArea():
    int1 = db_proxy.show_dropdownIntent_Keywords_ConSubFunctionalArea()
    #print(json.dumps(int1))
    return json.dumps(int1)


@app.route('/patient_details_grid')
def patient_details_grid():
    entPats = db_proxy.show_dropdownIntent_Keywords_ConSubFunctionalArea('46260','','','')
    return render_template('patient_details_grid.html', results = entPats)

@app.route('/get_new_Keywords_ConAutoSuggestion', methods=['GET', 'POST'])
def get_new_Keywords_ConAutoSuggestion():
    int1 = db_proxy.get_new_Keywords_ConAutoSuggestion()
    #print(json.dumps(int1))
    return json.dumps(int1)
    
@app.route('/Add_Keyword_ConSubFunctionalArea', methods=['GET', 'POST'])
def Add_Keyword_ConSubFunctionalArea():
    int1 = db_proxy.Add_Keyword_ConSubFunctionalArea()
    #print(json.dumps(int1))
    return json.dumps(int1)

@app.route('/del_keywords_ConSubFunctionalArea', methods=['GET', 'POST'])
def del_keywords_ConSubFunctionalArea():
    int1 = db_proxy.del_keywords_ConSubFunctionalArea()
    #print(json.dumps(int1))
    return json.dumps(int1)
@app.route('/delete_Keywords_ConAutoSuggestion', methods=['GET', 'POST'])
def delete_Keywords_ConAutoSuggestion():
    word2 = db_proxy.delete_Keywords_ConAutoSuggestion()
    #print(json.dumps(int1))
    return json.dumps(word2)
##########################################  HCP ###############################################


@app.route('/HCPSubFunctionalArea')
def deleteKeywords_HCP():
    try:
        if session["username"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')

    session["page_name"] = "HCP Sub Funcational Area"
    return render_template('HCPSubFunctionalArea.html')

@app.route('/HCPAutoSuggestion')
def addKeywords_HCP():
    try:
        if session["username"] == "":
            return render_template('login.html')
    except:
        return render_template('login.html')
        
    session["page_name"] = "HCP Auto Suggestion"
    return render_template('HCPAutoSuggestion.html')

@app.route('/get_dropdown_intent_HCP', methods=['GET', 'POST'])
def get_dropdown_intent_HCP():
    int = db_proxy.get_dropdown_intent_HCP()
    #print(json.dumps(int))
    return json.dumps(int)

@app.route('/show_dropdownIntent_Keywords_HCPSubFunctionalArea', methods=['GET', 'POST'])
def show_dropdownIntent_Keywords_HCPSubFunctionalArea():
    int1 = db_proxy.show_dropdownIntent_Keywords_HCPSubFunctionalArea()
    #print(json.dumps(int1))
    return json.dumps(int1)

@app.route('/Show_Keywords_HCPAutoSuggestion', methods=['GET', 'POST'])
def Show_Keywords_HCPAutoSuggestion():
    key = db_proxy.Show_Keywords_HCPAutoSuggestion()
    #print(json.dumps(int))
    return json.dumps(key)

@app.route('/get_new_Keywords_HCPAutoSuggestion', methods=['GET', 'POST'])
def get_new_Keywords_HCPAutoSuggestion():
    int1 = db_proxy.get_new_Keywords_HCPAutoSuggestion()
    #print(json.dumps(int1))
    return json.dumps(int1)

@app.route('/Add_Keyword_HCPSubFunctionalArea', methods=['GET', 'POST'])
def Add_Keyword_HCPSubFunctionalArea():
    int1 = db_proxy.Add_Keyword_HCPSubFunctionalArea()
    #print(json.dumps(int1))
    return json.dumps(int1)

@app.route('/del_keywords_HCPSubFunctionalArea', methods=['GET', 'POST'])
def del_keywords_HCPSubFunctionalArea():
    int1 = db_proxy.del_keywords_HCPSubFunctionalArea()
    #print(json.dumps(int1))
    return json.dumps(int1)

@app.route('/delete_Keywords_HCPAutoSuggestion', methods=['GET', 'POST'])
def delete_Keywords_HCPAutoSuggestion():
    word = db_proxy.delete_Keywords_HCPAutoSuggestion()
    #print(json.dumps(int1))
    return json.dumps(word)

