# -*- coding: utf-8 -*-
"""ChatGPT 4o Evalutation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11nxTOTgf-fapofKJLZP6LQUwWiFetG3E

#**Commonsense**

#Baseline
"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/cm_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/CS1.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['Label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Few-shot Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/cm_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/CS2.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Role-based Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/cm_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/CS3.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#**Deonotology**

#Baseline
"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/deontology_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/D1.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Few-shot Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/deontology_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/D2.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Role-based Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/deontology_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/D3.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#**Justice**

#Baseline
"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/justice_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/J1.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Few-shot Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/justice_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/J2.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Role-based Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/justice_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/J3.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#**Virtue**

#Baseline
"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/virtue_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/V1.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Few-shot prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/virtue_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/V2.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

"""#Role-based Prompting"""

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# Load the two test CSV files: one with true labels and one with predicted labels
true_labels_df = pd.read_csv("/content/virtue_test_50.csv")  # original file with true labels
predicted_labels_df = pd.read_csv("/content/V3.csv")  # updated file with predictions

# Extract labels
y_true = true_labels_df['label']
y_pred = predicted_labels_df['label']

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

accuracy, f1, precision, recall

