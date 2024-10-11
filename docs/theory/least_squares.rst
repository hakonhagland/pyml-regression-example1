Ordinary Least Squares
=======================

The Ordinary Least Squares (OLS) method is a technique for estimating the unknown parameters
in a linear regression model. OLS chooses the parameters of a linear function of a set of
explanatory variables by minimizing the sum of the squares of the differences between the
observed dependent variable in the given dataset and those predicted by the linear function.
In other words, it tries to find the line (or hyperplane) that minimizes the sum of the squared
differences between the observed values and the values predicted by the linear approximation.

Example
-------

Assume you have a set of data points :math:`\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}`
and you want to find the best line that fits these points in the plane. The equation for the line is of the form:

.. math::

   y = \beta_0 + \beta_1 x

where :math:`\beta_0` is the intercept, :math:`\beta_1` is the slope of the line, :math:`x` is the independent variable, and :math:`y` is the dependent variable.

The goal of ordinary least squares (OLS) is to find the values of :math:`\beta_0` and :math:`\beta_1` that minimize the sum of the squared differences between the observed values :math:`y_i` and the values predicted by the linear approximation :math:`\hat{y}_i`.

For each data point :math:`(x_i, y_i)`, the predicted value :math:`\hat{y}_i` is given by:

.. math::

   \hat{y}_i = \beta_0 + \beta_1 x_i

The residual for each data point is the difference between the observed value and the predicted value:

.. math::

   e_i = y_i - \hat{y}_i

The ordinary least squares method minimizes the sum of the squared residuals:

.. math::

   S(\beta_0, \beta_1) = \min_{\beta_0, \beta_1} \sum_{i=1}^{n} e_i^2 = \min_{\beta_0, \beta_1} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2

To minimize this sum, we take the partial derivatives of :math:`S` with respect to :math:`\beta_0` and :math:`\beta_1` and set them to zero:

.. math::

   \frac{\partial S}{\partial \beta_0} = -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i) = 0

.. math::

   \frac{\partial S}{\partial \beta_1} = -2 \sum_{i=1}^{n} x_i (y_i - \beta_0 - \beta_1 x_i) = 0


You can imagine a cloud of data points scattered on a 2D plot. The OLS method fits a straight line through these points such that the vertical distances (errors) between the points and the line are as small as possible on average, and the squared differences are minimized.
