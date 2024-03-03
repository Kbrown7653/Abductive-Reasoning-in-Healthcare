from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

class AbductiveReasoningDiagnosis:
    def __init__(self, symptom_database, diagnosis_info):
        self.symptom_database = symptom_database
        self.diagnosis_info = diagnosis_info

    @classmethod
    def load_from_files(cls, symptom_filename, info_filename):
        with open(symptom_filename, 'r') as symptom_file, open(info_filename, 'r') as info_file:
            symptom_database = json.load(symptom_file)
            diagnosis_info = json.load(info_file)
        return cls(symptom_database, diagnosis_info)

    def diagnose(self, user_data):
        user_symptoms = user_data['symptoms']
        possible_conditions = []

        for condition, symptoms in self.symptom_database.items():
            matching_symptoms = set(user_symptoms) & set(symptoms)
            probability = len(matching_symptoms) / len(symptoms) * 100

            if probability > 0:
                possible_conditions.append((condition, probability))

        if not possible_conditions:
            return "Unable to determine the diagnosis based on the provided symptoms."

        possible_conditions.sort(key=lambda x: x[1], reverse=True)

        result = []
        for condition, probability in possible_conditions:
            diagnosis_data = {
                'condition': condition,
                'probability': f'{probability:.2f}%',
                'definition': self.diagnosis_info.get(condition, {}).get('definition', ''),
                'treatment': self.diagnosis_info.get(condition, {}).get('treatment', ''),
                'medications': self.diagnosis_info.get(condition, {}).get('medications', [])
            }
            result.append(diagnosis_data)

        return result

diagnosis_system = AbductiveReasoningDiagnosis.load_from_files('symptom_database.json', 'diagnosis_info.json')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        user_data = {
            'name': request.form.get('name'),
            'age': request.form.get('age'),
            'symptoms': request.form.get('symptoms').split(',')
        }
        user_data['symptoms'] = [symptom.strip().lower() for symptom in user_data['symptoms']]
        result = diagnosis_system.diagnose(user_data)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
