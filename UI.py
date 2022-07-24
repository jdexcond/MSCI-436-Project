import pickle
import streamlit as st
import pandas as pd
model = pickle.load(open('lrmodel.pkl','rb'))

st.title('Insurance Claims Charges Predictor')
st.header('Input insurance holder information:')

def user_input(): 
    age = float(st.number_input('Age:'))
    sex = int(convert_sex(st.radio('Sex:', options = ['M', 'F'])))
    bmi = float(st.number_input('BMI:'))
    children = float(st.number_input('Num. of Children:'))
    smoker = int(convert_smoker(st.radio('Smoker:', options = ['Y', 'N'])))

    return pd.DataFrame({'age': [age], 'sex': [sex], 'bmi': [bmi], 'children':[children], 'smoker':[smoker]})


def convert_sex(input): 
    return 1 if input=='M' else 0 

def convert_smoker(input): 
    return 1 if input=='Y' else 0 

with st.form(key='input'): 
    df = user_input()
    st.form_submit_button('Submit')

X = df

output = model.predict(X)


st.header('Predicted Insurance Charge:')
st.header('$' + str(round(output[0],2)))
