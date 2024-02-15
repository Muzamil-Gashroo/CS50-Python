

def main():

   get = input("whats time:")
   realtime = convert(get)

   if realtime >=7 and realtime <=10:
    print("Breakfast time")
   elif realtime >= 12 and realtime <= 13:
    print("Lunch time")
   elif realtime >=17 and realtime <=24:
    print("Dinner time")

def convert(time):
   hours, min = time.split(":")
   return float(hours) + float(min)/60

if __name__ == "__main__":
    main()


