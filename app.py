import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import pickle
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

page = st.sidebar.selectbox("Select Activity", ["Introduction", "Analytics","Percentage Prediction",])
st.sidebar.text(" \n")


df = pd.read_csv("DATA.csv")

pkl_file1 = open('insurancelr.pkl', 'rb')

lr = pickle.load(pkl_file1)

if page=="Introduction":
    img= Image.open("Dashboard 2.jpg")
    st.sidebar.image(img)
    st.header("Prediction of Insurance Premium Pay Defaulters")
    st.text(" \n")
    img= Image.open("Introduction.jpg")
    st.image(img)


    st.subheader("1 Your client is an Insurance company and they need your help in building a model to predict whether the policyholder (customer) will pay next premium on time or not..")

    st.subheader("2 An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that you pay regularly to an insurance company for this guarantee.")
    st.subheader("3 Building a model to predict whether a customer would make the premium payment can be extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers who are less likely to pay and convince them to continue making timely payment.")
    st.subheader("4 Now, in order to predict, whether the customer would pay the next premium or not, you have information about past premium payment history for the policyholders along with their demographics (age, monthly income, area type) and sourcing channel etc.")

    st.header("Features that depends on prediction of Policy payment")
    st.subheader("* Percentage of premium amount paid by cash or credit card")
    st.subheader("* Age in years of policy holder")
    st.subheader("* Monthly Income of policy holder in rupees")

    st.subheader("* No of premiums late by 3 to 6 months")
    st.subheader('* No of premiums late by 6 to 12 months')
    st.subheader('* No of premiums late by more than 12 months')
    st.subheader("* Total premiums paid on time till now")
    st.subheader('* Area type of Residence ')

    st.subheader("* Underwriting Score of the applicant at the time of application")
    st.write("  ( Insurers use credit-based insurance scores primarily in underwriting and rating of consumers. Underwriting is the process by which the insurer determines whether a consumer is eligible for coverage and rating is the process that determines how much premium to charge a consumer.underwriting simply means that your lender verifies your income, assets, debt and property details in order to issue final approval for your loan.)")

if page == "Analytics" :
    img= Image.open("Dashboard 2.jpg")
    st.sidebar.image(img)
    st.text(" \n")
    img= Image.open("Analytics.jpg")
    st.image(img)
    st.header("Distribution of Percentage of premium amount paid by cash or credit card")

    fig = px.histogram(df, x="perc_premium_paid_by_cash_credit")
    st.plotly_chart(fig,use_container_width=10)


    st.header("Distribution of Age in years of policy holder")

    fig = px.histogram(df, x="age_in_years")
    st.plotly_chart(fig,use_container_width=10)

    st.header("Percentage premium paid in cash and credit")
    st.text(" \n")
    l1 = [x for x in range(0,79853)]
    df2 = df
    df2["id"] = l1
    fig, ax = plt.subplots(1, 2, sharey='row', dpi = 100)
    ax[0].set_title('> 85%')
    sns.barplot(x = 'target', y = 'count', ax = ax[0],data = df2[df2.percentage_premium_paid_cash_credit > 85].groupby('target').nunique()['id'].reset_index().rename(columns = {'id': 'count'}))
    ax[1].set_title('< 85%')
    sns.barplot(x = 'target', y = 'count', ax = ax[1],data = df2[df2.percentage_premium_paid_cash_credit < 85].groupby('target').nunique()['id'].reset_index().rename(columns = {'id': 'count'}))
    plt.suptitle('Percentage premium paid in cash and credit')
    plt.savefig('WC.jpg')
    img= Image.open("WC.jpg")
    st.image(img)

    st.header("Distribution of Income")

    fig = px.histogram(df, x="Income")
    st.plotly_chart(fig,use_container_width=10)













if page =="Percentage Prediction" :
    img= Image.open("Dashboard 2.jpg")
    st.sidebar.image(img)

    st.header("Prediction of Insurance Premium Pay Defaulters")
    #st.subheader("Your client is an Insurance company and they need your help in building a model to predict whether the policyholder (customer) will pay next premium on time or not..")
    st.text(" \n")
    img= Image.open("Prediction.jpg")
    st.image(img)
    form = st.form(key='my_form2')

    x1 = form.text_input(label='Age in years of policy holder')
    form.text(" \n")
    x2 = form.text_input(label='Monthly Income of policy holder in rupees')
    form.text(" \n")
    x3 = form.text_input(label='Percentage of premium amount paid by cash or credit card')
    form.text(" \n")
    x4 = form.text_input(label='Underwriting Score of the applicant at the time of application')
    form.text(" \n")
    x5 = form.text_input(label='No of premiums late by 3 to 6 months')
    form.text(" \n")
    x6 = form.text_input(label='No of premiums late by 6 to 12 months')
    form.text(" \n")
    x7 = form.text_input(label='No of premiums late by more than 12 months')
    form.text(" \n")
    x8 = form.text_input(label ="Total premiums paid on time till now")
    form.text(" \n")
    x9 = form.selectbox('Area type of Residence', ['Urban','Rural'], key=1)
    form.text(" \n")

    form.text(" \n")

    submit_button = form.form_submit_button(label='Predict Percentage')
    if submit_button:


        r = {"Urban":0 ,"Rural":1}
        x9 = int(r[x9])

        l = [[float(x2),float(x5),float(x6),float(x7),float(x4),float(x8),x9,float(x3),float(x1)]]
        pred = lr.predict_proba(l)[:,1]
        st.text(" \n")
        a = "Percentage"+ " : " +str(float(pred))
        st.write(a)


#
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
#
# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
#
# set_png_as_page_bg('backgroung.png')
