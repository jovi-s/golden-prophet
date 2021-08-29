import pandas as pd
from pandas import to_datetime
from matplotlib import pyplot
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

class GoldProphet():
	"""Code referenced from:
	https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python/
	"""

	def __init__(self, path):
		self.path = path
		# define the model
		self.model = Prophet()

	def load_data(self):
		# load data
		self.monthly_df = pd.read_csv(self.path)

		# prepare expected column names
		self.monthly_df.columns = ['ds', 'y']
		self.monthly_df['ds']= to_datetime(self.monthly_df['ds'])
		return self.monthly_df

	def train(self):
		# fit the model
		self.model.fit(self.monthly_df)
		return self.model

	def predict(self):
		# define the period for which we want a prediction
		future = list()
		for i in range(1, 13):
			date = '2021-%02d' % i
			future.append([date])
		future = pd.DataFrame(future)
		future.columns = ['ds']
		future['ds']= to_datetime(future['ds'])
		# use the model to make a forecast
		self.forecast = self.model.predict(future)
		# summarize the forecast
		print(self.forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
		# plot forecast
		self.model.plot(self.forecast)
		pyplot.show()
	
	def mae_evalution(self):
		"""objective estimate of a forecast model’s performance.
		This can be achieved by holding some data back from the model,
		such as the last 12 months. Then, fitting the model on the first
		portion of the data, using it to make predictions on the held-pack 
		portion, and calculating an error measure, such as the mean 
		absolute error across the forecasts.
		"""
		# create test dataset, remove last 12 months
		train = self.monthly_df.drop(self.monthly_df.index[-12:])
		# fit the model
		self.mae_model = self.model.fit(train)

		# define the period for which we want a prediction
		future = list()
		for i in range(1, 13):
			date = '2021-%02d' % i
			future.append([date])
		future = pd.DataFrame(future)
		future.columns = ['ds']
		future['ds'] = to_datetime(future['ds'])
		# use the model to make a forecast
		forecast = self.mae_model.predict(future)
		# calculate MAE between expected and predicted values for month
		y_true = self.monthly_df['y'][-12:].values
		y_pred = forecast['yhat'].values
		mae = mean_absolute_error(y_true, y_pred)
		print('MAE: %.3f' % mae)
		# plot expected vs actual
		pyplot.plot(y_true, label='Actual')
		pyplot.plot(y_pred, label='Predicted')
		pyplot.legend()
		pyplot.show()