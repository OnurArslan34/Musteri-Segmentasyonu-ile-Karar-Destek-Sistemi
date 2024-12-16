def preprocess_input(user_input, label_encoders):
    for column, encoder in label_encoders.items():
        if column in user_input:
            user_input[column] = encoder.transform([user_input[column]])[0]
    return user_input
