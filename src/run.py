import argparse

from .gold_prophet import GoldProphet


def run(data_path, evaluation):
	model=GoldProphet(data_path)
	model.load_data()

	if evaluation:
		model.mae_evalution()
	else:
		model.train()
		model.predict()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-p','--data_path', default="./data/gold_price_monthly.csv")
	parser.add_argument('-e','--eval', default=False)
	args = parser.parse_args()

	run(args.data_path,
		args.eval
	)