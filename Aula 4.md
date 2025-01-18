# Bayesian Inference

## Motivation
- Sometimes, the joint probability distribution is not available, but we are given the conditional probabilities
- Updating beliefs, or making predictions, based on evidence

### Product Rule
$$
\begin{align*}
P(A \cap B) = P(A \mid B ) * P(B) \cr
P(A \cap B) = P(B \mid A) * P(A)
\end{align*}
$$


### Bayes Rule

$$P(A\cap B) = P(B \cap A)$$
$$P(A \mid B) * P(B) = P(B \mid A) * P(A)$$
ou
$$
P(A \mid B) = 
\frac{P(B \mid A) *P(A)}{P(B)} 
$$

ou 
$$
P(B \mid A) = 
\frac{P(A \mid B) *P(B)}{P(A)} 
$$

### Bayes Rule: Hypothesis and Evidence

$$P(H \mid E) = 
\frac{P(E \mid H)*P(H)}{P(E)}
$$
- The degree of belief in the hypothesis, should be determined by: “how likely the hypothesis is before the evidence was observed and, if the hypothesis is true, what are the odds of observing the evidence, scaled by how common the evidence is whether the hypothesis is true or not”

### Bayes Inference 
- Method of statistical inference
- Based on Bayes’ Rule
- It is used to update the probability of a hypothesis as more evidence or information becomes available
- Allows us to make predictions based on the evidence

### Bayes' Rule: terminology

$$P(H \mid E) = 
\frac{P(E \mid H)*P(H)}{P(E)}
$$
P(H) – prior: how much we believe the “idea” before seeing the evidence
P(H|E) – posterior: how much we believe the “idea” after seeing the evidence
P(E|H) – likelihood: how much the evidence supports the “idea”
P(E) – evidence: the new information that we have

At high level, Bayes’ Theorem is a way to update our beliefs based on new
evidence:
$$Posterior = \frac{Likelihood*Prior}{Evidence}$$

If we know: 
$$P(Visible \ effect \mid Cause)$$
where the visible effect is the evidence, we can use Bayes' Theorem to find : 
	$$P(Cause \mid Visible \ effect)$$
	It's the essence of the Bayeseian Inference 

> Bayes’ Theorem is a way to:
▶ Update beliefs based on new evidence or information
▶ Calculate conditional probabilities, determining how likely an event is, given
prior knowledge of related events
▶ Combine prior knowledge with observed data to make more accurate
predictions

Quiz 4.1
2
In a quality control process at a factory, 3% of the products are defective. The inspection system correctly identifies 90% of defective products (true positive rate). However, it falsely marks 5% of non-defective products as defective (false positive rate).

If a product is flagged as defective by the inspection system, what is the probability that it is actually defective?

P(D) = 0,03
$P(F\mid D) = 0,9$
P(F|D') = 0,05

P(D|F) = ? 
P(F)=P(F|D ) * P(D) + P(F|D')* P(D')
P(D') = 1 - P(D) = 0,97
P(F) = 0,90 * 0,03 + 0,05* 0,97 = 0,0755

	$P(D|F) = \frac{P(F|D) * P(D)}{P(F)}$

P(D|F) = (0.90 * 0,03) / 0,0755 = 0,357615894

