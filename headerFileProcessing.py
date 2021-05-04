
class headerFileProcessing(object):
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.headerFileName = None
        
	#get time data
    def readDays(self, fileName):
        if not(self.isValid(fileName)):
            showError()
			return 0
        file1 = open(fileName, 'r') 
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
            #print("Line{}: {}".format(count, line.strip())) 
            if 'displacement (mm)' in line:
                tmp=line.split(' ')
                tmp_day=float(tmp[-1])
    #            print(np.rint(tmp_day))
                x.append(np.rint(tmp_day))
        file1.close()
        days=np.array(x)
        days=days.reshape((-1, 1))
        return days
	def showError():
		print("Cannot open file")
		#msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        #msg.setText("Error opening file!")
        #msg.setInformativeText('Cannot open gamma header file')
        #msg.setWindowTitle("Error")
        #msg.exec_()
