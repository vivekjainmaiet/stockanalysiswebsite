from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Form
from fastapi.responses import RedirectResponse
import pandas as pd
import numpy as np
from database import *
from param import config
import mysql.connector as connection
from datetime import date

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

templates = Jinja2Templates(directory="templates")


@app.get("/")
def main(request:Request):
    '''
    Create Stock dashboard for analysis
    '''
    stock_filter = request.query_params.get('search',False)
    conn = connection.connect(**config)
    mycursor = conn.cursor()
    if stock_filter == False:
        stock_filter = 'INFY'

    query = f"SELECT * FROM stocksdb.StocksList where StockCode ='{stock_filter}';"
    mycursor.execute(query)
    stock_details = mycursor.fetchone()
    #print(stock_details)

    query = "SELECT * FROM stocksdb.StocksList;"
    mycursor.execute(query)
    stock_list = mycursor.fetchall()

    query = "SELECT * FROM stocksdb.raw_news where ticker = 'IT';"
    mycursor.execute(query)
    news_list= mycursor.fetchall()


    query = "SELECT * FROM stocksdb.raw_recommendation where ticker = 'IT';"
    mycursor.execute(query)
    recommendation_list = mycursor.fetchall()

    query = "SELECT * FROM stocksdb.raw_technical ORDER BY ID DESC LIMIT 1;"
    mycursor.execute(query)
    technical_data = mycursor.fetchone()
    print(technical_data)

    return templates.TemplateResponse(
        "home.html", {
            "request": request,
            "stock": stock_details,
            "stock_list": stock_list,
            "news_list": news_list,
            "recommendation_list": recommendation_list,
            "technical_data": technical_data
        })
