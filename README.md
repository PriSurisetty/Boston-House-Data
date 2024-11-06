# Boston Housing Data

This project uses the Boston Housing dataset to analyze and predict housing prices based on various features like crime rate, number of rooms, and more. The dataset is preprocessed by handling missing values and normalizing the data using Min-Max scaling.

## Data ouput after it's been cleaned and preprocessed:

<img width="712" alt="Screenshot 2024-11-05 at 7 19 06 PM" src="https://github.com/user-attachments/assets/e23cfa9d-6aa7-41f4-9574-6a98f36b7483">


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Processing](#data-processing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, make sure you have Python 3 and the necessary dependencies installed.

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/Boston-House-Data.git
    ```
2. Navigate into the project directory:
    ```bash
    cd Boston-House-Data
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

> Make sure you have `scikit-learn`, `pandas`, and `numpy` installed.

## Usage

1. Open the project directory and run the Python script to preprocess the Boston Housing data.
    ```bash
    python preprocess_data.py
    ```

2. The script will read the `BostonHousing.csv` file, fill missing values in the 'rm' column with the mean value, and scale the data.

3. The cleaned and preprocessed data will be saved back to the CSV file.

## Data Processing

This project focuses on data cleaning and normalization:

1. **Missing Value Handling**: The missing values in the 'rm' (average number of rooms) column are replaced with the mean value of that column.
2. **Normalization**: The data is normalized using Min-Max scaling to transform the features to a range between 0 and 1.

## Contributing

Feel free to fork this repository and contribute! To suggest changes:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

