from flask import Flask,request,jsonify
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"
model = pickle.load(open('D:\\Hackathon\\student_placement_predictor\\adaboost_classifiermodel.pkl','rb'))


@app.route('/predict',methods=['POST'])
def predict():
    age = request.form.get('Age')
    #male = request.form.get('Male')
    #female = request.form.get('Female')
    gender = request.form.get('gender')
    stream = request.form.get('stream')
    '''
    enc = request.form.get('Electronics And Communication')
    cs = request.form.get('Computer Science')
    it = request.form.get('Information Technology')
    mechanical = request.form.get('Mechanical')
    electrical = request.form.get('Electrical')
    civil = request.form.get('Civil')
    '''
    internships = request.form.get('Internships')
    cgpa = request.form.get('CGPA')
    hostel = request.form.get('Hostel')
    backlog = request.form.get('HistoryOfBacklogs')
    '''
    result = {'Age': age, 'Male': male, 'Female': female,
             'Electronics And Communication': enc,
             'Computer Science': cs, 'Information Technology' : it,
             'Mechanical': mechanical, 'Electrical': electrical, "Civil": civil,
             "Internships": internships,"CGPA": cgpa,'Hostel': hostel,
             'HistoryOfBacklogs': backlog}
    '''
    # convert gender to numerical values
    if gender == 'male':
        male = 1
        female = 0
    else:
        male = 0
        female =1 

    # convert stream to numerical values
    if stream == 'Electronics And Communication':
        enc = 1
        cs = 0
        it = 0
        mechanical = 0
        electrical = 0
        civil = 0
    elif stream == 'Computer Science':
        enc = 0
        cs = 1
        it = 0
        mechanical = 0
        electrical = 0
        civil = 0
    elif stream == 'Information Technology':
        enc = 0
        cs = 0
        it = 1
        mechanical = 0
        electrical = 0
        civil = 0
    elif stream == 'Mechanical':
        enc = 0
        cs = 0
        it = 0
        mechanical = 1
        electrical = 0
        civil = 0
    elif stream == 'Electrical':
        enc = 0
        cs = 0
        it = 0
        mechanical = 0
        electrical = 1
        civil = 0
    else:
        enc = 0
        cs = 0
        it = 0
        mechanical = 0
        electrical = 0
        civil = 1

    # convert hostel to numerical values
    if hostel == 'yes':
        hostel_num = 1
    else:
        hostel_num = 0

    # convert backlog to numerical values
    if backlog == 'yes':
        backlog_num = 1
    else:
        backlog_num = 0

    input_query = np.array([[age,male,female,enc,cs,it,mechanical,electrical,civil,
                             internships,cgpa,hostel_num,backlog_num]])
    result = model.predict(input_query)[0]
    
    if result==1:
        return jsonify({'placement': 'Placed'})
    else:
        return jsonify({'placement': 'Not Placed'})
    '''
    return jsonify({'placement': str(result)})
    '''


if __name__=='__main__':
    app.run(debug=True)
