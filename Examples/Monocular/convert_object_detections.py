import json
import numpy
import os


input_file = "/home/mzins/dev/yolov5_bbox/out_detections_yolov5_bulle_1_pretrained.json"
output_folder = "../../data/yolo_bulle_1"

with open(input_file, "r") as fin:
    data = json.load(fin)

for d in data:
    name = os.path.splitext(os.path.basename(d["file_name"]))[0]
    dets = []
    for det in d["detections"]:
        cat = det["category_id"]
        s = det["detection_score"]
        bb = det["bbox"]
        w = bb[2]-bb[0]
        h= bb[3]-bb[1]
        out = [cat, bb[0], bb[1], w, h, s]
        dets.append(out)
    with open(os.path.join(output_folder, name + ".txt"), "w") as fout:
        for d in dets:
            fout.write("%d %d %d %d %d %f\n" % (d[0], d[1], d[2], d[3], d[4], d[5]))


