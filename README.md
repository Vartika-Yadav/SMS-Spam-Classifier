# SMS Spam Classifier

An end-to-end machine learning application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and Logistic Regression.

The project includes data preprocessing, text vectorization using TF-IDF, machine learning model training and evaluation, and an interactive Streamlit application for real-time predictions. The application is deployed on AWS EC2.

## Project Overview

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, or misleading links. This project uses machine learning to automatically identify whether an SMS message is likely to be spam.

The project follows a simple end-to-end machine learning workflow:

```text
SMS Dataset
     ↓
Data Cleaning
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Model Evaluation
     ↓
Streamlit Application
     ↓
AWS EC2 Deployment
```

## Features

* SMS spam/ham classification
* Text preprocessing and cleaning
* TF-IDF feature extraction
* Logistic Regression classification
* Model evaluation using standard classification metrics
* Interactive Streamlit web application
* Real-time message prediction
* Confidence/probability display
* Deployment on AWS EC2

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **NLTK**
* **Streamlit**
* **Joblib**
* **AWS EC2**
* **Git & GitHub**

## Dataset

The project uses the **SMS Spam Collection** dataset containing labeled SMS messages categorized as:

* `ham` — legitimate message
* `spam` — unwanted/spam message

The dataset is used to train and evaluate the machine learning model.

## Machine Learning Approach

### 1. Data Preprocessing

The raw SMS messages are cleaned before model training.

The preprocessing workflow includes:

* Removing unnecessary characters
* Converting text to lowercase
* Removing unnecessary whitespace
* Preparing the text for feature extraction

### 2. TF-IDF Vectorization

Since machine learning models cannot directly work with raw text, the SMS messages are converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF assigns higher importance to words that are useful for distinguishing between different messages while reducing the influence of very common words.

### 3. Classification Model

The primary classification model used in this project is **Logistic Regression**.

The model learns patterns from labeled SMS messages and predicts whether a new message belongs to the `spam` or `ham` class.

## Model Evaluation

The trained model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The final evaluation results will be documented here after training the model.

| Metric    | Score |
| --------- | ----: |
| Accuracy  |   TBD |
| Precision |   TBD |
| Recall    |   TBD |
| F1-Score  |   TBD |

## Application

The Streamlit application provides a simple interface where users can enter an SMS message and receive a prediction.

Example:

```text
Input:
Congratulations! You have won a free prize. Click here to claim it.

Prediction:
SPAM

Confidence:
TBD
```

For a normal message:

```text
Input:
Hey, are we still meeting at 6 PM?

Prediction:
HAM

Confidence:
TBD
```

## Project Structure

```text
SMS-Spam-Classifier/
│
├── data/
│   └── spam.csv
│
├── notebooks/
│   └── model_training.ipynb
│
├── src/
│   └── ...
│
├── app.py
├── requirements.txt
├── README.md
└── ...
```

The exact structure may be updated as the project develops.

## AWS Deployment

The trained machine learning application is deployed using **Amazon EC2**.

Deployment workflow:

```text
Local Development
       ↓
GitHub Repository
       ↓
AWS EC2 Instance
       ↓
Python Environment
       ↓
Streamlit Application
       ↓
Web Browser
```

AWS services and components used:

* **Amazon EC2** — hosts the Streamlit application
* **Security Groups** — controls inbound access to the application

The deployment details and public application URL will be added after deployment.

## How to Run Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd SMS-Spam-Classifier
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## Future Improvements

Possible improvements include:

* Comparing additional classification algorithms
* Improving text preprocessing
* Adding model explainability
* Handling multilingual messages
* Adding a message history feature
* Containerizing the application
* Adding automated model retraining

## Learning Outcomes

Through this project, I practiced:

* Working with real-world text data
* Data preprocessing
* NLP fundamentals
* TF-IDF feature extraction
* Binary classification
* Model evaluation
* Building an ML application with Streamlit
* Deploying a Python application on AWS EC2
* Managing a project using Git and GitHub

## Author

**Vartika Yadav**

B.Tech Computer Science & Engineering (Artificial Intelligence)

GitHub: [Vartika-Yadav](https://github.com/Vartika-Yadav)
