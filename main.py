def determine_age(age):
  if age < 18:
    return "child"
  else:
    return "adult"



def what_time_it_is(hour):
  if hour == 2:
    return "taco time 🌮"
  elif hour == 12: 
    return "peanut butter jelly time"
  else:
    return "nap time"


def blackjack(score):
  if score == 21:
    return "blackjack!"
  elif score > 21:
    return "bust"
  elif score < 17 and score > 21:
    return "Nice Hand!"
  else:
    return "Hit me!"


def get_first(lst):
    print(lst[0]) while lst != []



actual_list = [1,2,3,4,5]
print(get_first(actual_list))

def get_last(lst):
  if len(lst) > 0:
    return lst[-1]
  else:
    return None
print(get_last())