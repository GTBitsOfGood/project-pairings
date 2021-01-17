#
# A handy script that matches Bits of Good Developers
# with project teams according to their preferences.
#
# See the README for more information and instructions.
#
# Author: Max Karpawich <maxkarpawich@gmail.com>
#

import csv
import numpy as np
from scipy.optimize import linear_sum_assignment

csv_filename = 'example.csv'
csv_newline = '\n'
projects = [
    'Project A',
    'Project B',
    'Project C'
]

matrix = []
with open(csv_filename, newline=csv_newline) as file:
    csv_rows = list(csv.DictReader(file))
    proj_member_ratio = int(len(csv_rows) / len(projects))
    for i, csv_row in enumerate(csv_rows):
        semester_count = int(csv_row['Semesters']) + 1
        matrix_row = [0] * len(csv_rows)
        for j in range(len(projects)):
            proj_i = projects.index(csv_row[str(j + 1)])
            for k in range(proj_member_ratio):
                matrix_row[proj_i * proj_member_ratio + k] = (j + 1) * semester_count
        matrix.append(matrix_row)

    matrix = np.array(matrix)

    _, col_indices = linear_sum_assignment(matrix)

    teams = [[] for i in range(len(projects))]
    for i, col_index in enumerate(col_indices):
        proj_index = int(int(col_index) / proj_member_ratio)
        member_name = csv_rows[i]['Name']
        teams[proj_index].append(member_name)

    # prints out the team assignments
    for i in range(len(projects)):
        print(projects[i], '-', ', '.join(teams[i]))