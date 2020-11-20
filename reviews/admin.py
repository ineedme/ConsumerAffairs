from django.contrib import admin
from reviews.models import Review, Company


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "rating",
                    "title",
                    "company",
                    "reviewer",
                    "ip_address",
                    "submitted_at",
                    )
    search_fields = ("title",)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Company)
