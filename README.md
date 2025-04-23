# Iris-Flower-Classification
# 🌸 Iris Flower Classification

A machine learning project to classify Iris flowers into three species based on sepal and petal measurements using supervised learning techniques.

---

## 📁 Project Structure


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
2. (Optional) Create and activate a virtual environment:

Windows: python -m venv venv
venv\Scripts\activate

3. Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt

4. Ensure the dataset is available at data/Iris.csv. If not, download it manually from Kaggle:

Iris Dataset on Kaggle

5. Train the model:

bash
Copy
Edit
python src/train_model.py

6.Evaluate the model performance:

bash
Copy
Edit
python src/evaluate_model.py

7. Test the model with sample inputs:

bash
Copy
Edit
python test_model.py
