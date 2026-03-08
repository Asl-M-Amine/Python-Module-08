#!/usr/bin/env python3

import sys
import importlib
from typing import Any


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> dict[str, Any]:
    """
    Check if required packages are installed.
    Returns a dictionary of loaded modules.
    """
    loaded_modules: dict[str, Any] = {}

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package in REQUIRED_PACKAGES:
        spec = importlib.util.find_spec(package)

        if spec is None:
            print(f"[MISSING] {package}")
            print("\nInstall dependencies with:")
            print("pip install -r requirements.txt")
            print("or")
            print("poetry install")
            sys.exit(1)

        module = importlib.import_module(package)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {package} ({version}) - ready")

        loaded_modules[package] = module

    return loaded_modules


def generate_matrix_data(numpy_module: Any, size: int = 1000) -> Any:
    """
    Generate simulated matrix data using numpy.
    """
    rng = numpy_module.random.default_rng()
    data = rng.normal(loc=50, scale=10, size=size)
    return data


def analyze_data(pandas_module: Any, data: Any) -> Any:
    """
    Analyze data using pandas.
    """
    df = pandas_module.DataFrame({"matrix_signal": data})

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(df)} data points...")

    stats = df.describe()
    print("\nData summary:")
    print(stats)

    return df


def create_visualization(matplotlib_module: Any, df: Any) -> None:
    """
    Create a simple histogram visualization.
    """
    plt = matplotlib_module.pyplot

    print("\nGenerating visualization...")

    plt.figure()
    plt.hist(df["matrix_signal"], bins=30)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)

    print(f"\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    """
    Main program execution.
    """
    modules = check_dependencies()

    numpy_module = modules["numpy"]
    pandas_module = modules["pandas"]
    matplotlib_module = modules["matplotlib"]

    data = generate_matrix_data(numpy_module)
    df = analyze_data(pandas_module, data)
    create_visualization(matplotlib_module, df)


if __name__ == "__main__":
    main()