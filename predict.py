import joblib
import sys

def load_model():
    model = joblib.load('spam_detector_model.pkl')
    vectorizor = joblib.load('spam_detector_vectorizor.pkl')
    return model, vectorizor

def predict(text):
    model, vectorizor = load_model()
    text_transformed = vectorizor.transform([text])
    prediction = model.predict(text_transformed)
    return "spam" if prediction[0] == 1 else "Not Spam"

if __name__ == "__main__":
    text = sys.argv[1] #"Hello world!"
    prediction = predict(text)
    print(f"The message is: {prediction}")




