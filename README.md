# AI-Driven-Quantitative-Trading-Strategy
This project implements a Walk-Forward Backtesting Engine using TensorFlow and Keras. Unlike standard "Price Prediction" models, this engine optimizes for the Sharpe Ratio directly, ensuring that the AI prioritizes consistent, low-volatility growth over high-risk gambling.
Differentiable Sharpe Loss: A custom loss function that trains the Neural Network to maximize risk-adjusted returns rather than just directional accuracy.
Transaction Cost Awareness: Includes a built-in penalty for turnover (0.1% per trade), reflecting real-world slippage and commissions.
Walk-Forward Validation: Simulates real trading by retraining the model on a rolling window, preventing "look-ahead" bias.
Confidence Filtering: Uses a tanh-activation threshold to only execute trades when the model signal is strong.
