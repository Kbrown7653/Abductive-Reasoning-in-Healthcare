import json

def load_data_from_file(filename):
    """
    Load data from a JSON file.
    
    Parameters:
        filename (str): The name of the JSON file.
        
    Returns:
        dict: The loaded data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def extract_disease_probability(disease):
    """
    Extract the probability of a disease from the disease probability database.
    
    Parameters:
        disease (str): The name of the disease.
        
    Returns:
        float: The probability of the disease.
    """
    return disease_probabilities.get(disease, 0.0)

def extract_symptoms_given_disease_probability(disease, symptom):
    """
    Extract the probability of a symptom given a disease from the symptoms|disease probability database.
    
    Parameters:
        disease (str): The name of the disease.
        symptom (str): The name of the symptom.
        
    Returns:
        float: The probability of the symptom given the disease.
    """
    return symptoms_given_disease_probabilities.get(disease, {}).get(symptom, 0.0)

def extract_symptoms_probability(symptom):
    """
    Extract the probability of a symptom from the symptoms probability database.
    
    Parameters:
        symptom (str): The name of the symptom.
        
    Returns:
        float: The probability of the symptom.
    """
    return symptoms_probabilities.get(symptom, 0.0)

def calculate_posterior_probability(symptoms, disease):
    """
    Calculate the posterior probability using Bayes' theorem.
    
    Parameters:
        symptoms (list): List of observed symptoms.
        disease (str): The hypothesized disease.
        
    Returns:
        float: Posterior probability of the disease given the symptoms.
    """
    posterior_probability = 1.0
    for symptom in symptoms:
        likelihood = extract_symptoms_given_disease_probability(disease, symptom)
        prior_probability = extract_disease_probability(disease)
        general_symptoms_probability = extract_symptoms_probability(symptom)
        
        if general_symptoms_probability == 0:
            return 0.0  # Return 0 if general_symptoms_probability is 0 to avoid division by zero error
        
        posterior_probability *= (likelihood * prior_probability) / general_symptoms_probability
    
    return posterior_probability

# Load data from JSON files
disease_probabilities = load_data_from_file('disease_probabilities.json')
symptoms_given_disease_probabilities = load_data_from_file('symptoms_given_disease_probabilities.json')
symptoms_probabilities = load_data_from_file('symptoms_probabilities.json')

def get_user_input():
    """
    Get user input for symptoms.
    
    Returns:
        list: List of symptoms entered by the user.
    """
    symptoms = input("Enter your symptoms separated by commas: ").strip().split(',')
    return [symptom.strip() for symptom in symptoms]

def main():
    user_symptoms = get_user_input()
    print("Calculating posterior probabilities...\n")
    
    posterior_probabilities = []
    
    for disease in disease_probabilities:
        posterior_probability = calculate_posterior_probability(user_symptoms, disease)
        posterior_probabilities.append((disease, posterior_probability))
    
    # Sort posterior probabilities in descending order
    posterior_probabilities.sort(key=lambda x: x[1], reverse=True)
    
    # Print the top 3 diseases
    print("Top 3 possible diseases based on posterior probability:")
    for i, (disease, probability) in enumerate(posterior_probabilities[:3], start=1):
        probability_percentage = round(probability * 100, 2)
        print(f"{i}. {disease}: {probability_percentage:.2f}%")

if __name__ == "__main__":
    main()