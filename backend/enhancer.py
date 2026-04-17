import os

def enhance_video(input_video):
    output_video = "outputs/enhanced.mp4"

    os.system(
        f"ffmpeg -i {input_video} -vf eq=contrast=1.2:brightness=0.05:saturation=1.3 {output_video}"
    )

    return output_video
