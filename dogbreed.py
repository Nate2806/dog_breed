class dog:
    animal="Dog"
    def __init__(self,colour,breed):
        self.colour=colour
        self.breed=breed

dog1=dog("Black","Rotweiler")
dog2=dog("Golden","Golden Retriever")
print("Animal:{0},The colour of the first dog is {1} and its breed is {2}, The colour of the second dog is {3} and its breed is {4}".format(dog1.animal,dog1.colour,dog1.breed,dog2.colour,dog2.breed))