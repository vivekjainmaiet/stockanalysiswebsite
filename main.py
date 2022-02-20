from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
from database import *
from param import config
import mysql.connector as connection

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def main(request:Request):
    '''
    Create Stock dashboard for analysis
    '''

    conn = connection.connect(**config)
    mycursor = conn.cursor()

    query = "SELECT * FROM stocksdb.StocksList where StockCode = 'INFY';"
    mycursor.execute(query)
    stock_details = mycursor.fetchall()

    query = "SELECT * FROM stocksdb.raw_news where ticker = 'IT';"
    mycursor.execute(query)
    news_list= mycursor.fetchall()


    query = "SELECT * FROM stocksdb.raw_recommendation where ticker = 'IT';"
    mycursor.execute(query)
    recommendation_list = mycursor.fetchall()

    query = "SELECT * FROM stocksdb.raw_technical ORDER BY ID ASC LIMIT 1;"
    mycursor.execute(query)
    technical_data = mycursor.fetchall()
    #print(technical_data)

    query = "SELECT * FROM stocksdb.raw_technical ORDER BY ID DESC"
    mycursor.execute(query)
    technical_data = mycursor.fetchall()

    return templates.TemplateResponse(
        "home.html", {
            "request": request,
            "stock": stock_details,
            "news": news_list,
            "recommendation_list": recommendation_list,
            "technical_data": technical_data
        })
