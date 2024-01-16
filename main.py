import numpy as np
import streamlit as st
import pickle


# Load the trained model
with open('trained_model.pkl', 'rb') as model_file:
    trained_model = pickle.load(model_file)

st.title('Titanic Survival Prediction')


st.write("Note")
st.write(f"Please give input based on the changes what we did in data")

# Get input features from the user
input_features = []

# Assuming you have a list of feature names
feature_names = ['Pclass','Sex', 'Fare','SibSp','Parch','Cabin', 'Embarked']
for feature_name in feature_names:
    value = st.number_input(f"Enter value for {feature_name}: ")
    input_features.append(value)

# Add a prediction button
if st.button('Predict'):
    # Convert input features to a NumPy array
    input_features_array = np.array(input_features).reshape(1, -1)

    # Make predictions using the loaded model
    predicted_class = trained_model.predict(input_features_array)
    st.write(f"Predicted class: {survival_dict.get(predicted_class[0])}")




    
  
       
