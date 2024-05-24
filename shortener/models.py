from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    use_for_related_fields = True  # 옵션은 기본 매니저로 이 매니저를 정의한 모델이 있을 때 이 모델을 가리키는 모든 관계 참조에서 모델 매니저를 사용할 수 있도록 한다.

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField('삭제일', null=True, default=None)


    class Meta:
        abstract = True


    objects = SoftDeleteManager()  # 커스텀 매니저
    all_objects = models.Manager()


    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


    def restore(self):  # 삭제된 레코드를 복구한다.
        self.is_deleted = False
        self.deleted_at = None
        self.save()

class ShortLinkModel(SoftDeleteModel, SoftDeleteManager):
    origin_url = models.TextField()
    short_url = models.TextField()
    hash_value = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.origin_url