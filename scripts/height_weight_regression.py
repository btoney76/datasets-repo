#!/usr/bin/env python3
"""Perform simple linear regression of height on weight."""

import csv

DATA_PATH = 'data/Height Weight.csv'


def read_data(path):
    """Read weight and height columns from CSV."""
    weights = []
    heights = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                weights.append(float(row['weight']))
                heights.append(float(row['height']))
            except ValueError:
                # Skip rows with invalid data
                continue
    return weights, heights


def linear_regression(x, y):
    """Return slope and intercept for y ~ x."""
    n = len(x)
    if n == 0:
        raise ValueError('Empty data')
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    num = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    den = sum((xi - x_mean) ** 2 for xi in x)
    if den == 0:
        raise ValueError('No variation in independent variable')
    slope = num / den
    intercept = y_mean - slope * x_mean
    return slope, intercept


def r_squared(x, y, slope, intercept):
    """Compute coefficient of determination for fitted line."""
    mean_y = sum(y) / len(y)
    ss_tot = sum((yi - mean_y) ** 2 for yi in y)
    ss_res = sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y))
    if ss_tot == 0:
        return 0.0
    return 1 - ss_res / ss_tot


if __name__ == '__main__':
    weights, heights = read_data(DATA_PATH)
    slope, intercept = linear_regression(weights, heights)
    r2 = r_squared(weights, heights, slope, intercept)
    print(f"Intercept: {intercept:.4f}")
    print(f"Slope: {slope:.4f}")
    print(f"R^2: {r2:.4f}")

