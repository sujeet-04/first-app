# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:37:38 2020

@author: Sujeet
"""


from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
     'author' : 'sujeet',
     'title' : 'Data Science',
     'content' : "first header",
     'date_posted' : 'September 15,2020'
    },
    {
     'author' : 'sujeet',
     'title' : 'Data Science',
     'content' : 'Detail',
     'date_posted' : 'April 18,2020'
    }
    ]

@app.route("/")
def hello() :
    return render_template('home.html',posts = posts)
    



@app.route("/about")
def about() :
    return render_template('About.html',title='About')
    
app.run(debug=True)

