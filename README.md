# Abductive-Reasoning-in-Healthcare
Here in the README We can Notes Points to discuss, questions as well as notes on progress check

1/30/24 - Presentation and introduction to project. Established goals for the project and what the plan looks like moving forward. 

# Minimal Viable Project Overview
1. We must find a dataset that we will use
	1. Ideally the dataset will have symptoms and diagnosis 
	2. We will use the dataset to generate our hypothesis and method of evaluating our hypothesis 
2. Once the dataset is used we will turn the data into a single vector $v \in [0,1]^n$ where $n$ are all known symptoms 
	1. Each element of the vector is the probability of having the disease and whatever symptom the element represents 
	2. The reason in doing this is because we will encode our symptoms vector in the same way which will allow us to use distance metrics to determine which hypothesis are the best explanation
 		3. The symptoms vector will be binary (yes no for each possible symptom)  	
3. We will then encode our patients symptoms aka the evidence we want to explain, and find the minimum $m$ nearest neighbors 
	1. We can pick however many we want obviously the one closest will best explain it best but **for future purposes maybe we search for similar diseases in a separate dataset to find an even better explanation** 
4. Measuring the Quality of an explanation
	1. The Euclidean Distance from the vector will be interpreted as the goodness of explanation with $n$ being the worst explanation and $0$ being the best explanation 
5. We  further do a column by column comparison saying why the disease is a good explanation or not for each symptom. 
6. Conclude that the best explanation is the disease that is closest to the symptoms of the patient or a combination of non-mutually exclusive diseases. 
	1. We modify this but it is meant to be the most naive version of our project 
	2. We will begin without doing the combination of diseases 
