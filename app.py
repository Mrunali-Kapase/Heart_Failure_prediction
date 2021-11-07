import flask
from flask import Flask, render_template, request
import joblib

model = joblib.load('logistic_heart_86.pkl')

#initializing the flask
app = Flask(__name__)

@app.route('/')
def heart_pred():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
        
    Age = request.form.get('Age')
    Gender = request.form.get('gender')
    RestingBP = request.form.get('RestingBP')
    Cholesterol = request.form.get('Cholesterol')
    FastingBS = request.form.get('FastingBS')
    MaxHR = request.form.get('MaxHR')
    ST_Slope = request.form.get('ST_Slope')
    Oldpeak = (request.form.get('Oldpeak'))
    ChestPainType = request.form.get('ChestPainType')
    RestingECG = request.form.get('RestingECG')
    ExerciseAngina = request.form.get('ExerciseAngina')

    if(Gender=='M'):
        Sex_M=1
    else:
        Sex_M=0

    if(ChestPainType=='ATA'):
        ChestPainType_ATA =1
        ChestPainType_NAP =0
        ChestPainType_TA = 0
    elif (ChestPainType=='NAP'):
        ChestPainType_ATA =0
        ChestPainType_NAP =1
        ChestPainType_TA = 0
    elif (ChestPainType=='TA'):
        ChestPainType_ATA =0
        ChestPainType_NAP =0
        ChestPainType_TA = 1
    else:
        ChestPainType_ATA =0
        ChestPainType_NAP =0
        ChestPainType_TA = 0

    if(RestingECG=='Normal'):
        RestingECG_Normal =1
        RestingECG_ST = 0
    elif (RestingECG=='ST'):
        RestingECG_Normal =0
        RestingECG_ST = 1
    else :
        RestingECG_Normal =0
        RestingECG_ST = 0

    if(ST_Slope=='Flat'):
        ST_Slope_Flat =1
        ST_Slope_Up = 0
    elif (ST_Slope=='Up'):
        ST_Slope_Flat =0
        ST_Slope_Up = 1
    else :
        ST_Slope_Flat =0
        ST_Slope_Up = 0

    if(ExerciseAngina=='Y'):
        ExerciseAngina_Y =1
    else :
        ExerciseAngina_Y =0


    prediction=model.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, Sex_M, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_Normal, RestingECG_ST, ExerciseAngina_Y, ST_Slope_Flat, ST_Slope_Up]])
    output=prediction[0]
    if output==0:
        return render_template('home.html',prediction_text="Patient does not heart disease")
    else:
        return render_template('home.html',prediction_text="Patient have Heart disease") 

   
if __name__ == '__main__':
    app.run(debug=True)