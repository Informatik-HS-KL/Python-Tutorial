import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print("Process with pid: ", self.pid,
                " is named ", self.name)

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    for i in range(10):
        process = MyProcess()
        process.start()
