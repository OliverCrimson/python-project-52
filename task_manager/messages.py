from enum import Enum
from django.utils.translation import gettext_lazy as _


class Flashes(Enum):
    LABEL_CREATED = _('Label created')
    LOGGED_IN = _('Logged in successfully')
    LOGGED_OUT = _('Logged out successfully')
    LABEL_UPDATED = _('Label updated successfully')
    LABEL_DELETED = _('Label deleted')
    LABEL_ERROR = _('Unable to delete label which being used')
    TASK_CREATED = _('Task created')
    TASK_UPDATE = _('Task updated')
    TASK_DELETE = _('Task deleted')
    STATUS_CREATE = _('Status created')
    STATUS_UPDATE = _('Status updated')
    STATUS_DELETE = _('Status deleted')
    STATUS_ERROR = _('Unable to delete status which is being used')
    USER_REGISTERED = _('User successfully registered')
    USER_DELETE = _('User successfully deleted')
    USER_UPDATED = _('Successfully updated user')
    UNAUTHORIZED = _('You are not authorized! Please log in.')
    NO_PERMISSION_TASK = _('Task can be deleted by one who created it')
    NO_PERMISSION_USER_UPDATE = _('You have no permission for updating another user')
