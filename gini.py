# Needed for the control of the arrays
import numpy as np


# Dummy values to test the code
##################################################
values = np.array([[1, 1, 1, 0, 0, 0, 0, 1, 0],
                   [1, 1, 0, 0, 1, 1, 0, 0, 1],
                   [1, 1, 0, 1, 0, 0, 0, 1, 0]])

char1 = np.array(values[0])
char2 = np.array(values[1])
char_class = np.array(values[2])
##################################################

#The function that work for the main part
##################################################
def count_true_values(x, c):
    array = np.where(c == 1)[0]
    valsOf1 = np.where(x[array] == 1)[0]
    return valsOf1

def count_false_values(c,x):
    array = np.where(x == 1)[0]
    valsOf1 = np.where(c[array] == 0)[0]
    return valsOf1

##################################################
#   The main part of the code, proceed with caution
##################################################
def gini(characteristic, x):
    #GINI(CLASS) is this first part
    GINI_x = [0,0]
    GINI_x[0] = len(count_true_values(x, x))/len(x)
    GINI_x[1] = 1-GINI_x[0]
    GINI_x_result = 1-(np.power(GINI_x[0], 2)+np.power(GINI_x[1], 2))
    #GINI(CHAR=TRUE) is this part
    GINI_true_c = [0,0]
    GINI_true_c[0] = len(count_true_values(characteristic, x))/np.count_nonzero(characteristic, axis=0)
    GINI_true_c[1] = 1-GINI_true_c[0]
    GINI_true_c_result = 1-(np.power(GINI_true_c[0], 2)+np.power(GINI_true_c[1], 2))
    #GINI(CHAR=FALSE) is this part
    GINI_false_c = [0,0]
    GINI_false_c[0] = len(count_false_values(characteristic, x))/(len(x)-np.count_nonzero(characteristic, axis=0))
    GINI_false_c[1] = 1-GINI_false_c[0]
    GINI_false_c_result = 1-(np.power(GINI_false_c[0], 2)+np.power(GINI_false_c[1], 2))
    #WEIGHTED AVERAGE at the end
    weighted_average = GINI_x_result - ((len(count_true_values(characteristic, characteristic))/len(characteristic))*GINI_true_c_result + ((len(characteristic)-len(count_true_values(characteristic, characteristic)))/len(characteristic))*GINI_false_c_result)
    # GINIGain =
    return weighted_average

# print(gini(char1, char_class))
# print(gini(np.array([0, 1, 1 , 1, 1, 0]),np.array([0, 0, 1 , 0, 0, 1]) ))
