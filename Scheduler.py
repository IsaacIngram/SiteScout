import threading, time, Webpage


class Scheduler:
    def __init__(self):
        self.thread = None
        self.stopRequested = False

    def start(self):
        """
        Start the scheduler
        :return:
        """
        if self.thread is None:
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
        else:
            print("Unable to start scheduler. A running instance already exists.")
        print("Thread started")

    def run(self):
        """
        Run the scheduler. This should ONLY be called by the start function.
        :return:
        """
        
        test = Webpage.Webpage("https://sitescouttest.netlify.app/sitescouttest.html")

        while not self.stopRequested:
            # CODE TO RUN HERE
            pass

    def stop(self):
        """
        Stop the scheduler. THis merely requests a stop, so the scheduler will finish its current iteration before
        stopping.
        :return:
        """
        self.stopRequested = True
