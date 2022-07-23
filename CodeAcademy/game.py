class Loop:
    def __init__(self):
        self.running = True

    def mainloop(self):
        xcount = 0
        print "Starting"
        while self.running:
            while xcount < 100:
                print "Running (" + str(xcount) + ")"
                xcount += 1
            if xcount == 100:
                self.running = False
        print "Finished"

if __name__ == '__main__':
    print "Starting"
    g = Loop()
    g.mainloop()
    print "Finished"
