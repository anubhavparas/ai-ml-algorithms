import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out_done = False
for i in range(1, 2259):
    if i % 100 == 0:
        frame = cv2.imread('./media/frame'+str(i)+'.png')
        print(i, './media/frame'+str(i)+'.png', frame.shape)
        if not out_done:
            out = cv2.VideoWriter("./media/astar_nonholonomic_video_2.mp4", fourcc, 5.0, (frame.shape[1], frame.shape[0]))
            out_done = True
        out.write(frame)

frame = cv2.imread('./media/frame.png')
out.write(frame)
out.release()
