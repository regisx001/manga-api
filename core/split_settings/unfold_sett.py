from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


USERS_TABS = [
    {
        "models": [
            "users.user",
        ],
        "items": [
            {
                "title": _("Users"),
                "link": reverse_lazy("admin:users_user_changelist"),
            },
            {
                "title": _("Users Profiles"),
                "link": reverse_lazy("admin:users_userprofile_changelist"),
            },
            {
                "title": _("Users Group"),
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "models": [
            "users.userprofile",
        ],
        "items": [
            {
                "title": _("Users"),
                "link": reverse_lazy("admin:users_user_changelist"),
            },
            {
                "title": _("Users Profiles"),
                "link": reverse_lazy("admin:users_userprofile_changelist"),
            },
            {
                "title": _("Users Group"),
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    }, {
        "models": [
            "auth.group",
        ],
        "items": [
            {
                "title": _("Users"),
                "link": reverse_lazy("admin:users_user_changelist"),
            },
            {
                "title": _("Users Profiles"),
                "link": reverse_lazy("admin:users_userprofile_changelist"),
            },
            {
                "title": _("Users Group"),
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
]


TABS = [
    *USERS_TABS,
]

SIDEBAR_CONFIG = {
    "show_search": True,
    "show_all_applications": True,
    "navigation": [
        {
            "title": _("Navigation"),
            "separator": True,
            "items": [
                {
                    "title": _("Dashboard"),
                    "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                    "link": reverse_lazy("admin:index"),
                    # "badge": "sample_app.badge_callback",
                },
                {
                    "title": _("Users"),
                    "icon": "people",
                    "link": reverse_lazy("admin:users_user_changelist"),
                },
                {
                    "title": _("Manga"),
                    "icon": "library_books",
                    "link": reverse_lazy("admin:manga_manga_changelist"),
                },
            ],
        },
    ],
}

COLORS = {
    "primary": {
        "50": "250 245 255",
        "100": "243 232 255",
        "200": "233 213 255",
        "300": "216 180 254",
        "400": "192 132 252",
        "500": "168 85 247",
        "600": "147 51 234",
        "700": "126 34 206",
        "800": "107 33 168",
        "900": "88 28 135",
    },
},

UNFOLD = {
    "SITE_TITLE": "Admin",
    "SITE_HEADER": "ADMINISTRATION",
    # "SITE_URL": "/",
    "SITE_ICON": lambda request: static("admin/logo.svg"),
    "SITE_SYMBOL": "speed",  # symbol from icon set
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    "LOGIN": {
        "image": lambda r: static("admin/login-bg.svg"),
        # "redirect_after": lambda r: reverse_lazy("admin:APP_MODEL_changelist"),
    },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/script.js"),
    # ],
    # "COLORS": COLORS,

    # "EXTENSIONS": {
    #     "modeltranslation": {
    #         "flags": {
    #             "en": "🇬🇧",
    #             "fr": "🇫🇷",
    #             "nl": "🇧🇪",
    #         },
    #     },
    # },
    "SIDEBAR": SIDEBAR_CONFIG,
    "TABS": TABS
}


def badge_callback(request):
    return 3
