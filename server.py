#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
# import sys
# import os
# import gevent.pywsgi
# import argparse


app = Flask(__name__, template_folder= "template", static_folder= "static")
css = "./static/style.css"

@app.route('/')
def start():
    return render_template("index.html", css=css)
    # return 'Hello, World!'

@app.route('/about')
def about():
    return render_template('about.html',  css=css)

@app.route('/projects')
def projects():
    return render_template('projects.html', css=css)

@app.route('/contact')
def contact():
    return render_template('contact.html', css=css)

###########################################################################

# def main():
#     parser = argparse.ArgumentParser()

#     parser.add_argument('-p', '--port', default=8080, 
#         help="Port to be used. Default: 8080")

#     parser.add_argument('-i', '--ip', default="127.0.0.1", 
#         help="IP to be used. Default: 127.0.0.1")

#     args = parser.parse_args()

#     print("-----------------------------------------------------------")
#     print("Listening on: " + str(args.ip) + ":" + str(args.port))
#     print("-----------------------------------------------------------")
    
#     app_server = gevent.pywsgi.WSGIServer((args.ip, int(args.port)), app)
#     app_server.serve_forever()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)