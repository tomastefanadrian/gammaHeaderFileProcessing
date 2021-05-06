class headerFileProcessing(object):
    def __init__( self, fileName ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.headerFileName = fileName
        self.days=None
        self.dates=[]
        self.referenceDate=[]
        self.referencePointCoordinates=[]
        
    #get time data
    
    def readData(self):
        try:
            file1 = open(self.headerFileName, 'r') 
            count = 0
            x=[]
            while True: 
                count += 1
                # Get next line from file 
                line = file1.readline() 
                # if line is empty 
                # end of file is reached 
                if not line: 
                    break
  
                if 'displacement (mm)' in line:
                    tmp=line.split(' ')
                    tmp[:] = [x for x in tmp if x]
                    tmp_day=int(float(tmp[-1]))
                    x.append(tmp_day)
                    indexDate = [i for i in range(len(tmp)) if tmp[i] == 'date:']
                    indexDate=indexDate[0]
                    self.dates.append(tmp[indexDate+1])
                    self.dates.append(tmp[indexDate+2])
                    self.dates.append(tmp[indexDate+3])
                    if (tmp_day==0):
                        self.referenceDate.append(tmp[indexDate+1])
                        self.referenceDate.append(tmp[indexDate+2])
                        self.referenceDate.append(tmp[indexDate+3])
                    # indexDate=indexDate+1
                    # dateCount=1
                    # while(dateCount<3):
                    #     if tmp[indexDate].isnumeric():
                    #         self.dates.append(tmp[indexDate])
                    #         if (tmp_day==0):
                    #             self.referenceDate.append(tmp[indexDate])
                    #         dateCount=dateCount+1
                    #     indexDate=indexDate+1
                        
                if 'reference point easting, northing (m):' in line:
                    tmp=line.split(' ')
                    for i in tmp:
                        try:
                            self.referencePointCoordinates.append(float(i))
                        except:
                            pass
                                
            file1.close()
            self.days=x

        except Exception as e:
            print(e)
            print("Error reading data from file .... or something!")
            
    def getDays(self):
        return self.days
    
    def getDates(self):
        return self.dates
    
    def getReferenceDate(self):
        return self.referenceDate
    
    def getReferencePoint(self):
        return self.referencePointCoordinates
    
    
    def showError(self):
        print("Cannot open file")
        #msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        #msg.setText("Error opening file!")
        #msg.setInformativeText('Cannot open gamma header file')
        #msg.setWindowTitle("Error")
        #msg.exec_()


