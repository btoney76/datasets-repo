# Datasets Repository

A curated collection of custom datasets in CSV format for easy access, analysis, and experimentation.

## Contents

| File                             | Description                                                       |
| -------------------------------- | ----------------------------------------------------------------- |
| `data/Height Weight.csv`         | Height vs. weight measurements                                    |
| `data/House Price.csv`           | Housing prices with features like square footage, bedrooms, etc. |
| `data/Productivity.csv`          | Productivity metrics over time                                    |
| `data/S&P 500.csv`               | S&P 500 historical daily closing prices                           |
| `data/Smoking Mothers.csv`       | Study on maternal smoking effects on birth outcomes               |

## Repository Structure

```

.
├── README.md
├── .gitignore
├── data/
│   ├── Height Weight.csv
│   ├── House Price.csv
│   ├── Productivity.csv
│   ├── S\&P 500.csv
│   └── Smoking Mothers.csv
└── scripts/
   └── script.py

````

## Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/datasets-repo.git
   cd datasets-repo
````

2. **Load a dataset in Python**

   ```python
   import pandas as pd

   df = pd.read_csv("data/House Price.csv")
   print(df.head())
   ```

3. **(Optional) Extend or repurpose the fetch script**
   The `scripts/fetch_datasets.py` file can be modified to download or process any datasets you choose.

## Adding Your Own Datasets

1. Drop your CSV file into the `data/` folder.
2. Update this README’s **Contents** table with a brief description.

## License

This project is licensed under the MIT License.
