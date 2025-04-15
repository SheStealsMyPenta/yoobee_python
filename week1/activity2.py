import numpy as np

# Given scores
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Average score per student (row-wise)
student_avg = np.mean(scores, axis=1)
print("Average score per student:", student_avg)

# Average score per subject (column-wise)
subject_avg = np.mean(scores, axis=0)
print("Average score per subject:", subject_avg)

# Total score per student
total_scores = np.sum(scores, axis=1)

# Student index with highest total score
top_student_idx = np.argmax(total_scores)
print("Student with highest total score (row index):", top_student_idx)

# Add 5 bonus points to third subject (column index 2)
scores[:, 2] += 5
print("Scores after adding 5 bonus to 3rd subject:\n", scores)