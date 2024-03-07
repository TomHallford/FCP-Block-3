import matplotlib.pyplot as plt


def main():
    genetic_data = 'cgtacgttgacgtgcgtacgtgcgaggggtatacgta'
    base_counts = [genetic_data.count(val) for val in 'acgt']
    plt.bar(['A', 'C', 'G', 'T'], base_counts, color=["red", "green", "yellow", "blue"])
    plt.title("Nucleotide count")
    plt.xlabel("Nucleotide")
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    main()

