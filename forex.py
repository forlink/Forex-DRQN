import numpy as np

class Forex:
  def __init__(
    self,
    PriceMap,
    count,
  ):
    self.PriceMap = PriceMap
    self.PriceArr = None
    self.PricePtr = 0

    self.date = ''
    self.count = count

    self.featureLen = 0

  def setDate(self, date):
    self.date = date

    self.PriceArr = self.PriceMap[date]
    self.PricePtr = len(self.PriceArr) - 1
    self.featureLen = self.count * (len(self.PriceArr[0]) - 2)

  def getTime(self):
    # number time is at last column
    startTime = int(self.PriceArr[-1, -1]) + 5 * 60 * 1000 * self.count
    endTime = int(startTime + 5 * 86400 * 1000) # number
    return startTime, endTime

  def getPrice(self, time):
    while self.PricePtr >= 0 and time >= self.PriceArr[self.PricePtr, -1]:
      self.PricePtr -= 1

    self.PricePtr += 1

    observation = \
      np.reshape(self.PriceArr[self.PricePtr + 1 : self.PricePtr + self.count + 1, 0:-2],
                 self.featureLen)

    price = self.PriceArr[self.PricePtr, 0]

    return price, observation
