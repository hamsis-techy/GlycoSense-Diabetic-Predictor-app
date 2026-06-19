import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle as pkl


# load the GlycoSense Model
Glyco_classifier_model = pkl.load(open('GlycoSense_model.pkl', 'rb'))

def glyco_predict(inputs):
  
  # changing the input_data to numpy array
  inputs_arr = np.asarray(inputs).reshape(1,-1)

  prediction = Glyco_classifier_model.predict(inputs_arr)
  print(prediction)

  if (prediction[0] == 0):
    return('The person is not diabetic')
  else:
    return('The person is diabetic')

def main():
    st.header('GlycoSense - Diabeties Predictor')

    Pregnancies    = st.text_input('Number of Pregnancies')
    Glucose	       = st.text_input('Glucose level')
    BloodPressure	 = st.text_input('BP level')
    SkinThickness	 = st.text_input('SkinThickness value')
    Insulin       	= st.text_input('Insulin level')
    BMI	           = st.text_input('BMI')
    DiabetesPedigreeFunction	= st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age')

    diagnosis = ''
    if st.button('Diabetic Test Result'):
      diagnosis = glyco_predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
  
    st.success(diagnosis)
	
if __name__ == '__main__':
	main()
