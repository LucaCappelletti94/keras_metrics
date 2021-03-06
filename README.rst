extra_keras_metrics
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Additional metrics integrated with the Keras NN library.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install extra_keras_metrics

Tests Coverage
----------------------------------------------
Since some software handling coverages sometimes get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

How do I use this package?
----------------------------------------------
Other than by importing the single metrics from the package, we make available
also sets of metrics.

Multi-class metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To retrieve an instance of the set of multi-class metrics you can use:

.. code:: python

    from extra_keras_metrics import get_minimal_multiclass_metrics

    model = my_keras_model()
    model.compile(
        optimizer="nadam",
        loss="categorical_crossentropy",
        metrics=get_minimal_multiclass_metrics()
    )

Binary metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To retrieve an instance of the set of binary-class metrics you can use:

.. code:: python

    from extra_keras_metrics import get_standard_binary_metrics

    model = my_keras_model()
    model.compile(
        optimizer="nadam",
        loss="binary_crossentropy",
        metrics=get_standard_binary_metrics()
    )

All the binary metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We have implemented all sorts of binary metrics, including some relatively
more obscure ones. If you want ALL the binary metrics we implemented you can
use the following method:

.. code:: python

    from extra_keras_metrics import get_complete_binary_metrics

    model = my_keras_model()
    model.compile(
        optimizer="nadam",
        loss="binary_crossentropy",
        metrics=get_complete_binary_metrics()
    )

Extras
----------------------------
I've created also another couple packages you might enjoy this other one,
called `extra_keras_utils <https://github.com/LucaCappelletti94/extra_keras_utils>`_
that contains some commonly used code for Keras projects and
`plot_keras_history <https://github.com/LucaCappelletti94/plot_keras_history>`
which automatically plots a Keras training history.


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/extra_keras_metrics.png
   :target: https://travis-ci.org/LucaCappelletti94/extra_keras_metrics
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_extra_keras_metrics&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_extra_keras_metrics
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_extra_keras_metrics&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_extra_keras_metrics
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_extra_keras_metrics&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_extra_keras_metrics
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/extra_keras_metrics/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/extra_keras_metrics?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/extra-keras-metrics.svg
    :target: https://badge.fury.io/py/extra_keras_metrics
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/extra-keras-metrics
    :target: https://pepy.tech/badge/extra-keras-metrics
    :alt: Pypi total project downloads 

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/5c1fbcfbffc047e6bf810e9372198a5b
    :target: https://www.codacy.com/app/LucaCappelletti94/extra_keras_metrics?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/extra_keras_metrics&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/b1008a3d75104ce62162/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/extra_keras_metrics/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/b1008a3d75104ce62162/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/extra_keras_metrics/test_coverage
    :alt: Code Climate Coverate
