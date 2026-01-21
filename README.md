# UCS654_assign_1
## Methodology

### Roll-Number-Dependent Nonlinear Mapping

The input feature \( x \) is transformed into a new variable \( z \) using a nonlinear mapping that depends on the student’s roll number.

**Transformation Formula:**

$$
z = T_r(x) = x + a_r \cdot \arcsin(b_r x)
$$

The parameters \( a_r \) and \( b_r \) are computed from the university roll number \( r \) as:

$$
a_r = 0.05 \times (r \bmod 7), \quad
b_r = 0.3 \times (r \bmod 5 + 1)
$$

For **Roll Number 102303803**, the resulting constants are:

$$
a_r = 0.3, \quad b_r = 1.2
$$

**Final Transformation Equation:**

$$
z = x + 0.3 \cdot \arcsin(1.2x)
$$

---

### Probability Density Function Modeling

The transformed variable \( z \) is modeled using the following probability density function:

$$
\hat{p}(z) = c \cdot e^{-\lambda (z - \mu)^2}
$$

The parameters of the model are defined mathematically as:

$$
\mu = \mathbb{E}[z]
$$

$$
\sigma^2 = \mathbb{E}[(z - \mu)^2]
$$

$$
\lambda = \frac{1}{2\sigma^2}
$$

$$
c = \sqrt{\frac{\lambda}{\pi}}
$$

---

## Results

| Parameter | Value |
|----------|-------|
| μ        | 25.80962289781127 |
| λ        | 0.0015169449810445133 |
| c        | 0.02197404342089438 |

---

## Colab Notebook Link

https://colab.research.google.com/drive/1OKK103p0d6bMM_hWgVdB-Y_fjyj0BlvK?usp=sharing
