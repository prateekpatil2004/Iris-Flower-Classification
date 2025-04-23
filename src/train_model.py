from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from preprocess import load_data

df, feature_names = load_data()

X_train, X_test, y_train, y_test = train_test_split(
    df[feature_names], df['species'], test_size=0.2, random_state=42)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Save model
import os
from pathlib import Path

# Get the absolute path to the outputs directory
current_dir = Path(__file__).parent  # src/ directory
output_dir = current_dir.parent / "outputs"  # goes up to IRIS/, then into outputs/

# Ensure the directory exists
output_dir.mkdir(exist_ok=True)

# Save the model
model_path = output_dir / "iris_model.pkl"
joblib.dump(clf, model_path)
