app_name = "library_manag"
app_title = "Library Manag"
app_publisher = "aqu"
app_description = "manage library"
app_email = "aqu@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_manag",
# 		"logo": "/assets/library_manag/logo.png",
# 		"title": "Library Manag",
# 		"route": "/library_manag",
# 		"has_permission": "library_manag.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_manag/css/library_manag.css"
# app_include_js = "/assets/library_manag/js/library_manag.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_manag/css/library_manag.css"
# web_include_js = "/assets/library_manag/js/library_manag.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_manag/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_manag/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_manag.utils.jinja_methods",
# 	"filters": "library_manag.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_manag.install.before_install"
# after_install = "library_manag.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_manag.uninstall.before_uninstall"
# after_uninstall = "library_manag.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_manag.utils.before_app_install"
# after_app_install = "library_manag.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_manag.utils.before_app_uninstall"
# after_app_uninstall = "library_manag.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_manag.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_manag.tasks.all"
# 	],
# 	"daily": [
# 		"library_manag.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_manag.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_manag.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_manag.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_manag.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_manag.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_manag.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["library_manag.utils.before_request"]
# after_request = ["library_manag.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_manag.utils.before_job"]
# after_job = ["library_manag.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_manag.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
website_route_rules = [
    {"from_route": "/book-details/<isbn>", "to_route": "book-details"}
]

override_whitelisted_methods = {
    "POST /api/method/library_manag.api.create_book": "library_manag.api.create_book",
    "GET /api/method/library_manag.api.get_books": "library_manag.api.get_books",
    "GET /api/method/library_manag.api.get_book_details": "library_manag.api.get_book_details",
    "POST /api/method/library_manag.api.update_book": "library_manag.api.update_book",
    "POST /api/method/library_manag.api.delete_book": "library_manag.api.delete_book",
    "POST /api/method/library_manag.api.create_member": "library_manag.api.create_member",
    "GET /api/method/library_manag.api.get_member": "library_manag.api.get_member",
    "POST /api/method/library_manag.api.update_member": "library_manag.api.update_member",
    "POST /api/method/library_manag.api.delete_member": "library_manag.api.delete_member",
    "POST /api/method/library_manag.api.create_loan": "library_manag.api.create_loan",
    "GET /api/method/library_manag.api.get_loan": "library_manag.api.get_loan",
    # "POST /api/method/library_manag.api.update_loan": "library_manag.api.update_loan",
    # "POST /api/method/library_manag.api.delete_loan": "library_manag.api.delete_loan"
}