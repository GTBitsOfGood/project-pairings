A useful Python script for matching Bits of Good
developers together with their project teams.

## The algorithm

When framed as an [assignment problem](https://en.wikipedia.org/wiki/Assignment_problem), the problem of matching together developers with their project teams becomes rather trivial.

Each project and developer is defined as a node on a weighted bipartite graph, where
the weight of the edges between project and developer nodes is equivalent to the rank that the developer assigned to that project, multiplied by the number of semesters that they have been in Bits of Good. For example, if John has been a part of Bits of Good for `3` semesters, and ranks the Mapscout project as his *second* choice, then the weight of the edge between the John & Mapscout nodes is calculated as follows:

```
weight = [rank] * [# semesters] = 2 * 3 = 6
```

The graph is then constructed as a *square* cost matrix, per the requirements of the [linear sum assignment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html) function provided by the SciPy library. Each project and developer node is given an index, such that an entry in the matrix at column `i` and row `j` is the weight of the edge between the *ith* project and *jth* developer.

In order to construct a *square* cost matrix when there are more developers than project teams, the algorithm follows "Approach 1" described in [this StackOverflow thread](https://stackoverflow.com/questions/48108496/hungarian-algorithm-multiple-jobs-per-worker) such that each project node is duplicated `n` times, where `n` is the multiple of the `m` projects that equals the number of developers `p`:

```
m * n = p
```

**NOTE:** In the event that there is no multiple of `m` that yields `p`, fake developers can be added to the CSV with `-1` semesters in Bits of Good, such that the number of developer nodes `p` becomes a multiple of `m` without significantly disrupting the result. An example of this can be found in the provided [example.csv](/example.csv) file.

Finally, the linear sum assignment function yields a set of unique indexes that point to each of the duplicated project nodes. Duplicate project nodes are combined together again into one, and the developers are printed out in a list next to each project. Voila! You have taken care of 70% of the work needed to match together developers with their project teams.

## Setup & operation

To set up the script, you must provide a properly formatted CSV file that matches the general layout of the provided [example.csv](/example.csv). Then, edit the following variables in the script:

- `csv_filename`: The file name of your CSV.
- `csv_newline`: The newline characters of your CSV.
- `projects`: A list of the projects that you are matching developers with.

With the CSV & script properly set up, you just need to run the script with:
```
python pair.py
```

## License

This repository is licensed under the [MIT License](/LICENSE.txt).