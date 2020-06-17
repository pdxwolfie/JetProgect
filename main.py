class Jet:

  def __init__(self,jetEngineSizeInput,jetbodycolorInput,wingspansizeInput,jetframeTypeInput,isjet):
    self.jetEngine=jetEngineSizeInput
    self.jetbodycolor=jetbodycolorInput
    self.jetWingspan=wingspansizeInput
    self.jetframe=jetframeTypeInput
    self.jet=isjet


  def fly(self):
    print("Feel that wind!")

  def speedup(self):
    print("FASTER! FASTER")

  def falling(self):
    print("WE ARE ALL GOING TO DIE!!!")

  def turn(self,turnDirection):
   print("you're turning "+turnDirection)



print("Hello there old chap! and welcome to Nicholas's privet jet company.")
print("What would you like you're Jet engine size to be?")
jetEngineSizeInput=input()

print("Now it's time to choose your jets color.")
jetbodycolorInput=input()
print("Now the wingspan size.")
wingspansizeInput=input()
print("already to the last one WOW, ok now how would you like your jet's frame to be like?")
jetframeTypeInput=input()
print("Here is your order!")



NicholasJet=Jet(jetEngineSizeInput,jetbodycolorInput,wingspansizeInput,jetframeTypeInput,True) 