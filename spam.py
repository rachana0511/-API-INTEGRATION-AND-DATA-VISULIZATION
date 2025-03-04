#importing require libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score , classification_report

emails = {
    "Get rich Quick! Click here to win a million dollars!",
    "Hello, could you please review this document for me ",
    "Discounts on luxuary watches and handbages!",
    "Meeting scheduled for tommarow , please confirm your attendence.",
    "Congratulations, yoy've won a free gift card!",
}

labels = [1,0,1,0,1]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(emails)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2)

model = MultinomialNB()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy: ", accuracy)
print("Classification Report:\n", report)

new_email = ["you've won a free cruise vacation"]
new_email_vectorzied = vectorizer.transform(new_email)
predicted_label = model.predict(new_email_vectorzied)

if predicted_label[0]  == 0:
    print("predicted as not spam.")
else:
    print("predicted as spam.")
