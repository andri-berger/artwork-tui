# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Andri Berger
#
# This file is part of layout-tui.
#
# layout-tui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import numpy as np
import vtracer
import cv2


def clamp(value, max_val, min_val):
    value = max(0, min(value, 100))
    range = max_val - min_val
    ranges = value / 100.0
    total = range * ranges
    return total + min_val

def tracer(args, args0):
    svg = vtracer.convert_raw_image_to_svg(args,
        filter_speckle=int(clamp(args0['setting_0'], 0, 50)),
        layer_difference=int(clamp(args0['setting_1'], 1, 31)) | 1,
        length_threshold=float(clamp(args0['setting_2'], 1, 100)),
        splice_threshold=int(clamp(args0['setting_3'], 0, 20)),
        corner_threshold=int(clamp(args0['setting_4'], 1, 179)),
        path_precision=int(clamp(args0['setting_5'], 1, 10)),
        color_precision=int(clamp(args0['setting_6'], 10, 12)),
        hierarchical=args0['setting_7'],
        mode=args0['setting_8'],
        img_format='png')

    return svg.encode('utf-8')


def opencv(args, args0):
    setting = args0['setting']
    setting0 = args0['setting0']
    setting1 = args0['setting1']
    setting2 = args0['setting2']

    img = cv2.imdecode(
        np.frombuffer(args,
        dtype=np.uint8),
        cv2.IMREAD_UNCHANGED)
    rgb = img[:, :, :3]
    alpha = img[:, :, 3]
    ys, xs = np.where(alpha > 0)
    y_min, y_max = ys.min(), ys.max()
    x_min, x_max = xs.min(), xs.max()
    sub_rgb = rgb[y_min:y_max + 1, x_min:x_max + 1]

    if setting == 1:
        enhance = cv2.xphoto
        enhanced = enhance.oilPainting(sub_rgb,
            int(clamp(setting0, 3, 11)) | 1,
            int(clamp(setting1, 1, 5)) | 1)

    elif setting == 2:
        enhanced = cv2.stylization(sub_rgb,
            sigma_s=int(clamp(setting0, 30, 100)),
            sigma_r=float(clamp(setting1, 0.2, 0.7)))

    elif setting == 3:
        enhanced = cv2.detailEnhance(sub_rgb,
            sigma_s=float(clamp(setting0, 5, 100)),
            sigma_r=float(clamp(setting1, 0.1, 0.5)))

    elif setting == 4:
        _, enhanced = cv2.pencilSketch(sub_rgb,
            sigma_s=float(clamp(setting0, 30, 100)),
            sigma_r=float(clamp(setting1, 0.05, 0.3)),
            shade_factor=float(clamp(setting2, 0.02, 0.05)))

    elif setting == 5:
        adaptive_II = int(clamp(setting1, 0, 20))
        adaptive_I = int(clamp(setting0, 3, 51)) | 1
        medianBlur = int(clamp(setting2, 3, 15)) | 1

        gray = cv2.cvtColor(sub_rgb, cv2.COLOR_RGB2GRAY)
        gray_blur = cv2.medianBlur(gray, medianBlur)
        edges = cv2.adaptiveThreshold(
            gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, adaptive_I, adaptive_II)
        color = cv2.bilateralFilter(sub_rgb, 24, 75, 75)
        enhanced = cv2.bitwise_and(color, color, mask=edges)

    rgb[y_min:y_max + 1, x_min:x_max + 1] = enhanced
    b, g, r = cv2.split(rgb)
    processed = cv2.merge([b, g, r, alpha])
    _, encoded_img = cv2.imencode('.png', processed)
    image_bytes = encoded_img.tobytes()

    return image_bytes


import locale

lang, encoding = locale.getdefaultlocale()  # e.g., 'de_CH', 'en_US', 'fr_FR'
if lang and '_' in lang:
    country_code = lang.split('_')[1]



