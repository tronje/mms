import numpy as np
import matplotlib.pyplot as plt


def GenerateSignal(sigma_v, mu_x, sigma_x):
    x = np.arange(10000)
    H1 = np.random.randint(2,size=len(x))

    # Generate the gaussian noise V
    y = np.random.normal(0,sigma_v,len(x))

    # Generate Signal
    y[H1] += np.random.normal(mu_x,sigma_x,len(x))
    return (x,y, H1)

def Detect(signal, threshold):
    return signal > threshold

def PlotROC(mu_x):
    x, y, GroundTruth = GenerateSignal(1, mu_x, 1)
    tau = np.linspace(-5,5)

    NumH1 = sum(GroundTruth)
    NumH0 = len(GroundTruth)-NumH1

    HitFreq = np.zeros(len(tau))
    FalseAlarmFreq = np.zeros(len(tau))
    for i,t in enumerate(tau):
        test = Detect(y, t)
        HitFreq[i] = sum(test[GroundTruth==1])/NumH1
        FalseAlarmFreq[i] = sum(test[GroundTruth==0])/NumH0

    # plt.xlabel("tau")
    # plt.plot(tau, HitFreq)
    # plt.plot(tau, FalseAlarmFreq)
    # plt.show()

    plt.suptitle("ROC - " + r'$\mu_x = $' + str(mu_x))
    plt.xlabel("Hit Frequency")
    plt.ylabel("False Alarm Frequency")
    plt.plot(HitFreq, FalseAlarmFreq)
    plt.show()


if __name__ == "__main__":
    # Exercise 1.a)
    PlotROC(1)

    # Exercise 1.b)
    PlotROC(0)
    PlotROC(2)

    # Exercise 1.c)
    PlotROC(-3)
