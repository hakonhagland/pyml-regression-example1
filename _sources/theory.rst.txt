Theory
======

The ``sklearn.linear_model.LinearRegression.fit()`` method is the most common method used to fit a
linear regression model. It is implemented as an
`Ordinary Least Squares method <https://en.wikipedia.org/wiki/Ordinary_least_squares>`_
and wrapped as a predictor object.

`LinearRegression <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression>`_
fits a linear model with coefficients :math:`w = (w_1, ..., w_p)`
to minimize the residual sum of squares between the observed targets in the dataset, and the targets
predicted by the linear approximation. Mathematically it solves a problem of the form:

.. math::

   \min_w ||Xw - y||^2_2
