from flask import Flask, request, render_template_string, send_from_directory, jsonify
import os
import subprocess
import glob
app = Flask(__name__)

# Diretórios
UPLOAD_FOLDER = 'uploads'
BUILD_FOLDERs = 'download'
BUILD_FOLDER = 'tmp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BUILD_FOLDER, exist_ok=True)
os.makedirs(BUILD_FOLDERs, exist_ok=True)

# Contador global para arquivos
file_counter = 0

# Página HTML
HTML_ERROR = '''
<!DOCTYPE html>
<html>
<head>
    <title>C Compiler Server</title>
    <style>
        body {
            background-color: yellow;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <h1>error file not found</h1>
    </body>
</html>
'''
@app.route('/')
def index():
    
    f11=False
    try:
        f1=open("index.html","r")
        f11=True
    except:
        f11=False
    if True!=f11:
        try:
            f1=open("main.html","r")
            f11=True
        except:
            f11=False


    if True!=f11:
        try:
            f1=open("load.html","r")
            f11=True
        except:
            f11=False


    if f11:
        
        HTML_TEMPLATE=f1.read()
        f1.close()
        return HTML_TEMPLATE
    else:
        arquivos = glob.glob("*.html")
        return "<br>".join(arquivos)
    return HTML_ERROR

@app.route('/<filename>')
def render_file(filename):
    if filename.find("..")>-1:
        return HTML_ERROR
    if filename.find(".gif")>0 or filename.find(".jpg")>0 or filename.find(".png")>0 or filename.find(".bmp")>0 or filename.find(".ico")>0:
        print("image")
        try:
            f1=open(filename,"r")
            HTML_TEMPLATE=f1.read()
            f1.close()
            return str(HTML_TEMPLATE)
        except:
        
            return str(HTML_ERROR)
    if filename.find(".html")<0 and  filename.find(".htm")<0 and filename.find(".htma")<0 and filename.find(".hta")<0:
        print (filename)
        f11=False
        
            


        try:
            os.system("./"+filename+" > out.txt")
            f11=True
            s=""
            f1=open("out.txt","r")
            s=f1.read()
            f1.close()   
                
            print(s)
            return s
        except:
            return HTML_ERROR    
        
        
    f1=False
    try:    
         f1=open(filename,"r")
         f11=True
    except:
         f11=False



    if True!=f11:
        return HTML_ERROR
    else:
        HTML_TEMPLATE=f1.read()
        f1.close()
        return HTML_TEMPLATE

    return HTML_ERROR


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

