from enum import Enum


class Flashes(Enum):
    LABEL_CREATED = 'Label created'
    LOGGED_IN = 'Logged in successfully'
    LOGGED_OUT = 'Logged out successfully'
    LABEL_UPDATED = 'Label updated successfully'
    LABEL_DELETED = 'Label deleted'
    LABEL_ERROR = 'Unable to delete label which being used'
    TASK_CREATED = 'Task created'
    TASK_UPDATE = 'Task updated'
    TASK_DELETE = 'Task deleted'
    STATUS_CREATE = 'Status created'
    STATUS_UPDATE = 'Status updated'
    STATUS_DELETE = 'Status deleted'
    STATUS_ERROR = 'Unable to delete status which is being used'
    USER_REGISTERED = 'User successfully registered'
    USER_DELETE = 'User successfully deleted'
    USER_UPDATED = 'Successfully updated user'
    UNAUTHORIZED = 'You are not authorized! Please log in.'
    NO_PERMISSION_TASK = 'Task can be deleted by one who created it'
    NO_PERMISSION_USER_UPDATE = 'You have no permission for updating another user'
