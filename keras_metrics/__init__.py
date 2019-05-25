import keras
from .average_precision_at_k import average_precision_at_k
from .accuracy import accuracy
from .auprc import auprc
from .auroc import auroc
from .false_negatives import false_negatives
from .false_positives import false_positives
from .false_negatives_at_thresholds import false_negatives_at_thresholds
from .false_positives_at_thresholds import false_positives_at_thresholds
from .mean_absolute_error import mean_absolute_error
from .mean_cosine_distance import mean_cosine_distance
from .mean_iou import mean_iou
from .mean_per_class_accuracy import mean_per_class_accuracy
from .mean_relative_error import mean_relative_error
from .mean_squared_error import mean_squared_error
from .precision import precision
from .precision_at_k import precision_at_k
from .precision_at_thresholds import precision_at_thresholds
from .recall import recall
from .recall_at_k import recall_at_k
from .recall_at_thresholds import recall_at_thresholds
from .root_mean_squared_error import root_mean_squared_error
from .sensitivity_at_specificity import sensitivity_at_specificity
from .specificity_at_sensitivity import specificity_at_sensitivity
from .true_negatives import true_negatives
from .true_negatives_at_thresholds import true_negatives_at_thresholds
from .true_positives import true_positives
from .true_positives_at_thresholds import true_positives_at_thresholds

non_parametric_metrics = [
    accuracy,
    auprc,
    auroc,
    false_negatives,
    false_positives,
    mean_absolute_error,
    mean_squared_error,
    precision,
    recall,
    root_mean_squared_error,
    true_negatives,
    true_positives
]

non_parametric_metrics_names = {m.__name__:m for m in non_parametric_metrics}

parametric_metrics = [
    average_precision_at_k,
    false_negatives_at_thresholds,
    false_positives_at_thresholds,
    mean_cosine_distance,
    mean_iou,
    mean_per_class_accuracy,
    mean_relative_error,
    precision_at_k,
    precision_at_thresholds,
    recall_at_k,
    recall_at_thresholds,
    sensitivity_at_specificity,
    specificity_at_sensitivity,
    true_negatives_at_thresholds,
    true_positives_at_thresholds
]

old_get = keras.metrics.get
def get(identifier):
    global non_parametric_metrics_names
    if identifier in non_parametric_metrics_names:
        return non_parametric_metrics_names[identifier]
    return old_get(identifier)

keras.metrics.get = get

metrics = non_parametric_metrics + parametric_metrics

__all__ = ["metrics", "non_parametric_metrics", "parametric_metrics"] + [m.__name__ for m in metrics]
