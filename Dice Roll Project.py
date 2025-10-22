import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# Use relative paths (assuming images are in an "images" folder)
faces = {
    1: Path("C:/Users/taufi/Downloads/inverted-dice-1.png"),
    2: Path("C:/Users/taufi/Downloads/inverted-dice-2.png"),
    3: Path("C:/Users/taufi/Downloads/inverted-dice-3.png"),
    4: Path("C:/Users/taufi/Downloads/inverted-dice-4.png"),
    5: Path("C:/Users/taufi/Downloads/inverted-dice-5.png"),
    6: Path("C:/Users/taufi/Downloads/inverted-dice-6.png")
}

while True:
    choice = input("Roll the dice? (Y/N): ")
    if choice.lower() == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # Load and show images
        img1 = mpimg.imread(faces[die1])
        img2 = mpimg.imread(faces[die2])

        plt.figure(figsize=(4, 2))
        plt.subplot(1, 2, 1)
        plt.imshow(img1)
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(img2)
        plt.axis("off")

        plt.show()
        print(f"You rolled {die1} and {die2}")

    elif choice.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Please input Y or N")
