# A review on Probability

- **Unconditional Probability**
- **Conditional Probability**

- Traditional AI - Based on logic and reasoning
- Real world - Uncertainty
- To deal with uncertainty - Probability theory - fundamental to build intelligent systems that can reason under uncertainty

- Random Experiment - process that leads to one of several possible outcomes

- Event - subset of outcomes of a random experiment
	    - Notation is a capital letter, like A, B, C  

- Random Variable - a function that maps a real number to each possible outcome of a random experiment
	- the notation is a capital letter like X, Y; Z

- Probability - probability of an event indicates the likelihood of the event ocurring
	- Notation  - P(A), P(B), P(C)
	- Probability of event A: 0 <=P(A)<=1

- More on probability
	- Probability of the empty set - P(0) = 0
	- Probability of the sample space - P(Omega) = P(all possibilities) = Sum P(each element0) = 1
	- Probability of the complement of an event (not A) - P(not A) =1 - P(A)

- **Joint Probability (AND)**
	- Notation - P(A;B) or P(A∩B)
	- refers to the probability of two events occurring simultaneously. If you have two events, Aand B, their joint probability is the likelihood that **both** A and B happen at the same time. Mathematically, the joint probability is denoted as P(A∩B), where A∩B represents the **intersection** of events A and B.
	- P(A∩B) = P(A) x P(B) if A and B are independent
	
- **Probability of the Union of Two Events (OR)**
	- the likelihood that at least one of the events occurs. If A and B are two events, the **union** of A and B, denoted as A∪B , represents the event that either A, B, or both happen.
	- Formula: P(A∪B)=P(A)+P(B)−P(A∩B)
			- P(A∪B)=P(A)+P(B)  If events A and B are **mutually exclusive**
			- P(A∩B)=P(A)×P(B) If A and B are independent
## Conditional Probability

- Formula: P(A∣B)=P(A∩B)/P(B)​
- is the probability of an event occurring given that another event has already occurred. It's a way to refine probabilities based on additional information.

### Independence between events- the product rule
- Formula - P(A∩B)=P(A)×P(B∣A)
- The **Product Rule** in probability theory is used to calculate the joint probability of two events, A and B, based on the probability of one event and the conditional probability of the other. It essentially breaks down the joint probability P(A∩B) using conditional probability.
- Where:
	- P(A∩B) is the joint probability of both events Aand B happening.
	- P(A) is the probability of event A occurring.
	- P(B∣A) is the conditional probability of event B occurring given that event Ahas already occurred.

4.
Total possible outcome = 2² = 4
sample space  S = (H,T), (T, H) 
2/4 = 0,500

10.
40 cards - 2 cards are drawn
P(A) = 4/40 = 0,1
P(B) =  36/40 = 0,9
P (A|B) = P(A) * P(B) = 0,1 * 0,9 = 0,09

11.
P(A) = 0,4
P(B) = 0,35
P(C)  = 0,25

P(D)  = defective
P(D|A) = 0,02 = P(D∩A) / P(A) (=)  P(D∩A) = 0,02 x 0,4 = 0,08 
P(D|B) = 0,04 = P(D∩B) / P(B) (=) P(D∩B) = 0,04 x 0,35 = 0,14
P(D|C) = 0,05 = P(D∩C) / P(C) (=) P(D∩C) = 0,05 x 0,25 = 0,0125

P(D) = P(D∩A) + P(D∩B) +  P(D∩C) = 0,08 + 0,14 +  0,0125 = 0,2325

7. 
- P(A) = 10/40 = 0,25
- P(B) = 4/40 = 0,1
- P(A AND B) = 1/40 
- P(A OR B)  = P(A) + P(B) - P(A AND B) = 0,25 + 0,1 - 0,025 = 0,325

9 
- P(X= 1 AND Y=1) = 0,015
- P(Y=1) = 0,02
\
P (X=1 | Y = 1) = P(X= 1 AND Y=1) / P(Y=1) = 0,015/0,02 = 0,75

10 
- P(1 ser As)=P(A) = 4/40 = 0,1
- P(2 ser não As)=P(B) = 36/39 = 0,923076923
- P(A AND B) = 0,092307692

- P(1 não ser As)= P(C) = 36/40 = 0,9
- P(2 ser As)= P(D) = 4/39 = 0,102564103
- P(B AND A) = 0,092307693

11 
- P(A)  = 0,05
- P(not A) = 0,95
- P(B|A) = 0,90
- P(not B | not A) = 0,95
-  P(B AND A) = P(B|A) x P(A) = 0,90x0,05 = 0,045
- P(B) = P(B|A) x P(A) =  