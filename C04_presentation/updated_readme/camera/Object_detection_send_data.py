import sensor, image, time, os, ml, math, uos, gc
from ulab import numpy as np
import pyb
from machine import LED

usb = pyb.USB_VCP()  # Use USB serial communication

led_red = pyb.LED(1)    # Red LED
led_green = pyb.LED(2)  # Green LED
led_blue = pyb.LED(3)   # Blue LED

def set_led_color(color):
    """Change LED color: 'yellow' (red + green) or 'blue'."""
    led_red.off()
    led_green.off()
    led_blue.off()

    if color == "yellow":
        led_red.on()
        led_green.on()
    elif color == "blue":
        led_blue.on()
    elif color == "green":
        led_green.on()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((240, 240))
sensor.skip_frames(time=2000)

net = None
labels = None
min_confidence = 0.5

try:
    net = ml.Model("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    raise Exception('Failed to load "trained.tflite": ' + str(e))

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception('Failed to load "labels.txt": ' + str(e))

colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
threshold_list = [(math.ceil(min_confidence * 255), 255)]

def fomo_post_process(model, inputs, outputs):
    ob, oh, ow, oc = model.output_shape[0]
    x_scale = inputs[0].roi[2] / ow
    y_scale = inputs[0].roi[3] / oh
    scale = min(x_scale, y_scale)
    x_offset = ((inputs[0].roi[2] - (ow * scale)) / 2) + inputs[0].roi[0]
    y_offset = ((inputs[0].roi[3] - (ow * scale)) / 2) + inputs[0].roi[1]
    l = [[] for _ in range(oc)]

    for i in range(oc):
        img = image.Image(outputs[0][0, :, :, i] * 255)
        blobs = img.find_blobs(threshold_list, x_stride=1, y_stride=1, area_threshold=1, pixels_threshold=1)
        for b in blobs:
            rect = b.rect()
            x, y, w, h = rect
            score = img.get_statistics(thresholds=threshold_list, roi=rect).l_mean() / 255.0
            x = int((x * scale) + x_offset)
            y = int((y * scale) + y_offset)
            w = int(w * scale)
            h = int(h * scale)
            l[i].append((x, y, w, h, score))
    return l

clock = time.clock()

while True:
    time.sleep(2)
    clock.tick()
    img = sensor.snapshot()

    # Run model prediction and post-process
    for i, detection_list in enumerate(net.predict([img], callback=fomo_post_process)):
        if i == 0 or len(detection_list) == 0:
            continue  # Skip background class and empty detections

        for x, y, w, h, score in detection_list:
            center_x = math.floor(x + (w / 2))
            center_y = math.floor(y + (h / 2))
            print(f"x {center_x}\ty {center_y}\tscore {score:.2f}")

            # Draw detection on image (optional for OpenMV IDE view)
            img.draw_circle((center_x, center_y, 12), color=colors[i % len(colors)])

            # ✅ Format the detection data for sending
            detection_data = f"{labels[i]},{center_x},{center_y},{score:.2f}\n"

            # ✅ Change LED color based on detected object
            if labels[i] == "plastic":
                set_led_color("yellow")  # Yellow for plastic
            elif labels[i] == "paper":
                set_led_color("blue")    # Blue for paper
            else:
                set_led_color("off")

            # ✅ Send detection data via USB (Virtual COM)
            usb.write(detection_data)

    if (usb.any()):
        message = usb.readline()
        if(message == b"ready\n"):
            set_led_color("green")
