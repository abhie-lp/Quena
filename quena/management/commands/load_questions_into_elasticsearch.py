from quena.models import Question
from django.core.management import BaseCommand
from quena.service import elasticsearch


class Command(BaseCommand):
    help = "Load all questions into Elasticsearch"

    def handle(self, *args, **options):
        queryset = Question.objects.all()
        all_loaded = elasticsearch.bulk_load(queryset)
        if all_loaded:
            self.stdout.write(self.style.SUCCESS(
                "Successfully loaded all questions into elasticsearch."
            ))
        else:
            self.stdout.write(
                self.style.WARNING("Some questions not loaded. See logged errors.")
            )