class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():

    #create Flight
    f = Flight(origin="New York", destination="Paris", duration = 540)

    #change the value of variables
    f.duration += 10

    #print details about Flight
    print(f.origin)
    print(f.destination)
    print(f.duration)

if __name__=="__main__":
    main()
