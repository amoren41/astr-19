
class redpanda:
    def __init__(self, armLength, legLength, eyes, tail, furry):
        self.armLength = armLength
        self.legLength = legLength
        self.eyes = eyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print("this is my favorite animal the red panda")
        print("arm length:", self.armLength)
        print("leg length:", self.legLength)
        print("number of eyes:", self.eyes)
        print("has tail:", self.tail)
        print("is furry:", self.furry)
        print("they stand up to scare off predators ")

def main():
    panda = redpanda(11 , 25, 2, True, True)
    panda.describe()

main()
