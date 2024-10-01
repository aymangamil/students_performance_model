import streamlit as st
import pickle
import numpy as np

# Load model and scaler
with open(r"C:\Users\Ayman\Downloads\saved_scaler_linear_new.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

with open(r"C:\Users\Ayman\Downloads\saved_linear_model_new.pkl", 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

expected_columns = [
    'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores', 
    'Tutoring_Sessions', 'Physical_Activity', 'Parental_Involvement_Low',
    'Parental_Involvement_Medium', 'Access_to_Resources_Low', 
    'Access_to_Resources_Medium', 'Extracurricular_Activities_Yes',
    'Motivation_Level_Low', 'Motivation_Level_Medium', 'Internet_Access_Yes', 
    'Family_Income_Low', 'Family_Income_Medium', 'Teacher_Quality_Low',
    'Teacher_Quality_Medium', 'School_Type_Public', 'Peer_Influence_Neutral',
    'Peer_Influence_Positive', 'Learning_Disabilities_Yes',
    'Parental_Education_Level_High School', 'Parental_Education_Level_Postgraduate',
    'Distance_from_Home_Moderate', 'Distance_from_Home_Near', 'Gender_Male'
]

# Streamlit UI
st.title("Student Performance Prediction")
st.image(r"C:\Users\Ayman\Downloads\WhatsApp Image 2024-09-24 at 16.27.31_0cfd7f07.jpg", use_column_width=True)

st.header("Enter Student Details:")

# Collecting user input
hours_studied = st.number_input("Hours Studied:", min_value=0.0)
attendance = st.number_input("Attendance:", min_value=0.0)
sleep_hours = st.number_input("Sleep Hours:", min_value=0.0)
previous_scores = st.number_input("Previous Scores:", min_value=0.0)
tutoring_sessions = st.number_input("Tutoring Sessions:", min_value=0.0)
physical_activity = st.number_input("Physical Activity:", min_value=0.0)

parental_involvement = st.selectbox("Parental Involvement:", ["Low", "Medium", "High"])
access_to_resources = st.selectbox("Access to Resources:", ["Low", "Medium", "High"])
extracurricular_activities = st.selectbox("Extracurricular Activities:", ["Yes", "No"])
motivation_level = st.selectbox("Motivation Level:", ["Low", "Medium", "High"])
internet_access = st.selectbox("Internet Access:", ["Yes", "No"])
family_income = st.selectbox("Family Income:", ["Low", "Medium", "High"])
teacher_quality = st.selectbox("Teacher Quality:", ["Low", "Medium", "High"])
school_type = st.selectbox("School Type:", ["Public", "Private"])
peer_influence = st.selectbox("Peer Influence:", ["Neutral", "Positive", "Negative"])
learning_disabilities = st.selectbox("Learning Disabilities:", ["Yes", "No"])
parental_education_level = st.selectbox("Parental Education Level:", ["High School", "Undergraduate", "Postgraduate"])
distance_from_home = st.selectbox("Distance from Home:", ["Near", "Moderate", "Far"])
gender = st.selectbox("Gender:", ["Male", "Female"])

# Submit button
if st.button("Submit"):
    try:
        # Convert inputs to features list
        features = [
            hours_studied, attendance, sleep_hours, previous_scores, tutoring_sessions, physical_activity,
            1 if parental_involvement == "Low" else 0,
            1 if parental_involvement == "Medium" else 0,
            1 if access_to_resources == "Low" else 0,
            1 if access_to_resources == "Medium" else 0,
            1 if extracurricular_activities == "Yes" else 0,
            1 if motivation_level == "Low" else 0,
            1 if motivation_level == "Medium" else 0,
            1 if internet_access == "Yes" else 0,
            1 if family_income == "Low" else 0,
            1 if family_income == "Medium" else 0,
            1 if teacher_quality == "Low" else 0,
            1 if teacher_quality == "Medium" else 0,
            1 if school_type == "Public" else 0,
            1 if peer_influence == "Neutral" else 0,
            1 if peer_influence == "Positive" else 0,
            1 if learning_disabilities == "Yes" else 0,
            1 if parental_education_level == "High School" else 0,
            1 if parental_education_level == "Postgraduate" else 0,
            1 if distance_from_home == "Moderate" else 0,
            1 if distance_from_home == "Near" else 0,
            1 if gender == "Male" else 0
        ]

        features_array = np.array([features])

        if features_array.shape[1] != len(expected_columns):
            st.error("Feature count mismatch.")
        else:
            # Scale features and make prediction
            features_scaled = scaler.transform(features_array)
            predicted_exam_score = model.predict(features_scaled)

            st.success(f"Predicted Exam Score: {predicted_exam_score[0]:.2f}")

    except ValueError as e:
        st.error(f"Error: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")