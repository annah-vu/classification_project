# Classification Project - Telco Churn
Project Description: machine learning project for telco churn

## Project Objectives

-Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.

-Create modules (acquire.py, prepare.py) that make your process repeateable.

-Construct a model to predict customer churn using classification techniques.

-Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.

-Answer panel questions about your code, process, findings and key takeaways, and model.

<br>
<br>
<br>
<br>

## Project Goals
- Find drivers for customer churn at Telco.
- Construct a ML classification model that accurately predicts customer churn.
- Document your process well enough to be presented or read like a report.
<br>
<br>

## Audience

Target audience for my notebook walkthrough is the Codeup Data Science team. 
<br>
<br>
<br>
<br>


## Deliverables
1.) a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

2.) a README.md file containing the project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), key findings, recommendations, and takeaways from your project.

3.) a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). These predictions should be from your best performing model ran on X_test. Note that the order of the y_pred and y_proba are numpy arrays coming from running the model on X_test. The order of those values will match the order of the rows in X_test, so you can obtain the customer_id from X_test and concatenate these values together into a dataframe to write to CSV.

4.) individual modules, .py files, that hold your functions to acquire and prepare your data.

5.) a notebook walkthrough presentation with a high-level overview of your project (5 minutes max). You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.
<br>
<br>

## Data Dictionary
- tenure = customer tenure in months
- 
-is_senior_citizen =	0 signifies a senior-aged customer, 1 signifies a customer younger than the senior age

-customer_id	= company assigned identification number

-gender=	Male for customers that identify as male, Female for customers that identify as female

-is_female = 1 if customer is female, 0 if not.

-partner	= No indicates customer is single, Yes indicates customer has a partner

-dependents=	Yes indicates customer has at least 1 dependent(s), No indicates customer has no dependents

-phone_service=	1 indicates customer has phone service, else 0.

-multiple_lines = 1 if the customer is using multiple phone lines, 0 if not.

-online_security = 1 if customer has online security, 0 if not.

-device_protection = 1 if customer has device protection, 0 if not.

-tech_support = 1 if customer has tech support, 0 if not.

-streaming_tv = 1 if customer is streaming tv, 0 if not. 

-streaming_movies = 1 if customer is streaming movies, 0 if not.

-paperless_billing = 1 if customer is enrolled in paperless billing, 0 if not. 

-dsl = 1 if customer uses dsl

-fiber_optic = 1 if customer uses fiber optic

-internet_service=	1 indicates customer has internet service, else 0.

-contract_type=	0 - month-to-month, 1 - 1 year, 2- 2 year

-monthly = 1 if customer is a monthly contracted customer, 0 if else.

-one_year = 1 if customer is a 1 year contracted customer, 0 if else.

-two_year = 1 if customer is a 2 year contracted customer, 0 if else. 

-payment type=	payment method of charges for the customer.

-no_internet = 1 if customer has no kind of internet service, 0 if else.

-bank_transfer = 1 if customer pays by bank transfer, 0 if other.

-credit_card = 1 if customer pays with credit card, 0 if other.

-electronic_check = 1 if customer pays with electronic check, 0 if other. 

-mailed_check = 1 if customer pays with mailed check, 0 if other. 

-total_charges=	total amount charged to customer account historically

-monthly_charges	=bill total for each month with current service

-churn= Yes (1) indicates customer has left, No (0) indicates customer is still using our services
