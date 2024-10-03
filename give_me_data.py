def has_permission(user_info, accessing_data):
    if accessing_data + '_deny' in user_info:
        return False
    if accessing_data + '_allow' in user_info:
        return True
    if '*_deny' in user_info:
        return False
    if '*_allow' in user_info:
        return True
    return False
