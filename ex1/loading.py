import importlib
import sys
from typing import Any, List, Dict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def check_dependencies(packages: List[str]) ->  bool:
    print("LOADING STATUS: Loading programs...")
    all_ok = True
    for package in packages:
        try:
            lib = importlib.import_module(package)
            version = getattr(lib, "__version__", "unknown")
            print(f"OK - package {package} version {version} - Ready !")
        except ImportError:
            print(f"Error, package {package} is missing !")
            all_ok = False
        return all_ok

def analyze_matrix_data() -> pd.DataFrame:
    print("Analyzing Matrix data...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=['Signal_Strength'])
    return df

def create_visualization(df: pd.DataFrame) -> None:
    print("Generating visualization...")
    df.hist(bins=50)
    plt.title("Matrix Signal Analysis")
    plt.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")

def main() -> None:
    required = ["pandas", "numpy", "matplotlib"]
    
    if not check_dependencies(required):
        print("\nERROR: Packages couldn't be installed !")
        print("Use 'pip install -r requirements.txt' or 'poetry install'")
        sys.exit(1)
        
    df = analyze_matrix_data()
    create_visualization(df)
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
