import numpy as np
import matplotlib.pyplot as plt


def GenerateSignal(sigma_v, mu_x, sigma_x):
    x = np.arange(10000)
    H1 = np.random.randint(2,size=len(x))
    
    # Generate the gaussian noise V
    y = np.random.normal(0,sigma_v,len(x))

    # Generate Signal
    y[np.where(H1==1)] += np.random.normal(mu_x,sigma_x,len(x))[np.where(H1==1)]
    return (x,y, H1)

def Detect(signal, threshold):
    return signal > threshold

def PlotROC(mu_x):
    x, y, GroundTruth = GenerateSignal(1, mu_x, 1)
    #plt.plot(x,y)
    plt.show()
    
    tau = np.linspace(-5,5)

    NumH1 = sum(GroundTruth)
    NumH0 = len(GroundTruth)-NumH1

    HitFreq = np.zeros(len(tau))
    FalseAlarmFreq = np.zeros(len(tau))
    for i,t in enumerate(tau):
        test = Detect(y, t)
        HitFreq[i] = sum(test[np.where(GroundTruth==1)])/NumH1
        FalseAlarmFreq[i] = sum(test[np.where(GroundTruth==0)])/NumH0

    # plt.xlabel("tau")
    # plt.plot(tau, HitFreq)
    # plt.plot(tau, FalseAlarmFreq)
    # plt.show()

    plt.suptitle("ROC - " + r'$\mu_x = $' + str(mu_x))
    plt.ylabel("Hit Frequency")
    plt.xlabel("False Alarm Frequency")
    plt.plot(FalseAlarmFreq,HitFreq)
    plt.show()


if __name__ == "__main__":
    # Exercise 1.a)
    # This is a bad detector, because for low false alarm rate it still only has a low hit rate.
    # An ideal detector would have an curve, which rises fast tu an hit rate close to 1 and then levels out.
    PlotROC(1)

    # Exercise 1.b)
    # mu_x of 0 makes the problem more difficult and mu_x of 2 makes it easier.
    PlotROC(0)
    PlotROC(2)

    # Exercise 1.c)
    # This is still a good detector, but for the wrong problem. It detect H1 if it is H0 and H0 if it is H1.
    PlotROC(-3)
