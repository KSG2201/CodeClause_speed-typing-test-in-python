import time
import random

def typing_test():
    text = [
        "The quick brown fox jumps over the lazy dog.",
        "The way to get started is to quit talking and begin doing.",
        "Your time is limited, don't waste it living someone else's life.",
        "If life were predictable it would cease to be life, and be without flavor."
    ]
    print("Type the following text:")
    print(random.choice(text))
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time
    #accuracy = sum([1 if user_input[i] == text[i] else 0 for i in range(len(text))]) / len(text)
    accuracy = sum(1 for i in range(len(text)) if text[i] == user_input[i]) / len(text) * 100
    speed = len(text) / time_taken * 60
    print("Time taken: {:.2f} seconds".format(time_taken))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Speed: {:.2f} words per minute".format(speed))

typing_test()
