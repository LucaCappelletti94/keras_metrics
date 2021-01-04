import tensorflow as tf
from .binary_metric import BinaryMetric
from tensorflow.keras.backend import epsilon

class PrevalenceThreshold(BinaryMetric):
    def _custom_metric(self):
        tpr = self.tp / (self.tp + self.fn + epsilon())
        tnr = self.tn / (self.tn + self.fp + epsilon())
        return (tf.math.sqrt(tpr*(1 - tnr)) + tnr - 1) / (tpr + tnr - 1 + epsilon())