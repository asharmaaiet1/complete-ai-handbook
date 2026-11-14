# Discrete Mathematics and Graph Theory

## Learning objectives

By the end of this guide, you should be able to:

- Describe sets, logic, and counting as tools for reasoning about distinct choices.
- Represent connected objects as nodes and edges in a graph.
- Explain how graph search can find reachable places or states.

**Difficulty:** Beginner to intermediate  
**Prerequisites:** Mathematical foundations; no calculus required for the introductory topics.

## Overview

Discrete mathematics studies countable objects and the rules connecting them. Graph theory focuses on networks of objects and relationships. These ideas support search, reasoning, data structures, and models that work with connected entities.

## Topics Covered

### Discrete reasoning

- Sets, subsets, unions, intersections, and Cartesian products.
- Propositions, logical operators, implications, and quantifiers.
- Basic proof ideas: direct reasoning, contradiction, and induction (for reading arguments, not as a prerequisite for applied ML).
- Counting with permutations, combinations, and the multiplication rule.

### Graphs and trees

- Vertices and edges; directed, undirected, weighted, and bipartite graphs.
- Paths, cycles, connected components, and degree.
- Trees, search trees, and basic traversal ideas.
- Adjacency lists and matrices as ways to store a graph.

### Growth and complexity

- Sequences and recurrence relations at an intuitive level.
- Big-O notation as a description of how resource use grows with input size.

## Learn the idea

Discrete math deals with separate, countable choices, such as a set of labels or a collection of links. Logic gives rules for statements that can be true or false. Counting helps estimate how many possibilities a program may need to examine.

A graph is a set of nodes and connections called edges. A road map can be modeled with places as nodes and roads as edges. If roads have different lengths, the edges can carry weights. A path is a sequence of connected edges. Searching a graph means visiting nodes according to a rule, such as exploring nearby nodes before farther ones.

## Example in AI: finding a route through connected places

A route planner can represent locations as nodes and roads as edges. Suppose its small map has roads `A—B`, `A—C`, and `B—D`. From A, B and C are one road away; D can be reached in two roads through B. A graph search can find which places are reachable and, with suitable edge weights, compare routes. Graphs are useful whenever an AI task involves relationships or paths, such as a map, a network of linked pages, or steps between game states.

## Try it

In the example, how many roads are in the path from A to D?

??? success "Check your answer"
    Two: `A—B` and `B—D`.

## AI Applications

Graphs represent roads, social networks, knowledge graphs, and dependencies between variables. Search algorithms explore graphs of possible states. Decision trees and computation graphs organize branching or connected operations. Discrete reasoning also underlies constraint solving and symbolic AI.

## Recommended References

- [MIT OpenCourseWare 6.042J: Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/) — free course on logic, proof, counting, and graphs; more rigorous than the overview here.
- [MIT Open Learning Library: Mathematics for Computer Science](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/) — online course version with structured materials.
- [NetworkX tutorial](https://networkx.org/documentation/stable/tutorial.html) — practical graph representation and operations in Python; pair with a math resource for theory.

---

[← Previous: Information Theory](07-information-theory.md) · [Next: Numerical Methods →](09-numerical-methods.md)
