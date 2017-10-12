import colorsys as _colorsys
import numpy as _np
import matplotlib.pylab as _plt

class Color(object):
    def __init__(self, color, model='hsv', color_scale = 1):
        if type(color).__name__ in ['list', 'tuple']:
            color = _np.array(color)

        color = color.astype(_np.float)
        color /= color_scale

        if len(color) == 4:
            color, alpha = color[:-1], color[-1]
        else:
            alpha = 1

        if model == 'rgb':
            color = _np.array(_colorsys.rgb_to_hsv(*color))

        if model == 'hls':
            rgb = _colorsys.hls_to_rgb(*color)
            color = _np.array(_colorsys.rgb_to_hsv(*rgb))

        self._hsv = color
        self.alpha = alpha

    @property
    def rgb(self):
        #         self.model = 'rgb'
        rgb = _np.array(_colorsys.hsv_to_rgb(*self.hsv))
        return rgb

    @property
    def rgba(self):
        #         self.model = 'rgb'
        rgb = _np.array(_colorsys.hsv_to_rgb(*self.hsv))
        rgba = _np.zeros(4)
        rgba[:-1] = rgb
        rgba[-1] = self.alpha
        return rgba

    @property
    def brightness(self):
        return self._hsv[2]

    @brightness.setter
    def brightness(self, value):
        assert (0 <= value <= 1)
        self._hsv[2] = value

    @property
    def hsv(self):
        return self._hsv

    @property
    def hue(self):
        return self._hsv[0]

    @hue.setter
    def hue(self, value):
        #         assert(0<= value <= 1)
        self._hsv[0] = value

    @property
    def saturation(self):
        return self._hsv[1]

    @saturation.setter
    def saturation(self, value):
        assert (0 <= value <= 1)
        self._hsv[1] = value

    def show(self, alpha=True):
        f, a = _plt.subplots()
        a.axis('off')
        if alpha:
            f.set_facecolor(self.rgba)
        else:
            f.set_facecolor(self.rgb)