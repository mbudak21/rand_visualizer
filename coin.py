import matplotlib.pyplot as plt
import random as rnd

def plot_tosses(H, T):

    labels = ['Heads', 'Tails']

    # Plotting
    bars = plt.bar(labels, [H, T], color=['blue', 'red'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, ha='center', va='bottom')


    # Adding details
    plt.xlabel('Coin Toss Outcome')
    plt.ylabel('Number of Occurrences')
    plt.title('Results of ' + str(H+T) + ' Coin Tosses')
    plt.ylim(0, max(H, T)*2 )
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot
    plt.show()

def generate_tosses(n: int, w: int):
    heads = 0
    for _ in range(n):
        if rnd.random() < w:
            heads += 1
    return heads, n - heads


plot_tosses(*generate_tosses(1000000, 0.7))