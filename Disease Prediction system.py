# -*- coding: utf-8 -*-
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Disease Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Loading the models
diabetes_model = pickle.load(open('C:/Users/Sakshi Pawar/OneDrive/Desktop/Disease Prediction system/Disease saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Sakshi Pawar/OneDrive/Desktop/Disease Prediction system/Disease saved models/heart_disease_model.sav', 'rb'))
kidney_model = pickle.load(open('C:/Users/Sakshi Pawar/OneDrive/Desktop/Disease Prediction system/Disease saved models/kidney_model.pkl', 'rb'))
Breast_Cancer_Model = pickle.load(open('C:/Users/Sakshi Pawar/OneDrive/Desktop/Disease Prediction system/Disease saved models/Breast_Cancer_Model.pkl', 'rb'))

#Function for Home Page
def home_page():
    st.title("Disease Prediction System")
    st.subheader("Welcome to the Disease Prediction System")
    
    st.markdown("""
    ## Introduction
    This project aims to predict the likelihood of various diseases using machine learning techniques. The diseases covered in this system are:
    - Diabetes
    - Heart Disease
    - Kidney Disease
    - Breast Cancer
    
    The goal is to provide users with a preliminary diagnosis based on their health data, helping them take necessary medical advice and interventions promptly.
    
    ## Navigation
    Use the sidebar to navigate to different sections of the system:
    - **Registration**: New users can register to use the system.
    - **Diabetes Prediction**: Predict the likelihood of having diabetes.
    - **Heart Disease Prediction**: Predict the likelihood of having heart disease.
    - **Kidney Disease Prediction**: Predict the likelihood of having kidney disease.
    - **Breast Cancer Prediction**: Predict the likelihood of having breast cancer.
    
    ## How It Works
    Each prediction page requires you to input specific health parameters. The system uses pre-trained machine learning models to analyze these inputs and provide a prediction.
    """)
    
    st.image("C:/Users/Sakshi Pawar/OneDrive/Desktop/Disease Prediction system/medical.png", caption="Disease Prediction Overview", use_column_width=True)
    st.markdown("""
    ## Get Started
    Click on the links in the sidebar to start using the disease prediction tools. If you're a new user, please register first.
    """)

# Function to register a new user
def register_user(username, email, password):
    print("User Registered:")
    print("Username:", username)
    print("Email:", email)
    print("Password:", password)

# Function to display registration page
def register_page():
    st.title('New Users Registration')
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password == confirm_password:
            register_user(username, email, password)
            st.success("Registration successful!")
        else:
            st.error("Passwords do not match. Please try again.")

