# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:18:23 2022

@author: mjkipsz2
"""

import streamlit as st


def household():
    noofmembers=st.number_input("Enter Number of Members in your Household",min_value=1)
    electricity=st.number_input("Enter the kWh of Electricity Used")
    naturalgas=st.number_input("Enter kWh of Natural Gas Used ")
    heatingoil=st.number_input("Enter Litres of Heating Oil Used")
    coal=st.number_input("Enter Metric Tons of Coal Used")
    lpg=st.number_input("Enter Litres of LPG Used")
    propane=st.number_input("Enter Litres of Propane Used")
    woodenpellets=st.number_input("Enter Metric Tons of Wooden Pellets Used")
    f_electicity=((electricity/1000)*0.7080)
    f_naturalgas=((naturalgas/100)*0.02)
    f_heatingoil=((heatingoil/100)*0.27)
    f_coal=(coal*2.88)
    f_lpg=((lpg/100)*0.17)
    f_propane=((propane/100)*0.16)
    f_woodenpellets=(woodenpellets*0.07)
    total=(f_electicity+f_coal+f_heatingoil+f_lpg+f_naturalgas+f_propane+f_woodenpellets)/(noofmembers)
    st.title('Your Carbon Footprint is'+" "+str(total)+" "+"Metric Tonnes")

def publictransport():
    bus=((st.number_input("Enter the Distance Travelled in Bus")/1000)*0.10)
    coach=((st.number_input("Enter the Distance Travelled in Coach")/1000)*0.03)
    localtrain=((st.number_input("Enter the Distance Travelled in Local")/1000)*0.04)
    longdistancetrain=((st.number_input("Enter the Distance Travelled in Long Distance Train")/10000)*0.05)
    tram=((st.number_input("Enter the Distance Travelled in tram")/1000)*0.03)
    subway=((st.number_input("Enter the Distance Travelled in subway")/1000)*0.03)
    taxi=((st.number_input("Enter the Distance Travelled in taxi")/50)*0.01)
    total1=(bus+coach+localtrain+longdistancetrain+tram+subway+taxi)
    st.title('Your Carbon Footprint is'+" "+str(total1)+" "+"Metric Tonnes")
    
def carcarbonfootprint():
    carsize = st.selectbox(
    'Select Car Size',
    ('Sports car or large SUV (35 mpg)', 'Small or medium SUV, or MPV (46 mpg)','City, small, medium, large or estate car (52 mpg)','Enter Custom mpg'))
    carmileage = st.selectbox(
    'Select 12-month car mileage',
    ('Choose an Option','Low (6,000 miles)', 'Average (9,000 miles)','High (12,000 miles)','Enter Custom milage'))
    
    if carsize=='Sports car or large SUV (35 mpg)':
        size=35
    if carsize=='Small or medium SUV, or MPV (46 mpg)':
        size=46
    if carsize=='City, small, medium, large or estate car (52 mpg)':
        size=52

    if carmileage=='Choose an Option':
        mileage=0
    if carmileage=='Low (6,000 miles)':
        mileage=6000
    if carmileage=='Average (9,000 miles)':
        mileage=9000
    if carmileage=='High (12,000 miles)':
        mileage=12000

        
    carfootprint123=(((((mileage/size)*14.3)/1000)*0.907185)/1)
    st.title('Your Carbon Footprint is'+" "+str(carfootprint123)+" "+"Metric Tonnes")
    
