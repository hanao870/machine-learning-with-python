"""アイリスデータ."""
from sklearn.datasets import load_iris

iris_dataset = load_iris()
print(f"Keys of iris_dataset: \n{iris_dataset.keys()}")

# DESCR の最初の説明
print(iris_dataset["DESCR"][:193] + "\n...")

# 予測する花の種類
print(f"Target name: {iris_dataset['target_names']}")

# 特徴量の説明
print(f"Feature names: \n{iris_dataset['feature_names']}")

# データ本体の type
print(f"Type of data: {type(iris_dataset['data'])}")

# データの形
print(f"Shape of data: {iris_dataset['data'].shape}")

# 最初の 5 つのサンプルを表示
print(f"First five columns os data:\n{iris_dataset['data'][:5]}")

# 測定された個々の花の種類
print(f"Type of target: {type(iris_dataset['target'])}")

# target データの形
print(f"Shape of target: {iris_dataset['target'].shape}")

# target データの種類
print(f"Target:\n{iris_dataset['target']}")
