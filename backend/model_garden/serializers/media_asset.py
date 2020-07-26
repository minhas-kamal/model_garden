from rest_framework import serializers

from model_garden.constants import LabelingTaskStatus
from model_garden.models import MediaAsset


class MediaAssetSerializer(serializers.ModelSerializer):
  dataset_id = serializers.SerializerMethodField()
  remote_label_path = serializers.SerializerMethodField()

  class Meta:
    model = MediaAsset
    fields = (
      'dataset_id',
      'filename',
      'remote_path',
      'remote_label_path',
    )

  def get_dataset_id(self, obj: MediaAsset) -> str:
    return obj.dataset.id

  def get_remote_label_path(self, obj: MediaAsset) -> str:
    if obj.labeling_task and (obj.labeling_task.status == LabelingTaskStatus.SAVED
                              or obj.labeling_task.status == LabelingTaskStatus.ARCHIVED):
      return obj.remote_xml_path


class MediaAssetIDSerializer(serializers.Serializer):
  id = serializers.ListField(
    child=serializers.IntegerField(),
    required=True,
    allow_empty=False,
    min_length=1,
  )
