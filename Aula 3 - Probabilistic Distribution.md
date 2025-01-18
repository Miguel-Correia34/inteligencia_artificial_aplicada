-  Probability does not come alone
- Marginalizing probability
	
- Example - sum of two dice rolls 


- 0 <Probability < 1
- Sum of all probabilities in the distribution = 1

- P(A, B) = P(A) x P(B) - if independent
### Joint probability distribution - independent events
- Given two probability distributions P(X) and P(Y) the joint probability distribution of X and Y is: P(X,Y) = P(X= xi ∩ Y= yi) = P(X=xi) x P(Y=yi) 
	P(X) -> headache - 0,2
		 not headach - 0,8
- P(h,e) = P(h) x P(e) = 0,2 x 0,5
- P(h, o) = P(h)x P(o) = 0,2 x 0.5
- P(not h, e) = P(not h) x P(e) = 0,3 x 0,5 = 0,4

### Marginalization 
- If we want to compute the marginal distribution of X over the joint distribution P(X)

### Joint probability distribution - dependent events
- P(X,Y) = P(Xi|Yi) x P(Yi)

### Inference by enumeration 
- method used in probabilistic reasoning, particularly within the context of Bayesian networks or other graphical models. It involves systematically calculating the probabilities of different outcomes by considering all possible combinations of variables. Here's a breakdown of how it works:

### Key Concepts

1. **Probability Distribution**: Inference by enumeration assumes you have a joint probability distribution over all relevant variables. This distribution contains all the probabilities of every possible combination of events.
    
2. **Marginalization**: The goal is often to compute the marginal probability of a subset of variables, while ignoring (or summing out) the others. For instance, if you want to find the probability of variable AAA, given a joint distribution involving AAA, BBB, and CCC, you would sum over all possible values of BBB and CCC:
    
    P(A)=∑B∑CP(A,B,C)P(A) = \sum_{B} \sum_{C} P(A, B, C)P(A)=B∑​C∑​P(A,B,C)
3. **Exhaustive Enumeration**: In inference by enumeration, you explicitly enumerate all possible configurations of the variables in the model. You then compute the joint probability for each configuration and sum them to find the desired marginal probability.
    

### Steps of Inference by Enumeration

1. **Define the Variables**: Identify all the variables in your model and their possible values.
    
2. **List Possible Combinations**: Create a list of all combinations of variable states (for instance, if AAA can be true or false, and BBB can also be true or false, the combinations would be (A=true,B=true),(A=true,B=false),(A=false,B=true),(A=false,B=false)(A=true, B=true), (A=true, B=false), (A=false, B=true), (A=false, B=false)(A=true,B=true),(A=true,B=false),(A=false,B=true),(A=false,B=false)).
    
3. **Compute Joint Probabilities**: For each combination, calculate the joint probability using the joint probability distribution.
    
4. **Sum Probabilities**: To find the marginal probability of a variable or a set of variables, sum the joint probabilities of all relevant combinations.

Let’s work through an example of inference by enumeration using a simple scenario involving two binary variables: **Weather** (Sunny or Rainy) and **Activity** (Play or Stay).

### Scenario

Imagine we have the following joint probability distribution:

|Weather|Activity|Probability|
|---|---|---|
|Sunny|Play|0.4|
|Sunny|Stay|0.1|
|Rainy|Play|0.1|
|Rainy|Stay|0.4|

From this table, we can see all combinations of weather and activity along with their probabilities.

### Goal

Let's say we want to calculate the marginal probability of the event **Activity = Play**, denoted as P(Play)P(\text{Play})P(Play).

### Steps of Inference by Enumeration

1. **Identify Variables**: Here, the variables are **Weather** and **Activity**.
    
2. **List Possible Combinations**: We can see there are four possible combinations:
    
    - (Sunny,Play)(Sunny, Play)(Sunny,Play)
    - (Sunny,Stay)(Sunny, Stay)(Sunny,Stay)
    - (Rainy,Play)(Rainy, Play)(Rainy,Play)
    - (Rainy,Stay)(Rainy, Stay)(Rainy,Stay)
3. **Compute Joint Probabilities**: From our table, we already have the joint probabilities:
    
    - P(Sunny,Play)=0.4P(Sunny, Play) = 0.4P(Sunny,Play)=0.4
    - P(Sunny,Stay)=0.1P(Sunny, Stay) = 0.1P(Sunny,Stay)=0.1
    - P(Rainy,Play)=0.1P(Rainy, Play) = 0.1P(Rainy,Play)=0.1
    - P(Rainy,Stay)=0.4P(Rainy, Stay) = 0.4P(Rainy,Stay)=0.4
4. **Sum Probabilities for the Marginal**: To find P(Play)P(\text{Play})P(Play), we sum the joint probabilities where **Activity** is Play:
    
    P(Play)=P(Sunny,Play)+P(Rainy,Play)P(\text{Play}) = P(Sunny, Play) + P(Rainy, Play)P(Play)=P(Sunny,Play)+P(Rainy,Play) P(Play)=0.4+0.1=0.5P(\text{Play}) = 0.4 + 0.1 = 0.5P(Play)=0.4+0.1=0.5

### Result

Thus, the marginal probability P(Play)P(\text{Play})P(Play) is **0.5**.

### Summary of the Process

- We systematically enumerated all combinations of the variables.
- We extracted the joint probabilities from the table.
- We summed the relevant probabilities to get the marginal probability of interest.

Inference by enumeration in this example was straightforward due to the small number of variables and outcomes. As mentioned earlier, this method becomes computationally challenging with larger numbers of variables or states, but it effectively illustrates the basic principles of probabilistic reasoning.