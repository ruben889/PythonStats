# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Press the green button in the gutter to run the script.
def getColor(GDPzScore):
   total = int((255*GDPzScore)/3)
   red = 0
   blue = 0
   #either red or blue because its closer to the mean
   #but the mean value should be purple
   # thinking of -255 as a rep of red but it shoudl be 255,0,0
   # thinking of 255 as a rep of blue iit should be 0,0,255
   if total >= 0:
      blue = 255
      red = (255 - abs(total))
   if total < 0:
      red = 255
      blue = (255-abs(total))
   color = '#%02x%02x%02x' % (red,0,blue)
   return color




if __name__ == '__main__':
   init = pd.read_csv(r'C:\Users\icand\Desktop\course Notes\test.csv')
   data = init.sort_values(by="GDP")
   poorcountries = data[data['GDP'] < .5]
   richcountries = data[data['GDP'] > .5]

   GDPmean = np.mean(data['GDP'])
   print(GDPmean)
   GDPdeviation = np.std(data['GDP'])
   print(GDPdeviation)
   # armenia rgb
   armeniaZ = (poorcountries.iloc[0]['GDP'] - GDPmean) / GDPdeviation
   print(getColor(armeniaZ))

   zscores =[]
   for x in data['GDP']:
      zscores.append((x-GDPmean)/GDPdeviation)

   colors = [getColor(z) for z in zscores]
   plt.scatter(data['GDP'],data['happyScore'], c=colors)

   for k,row in data.iterrows():
      plt.text(row['GDP'],
               row['happyScore'],
               row['country'])


   for r, b in data.iterrows():
      print(b["country"])
      print(b['GDP'])

   plt.show()

   # grey to green color scale based on gdp
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
