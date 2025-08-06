'''from flask import Flask, redirect, url_for, request,render_template
from proj import inter
from proj_single import inter1
app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def valid():
    if request.method == 'GET': 
        return render_template('file.html') 
    else:
        url = request.form['f_url']
        if int(request.form['f_id']) == 1:
	    inter1(url)
	elif int(request.form['f_id']) == 2:
	    inter(url)	
    return render_template('end.html')
if __name__ == '__main__':
    app.debug=True
    app.run()'''
 
from flask import Flask, redirect, url_for, request,render_template
from proj import inter
from proj_single import inter1
app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def valid():
        if(request.method == 'GET'):
                return render_template('file.html')
        else:
                url = request.form['f_url']
                if(int(request.form['f_id']) == 1):
                        inter1(url)
                elif(int(request.form['f_id']) == 2):
                        inter(url)
        return render_template('end.html')
if __name__ == '__main__':
        app.debug = True
        app.run()
