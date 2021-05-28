import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from env import host, username, password
from acquire import get_connection, new_telco_churn_data, get_telco_churn_data

from sklearn.model_selection import train_test_split

#Prep telco_churn

def num_distributions(df):
    '''
    This functions takes in a dataframe and displays
    the distribution of each numeric column.
    '''
    for col in df.columns:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()

def clean_telco_churn(df):
    df.total_charges = pd.to_numeric(df.total_charges, errors='coerce').astype('float64')
    df.total_charges = df.total_charges.fillna(value=df.total_charges.mean()).astype('float64')
    df.replace('No internet service', 'No', inplace=True)
    df.replace('No phone service', 'No', inplace = True)

    df["is_female"] = df.gender == "Female"
    df['is_female'] = (df['is_female']).astype(int)

    df["partner"] = df.partner == "Yes"
    df['partner'] = (df['partner']).astype(int)

    df["dependents"] = df.dependents == "Yes"
    df['dependents'] = (df['dependents']).astype(int)

    df["phone_service"] = df.phone_service == "Yes"
    df['phone_service'] = (df['phone_service']).astype(int)

    df["streaming_tv"] = df.streaming_tv == "Yes"
    df['streaming_tv'] = (df['streaming_tv']).astype(int)

    df["streaming_movies"] = df.streaming_movies == "Yes"
    df['streaming_movies'] = (df['streaming_movies']).astype(int)

    df["paperless_billing"] = df.paperless_billing == "Yes"
    df['paperless_billing'] = (df['paperless_billing']).astype(int)

    df["churn"] = df.churn == "Yes"
    df['churn'] = (df['churn']).astype(int)

    df["multiple_lines"] = df.multiple_lines == "Yes"
    df['multiple_lines'] = (df['multiple_lines']).astype(int)

    df["online_security"] = df.online_security == "Yes"
    df['online_security'] = (df['online_security']).astype(int)

    df["online_backup"] = df.online_backup == "Yes"
    df['online_backup'] = (df['online_backup']).astype(int)

    df["device_protection"] = df.device_protection == "Yes"
    df['device_protection'] = (df['device_protection']).astype(int)

    df["tech_support"] = df.tech_support == "Yes"
    df['tech_support'] = (df['tech_support']).astype(int)

    df = df.drop(columns =['payment_type_id', 'contract_type_id', 'internet_service_type_id'])
    df = df.drop(columns=['customer_id', 'gender'])

    dummy_df = pd.get_dummies(df[['internet_service_type', 'contract_type','payment_type']], drop_first=False)
    dummy_df = dummy_df.rename(columns={'internet_service_type_DSL': 'dsl',
                                   'internet_service_type_Fiber optic': 'fiber_optic',
                                   'internet_service_type_None': 'no_internet',
                                   'contract_type_Month-to-month': 'monthly',
                                   'contract_type_One year': 'one_year',
                                   'contract_type_Two year': 'two_year',
                                   'payment_type_Bank transfer (automatic)': 'bank_transfer',
                                   'payment_type_Credit card (automatic)': 'credit_card',
                                   'payment_type_Electronic check': 'electronic_check',
                                   'payment_type_Mailed check': 'mailed_check'})
    df = pd.concat([df, dummy_df], axis =1)
    df = df.drop(columns=['internet_service_type','contract_type','payment_type'])

    return df 


def telco_churn_split(df):
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test


def prep_telco_churn(df):
    df = clean_telco_churn(df)
    train, validate, test = telco_churn_split(df)
    return train, validate, test

