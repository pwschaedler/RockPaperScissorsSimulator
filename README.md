This is a small script that simulates games of Rock-Paper-Scissors betweens two players, "Scissor-Hands" Stacy and Maya "The Rock".

The initial idea came from two friends playing Rock-Paper-Scissors (RPS), but they would almost always use their respective signature moves. I decided to program a small RPS simulator that took a probability distribution for each player to decide which move they would use. This then extended to me wanting to visualize the simulations somehow. I decided on generating a heatmap where:
 - the X axis represents the probability of "Stacy" (Player 1) choosing scissors
 - the Y axis represents the probability of "Maya" (Player 2) choosing rock
 - the plot colors represent over some number of runs of the game the proportion of games that Maya (P2) won.

For each probability on the axes, the axis value determines the special probability denoted, and the other two probabilities for that player are evenly split. This generates a surface over various probabilities, and each point is run a number of times to determine a probability that Maya will beat Stacy. The program ends by showing this visualization.
