# Regression-Project

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)
6. [License](#license)
7. [Workflows](#workflows)

## Description
Regression is a fundamental supervised machine learning technique used to predict continuous numerical outcomes based on input features. This project focuses on applying regression to [The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic prices and the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102, 1978.] using a structured dataset. The analysis is designed to provide insights into the relationships between input features and the target variable while also delivering an accurate predictive model.

## Key Concepts Covered
1.Exploratory Data Analysis (EDA)
  Understand the data through visualization, summary statistics, and correlation analysis.

2.Data Preprocessing

- Handle missing values and outliers.
- Transform and encode categorical variables.
- Standardize or normalize numerical features.

3.Modeling and Evaluation

- Experiment with different regression techniques (Linear Regression, Decision Trees, Gradient Boosting, etc.).
- Use metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²) to evaluate model performance.

4.Feature Importance and Interpretability

- Understand which features influence predictions the most.
- Visualize model predictions versus actual values.
  
## Project Goals
1.Build a robust regression model to predict [target variable, e.g., house prices].                                      
2.Explore and visualize patterns in the data.                                                 
3.Highlight practical insights for stakeholders, such as the most influential factors affecting the target variable.                                          

## Technologies Used
- Python for data processing and modeling.
- Pandas and NumPy for data manipulation.
- Matplotlib and Seaborn for visualizations.
- Scikit-learn for machine learning algorithms and metrics.


## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/oscar/Regression-Project.git

## Usage
jupyter notebook notebooks/exploratory_analysis.ipynb

## Project Structure
Regression-Project/                                                    
│                                                    
├── data/                                                                    
│   ├── raw/                                                                      
│   ├── processed/                                                                
│                                                    
├── notebooks/                                                                    
│   ├── exploratory_analysis.ipynb                                                     
│   ├── regression_model.ipynb                                                          
│                                                    
├── scripts/                                                                      
│   ├── data_preprocessing.py                                                    
│   ├── model_training.py                                                    
│   ├── evaluation.py                                                    
│                                                    
├── visuals/                                                                      
│                                                    
├── README.md                                                                     
├── requirements.txt                                                              
├── LICENSE                                                                       
├── .gitignore                      
│   ├── workflows                                                                                     
│   ├── workflows_aws                                                                                 
│   ├── workflows_ngrok                                       


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Workflows 

**Workflows: Automating Deployment and Setup**                                            
This project provides three distinct workflows to enable deployment and environment setup across various platforms. Each is designed for specific use cases, as detailed below.

1. Workflows/streamlit.yml: **Deploying to Streamlit Cloud**                          
This workflow facilitates automatic deployment of the application to Streamlit Cloud, a free hosting service specifically designed for Streamlit-based applications.

   **Key Features:**
    - **Core File**: .github/workflows/streamlit.yml.            
    - Automatically installs dependencies from requirements.txt.                  
    - Configures environment variables and prepares necessary files, such as kaggle.json, for data access.                   
     - Ideal for simple and rapid deployments of Streamlit applications.
  
     **Benefits:**
     - Free hosting with public access.
     - Streamlined management of dependencies and environment setup.

2. workflows_ngrok/streamlit_ngrok_solution: **Running with Ngrok**
This workflow is intended to expose the local Streamlit application to the internet using Ngrok, a tool for creating secure HTTPS tunnels to localhost.

   **Key Features:**
    - Core File: workflows_ngrok/streamlit_ngrok_solution.
    - Configures Ngrok to create a tunnel and expose the application.
    - **Currently Non-Functional** due to recent changes in Ngrok's tunneling and endpoint APIs.
  
   **Current Limitations:**
    - Ngrok updates have broken compatibility with the current implementation.
    - Ongoing efforts aim to adapt this workflow to the latest Ngrok standards.
   **Future Use:**
    - This workflow has potential for temporary public exposure of local applications without a dedicated hosting platform.

3. workflows_aws/ec2_AWS.txt: **Deploying to AWS EC2**
This workflow outlines the steps for deploying the application on an AWS EC2 instance. It is suited for scalable and customizable environments.

**Key Steps:**
    - **Launch an EC2 Instance:** Use the AWS Management Console or AWS CLI to create an instance.
    - **User Data File:** Copy the commands in workflows_aws/ec2_AWS.txt and paste them into the "User Data" field during the instance setup. These commands:
    -- Install Python, pip, and Streamlit.
    -- Install dependencies from requirements.txt.
    -- Launch the application on the configured port.

**Benefits:**
  - Full control over the runtime environment.
  - Scalability to handle varying levels of traffic and usage.                                    

## Summary
Each workflow serves a distinct purpose:

- Streamlit Cloud: For quick and easy deployment.
- Ngrok: For temporary public testing (under development).
- AWS EC2: For robust and scalable deployments.

Follow the instructions in each workflow file to implement the desired deployment strategy.
