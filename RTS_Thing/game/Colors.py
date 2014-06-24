class Colors ():
    RED     = (255, 0, 0)
    GREEN   = (0, 255, 0)
    BLUE    = (0, 0, 255)
    
    @staticmethod
    def getShade (intensity, color):
        if intensity > 1 or intensity < 0:
            print ("ERROR: COLOR INTENSITY OUT OF RANGE")
        else:
            return (color [0] * intensity, 
                    color [1] * intensity, 
                    color [2] * intensity)