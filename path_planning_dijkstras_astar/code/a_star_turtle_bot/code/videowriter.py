import cv2
import numpy as np


def write_video(num_images, sample_num):
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out_done = False
    for i in range(1, num_images):
        if i % sample_num == 0:
            frame = cv2.imread('./media/frame'+str(i)+'.png')
            print(i, './media/frame'+str(i)+'.png', frame.shape)
            if not out_done:
                out = cv2.VideoWriter("./media/astar_nonholonomic_video_3.mp4", fourcc, 5.0, (frame.shape[1], frame.shape[0]))
                out_done = True
            out.write(frame)

    frame = cv2.imread('./media/frame.png')
    out.write(frame)
    out.release()


if __name__ == '__main__':
    write_video(1951, 100)

