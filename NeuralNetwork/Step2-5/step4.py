### Digits recognition example for ffnet ###

# Training file (data/ocr.dat) contains 68 patterns - first 58
# are used for training and last 10 are used for testing.
# Each pattern contains 64 inputs which define 8x8 bitmap of
# the digit and last 10 numbers are the targets (10 targets for 10 digits).
# Layered network architecture is used here: (64, 10, 10, 10).

from ffnet import ffnet, mlgraph, readdata
from random import randint

# Generate standard layered network architecture and create network
conec = mlgraph((64,10,10,10))
net = ffnet(conec)

# Read data file
print "READING DATA..."
data = readdata( 'data/ocr.dat', delimiter = ' ' )
input =  data[:, :64] #first 64 columns - bitmap definition
target = data[:, 64:] #the rest - 10 columns for 10 digits

# Train network with scipy tnc optimizer - 58 lines used for training
print "TRAINING NETWORK..."
net.train_tnc(input[:58], target[:58], maxfun = 2000, messages=1)

# chc Step4 Homework - start -

for i in range(58,68):
    for j in range(0, 64):
        r = randint(1,100)
        #if(r<=0): #0%
        #if(r<=1): #1%
        #if(r<=5): #5%
        if(r<=10):  #10%
            if(input[i][j] == 1):
                input[i][j] = 0
            else:
                input[i][j] = 1
                
# chc Step4 Homework - end -

# Test network - remaining 10 lines used for testing
print
print "TESTING NETWORK..."
output, regression = net.test(input[58:], target[58:], iprint = 2)

# Test Accuracy 
count = 0 
list = []
correct_output=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    max_index=0
    max = -1 
    for j in range(0,10):
        if(output[i][j] > max) :
            max_index=j
            max = output[i][j]
    if(target[58+i][max_index]==1) :
        correct_output[i] = 1
        print i+1,"th sample : Success"
        count=count+1
    else :
        print i+1,"th sample : Fail"
        list.append(i) 
    
print "Test Accuracy=",(count/10.0)*100.0
############################################################
# Make a plot of a chosen digit along with the network guess
try:
    from pylab import *
    from random import randint

    i=0
    if((count/10.0)*100.0 == 100):
        digitpat = randint(58, 67) #Choose testing pattern to plot
    else :
        while(1):
            i=randint(0, 9)
            if(correct_output[i] == 0):
                digitpat = i+58
                break       

    subplot(211)
    imshow(input[digitpat].reshape(8,8), interpolation = 'nearest')

    subplot(212)
    N = 10  # number of digits / network outputs
    ind = arange(N)   # the x locations for the groups
    width = 0.35       # the width of the bars
    bar(ind, net(input[digitpat]), width, color='b') #make a plot
    xticks(ind+width/2., ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
    xlim(-width,N-width)
    axhline(linewidth=1, color='black')
    title("Trained network (64-10-10-10) guesses a digit above...")
    xlabel("Digit")
    ylabel("Network outputs")

    show()
except ImportError, e:
    print "Cannot make plots. For plotting install matplotlib.\n%s" % e
