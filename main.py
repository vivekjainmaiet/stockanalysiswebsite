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
import json

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
    mycursor = conn.cursor(dictionary=True)
    if stock_filter == False:
        stock_filter = 'Tata Consultancy Services Limited'

    #breakpoint()
    query = f"SELECT * FROM stocksdb.StocksList where StockName ='{stock_filter}';"
    mycursor.execute(query)
    stock_details = mycursor.fetchone()

    #print(stock_details)

    query = "SELECT * FROM stocksdb.StocksList;"
    mycursor.execute(query)
    stock_list = mycursor.fetchall()

    query = f"SELECT * FROM stocksdb.raw_news where stock_id = {stock_details['ID']} ORDER BY ID DESC LIMIT 5;"
    mycursor.execute(query)
    news_list= mycursor.fetchall()

    query = f"SELECT Financial_Year,Total_Revenue FROM stocksdb.raw_fundamental where stock_id = {stock_details['ID']} ORDER BY ID ASC LIMIT 5;"
    mycursor.execute(query)
    fundamental_data = mycursor.fetchall()
    import json
    fundamental_data = json.dumps(fundamental_data)
    #fundamental_data = fundamental_data.replace("'", '"')

    #print(json.dumps(fundamental_data))

    #json_for = []

    #for data in fundamental_data:

        #json_string = json.dumps(data)
        #json_for.append(json_string)

    #print(json_for)

    query = f"SELECT * FROM stocksdb.raw_recommendation where stock_id = {stock_details['ID']} ORDER BY ID DESC LIMIT 5;"
    mycursor.execute(query)
    recommendation_list = mycursor.fetchall()

    query = f"SELECT * FROM stocksdb.raw_technical where stock_id = {stock_details['ID']} ORDER BY ID DESC LIMIT 1;"
    mycursor.execute(query)
    technical_data = mycursor.fetchone()
    #print(technical_data)

    return templates.TemplateResponse(
        "home.html", {
            "request": request,
            "stock": stock_details,
            "stock_list": stock_list,
            "news_list": news_list,
            "recommendation_list": recommendation_list,
            "technical_data": technical_data,
            "list_revenue_chart": fundamental_data
        })
