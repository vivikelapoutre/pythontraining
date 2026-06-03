import sys

def FunctionThatDoesStuffWithTwoVariables(variable1, variable2):
    return variable1 + variable2

def FUNCTIONDOINGOTHERSTUFFWITHVARIABLES(variable1, variable2, variable3):                                                                                                                                                                                                                                                                                             # heb je deze comment gevonden?
    return variable1 * variable2

def the_best_function(first_variable, second_variable):
  """
  This is the best function because reasons. We are going to divide one of the variables by the other. So it's important to check if it's zero. In that case, we want to replace the result by 0.
  """
  if first_variable == 0:
      return second_variable / (1)
  return second_variable / first_variable















































def FunctionThatCan_do_everything(a, b, c, d, e = 8, f = 11):
    # initialize variable with False
    number = False
    # check if a is above 10
    if a > 10:
        # loop over all elements in b
        for g in b:
            # add f to g and assign to c
            c = g + d
        # addign true if c over 5
        if c > 5: number = True
    # if a is not above 10, go here
    elif a < 10:
        # check for true
        if number == True:
            # use the first element of b
            c = b [0]
        else:
            # in other cases, take the last element of b
            c = b [-1]
    
    return None
