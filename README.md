# Wazowski
Wazowski is a web app that aims to reduce the amount of food waste. This is done using a combination of various factors:
- Using previous demand data for various grocery items, we use LSTMs to predict potential demand in the future. This in combination with knowing the inventory and expiry dates for various grocery items, we make a recommendation to the grocer: either reduce the price (in order to encourage demand, if based on past prices there is potential for increased demand), or donate the food items prior to expiry. This reduces the amount of wasted food as the food is either bought by the consumer, or donated and put towards a good cause.
- The model for setting the food price based on demand depends on a variety of factors. Using time series data from the past, and factoring in potential demand and supply, we use basic economics in order to predict the best price for the market.