# Function to display diabetes prediction page
def diabetes_prediction_page():
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Function to display heart disease prediction page
def heart_disease_prediction_page():
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex (0 = female and 1 = Male)')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) if x else 0.0 for x in user_input]  # Convert to float and handle empty inputs
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError as e:
            st.error(f"Invalid input: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    st.success(heart_diagnosis)


# Function to display kidney disease prediction page
def kidney_disease_prediction_page():
    st.title("Kidneys Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')

    with col2:
        blood_pressure = st.text_input('Blood Pressure')

    with col3:
        specific_gravity = st.text_input('Specific Gravity')

    with col4:
        albumin = st.text_input('Albumin')

    with col5:
        sugar = st.text_input('Sugar')

    with col1:
        red_blood_cells = st.text_input('Red Blood Cell (normal=0 and if not then 1)')

    with col2:
        pus_cell = st.text_input('Pus Cell (normal=0 and if not then 1)')

    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps (not present=0 and if yes then 1)')

    with col4:
        bacteria = st.text_input('Bacteria (not present=0 and if yes then 1)')

    with col5:
        blood_glucose_random = st.text_input('Blood Glucose Random')

    with col1:
        blood_urea = st.text_input('Blood Urea')

    with col2:
        serum_creatinine = st.text_input('Serum Creatinine')

    with col3:
        sodium = st.text_input('Sodium')

    with col4:
        potassium = st.text_input('Potassium')

    with col5:
        haemoglobin = st.text_input('Haemoglobin')

    with col1:
        packed_cell_volume = st.text_input('Packet Cell Volume')

    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col4:
        hypertension = st.text_input('Hypertension (yes=1 and no=0)')

    with col5:
        diabetes_mellitus = st.text_input('Diabetes Mellitus (yes=1 and no=0)')

    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease (yes=1 and no=0)')

    with col2:
        appetite = st.text_input('Appetitte (good=1 and bad=0)')

    with col3:
        peda_edema = st.text_input('Peda Edema (yes=1 and no=0)')

    with col4:
        aanemia = st.text_input('Aanemia (yes=1 and no=0)')

    kindey_diagnosis = ''
    if st.button("Kidney's Test Result"):
        user_input = [age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps,
                      bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin,
                      packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus,
                      coronary_artery_disease, appetite, peda_edema, aanemia]
        user_input = [float(x) for x in user_input]
        prediction = kidney_model.predict([user_input])
        if prediction[0] == 1:
            kindey_diagnosis = "The person has Kidney's disease"
        else:
            kindey_diagnosis = "The person does not have Kidney's disease"
    st.success(kindey_diagnosis)

# Function to display breast cancer prediction page
def breast_cancer_prediction_page():
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('Mean Radius')

    with col2:
        mean_texture = st.text_input('Mean Texture')

    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')

    with col1:
        mean_area = st.text_input('Mean Area')

    with col2:
        mean_smoothness = st.text_input('Mean Smoothness')

    with col3:
        mean_compactness = st.text_input('Mean Compactness')

    with col1:
        mean_concavity = st.text_input('Mean Concavity')

    with col2:
        mean_concave_points = st.text_input('Mean Concave Points')

    with col3:
        mean_symmetry = st.text_input('Mean Symmetry')

    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')

    with col2:
        radius_se = st.text_input('Radius SE')

    with col3:
        texture_se = st.text_input('Texture SE')

    with col1:
        perimeter_se = st.text_input('Perimeter SE')

    with col2:
        area_se = st.text_input('Area SE')

    with col3:
        smoothness_se = st.text_input('Smoothness SE')

    with col1:
        compactness_se = st.text_input('Compactness SE')

    with col2:
        concavity_se = st.text_input('Concavity SE')

    with col3:
        concave_points_se = st.text_input('Concave Points SE')

    with col1:
        symmetry_se = st.text_input('Symmetry SE')

    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')

    with col3:
        worst_radius = st.text_input('Worst Radius')

    with col1:
        worst_texture = st.text_input('Worst Texture')

    with col2:
        worst_perimeter = st.text_input('Worst Perimeter')

    with col3:
        worst_area = st.text_input('Worst Area')

    with col1:
        worst_smoothness = st.text_input('Worst Smoothness')

    with col2:
        worst_compactness = st.text_input('Worst Compactness')

    with col3:
        worst_concavity = st.text_input('Worst Concavity')

    with col1:
        worst_concave_points = st.text_input('Worst Concave Points')

    with col2:
        worst_symmetry = st.text_input('Worst Symmetry')

    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    breast_cancer_diagnosis = ''
    if st.button("Breast Cancer Test Result"):
        user_input = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
                      mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_se, texture_se,
                      perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,
                      fractal_dimension_se, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
                      worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]
        try:
            user_input = [float(x) if x else 0.0 for x in user_input]
            breast_cancer_prediction = Breast_Cancer_Model.predict([user_input])
            if breast_cancer_prediction[0] == 1:
                breast_cancer_diagnosis = "The person has breast cancer"
            else:
                breast_cancer_diagnosis = "The person does not have breast cancer"
        except ValueError as e:
            st.error(f"Invalid input: {e}")
    st.success(breast_cancer_diagnosis)

# Main function
def main():
    with st.sidebar:
        selected = option_menu('Disease Prediction System',
                              ['Home','Registration', 'Diabetes Prediction', 'Heart disease Prediction', 'Kidney Disease Prediction', 'Breast Cancer Prediction'],
                              icons=['house','person', 'activity', 'heart', 'capsule', 'gender-female'],
                              default_index=0)
    if selected == 'Home':
        home_page()
    elif selected == 'Registration':
        register_page()
    elif selected == 'Diabetes Prediction':
        diabetes_prediction_page()
    elif selected == 'Heart disease Prediction':
        heart_disease_prediction_page()
    elif selected == 'Kidney Disease Prediction':
        kidney_disease_prediction_page()
    elif selected == 'Breast Cancer Prediction':
        breast_cancer_prediction_page()

if __name__ == "__main__":
    main()
  port = int(os.getenv("PORT", 8501))
    st.run(port=port)

