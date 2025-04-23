# Iris-Flower-Classification
# 🌸 Iris Flower Classification

A machine learning project to classify Iris flowers into three species based on sepal and petal measurements using supervised learning techniques.

---

## 📁 Project Structure
iris-classification/
│
├── data/                            # (optional - for storing CSV if downloaded manually)
│   └── Iris.csv
│
├── notebooks/
│   └── EDA_and_Modeling.ipynb       # EDA and visualization (feature importance, etc.)
│
├── outputs/                         # Store model artifacts and plots
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── iris_model.pkl
│
├── src/
│   ├── load_from_kaggle.py         # ✅ Loads dataset using kagglehub
│   ├── preprocess.py               # Functions for data cleaning and preparation
│   ├── train_model.py              # Training script (Random Forest)
│   └── evaluate.py                 # Model evaluation (metrics and confusion matrix)
│
├── requirements.txt                # Python packages needed
├── README.md                       # 📄 Project overview, usage, instructions
└── .gitignore                      # Ignore outputs/, __pycache__/, .ipynb_checkpoints, etc.


---

## 📌 Objective

- Classify Iris flowers into one of the three species:
  - *Iris-setosa*
  - *Iris-versicolor*
  - *Iris-virginica*

- Identify the most significant features for classification.

- Achieve high classification accuracy.

---

## 📊 Dataset

- **Source**: [Iris dataset on Kaggle](https://www.kaggle.com/uciml/iris)
- **Features**:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **Target**: Species (Setosa, Versicolor, Virginica)

---

## ⚙️ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/iris-flower-classification.git
   cd iris-flower-classification

2. Setup a Virtual Environment:
   ```bash
   python -m venv venv

3.Install dependencies:
  ```bash
   pip install -r requirements.txt
1. Train the Model
Run from the project root:

bash
python src/train_model.py
Output: Saves iris_model.pkl to outputs/.

2. Evaluate the Model
bash
python src/evaluate.py
Output:

Prints accuracy and classification report.

Saves confusion_matrix.png to outputs/.

3. Jupyter Notebooks:
Explore notebooks/EDA_and_Model_Training.ipynb for interactive analysis.

📊 Results
Model: Random Forest Classifier

Accuracy: ~96-98% (varies with random seed)

Confusion Matrix:
Confusion Matrix

