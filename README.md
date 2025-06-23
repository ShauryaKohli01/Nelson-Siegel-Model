# Nelson-Siegel-Model


Nelson-Siegel Model is a mathematical model which is used to define the shape of yield curve. This model was developed by Charles Nelson and Andrew Siegel in 1987. It is a graph that shows the interest rate (yield) for borrowing money over different lengths of time (maturity), from 1 month to 30+ years. 

# Mathematical Formula of the Nelson-Siegel Model


![image](https://github.com/user-attachments/assets/4237a5a4-5b18-4e9f-b44e-359be2a53d53)


Each parameter plays a specific role:

1. β₀ (Level): Long-term yield

2. β₁ (Slope): Difference between short- and long-term rates

3. β₂ (Curvature): Captures the hump in mid-term rates

4. λ (Decay factor): Determines where the curvature peaks

This structure enables the model to fit real-world yield curves efficiently.

# Files Included on Python and Excel

Nelson Siegel Model on Python includes: 

1. Pandas, Numpy, and scipy.optimize. 

2. It is includes the 2D and 3D figure plotting.

Nelson Siegal Model on Excel includes: 

1. Excel version with formulae

2. Solver to minimize error

# Install dependencies:

pip install numpy pandas matplotlib scipy (in the Terminal)

# Visual Representation on Python 

![image](https://github.com/user-attachments/assets/1a1b3212-e9fd-4699-aa08-77137df2d63a)


In the lefthand side, we can see the 3D surface plot of historical yield curves over time and maturity.
The X-axis shows different dates, the Y-axis represents maturities (e.g., 1M, 2Y, 10Y), and the Z-axis shows the interest rate (yield).
The color gradient (blue to red) illustrates how yields vary over both time and term. It’s useful for understanding how the entire yield curve evolves over time.

In the righthand side, we can see the 2D representation of the NS Model, The red line represents the actual observed yields from the dataset.
The blue line is the yield curve estimated using the Nelson-Siegel model. This shows how well the model fits the real market data.

# Conclusion

Building the Nelson-Siegel model in both Excel and Python helped me understand how interest rates behave over time and how markets price risk. It's a fundamental tool for economists, policymakers, and investors to make return on their investments.

This project deepened my understanding of interest rate modeling, curve fitting, and economic interpretation. It showed me how financial theory, math, and programming come together in real-world tools used by professionals in banks and central institutions.

For a detailed explanation of the model and its implementation, read the full article on my Substack: 
https://substack.com/home/post/p-166579391









