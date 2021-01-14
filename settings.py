import os
from dotenv import load_dotenv
load_dotenv()

framework = os.getenv("framework")
weights = os.getenv("weights")
size = int(os.getenv("size"))
tiny = os.getenv("tiny") == "True"
model = os.getenv("model")
video = os.getenv("video")
output = os.getenv("output")
output_format = os.getenv("output_format")
iou = float(os.getenv("iou"))
score = float(os.getenv("score"))
dont_show = os.getenv("dont_show") == "True"
