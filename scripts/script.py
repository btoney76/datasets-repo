#!/usr/bin/env python3
"""
Load CSV datasets into pandas DataFrames.
"""

import pandas as pd

# Read CSV files into DataFrames
def main():
    height_weight = pd.read_csv('data/Height Weight.csv')
    house_price = pd.read_csv('data/House Price.csv')
    productivity = pd.read_csv('data/Productivity.csv')
    sp500 = pd.read_csv('data/S&P 500.csv')
    smoking_mothers = pd.read_csv('data/Smoking Mothers.csv')

    # Print basic info
    print(f"Height Weight shape: {height_weight.shape}")
    print(f"House Price shape: {house_price.shape}")
    print(f"Productivity shape: {productivity.shape}")
    print(f"S&P 500 shape: {sp500.shape}")
    print(f"Smoking Mothers shape: {smoking_mothers.shape}")

if __name__ == '__main__':
    main()
