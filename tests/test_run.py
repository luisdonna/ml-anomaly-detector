"""Check pipeline registration without running training or accessing local data."""

from ml_anomaly_detector.pipeline_registry import register_pipelines


def test_default_pipeline_is_training_pipeline():
    pipelines = register_pipelines()

    assert {"__default__", "training", "inference", "monitoring"} <= pipelines.keys()
    assert pipelines["training"].nodes
    assert pipelines["__default__"].nodes == pipelines["training"].nodes
