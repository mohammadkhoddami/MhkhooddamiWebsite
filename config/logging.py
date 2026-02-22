# my_project/settings/logging.py

import os


def get_logging_config(BASE_DIR, DEBUG):
    """
    تنظیمات لاگ‌گیری پروژه را بر اساس
    BASE_DIR (برای ساخت پوشه logs)
    و DEBUG (برای تعیین سطح لاگ و handlers)
    برمی‌گرداند.
    """

    # ساخت پوشه 'logs' در ریشه پروژه
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)

    # تعریف سطح لاگ برای کنسول بر اساس DEBUG
    console_log_level = "DEBUG" if DEBUG else "INFO"

    # تعریف handlers بر اساس DEBUG
    # در حالت DEV، فقط 'console'
    # در حالت PROD، 'console' + 'file_info' + 'file_error'
    root_handlers = ["console"]
    django_handlers = ["console"]
    my_app_handlers = ["console"]
    request_handlers = ["console"]

    if not DEBUG:
        root_handlers.extend(["file_info", "file_error"])
        django_handlers.extend(["file_info", "file_error"])
        my_app_handlers.extend(["file_info", "file_error"])
        request_handlers = ["file_error", "mail_admins"]

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            },
            "simple": {"format": "[%(levelname)s] %(message)s"},
        },
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
        },
        "handlers": {
            "console": {
                "level": console_log_level,
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "file_info": {
                "level": "INFO",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(LOG_DIR, "info.log"),
                "maxBytes": 10 * 1024 * 1024,  # 10 MB
                "backupCount": 5,
                "formatter": "verbose",
                "filters": ["require_debug_false"],
            },
            "file_error": {
                "level": "ERROR",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(LOG_DIR, "error.log"),
                "maxBytes": 5 * 1024 * 1024,  # 5 MB
                "backupCount": 5,
                "formatter": "verbose",
                "filters": ["require_debug_false"],
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "filters": ["require_debug_false"],
                "include_html": True,
            },
        },
        "loggers": {
            # لاگر ریشه
            "": {
                "handlers": root_handlers,
                "level": "DEBUG" if DEBUG else "INFO",
            },
            # لاگر جنگو
            "django": {
                "handlers": django_handlers,
                "level": "INFO",
                "propagate": False,
            },
            # لاگر خطاهای درخواست
            "django.request": {
                "handlers": request_handlers,
                "level": "ERROR",
                "propagate": False,
            },
            # لاگر کوئری‌های دیتابیس (فقط در DEV)
            "django.db.backends": {
                "level": "DEBUG",
                "handlers": ["console"],
                "filters": ["require_debug_true"],
                "propagate": False,
            },
            "users": {  # اپ کاربران
                "handlers": my_app_handlers,
                "level": "DEBUG",
                "propagate": False,
            },
            "products": {  # اپ محصولات
                "handlers": my_app_handlers,
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }
