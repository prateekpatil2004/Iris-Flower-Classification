import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from preprocess import load_data
from sklearn.model_selection import train_test_split
from pathlib import Path
import os

# Get the project root directory (IRIS/)
current_dir = Path(__file__).parent  # src/ folder
project_root = current_dir.parent   # IRIS/ folder
output_dir = project_root / "outputs"

# Ensure outputs directory exists
output_dir.mkdir(exist_ok=True)

# Load data
df, feature_names = load_data()
X_train, X_test, y_train, y_test = train_test_split(
    df[feature_names], df['species'], test_size=0.2, random_state=42)

# Load model (using absolute path)
model_path = output_dir / "iris_model.pkl"
clf = joblib.load(model_path)

# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save confusion matrix (absolute path)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig(output_dir / "confusion_matrix.png")  # Fixed path
plt.close()