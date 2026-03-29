# Spam Message Detection using Machine Learning

## Overview
This project focuses on building a machine learning model that can classify SMS messages as either spam or not spam (ham). The system analyzes the text of a message and predicts whether it is genuine or unwanted.

## Objective
The objective of this project is to apply machine learning techniques to automatically detect spam messages. It also aims to demonstrate the practical use of concepts such as text preprocessing, feature extraction, and classification.

## Methodology
The project follows a simple and structured approach:

- The dataset consists of labeled SMS messages categorized as spam or ham.
- The text data is cleaned by converting it to lowercase and removing unnecessary characters such as punctuation and numbers.
- The cleaned text is converted into numerical form using TF-IDF vectorization.
- A Multinomial Naive Bayes model is trained on the processed data.
- The model is then used to predict whether a new message is spam or not.

## Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Regular Expressions (re)  

## How to Run the Project

1. Install the required libraries:
   pip install -r requirements.txt

2. Run the program:
   python main.py

3. Enter a message when prompted to check whether it is spam or not.

## Example

Input:
Win ₹5000 now!!!

Output:
Spam

## Results
The model is able to identify common spam patterns and classify messages with reasonable accuracy. Its performance depends on the quality and size of the dataset used for training.

## Challenges Faced
- Handling small or limited datasets  
- Cleaning text data effectively  
- Improving model accuracy with simple techniques  

## Future Improvements
- Use a larger and more diverse dataset  
- Improve preprocessing techniques  
- Build a simple user interface for easier interaction  
- Experiment with more advanced machine learning models  

## Conclusion
This project demonstrates how machine learning can be used to solve a real-world problem like spam detection. It provides a clear understanding of how text data can be processed and used to train a classification model.
