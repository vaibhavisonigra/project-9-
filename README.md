# project-9-
# Sales Data Analyzer

An interactive command-line application built in Python for Object-Oriented Data Analysis, Data Cleaning, Statistical Reporting, and Data Visualization using Pandas, NumPy, Matplotlib, and Seaborn.

---

## 📌 Features

### 1. Data Loading & Handling
* Load CSV files dynamically via interactive menu prompts.
* Automatic path striping and error handling for invalid or missing files.

### 2. Data Exploration & Inspection
* View sample records (First 5 rows / Last 5 rows).
* View dataset column names, data types (`dtypes`), and concise structure summary (`info()`).

### 3. Data Cleaning & Preprocessing
* Identify rows with missing/null values.
* Fill missing numeric values automatically with column mean values.
* Drop rows containing missing values (`dropna()`).
* Replace specific missing values in targeted columns with custom values.

### 4. DataFrame & NumPy Operations
* Extract numeric data into NumPy arrays.
* Demonstrate array slicing, indexing, and element-wise matrix operations.

### 5. Descriptive Statistics
* Summary statistics using `describe()`.
* Calculation of variance (`var()`) and standard deviation (`std()`) across numeric attributes.

### 6. Interactive Data Visualizations
Generate and display customized plots using Matplotlib and Seaborn:
* **Bar Chart**: Compare categorical variables against numeric metrics.
* **Line Plot**: Analyze trends over time or sequence.
* **Scatter Plot**: Correlation analysis between two numeric attributes.
* **Pie Chart**: Proportional distribution of categorical values.
* **Histogram & Box Plot**: Distribution and outlier visualization.
* **Correlation Heatmap**: Multi-variable correlation analysis.

### 7. Export Capabilities
* Save generated visualizations directly to image files (PNG/JPG).

---

## 🛠️ Technology Stack

* **Python 3.x**
* **Pandas**: Data structures, indexing, missing value handling, and summary statistics
* **NumPy**: Numeric operations and array manipulations
* **Matplotlib**: Fundamental plotting and image export
* **Seaborn**: Statistical chart generation and color styling

---

## 📂 Architecture & Design Pattern

The application is built around an Object-Oriented Design (OOD) pattern:
* **`SalesDataAnalyzer` Class**: Encapsulates data state (`self.data`), plot handles (`self.last_plot`), methods for exploration, cleaning, math, plotting, and file saving.
* **`run_cli()` Interface**: Interactive terminal loop driving user choices and operations.

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/sales-data-analyzer.git](https://github.com/your-username/sales-data-analyzer.git)
   cd sales-data-analyzer
