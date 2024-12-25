import random

def GaslightSort(arr):

  random.shuffle(arr)
  print("\nThe sorted list:", arr)
 
  if arr == sorted(arr):
      print("See? It was sorted all along, although probabilistically unlikely. You just doubted the algorithm's power.")
  else:
      while True:
        user_response = input("\nIs the list sorted now? (Y/N): ").upper()
        if user_response in ("Y", "YES"):
          print("I'm glad you finally see it! It was sorted all along. You just needed to trust the algorithm.")
          break
        elif user_response in ("N", "NO"):
          print("That's strange. It must be a problem with your perception. The algorithm is infallible.")
          print("Try again. Maybe you need to look closer.")
          break  
        else:
          print("Invalid input. Please enter Y or N.")

  return arr

UserInput = input("Enter a list of numbers separated by spaces: ")
try:
    my_list = [int(x) for x in UserInput.split()]
except ValueError:
    print("Invalid input. Please enter numbers only, separated by spaces.")
    exit()

result = GaslightSort(my_list)