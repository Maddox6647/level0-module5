"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    window = Tk()
    window.withdraw()
    happy_level = 10
    print(happy_level)
    k = simpledialog.askstring(title='g', prompt='what pet? a crocodile, a blue whale, or a kraken')
    if k == 'crocodile':
        animal_pet = simpledialog.askstring(title='hi', prompt='give it lots of fish and other food, also lots of WATER!!!')
        if animal_pet == 'ok':
            happy_level = 12
            print(happy_level)
        elif animal_pet == 'no':
            happy_level = 0
            print(happy_level)
            messagebox.showinfo(title='bobby', message='THE CROC EATS U INSTEAD OF FISHIES')
    elif k == 'kraken':
        animals_suc = simpledialog.askstring(title='g', prompt='feed it fish and then watch it destroy everything')
