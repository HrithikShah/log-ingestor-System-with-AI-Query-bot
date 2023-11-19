from flask import Flask, render_template,request
import embedchainbot as bot
import sql as sh
import json_to_csv as jscv
import os

app= Flask(__name__)



#homepage 
@app.route('/')
def homepage():
    return render_template('index.htm')


#Uploading and training embedchain bot on the files same time and
# saving it in FILE folder in static folder 
@app.route('/', methods=['POST'] )
def upload():
    if request.method == 'POST':
         
         # GET the list of files from webpage
         files=request.files.getlist("file")


         #iterate for each file in the files list and save them
         for file in files:
             
             # get filename
             check = file.filename

             #string is list have filename at string[0] and extension at string[1] 
             string=check.split('.')

             #Checking whether uploaded file is .json or .csv file.
             if string[1] == 'json':
                  file.save('static/FILE/'+str(file.filename))
                  loc1='static/FILE/'+str(file.filename)

                  #Converting .json  to .csv file for easier uploading to database and training bot.
                  jscv.json_to_csv(loc1)
                  loc2='converted_json.csv'
                  bot.train(loc2)
                  sh.upload_to_db(loc2)
                  os.remove(loc2)
             elif string[1] == 'csv':
                    
                    file.save('static/FILE/'+str(file.filename))
                    loc='static/FILE/'+str(file.filename)
                    bot.train(loc)
                    sh.upload_to_db(loc)

    return render_template('index.htm')
         

#get response of our query from the embedchain bot
@app.route("/get")
def get_bot_response():
    userText= request.args.get('msg')
    bot_response=bot.query(userText)
    return bot_response


if __name__=="__main__":
    
    app.run(port=3000)