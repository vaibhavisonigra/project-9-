import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
try:
    import seaborn as sns
except ImportError:
    sns = None
    
class SalesDataAnalyzer:
    """Class encapsulating data operations, stats, and visualization."""

    def __init__(self, file_path=None):
        self.data = None
        self.last_plot = None  # Holds the current Matplotlib figure object
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        # Cleanup actions if necessary
        pass

    def load_data(self, file_path):
        """Load sales data from a CSV file."""
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return False
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return False

    # --- Data Exploration & Cleaning ---
    def explore_data(self, option):
        """Display sub-options for exploring data."""
        if self.data is None:
            print("No dataset loaded. Please load a CSV file first.")
            return

        if option == 1:
            print("--- First 5 rows ---")
            print(self.data.head())
        elif option == 2:
            print("--- Last 5 rows ---")
            print(self.data.tail())
        elif option == 3:
            print("--- Column Names ---")
            print(list(self.data.columns))
        elif option == 4:
            print("--- Data Types ---")
            print(self.data.dtypes)
        elif option == 5:
            print("--- Info Summary ---")
            print(self.data.info())
        else:
            print("Invalid option.")

    def handle_missing_data(self, option, column_name=None, fill_value=None):
        """Clean missing values in the dataset."""
        if self.data is None:
            print("No dataset loaded.")
            return

        missing_count = self.data.isnull().sum().sum()
        if missing_count == 0:
            print("No missing values found in the dataset!")
            return

        if option == 1:
            print("--- Rows with Missing Values ---")
            print(self.data[self.data.isnull().any(axis=1)])
        elif option == 2:
            num_cols = self.data.select_dtypes(include=[np.number]).columns
            self.data[num_cols] = self.data[num_cols].fillna(self.data[num_cols].mean())
            print("Missing numerical values filled with mean successfully.")
        elif option == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif option == 4:
            if column_name and fill_value is not None:
                self.data[column_name].fillna(fill_value, inplace=True)
                print(f"Replaced missing values in '{column_name}' with '{fill_value}'.")
            else:
                print("Column name or value missing.")

    # --- DataFrame & NumPy Operations ---
    def perform_dataframe_operations(self):
        """Demonstrate basic mathematical and indexing operations."""
        if self.data is None:
            print("No dataset loaded.")
            return

        # Extract numeric columns as NumPy array
        numeric_df = self.data.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            arr = numeric_df.to_numpy()
            print("--- NumPy Array Creation (First 3 rows) ---")
            print(arr[:3])

            print("--- NumPy Slicing Example (Column 0, First 5 rows) ---")
            print(arr[:5, 0])

            print("--- Element-wise Math Operation (Scale values by 1.1) ---")
            print((arr[:3] * 1.1))

    def generate_descriptive_statistics(self):
        """Generate statistical calculations."""
        if self.data is None:
            print("No dataset loaded.")
            return

        print("--- Descriptive Statistics ---")
        print(self.data.describe())

        # Additional standard deviation, variance, quantiles
        numeric_df = self.data.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            print("--- Variance ---")
            print(numeric_df.var())
            print("--- Standard Deviation ---")
            print(numeric_df.std())

    # --- Data Visualization ---
    def visualize_data(self, plot_type):
        """Create interactive plots using Matplotlib and Seaborn."""
        if self.data is None:
            print("No dataset loaded.")
            return

        fig, ax = plt.subplots(figsize=(8, 5))

        try:
            if plot_type == 1:  # Bar Plot
                x_col = input("Enter X-axis column name: ")
                y_col = input("Enter Y-axis column name: ")
                sns.barplot(data=self.data, x=x_col, y=y_col, ax=ax)
                ax.set_title(f"Bar Plot: {y_col} by {x_col}")

            elif plot_type == 2:  # Line Plot
                x_col = input("Enter X-axis column name: ")
                y_col = input("Enter Y-axis column name: ")
                sns.lineplot(data=self.data, x=x_col, y=y_col, ax=ax)
                ax.set_title(f"Line Plot: {y_col} vs {x_col}")

            elif plot_type == 3:  # Scatter Plot
                x_col = input("Enter X-axis column name: ")
                y_col = input("Enter Y-axis column name: ")
                sns.scatterplot(data=self.data, x=x_col, y=y_col, ax=ax)
                ax.set_title(f"Scatter Plot: {y_col} vs {x_col}")

            elif plot_type == 4:  # Pie Chart
                col = input("Enter category column name: ")
                val_counts = self.data[col].value_counts()
                ax.pie(val_counts, labels=val_counts.index, autopct='%1.1f%%')
                ax.set_title(f"Pie Chart: {col}")

            elif plot_type == 5:  # Histogram
                col = input("Enter numeric column name: ")
                sns.histplot(self.data[col], kde=True, ax=ax)
                ax.set_title(f"Histogram of {col}")

            elif plot_type == 6:  # Box Plot
                col = input("Enter numeric column name: ")
                sns.boxplot(y=self.data[col], ax=ax)
                ax.set_title(f"Box Plot of {col}")

            elif plot_type == 7:  # Heatmap
                num_df = self.data.select_dtypes(include=[np.number])
                sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", ax=ax)
                ax.set_title("Correlation Heatmap")

            else:
                print("Invalid choice.")
                plt.close(fig)
                return

            plt.tight_layout()
            self.last_plot = fig
            plt.show()
            print("Plot displayed successfully!")

        except KeyError:
            print("Error: Column name not found in dataset.")
            plt.close(fig)
        except Exception as e:
            print(f"Error generating plot: {e}")
            plt.close(fig)

    def save_visualization(self, file_name):
        """Save current visualization to a file."""
        if self.last_plot is None:
            print("No active visualization to save.")
            return

        try:
            self.last_plot.savefig(file_name)
            print(f"Visualization saved as '{file_name}' successfully!")
        except Exception as e:
            print(f"Error saving image: {e}")


# --- Interactive Menu Interface ---
def run_cli():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n" + "=" * 45)
        print("======== Data Analysis & Visualization ========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            file_path = input("Enter the path of the dataset (CSV file): ").strip()
            analyzer.load_data(file_path)

        elif choice == '2':
            print("== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice.isdigit():
                analyzer.explore_data(int(sub_choice))

        elif choice == '3':
            analyzer.perform_dataframe_operations()

        elif choice == '4':
            print("== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == '1':
                analyzer.handle_missing_data(1)
            elif sub_choice == '2':
                analyzer.handle_missing_data(2)
            elif sub_choice == '3':
                analyzer.handle_missing_data(3)
            elif sub_choice == '4':
                col = input("Enter column name: ").strip()
                val = input("Enter value: ").strip()
                analyzer.handle_missing_data(4, col, val)

        elif choice == '5':
            analyzer.generate_descriptive_statistics()

        elif choice == '6':
            print("== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Box Plot")
            print("7. Correlation Heatmap")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice.isdigit():
                analyzer.visualize_data(int(sub_choice))

        elif choice == '7':
            filename = input("Enter file name to save plot (e.g., scatter_plot.png): ").strip()
            analyzer.save_visualization(filename)

        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid selection, please try again.")


if __name__ == "__main__":
    run_cli()
    