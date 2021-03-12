# PyKCCA

Python implementation of Kernel Canonical Correlation Analysis

## INSTALLATION

To install the package from source, one should clone this package running the following::

    git clone https://github.com/sambit-giri/PyKCCA.git

To install the package in the standard location, run the following in the root directory::

    python setup.py install

In order to install it in a separate directory::

    python setup.py install --home=directory

One can also install it using pip by running the following command::

    pip install git+https://github.com/sambit-giri/PyKCCA.git

## Example

In this startup example, two artificially constructed datasets are created. The datasets depend on two latent variables.

    import numpy
    from PykCCA.kernels import DiagGaussianKernel
    from PykCCA import KCCA

    x1 = numpy.random.rand(100, 20)
    x2 = numpy.random.rand(100, 30)
    kernel = LinearKernel()
    cca = KCCA(kernel, kernel,
                    regularization=1e-5,
                    decomp='full',
                    method='kettering_method',
                    scaler1=lambda x:x,
                    scaler2=lambda x:x).fit(x1,x2)

    print("Done ",  cca.beta_)

    orig_y1 = cca.y1_
    orig_y2 = cca.y2_

    print("Trying to test")
    y1, y2 = cca.transform(x1, x2)
    print(numpy.allclose(y1, orig_y1))
    print(numpy.allclose(y2, orig_y2))





