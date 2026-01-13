# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.chanell_no= ''
      self.channels_list=[]
      self.volume=0
   
   def v_increase(self):
      if self.volume==10:
         return 'no'
      else:
         self.volume+=1

   def v_decrease(self):
      if self.volume==0:
         return 'no'
      else:
         self.volume-=1

   def turn_off(self):
      self.is_on= False

   def turn_on(self):
      self.is_on=True

   def set_channels(self,channels_list):
      channels_list= channels_list.split(',')
      for i in channels_list:
         self.channels_list.append(i)

   def show_channels(self):
      n=1
      for i in self.channels_list:
         print(f'{n}. {i}')
         n+=1

   def switch_ch(self,no):
      self.chanell_no=no
   
   def show_status(self):
      if self.is_on:
         print('The TV is on, channel', self.chanell_no, self.channels_list[self.chanell_no-1], 'volume is', self.volume)
      else:
         print('The TV is off')

one=TV()
one.set_channels('tvp1,tvp2,polsat,tvn')
one.switch_ch(2)
one.turn_on()
one.v_decrease()
one.v_decrease()    

one.show_status()
