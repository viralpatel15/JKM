app_name = "jkm"
app_title = "JKM"
app_publisher = "viral@fosserp.com"
app_description = "Company Custom app"
app_email = "viral@fosserp.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jkm/css/jkm.css"
# app_include_js = "/assets/jkm/js/jkm.js"

# include js, css files in header of web template
# web_include_css = "/assets/jkm/css/jkm.css"
# web_include_js = "/assets/jkm/js/jkm.js"
doctype_js = {
	"Payment Entry": "public/js/doctype_js/payment_entry.js",
	"Sales Invoice": "public/js/doctype_js/sales_invoice.js",
    "Journal Entry": "public/js/doctype_js/journal_entry.js"
}

doc_events = {
	"Payment Entry": {
		"on_submit": "jkm.api.pe_on_submit",
		"before_cancel": "jkm.api.pe_on_cancel",
	},
	"Journal Entry": {
    	"on_cancel": "jkm.jkm.doc_events.journal_entry.before_cancel",
	},
	"Duty DrawBack Claim":{
        "on_submit":"jkm.jkm.doctype.duty_drawback_claim.duty_drawback_claim.create_jv_on_submit"
    },
	"Rodtep Claim":{
        "on_submit":"jkm.jkm.doctype.rodtep_claim.rodtep_claim.create_jv_on_submit"
    },
    "Sales Invoice":{
        "validate":"jkm.jkm.doc_events.sales_invoice.validate",
        "on_submit": "jkm.api.si_on_submit",
        "on_cancel": "jkm.api.si_on_cancel"
    },
	"Lead":{
		"validate":"jkm.jkm.doc_events.lead.validate",
		"after_insert":"jkm.jkm.doc_events.lead.after_insert"
	}
}
# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jkm/public/scss/website"

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
# app_include_icons = "jkm/public/icons.svg"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "jkm.utils.jinja_methods",
# 	"filters": "jkm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jkm.install.before_install"
# after_install = "jkm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jkm.uninstall.before_uninstall"
# after_uninstall = "jkm.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "jkm.utils.before_app_install"
# after_app_install = "jkm.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "jkm.utils.before_app_uninstall"
# after_app_uninstall = "jkm.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jkm.notifications.get_notification_config"

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
# 		"jkm.tasks.all"
# 	],
# 	"daily": [
# 		"jkm.tasks.daily"
# 	],
# 	"hourly": [
# 		"jkm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jkm.tasks.weekly"
# 	],
# 	"monthly": [
# 		"jkm.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "jkm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jkm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "jkm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jkm.utils.before_request"]
# after_request = ["jkm.utils.after_request"]

# Job Events
# ----------
# before_job = ["jkm.utils.before_job"]
# after_job = ["jkm.utils.after_job"]

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
# 	"jkm.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

