class car:
    wheel=4 #class attr
    def soundsystem(self,m):
        self.music=m

bmw=car()
bmw.soundsystem('Harman')
print(bmw.music) #instance