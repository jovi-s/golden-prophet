# Golden Prophet

## About The Project

The aim of this project is to forecast the price of gold as a time series. The dataset provided contains the average price of gold on a monthly basis from 1950 till 2020. The column of gold price is measured as the price per ounce (Oz) in USD.

Prophet was used as it is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data.

The forecasting was made for the year 2021 and an upward trend was predicted by golden-prophet.



## Installation

1. Clone and change into the repo

   ```sh
   git clone https://github.com/jovi-s/golden-prophet.git && cd "$(basename "$_" .git)"
   ```

2. Install necessary packages

   ```
   pip install -r requirements.txt
   ```




## Usage

`python -m src.run --data_path --eval `

Arguments

- data_path (default=./data/)

  Path to the data used

- eval (default=False)

  Run MSE on model for evaluation

  

## Future Work Roadmap

- Perform statistical analysis on price to determine seasonality trend
- Prediction on log of price column
- Using intraday time series price data
- Performing regression on price column using features of other commodities and forex exchange



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

Jovinder Singh - [@j0v3s](https://twitter.com/j0v3s) - jovinder@yahoo.com

Project Link: [https://github.com/jovi-s/golden-prophet](https://github.com/jovi-s/golden-prophet)

Website: https://jovinder.com/

