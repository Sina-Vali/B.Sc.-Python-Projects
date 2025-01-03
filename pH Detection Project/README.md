# Problem Statement
In this section, the goal is to write a program that predicts the pH of a substance based on the color of an indicator applied to it.

The program works as follows:
1. The user provides an integer $k$ and a color as input.
2. The program traverses the dataset to find the $k$ closest colors based on distance.
3. It then predicts the pH by calculating the average pH of these $k$ closest colors.

## Input:
- A csv file containing the pH and (R, G, B) color of 653 different samples;
- 4 space-separated integers: R G B k.

## Output:
Predicted pH.
