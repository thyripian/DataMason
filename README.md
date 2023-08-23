
# DataMason

DataMason is a powerful Python package designed to make data analysis and manipulation easier for data professionals of all skill levels. It offers a collection of tools to clean, transform, analyze, and visualize datasets, allowing users to uncover insights and make informed decisions.

## Features

- **Data Cleaning**: Easily identify and address data quality issues.
- **Data Transformation**: Reshape and transform datasets to fit your analysis needs.
- **Data Analysis**: Perform insightful data analysis to uncover patterns and trends.
- **Data Visualization**: Create meaningful visualizations that help communicate findings.
- **Data Validation**: Validate data based on common rules and constraints.

## Installation

Install DataMason using pip:

```bash
pip install datamason
```

## Usage

### Importing the Package

```python
import datamason as dm
```

### Data Cleaning

```python
# Deduplicate rows
cleaned_data = dm.prepare.deduplicate(data)

# Fill gaps (missing values)
filled_data = dm.prepare.fill_gaps(cleaned_data)

# Trim outliers
final_data = dm.prepare.trim_outliers(filled_data)
```

### Data Transformation

```python
# Reshape data
reshaped_data = dm.transform.reshape_data(final_data)

# Encode categorical variables
encoded_data = dm.transform.encode_cats(reshaped_data)
```

### Data Analysis

```python
# Summarize the data
summary = dm.analyze.summarize(encoded_data)

# Find correlations
correlations = dm.analyze.find_correlations(encoded_data)
```

### Data Visualization

```python
# Plot a line chart
dm.visualize.plot_line(encoded_data, 'time', 'value')

# Plot a scatter chart
dm.visualize.plot_scatter(encoded_data, 'feature1', 'feature2')
```

### Data Validation

```python
# Define validation rules
rules = {
    'age': {'type': int, 'min_value': 0, 'max_value': 100},
    'name': {'type': str},
}

# Validate the data
is_valid, errors = dm.validate(encoded_data, rules)
```

## Contributing

We welcome contributions from the community to help improve DataMason. If you're interested in contributing, please follow these steps:

1. **Share Your Ideas**: Before making significant changes, send an email with your thoughts and recommendations to the contact below. We'll discuss your ideas and how they fit into the project.

2. **Fork the Repository**: If your idea is approved, you can fork the repository and work on your changes.

3. **Submit a Pull Request**: Once you've made your changes, submit a pull request for review. Please ensure that your code adheres to the existing coding standards and includes appropriate tests and documentation.

4. **Review and Merge**: We'll review your pull request and provide feedback if necessary. Upon approval, your contribution will be merged into the project.

5. **Acknowledgment**: Contributors are valued members of our community, and we'll acknowledge your hard work in our project documentation.

For any questions or further guidance, please contact us at thyripian@gmail.com](mailto:thyripian@gmail.com).

Thank you for considering contributing to DataMason!


## License

MIT License

## Contact

thyripian@gmail.com
