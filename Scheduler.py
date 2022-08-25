import threading, time, Webpage

class Scheduler:
    def __init__(self):
        self.thread = None
        self.stopRequested = False

    # Start the scheduler.
    def start(self):
        if self.thread == None:
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
        else:
            print("Unable to start scheduler. A running instance already exists.")
        print("Thread started")

    # Run the scheduler. This should ONLY be called by the start method.
    def run(self):
        
        test = Webpage.Webpage("https://sitescouttest.netlify.app/sitescouttest.html")

        while not self.stopRequested:
            print(test.getContentFromLineAndHtmlTag(test.getLinesFromContent("someCoolData")[0], "someCoolData"))
            

    # Stop the scheduler. This merely requests a stop, so the scheduler will finish its current iteration before stopping.
    def stop(self):
        self.stopRequested = True
