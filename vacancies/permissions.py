from rest_framework.permissions import BasePermission

from authentication.models import User


class VacancyCreatePermission(BasePermission):
    message = "adding vacancies for non hr user not allowed"

    def has_permission(self, request, view):
        if not request.user:
            return False

        if request.user.role == User.HR:
            return True
        return False
