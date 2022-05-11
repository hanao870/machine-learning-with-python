"""訓練データとテストデータ."""
from pathlib import Path

import matplotlib.pyplot as plt
import mglearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset["data"], iris_dataset["target"], random_state=0
)

print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")

# X_train のデータから DataFrame を作る、
# iris_dataset.feature_names の文字列を使ってカラムに名前を付ける
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

# データフレームから scatter matrix を作成し、y_train に従って色を付ける
grr = pd.plotting.scatter_matrix(
    iris_dataframe,
    c=y_train,
    figsize=(15, 15),
    marker="o",
    hist_kwds={"bins": 20},
    s=60,
    alpha=0.8,
    cmap=mglearn.cm3,
)

png_file = Path(__file__).parent / "img" / "scatter_matrix.png"

plt.savefig(png_file)
