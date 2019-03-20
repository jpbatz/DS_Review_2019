# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Linear Regression

> Unit 3, Lesson 1

---

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Outlined below | [Here](linear_regression.ipynb) |
| Solution  | Solution code for blanked out lesson samples | [Here](solution-code/linear_regression-solution.ipynb) |
| Datasets | Capital Bikeshare Rider Data | [Here](assets/dataset/bikeshare.csv) |
| Source Materials | Original files used to create this lesson | [Here](assets/slides/) |

---

## Learning Objectives

- Define data modeling and simple linear regression.
- Build a linear regression model using a dataset that meets the linearity assumption using the sci-kit learn library.
- Understand and identify multicollinearity in a multiple regression.

---

## Lesson Outline

- Introduce the bikeshare dataset
  - Read in the Capital Bikeshare data
  - Visualizing the data
- Linear regression basics
  - Form of linear regression
- Overview of supervised learning
  - Benefits and drawbacks of scikit-learn
  - Requirements for working with data in scikit-learn
  - Building a linear regression model in sklearn
  - scikit-learn's 4-step modeling pattern
- Build a linear regression model
- Using the model for prediction
  - Does the scale of the features matter?
- Work with multiple features
  - Visualizing the data (part 2)
  - Adding more features to the model
- What is Multicollinearity?
- How to select a model
  - Feature selection
  - Evaluation metrics for regression problems
  - Comparing models with train/test split and RMSE
  - Comparing testing RMSE with null RMSE
- Feature engineering to improve performance
  - Handling categorical features
  - Feature engineering
- Bonus material: Regularization
  - How does regularization work?
  - Lasso and ridge path diagrams
  - Advice for applying regularization
  - Ridge regression
- Comparing linear regression with other models


---

## Student Requirements

Before this lesson(s), students should already be able to:

- Collect data and perform basic data manipulations with Pandas
- Import libraries into Python scripts
- Create simple data visualizations using Python
- Explain basic statistical concepts including linear algebra and descriptive statistics

----

## Additional Resources

For more information on this topic, check out the following resources:

- [Ben Lorica: Six reasons why I recommend scikit-learn](http://radar.oreilly.com/2013/12/six-reasons-why-i-recommend-scikit-learn.html)
- Scikit-learn examples for [Lasso](http://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lars.html) and [Ridge](http://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html) Regression
- Scikit-learn documentation for [Lasso](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html),  [Ridge](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html), and [Elastic Net](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html) Regression
- [Analytics Vidhya's Compilation of Linear Regression Blogs](https://www.analyticsvidhya.com/blog/tag/linear-regression/)
- [Data School's "Friendly Introduction to Linear Regression" using Python](http://www.dataschool.io/linear-regression-in-python/)
