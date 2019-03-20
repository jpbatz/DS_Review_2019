# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Clustering

Unit 4 : DS Applications | Flex

---

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | k-means, DBSCAN, and hierarchical clustering | [Here](./clustering-starter.ipynb) |
| Solution  | Solution code for questions and exercises | [Here](./solution-code/clustering-solution.ipynb) |
| Datasets | Beer nutrition and cost | [Here](./data/beer.txt) |
| Extra Practice | Four additional labs for practice | [Here](./practice/) |

**Rapid Schedule:** For a half-lesson, consider only covering k-means. If additional time is needed, the k-means metric explanation could be skipped.

This lesson uses a small beer dataset describing beer name, calories, sodium content, alcohol percentage, and cost. This data set is ideal because it is easy to read it all and clusters into identifiable categories.

---

## Learning Objectives
- Determine the difference between supervised and unsupervised learning.
- Demonstrate how to apply k-means clustering.
- Demonstrate how to apply density-based clustering (DBSCAN).
- Define the Silhouette Coefficient and explain how it relates to clustering.


---

## Lesson Outline

TOTAL (170 min)

RAPID-SCHEDULE (80 min)
- Unsupervised Learning (15 min)
    - Unsupervised Learning Example: Coin Clustering
    - Common Types of Unsupervised Learning
    - Using Multiple Types of Learning Together
- Clustering (15 min)
- K-Means: Centroid Clustering (30 min)
    - Visual Demo
    - K-Means Assumptions
- K-Means Demo (20 min)
    - K-Means Clustering
    - Repeat With Scaled Data

---
OPTIONAL FOR FULL LESSON:
- DBSCAN: Density-Based Clustering (25 min)
    - Visual Demo
- DBSCAN Clustering Demo (10 min)
- Hierarchical Clustering (20 min)
- Clustering Metrics (15 min)
- Clustering, Classification, and Regression (15 min)
- Comparing Clustering Algorithms (5 min)
- Lesson Summary

---

## Student Requirements

Before this lesson(s), students should already be able to:

- Understand what supervised learning is.
- Understand k-NN and Voronoi diagrams.
- Prepare features and create models using scikit-learn.
- Graph data using Matplotlib.

---

## Additional Resources

- Scott Foreman-Roe's [breakdown](http://scott.fortmann-roe.com/docs/BiasVariance.html) of the bias-variance tradeoff featuring a discussion of KNN
- A [detailed discussion](https://saravananthirumuruganathan.wordpress.com/2010/05/17/a-detailed-introduction-to-k-nearest-neighbor-knn-algorithm/) of KNN
- A long, applied example of KNN applied to [image classification](http://cs231n.github.io/classification/ )
- Read the SKLearn [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) on implementing KNN
- Choosing the right [algorithm from SKLearn](http://scikit-learn.org/stable/tutorial/machine_learning_map/)
- A deeper dive into [Euclidian distance](http://www.econ.upf.edu/~michael/stanford/maeb4.pdf)
- Classifier comparsion from [SKLearn](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html) 
