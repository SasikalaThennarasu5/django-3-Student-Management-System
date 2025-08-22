from django.contrib import admin
from .models import Student, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "get_status")
    search_fields = ("name", "email")
    list_filter = ("enrollments__status",)
    inlines = [EnrollmentInline]

    def get_status(self, obj):
        latest = obj.enrollments.last()
        return latest.status if latest else "Not Enrolled"
    get_status.short_description = "Status"

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course_name", "status")
    list_filter = ("status",)
    search_fields = ("student__name", "course_name")
