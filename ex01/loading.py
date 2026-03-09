#!/usr/bin/env python3

import sys
import importlib
from typing import Any

REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib", "requests"]

PACKAGE_PURPOSE = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computing ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready",
}


def check_dependencies() -> dict[str, Any]:
    """
    Check if required packages are installed.
    Return loaded modules.
    """
    modules: dict[str, Any] = {}

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package in REQUIRED_PACKAGES:
        spec = importlib.util.find_spec(package)

        if spec is None:
            print(f"[MISSING] {package}")
            print("\nInstall dependencies using pip:")
            print("pip install -r requirements.txt")
            print("\nOr install using Poetry:")
            print("poetry install")
            sys.exit(1)

        module = importlib.import_module(package)
        version = getattr(module, "__version__", "unknown")

        purpose = PACKAGE_PURPOSE.get(package, "ready")
        print(f"[OK] {package} ({version}) - {purpose}")

        modules[package] = module

    return modules


def show_dependency_management_info() -> None:
    """
    Explain pip vs Poetry dependency management.
    """
    print("\nDependency Management Information:")
    print("- pip installs packages listed in requirements.txt")
    print("- Poetry uses pyproject.toml to manage dependencies and environments")
    print("- Poetry also handles virtual environments automatically")


def generate_matrix_data(numpy_module: Any, size: int = 1000) -> Any:
    """
    Generate simulated matrix signal data.
    """
    rng = numpy_module.random.default_rng()
    return rng.normal(loc=50, scale=10, size=size)


def analyze_data(pandas_module: Any, data: Any) -> Any:
    """
    Analyze matrix data using pandas.
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
    Create histogram visualization.
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

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    modules = check_dependencies()

    numpy_module = modules["numpy"]
    pandas_module = modules["pandas"]
    matplotlib_module = modules["matplotlib"]

    show_dependency_management_info()

    data = generate_matrix_data(numpy_module)
    df = analyze_data(pandas_module, data)
    create_visualization(matplotlib_module, df)


if __name__ == "__main__":
    main()
