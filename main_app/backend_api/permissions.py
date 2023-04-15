from rest_framework.permissions import BasePermission


class IsPerformers(BasePermission):
    """
    Get permission to object for author and performers
    """
    def has_object_permission(self, request, view, obj) -> bool:
        add_perfermers = obj.performers.all()
        permission_list = [query.username for query in add_perfermers]  # all performers
        permission_list.append(obj.author.username)                     # author have permission
        return str(request.user) in permission_list

