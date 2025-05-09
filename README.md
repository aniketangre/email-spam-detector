# Email Spam Detector

## Overview

The **Email Spam Detector** is a machine learning-based application designed to classify email messages as either "Spam" or "Not Spam". It uses a trained Naive Bayes model and TF-IDF vectorization to process and predict the nature of email content.

## Features

- **Spam Detection**: Classifies email messages as spam or not spam.
- **Pre-trained Model**: Utilizes a pre-trained Naive Bayes model for predictions.
- **Easy Integration**: Can be integrated into larger systems for automated email filtering.

## Project Structure

```
email-spam-detector/
│
├── spam_detector_model.pkl         # Pre-trained Naive Bayes model
├── spam_detector_vectorizor.pkl    # TF-IDF vectorizer
├── predict.py                      # Script for loading the model and making predictions
├── README.md                       # Project documentation
```

## Requirements

The project requires the following Python libraries:

- `joblib`
- `scikit-learn`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

### Predicting Spam

To predict whether a message is spam or not, use the `predict.py` script. The script loads the pre-trained model and vectorizer to classify the input text.

#### Example

Run the following command in your terminal:

```bash
python predict.py "Your message here"
```

**Output**:
The script will print whether the message is "Spam" or "Not Spam".

#### Sample Command

```bash
python predict.py "Congratulations! You've won a free gift card."
```

**Output**:
```
The message is: spam
```

### Integrating the Model

You can integrate the `predict` function from `predict.py` into your own application. Here's an example:

```python
from predict import predict

message = "Hello, this is a test email."
result = predict(message)
print(f"The message is: {result}")
```

## Model Training

The model was trained using a dataset of SMS messages. The training process involves:

1. **Data Loading**: Loading the dataset from a `.tsv` file.
2. **Text Vectorization**: Converting text into numerical features using TF-IDF.
3. **Model Training**: Training a Naive Bayes classifier on the vectorized data.
4. **Model Saving**: Saving the trained model and vectorizer using `joblib`.

For more details, refer to the training script in the `ml-model-api/spam_detector.py` file.

## Future Enhancements

- Add support for additional languages.
- Improve accuracy by experimenting with advanced models like transformers.
- Create a web interface for easier interaction.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Dataset: [SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- Libraries: `scikit-learn`, `joblib`
