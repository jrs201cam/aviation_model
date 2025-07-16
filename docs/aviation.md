# Aviation model
This model is a basic description of the aviation system

# Inputs


**Table 1: Table of standard conversions**

| Name | Symbol | Unit | Value | 
| ---- | ------ | ---- | ----- |
|Years to days| $\left[ d:y \right]$ | dy^-1^ | 365 |



**Table 2: Table of inputs**

| Name | Symbol | Unit | Value | Source |
| ---- | ------ | ---- | ----- | ------ |
| Passengers per year | $p_{y}$ | y^-1^ |4.46E9| [1]|
| Seats per aircraft | $s$ | - | 150 | [2] |
| Flights per aircraft per day | $f_{d}$ | d^-1^ | 2 | [3] |



**Table 3: Table of outputs**

| Name | Symbol | Unit | 
| ---- | ------ | ---- |
| Passengers per day | $p_{d}$ | d^-1^ |
| Aircraft per day | $a_{d}$ | d^-1^ |

# Model equations
The number of passengers travelling in the global fleet per day  ($p_{d}$) is given by equation ($\ref{eqn_1}$). Therefore, 12.2 million passengers travel on aircraft per day.

$$
\begin{equation}
p_{d} = \frac{p_{y}}{\left[ d:y \right]}
\label{eqn_1}
\end{equation}
$$

The number of aircraft that are required in the global fleet per day ($a_{d}$) is given by equation ($\ref{eqn_2}$). Therefore, 41,000 aircraft travel per day.

$$
\begin{equation}
a_{d} = \frac{p_{d}}{s \cdot f_{d}}
\label{eqn_2}
\end{equation}
$$



# References

[1] : https://ourworldindata.org/grapher/number-airline-passengers

[2] : TBC

[3] : TBC


# Appendix
## Link to markdown syntax
https://www.markdownguide.org/basic-syntax/

## A link to mkdocs documentation
https://www.mkdocs.org/user-guide/configuration/#documentation-layout

## A link to mkdocs-material documentation
https://squidfunk.github.io/mkdocs-material/
