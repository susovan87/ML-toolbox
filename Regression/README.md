# Regression

## Bias & Variance
The `bias` is error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs (`underfitting`).

The `variance` is error from sensitivity to small fluctuations in the training set. High variance can cause `overfitting`: modeling the random noise in the training data, rather than the intended outputs.


## Pros & Cons

| **Algorithm** |	**Pros** |	**Cons** |
| --- | --- | --- |
| *Linear regression* | Works on any size of dataset, gives informations about relevance of features | The Linear Regression Assumptions |
| *Polynomial Regression* | Works on any size of dataset, works very well on non linear problems | Need to choose the right polynomial degree for a good bias/variance tradeoff |
| *SVR* | Easily adaptable, works very well on non linear problems, not biased by outliers | Compulsory to apply feature scaling, not well known, more difficult to understand |
| *Decision Tree Regression* | Interpretability, no need for feature scaling, works on both linear / nonlinear problems | Poor results on too small datasets, overfitting can easily occur |
| *Random Forest Regression* | Powerful and accurate, good performance on many problems, including non linear | No interpretability, overfitting can easily occur, need to choose the number of trees |

