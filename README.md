# Article and Research"
https://bratanic-tomaz.medium.com/constructing-knowledge-graphs-from-text-using-openai-functions-096a6d010c17

Link To Shared Research Document:
https://docs.google.com/document/d/19q1fTSqnRNgdrKiL0f5uiZEiJC3vD_DfoRnni8Z1wt0/edit?usp=sharing

# Abductive-Reasoning-in-Healthcare
Here in the README We can Notes Points to discuss, questions as well as notes on progress check

1/30/24 - Presentation and introduction to project. Established goals for the project and what the plan looks like moving forward. 

# Minimal Valuable Project Overview
# Abductive-Reasoning-in-Healthcare
Here in the README We can Notes Points to discuss, questions as well as notes on progress check

1/30/24 - Presentation and introduction to project. Established goals for the project and what the plan looks like moving forward. 

# Minimal Valuable Project Overview
1. We must find a dataset that we will use
	1. Ideally the dataset will have symptoms and diagnosis 
	2. We will use the dataset to generate our hypothesis and method of evaluating our hypothesis 
2. Once the dataset is used we will turn the data into a single vector $v \in [0,1]^n$ where $n$ are all known symptoms 
	1. Each element of the vector is the probability of having the disease and whatever symptom the element represents 
	2. The reason in doing this is because we will encode our symptoms vector in the same way which will allow us to use distance metrics to determine which hypothesis are the best to test 
 	3. The symptoms vector will be binary (yes no for each possible symptom)  	
3. Measuring the Quality of an explanation
	1. The Euclidean Distance from the vector will be interpreted as the goodness of explanation with $n$ being the worst explanation and $0$ being the best explanation 	
4. We  further do a column by column comparison saying why the disease is a good explanation or not for each symptom.
	1. IF the absolute ditance between elements >= 1 then the explanation is impossible and is not a valid explanation  
5. Conclude the set of explanations is the set of ailments are all sets of valid explanations

6. Make a FLask api allow users to query our prediction system
	1. We take in the symptoms as a map with an entry for each of our symptom columns
 	2. We output the set of possible ailments the user has according to our model
7. We create a user interface to allow the users to interact in a user friendly manner 
