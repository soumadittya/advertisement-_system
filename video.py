import time

class Video:
    def __init__(self, link, duration):
        self.link = link
        self.duration = duration

    def play(self):
        import numpy as np
        import cv2

        # Open a sample video available in sample-videos
        vcap = cv2.VideoCapture(self.link)
        # if not vcap.isOpened():
        #    print "File Cannot be Opened"

        start_time = time.time()

        while (int(time.time() - start_time) < self.duration):
            # Capture frame-by-frame
            ret, frame = vcap.read()
            # print cap.isOpened(), ret
            if frame is not None:
                # Display the resulting frame
                cv2.imshow('frame', frame)
                # Press q to close the video windows before it ends if you want
                cv2.waitKey(30)




            else:
                print("Frame is None")
                break

        # When everything done, release the capture
        vcap.release()
        cv2.destroyAllWindows()
        print("Video stop")

if __name__ == '__main__':
    obj = Video('http://slike.s.llnwi.net/vi/1x/w1/1xw15bwoz9/4e37bddca0_F30_480p_900.mp4', 5)
    obj.play()
