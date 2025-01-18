# Variable Elimination
## Motivation
- Avoid the exponential growth of the number of operations when doing inference 
- **Inference** - is the process of using data analysis to _infer_ properties of an underlying distribution of probability. = dedução - Raciocínio ascendente (da causa para os efeitos).

A summary of Inference by Enumeration on the full JPD
Type of inference:
Marginal:
$P(Q) =\sum_{h1 ,...,hn} P(Q, h1, . . . , hn)$
Joint:
$P(Q1, . . . , Qm) =\sum_{h1 ,...,hn}P(Q1, . . . , Qm, h1, . . . , hn)$
Conditional:
$P(Q | e1, . . . , en) = \frac{\sum_{h1 ,...,hn} P(Q, e1, . . . , en, h1, . . . , hn)}{ \sum_{q,h1 ,...,hn} P(q, e1, . . . , en, h1, . . . , hn)}$
▶ We are “selecting” rows from the JPD that match the evidence
▶ We can ignore the denominator, as we can normalize

- Min-deg - eliminates 
- Min-fill