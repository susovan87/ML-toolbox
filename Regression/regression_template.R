# Regression Template

# Import dataset
dataset = read.csv('Data.csv')
# dataset = dataset[2:5]


# Encoding categorical data
dataset$Cat = factor(dataset$Cat,
                       levels = c('A', 'B', 'C'),
                       labels = c(1, 2, 3))


# Split dataset into Training set and Test set
# # install.packages('caTools')
# library(caTools)
# set.seed(12345)
# split = sample.split(dataset$Salary, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)


# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)


# Fit Regression Model (Create regressor)
# dataset$Cat2 = dataset$Cat^2
# dataset$Cat3 = dataset$Cat^3
# dataset$Cat4 = dataset$Cat^4
regressor = lm(formula = Salary ~ ., data = training_set)
summary(regressor)


# Predict result
y_pred = predict(regressor, data.frame(Level = 420))


# Visualize result
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Cat, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Cat, y = predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('ML Study (Regression Model)') +
  xlab('X Lable') +
  ylab('Y Lable')


# Visualize result in higher resolution with smoother curve
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Cat), max(dataset$Cat), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Cat, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Cat = x_grid))),
            colour = 'blue') +
  ggtitle('ML Study (Regression Model)') +
  xlab('X Lable') +
  ylab('Y Lable')
